#!/usr/bin/env python3
"""Updates docs/gm-commands.md from the `command` table of a running AzerothCore database.

Security and Syntax are taken from the database. Descriptions already on the page are kept;
only new commands get the help text of the database as their description.

    python tools/update_gm_commands.py                 asks for the connection, Enter keeps a default
    python tools/update_gm_commands.py -y              uses the defaults without asking
    python tools/update_gm_commands.py --check         only reports
    python tools/update_gm_commands.py --log file.log  writes the old and new values to that file
    python tools/update_gm_commands.py --host 10.0.0.5 --user root --password secret
"""
import argparse
import datetime
import getpass
import re
import subprocess
import sys
from pathlib import Path

# Connection defaults.
DEFAULTS = {"host": "127.0.0.1", "port": 3306, "user": "acore", "password": "acore",
            "world_db": "acore_world", "auth_db": "acore_auth"}
PAGE = Path(__file__).resolve().parent.parent / "docs" / "gm-commands.md"
# A log is always written when the page is changed; --log sets another file.
LOG_DIR = Path(__file__).resolve().parent / "logs"
# Roles that hold commands, best match first.
COMMAND_ROLES = (196, 197, 198, 199)
SECURITY_ROLES = (192, 193, 194, 195)
SECURITY_NAMES = {0: "SEC_PLAYER", 1: "SEC_MODERATOR", 2: "SEC_GAMEMASTER", 3: "SEC_ADMINISTRATOR",
                  4: "SEC_CONSOLE (do not give this security level to an account)"}
# Commands the core has without a row in the command table: never reported as removed.
NOT_IN_COMMAND_TABLE = ["pet rename", "reload spell_cone", "rbac account deny", "rbac account grant",
                        "rbac account list", "rbac account revoke"]
SYNTAX_FIXES = {"teleport group": "#location", "list object": "", "lookup object": "", "wp modify": "",
                "mmap": "$subcommand"}
HEADER = ["Command", "RBAC", "Security", "Console", "Syntax", "Description"]
ALIGN = "lcccll"


# ---------- database ----------

def query(conn, database, sql):
    """Runs a query with PyMySQL or mysql-connector if installed, else with the mysql command."""
    for module in ("pymysql", "mysql.connector"):
        try:
            driver = __import__(module, fromlist=["connect"])
        except ImportError:
            continue
        db = driver.connect(host=conn["host"], port=int(conn["port"]), user=conn["user"],
                            password=conn["password"], database=database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            return [tuple("" if v is None else str(v) for v in row) for row in cursor.fetchall()]
        finally:
            db.close()
    command = ["mysql", "-h", conn["host"], "-P", str(conn["port"]), "-u", conn["user"],
               f"-p{conn['password']}", "--batch", "--skip-column-names", "--default-character-set=utf8mb4",
               database, "-e", sql]
    try:
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    except FileNotFoundError:
        sys.exit("Error: no MySQL driver found. Install one with 'pip install pymysql', "
                 "or add the mysql command line client to your PATH.")
    if result.returncode:
        sys.exit("Error: " + result.stderr.strip().splitlines()[-1])
    return [tuple(unescape(cell) for cell in line.split("\t")) for line in result.stdout.splitlines()]


def unescape(cell):
    if cell == "NULL":
        return ""
    return re.sub(r"\\(.)", lambda m: {"n": "\n", "t": "\t", "r": "\r", "0": ""}.get(m.group(1), m.group(1)), cell)


def load_roles(conn):
    """Command name -> id of the role that holds its permission."""
    names = query(conn, conn["auth_db"], "SELECT id, name FROM rbac_permissions")
    links = query(conn, conn["auth_db"], "SELECT id, linkedId FROM rbac_linked_permissions")
    parents = {}
    for parent, child in links:
        parents.setdefault(int(child), []).append(int(parent))

    def role_of(permission, seen=()):
        best = None
        for parent in parents.get(permission, []):
            if parent in seen:
                continue
            if parent in COMMAND_ROLES:
                return parent
            found = parent if parent in SECURITY_ROLES else role_of(parent, seen + (permission,))
            if found and (best is None or found in COMMAND_ROLES):
                best = found
        return best

    roles = {}
    for permission, name in names:
        if name.startswith("Command:"):
            role = role_of(int(permission))
            if role:
                roles[name[8:].strip().lower()] = role
    return roles


# ---------- help text -> syntax and description ----------

def escape(text):
    text = text.replace("\\", "\\\\").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("*", "\\*").replace("`", "'")
    return re.sub(r"(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])", r"\\_", text)


def split_help(name, text):
    lines = [l.strip() for l in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    syntax, rest = None, []
    for i, line in enumerate(lines):
        match = re.match(r"(?i)^(?:syntax|usage)\s*:?\s*(\.?\S.*)$", line) if syntax is None else None
        if match:
            syntax = match.group(1)
        elif syntax is None and i == 0 and line.lower().startswith("." + name.lower()):
            syntax = line
        else:
            rest.append(line)
    syntax = re.sub(r"(?i)^(syntax\s*:\s*)+", "", (syntax or "." + name).strip()).rstrip("\\").strip()
    tokens = [t for t in syntax.split(" ") if t]
    i = 0
    while i < len(tokens) and i < len(name.split()) and re.fullmatch(r"\.?[A-Za-z0-9_]+", tokens[i]):
        i += 1
    if name in SYNTAX_FIXES:
        tokens, i = [t for t in SYNTAX_FIXES[name].split(" ") if t], 0
    closing = {"[": "]", "<": ">", "(": ")", '"': '"'}
    params, tail, j = [], None, i
    while j < len(tokens):
        token = tokens[j]
        if "./n" in token:
            first, second = token.split("./n", 1)
            params.append(first)
            tail = " ".join([second] + tokens[j + 1:])
            break
        opener = token[0] if token[0] in closing else ("(" if token.startswith("Optional(") else None)
        unbalanced = opener and (token.count('"') % 2 == 1 if opener == '"' else
                                 token.count(opener) > token.count(closing[opener]))
        if unbalanced:
            k, group = j, [token]
            while k + 1 < len(tokens) and closing[opener] not in tokens[k + 1]:
                k += 1
                group.append(tokens[k])
            if k + 1 < len(tokens):
                k += 1
                group.append(tokens[k])
            token, j = " ".join(group), k
        is_parameter = (token[0] in '$#[<"(' or "/" in token or "|" in token or ":" in token or token == "..."
                        or token.startswith("Optional(")
                        or (re.fullmatch(r"[a-z0-9_\]\[:]+", token) and token not in ("to", "will", "is", "the")))
        if not is_parameter:
            tail = " ".join(tokens[j:])
            break
        if token.endswith(".") and not token.endswith("..."):
            params.append(token[:-1])
            tail = " ".join(tokens[j + 1:])
            break
        params.append(token)
        j += 1
    syntax = ("." + name + " " + " ".join(params)).strip()
    if tail:
        tail = re.sub(r"^[-–.\s]+", "", tail).strip()
        if tail:
            rest.insert(0, tail[0].upper() + tail[1:])
    description = "<br>".join(escape(l) for l in rest if l)
    return syntax, "" if description.strip().upper() == "TODO" else description


# ---------- page ----------

def cells(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def read_page(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(newline)
    start = next(i for i, l in enumerate(lines) if l.startswith('<details class="cmd-list"'))
    end = max(i for i, l in enumerate(lines) if l.strip() == "</details>") + 1
    rows = {}
    for line in lines[start:end]:
        if line.startswith("|") and not line.startswith("| Command") and not line.startswith("| :"):
            c = cells(line)
            if len(c) == 6:
                name = re.sub(r"<[^>]+>", "", c[0])
                rbac = re.match(r"\[(\d+)\]", c[1])
                rows[name] = {"rbac": int(rbac.group(1)) if rbac else None, "security": int(c[2]),
                              "console": c[3], "syntax": c[4].strip("`").replace("\\|", "|"), "description": c[5]}
    return lines, start, end, rows, newline, raw.startswith(b"\xef\xbb\xbf")


def table(rows, anchors, with_security):
    body = []
    for name in sorted(rows, key=str.lower):
        r = rows[name]
        label = f'<span id="{re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")}">{name}</span>' if anchors else name
        rbac = f"[{r['rbac']}](rbac_linked_permissions#role-{r['rbac']})" if r["rbac"] else ""
        syntax = "`" + r["syntax"].replace("|", "\\|").replace("`", "'") + "`"
        body.append([label, rbac, str(r["security"]), r["console"], syntax, r["description"]])
    header, align = HEADER, ALIGN
    if not with_security:
        header, align = HEADER[:2] + HEADER[3:], ALIGN[:2] + ALIGN[3:]
        body = [r[:2] + r[3:] for r in body]
    last = len(header) - 1
    width = [len(header[c]) if c == last else max(3, len(header[c]), *(len(r[c]) for r in body))
             for c in range(len(header))]
    fmt = lambda r: "| " + " | ".join(r[c].ljust(width[c]) for c in range(len(header))) + " |"
    dashes = "| " + " | ".join(":" + "-" * (width[c] - 1) if align[c] == "l" else ":" + "-" * (width[c] - 2) + ":"
                               for c in range(len(header))) + " |"
    return [fmt(header), dashes] + [fmt(r) for r in body]


def build_lists(rows):
    out = ['<details class="cmd-list" open>', "<summary>All commands</summary>", ""]
    out += table(rows, True, True) + ["", "</details>", ""]
    for level, title in SECURITY_NAMES.items():
        part = {n: r for n, r in rows.items() if r["security"] == level}
        if part:
            out += ['<details class="cmd-list">', f"<summary>[{level}] - {title}</summary>", ""]
            out += table(part, False, False) + ["", "</details>", ""]
    return out[:-1]


def merge(rows, commands, roles, replace_rbac, remove_missing=False):
    """Applies the database to the rows of the page. Returns (what, command, old, new) changes."""
    changes = []
    for name, security, help_text in commands:
        syntax, description = split_help(name, help_text)
        role = roles.get(name.lower())
        row = rows.get(name)
        if row is None:
            rows[name] = {"rbac": role, "security": security, "console": "", "syntax": syntax,
                          "description": description}
            new = f"rbac {role or '-'} | security {security} | console (empty, fill in by hand) | {syntax} | {description}"
            changes.append(("added", name, None, new))
            continue
        if row["security"] != security:
            changes.append(("security", name, row["security"], security))
            row["security"] = security
        if row["syntax"] != syntax:
            changes.append(("syntax", name, row["syntax"], syntax))
            row["syntax"] = syntax
        if replace_rbac and role and role != row["rbac"]:
            changes.append(("rbac", name, row["rbac"] or "-", role))
            row["rbac"] = role
    known = {name for name, _, _ in commands} | set(NOT_IN_COMMAND_TABLE)
    review = []
    for name in sorted(set(rows) - known, key=str.lower):
        r = rows[name]
        old = f"rbac {r['rbac'] or '-'} | security {r['security']} | console {r['console']} | {r['syntax']} | {r['description']}"
        if remove_missing:
            del rows[name]
            changes.append(("removed", name, old, "(deleted from the page)"))
        else:
            review.append((name, old))
    return changes, review


def write_log(path, header, changes, review):
    lines = [header, ""]
    for what, name, old, new in changes:
        lines.append(f"{what}: {name}")
        if old is not None:
            lines.append(f"  old: {old}")
        lines.append(f"  new: {new}")
    if review:
        lines += ["", "REVIEW BY HAND: no longer in the command table, still on the page",
                  "(run with --remove-missing to delete them, or add them to NOT_IN_COMMAND_TABLE):"]
        for name, old in review:
            lines += [f"removed from the database: {name}", f"  old: {old}", "  new: (kept on the page)"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Log written to {path}")


# ---------- start ----------

def connection(args):
    conn = {key: getattr(args, key) if getattr(args, key) is not None else default
            for key, default in DEFAULTS.items()}
    given = any(getattr(args, key) is not None for key in DEFAULTS)
    if args.yes or given or not sys.stdin.isatty():
        return conn
    print("Database connection. Press Enter to keep the value in brackets.")
    for key, label in (("host", "Host"), ("port", "Port"), ("user", "User"), ("password", "Password"),
                       ("world_db", "World database"), ("auth_db", "Auth database")):
        shown = "*" * len(str(conn[key])) if key == "password" else conn[key]
        prompt = f"  {label} [{shown}]: "
        answer = getpass.getpass(prompt) if key == "password" else input(prompt).strip()
        if answer:
            conn[key] = answer
    return conn


def main():
    parser = argparse.ArgumentParser(description="AzerothCore wiki GM commands updater")
    parser.add_argument("--host")
    parser.add_argument("--port", type=int)
    parser.add_argument("--user")
    parser.add_argument("--password")
    parser.add_argument("--world-db", dest="world_db")
    parser.add_argument("--auth-db", dest="auth_db")
    parser.add_argument("--page", default=str(PAGE), help="path to gm-commands.md")
    parser.add_argument("--no-rbac", action="store_true", help="do not read the RBAC tables")
    parser.add_argument("--replace-rbac", action="store_true",
                        help="also update the RBAC column of commands already on the page (default: new commands only)")
    parser.add_argument("--remove-missing", action="store_true",
                        help="delete commands that are no longer in the command table (default: keep and flag them)")
    parser.add_argument("--check", action="store_true", help="only report what would change")
    parser.add_argument("--log", help="log file (default: tools/logs/update_gm_commands-<date>.log)")
    parser.add_argument("-y", "--yes", action="store_true", help="use the default connection without asking")
    args = parser.parse_args()

    page = Path(args.page)
    if not page.is_file():
        sys.exit(f"Error: '{page}' does not exist.")
    conn = connection(args)
    print(f"Reading {conn['world_db']}.command from {conn['user']}@{conn['host']}:{conn['port']}")
    commands = [(name, int(security), help_text) for name, security, help_text in
                query(conn, conn["world_db"], "SELECT name, security, help FROM command")]
    roles = {} if args.no_rbac else load_roles(conn)

    lines, start, end, rows, newline, bom = read_page(page)
    changes, review = merge(rows, commands, roles, args.replace_rbac, args.remove_missing)
    for what, name, old, new in changes:
        print(f"  {what}: {name}: {new}" if old is None else f"  {what}: {name}: {old} -> {new}")
    for name, _ in review:
        print(f"  REVIEW: removed from the database, still on the page: {name}")
    changed = changes
    stamp = datetime.datetime.now()
    log = Path(args.log) if args.log else LOG_DIR / f"update_gm_commands-{stamp:%Y%m%d-%H%M%S}.log"
    header = (f"update_gm_commands {stamp:%Y-%m-%d %H:%M:%S} | {'check only' if args.check else 'applied'} | "
              f"{conn['user']}@{conn['host']}:{conn['port']} {conn['world_db']} | {page}")
    if not changed:
        print(f"Nothing to do: all {len(commands)} commands match the page.")
    elif args.check:
        print(f"{len(changed)} changes. Run without --check to apply them.")
    else:
        lines[start:end] = build_lists(rows)
        page.write_bytes((b"\xef\xbb\xbf" if bom else b"") + newline.join(lines).encode("utf-8"))
        print(f"Applied {len(changed)} changes to {page}.")
    if review:
        print(f"{len(review)} commands need a manual review. Use --remove-missing to delete them from the page.")
    if args.log or ((changed or review) and not args.check):
        write_log(log, header, changes, review)
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
