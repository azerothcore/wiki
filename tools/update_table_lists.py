#!/usr/bin/env python3
"""Adds new database table pages to the database lists and the Database Index,
and new DBC file pages to the DBC Index.

    python tools/update_table_lists.py                  adds the missing lines
    python tools/update_table_lists.py --check          only reports
    python tools/update_table_lists.py path/to/docs     uses another docs folder
    python tools/update_table_lists.py --log file.log   writes what was added to that file
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

# Sub-folders of docs to update: "" is English.
LANGUAGES = ["", "es", "cn"]
# Databases: the name used in "database-<name>.md" and its heading on the Database Index.
DATABASES = {"auth": "Auth", "characters": "Characters", "world": "World"}
INDEX_PAGE = "database-index.md"
# Pages about client DBC files link back to this page and are listed on it.
DBC_INDEX_PAGE = "dbc-index.md"
# A log is always written when a list is changed; --log sets another file.
LOG_DIR = Path(__file__).resolve().parent / "logs"

# Default docs folder; another one can be given as the first argument.
DOCS = Path(__file__).resolve().parent.parent / "docs"
# A back link is a line that holds nothing but the link.
BACK_LINK = re.compile(r"(?m)^\[[^\]]+\]\(database-(%s)\)\s*$" % "|".join(DATABASES))
ENTRY = re.compile(r'^[-*] \[([^\]]+)\]\(([^)\s]+)(?: "[^"]*")?\)\s*$')
# Link title in the lists of a page that only has column names and types (shown with a diamond).
COLUMNS_ONLY = "Columns only"
# Link title of a page with comments, descriptions or content (shown with a dot).
DOCUMENTED = "Documented"
# A row of the structure table with something in its last (Comment) column.
COMMENT = re.compile(r"^\| *(\d+|\[[^\]]+\]\(#[^)]*\)) *\|.*\| *[^|\s:-][^|]*\|\s*$")
# Language notes and links to other DBC files do not count as documentation.
LOCALE_NOTE = re.compile(r"\| *(Assumed |Unknown language|ID in \[|Race mask|Class mask|Bitmask of )[^|]*\|\s*$")
SECTION = re.compile(r"^(#{2,4} |<details|\*\*.+\*\*\s*$)")
LETTER = re.compile(r"(#{2,4}) (\w)")


def read(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    newline = "\r\n" if "\r\n" in text else "\n"
    return text.split(newline), newline, raw.startswith(b"\xef\xbb\xbf")


def write(path, lines, newline, bom):
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + newline.join(lines).encode("utf-8"))


def table_pages(folder):
    """Table pages are recognised by their back link in the first lines."""
    pages = {db: [] for db in DATABASES}
    for path in sorted(folder.glob("*.md")):
        head = "\n".join(path.read_text(encoding="utf-8-sig", errors="replace").splitlines()[:15])
        match = BACK_LINK.search(head)
        if match and not path.name.startswith("database-"):
            pages[match.group(1)].append(path.stem)
    return pages


def insert_sorted(lines, first, last, label, target, bullet):
    position = last
    while position > first and not ENTRY.match(lines[position - 1]):
        position -= 1
    for i in range(first, last):
        entry = ENTRY.match(lines[i])
        if entry and entry.group(1).lower() > label.lower():
            position = i
            break
    lines.insert(position, f"{bullet} [{label}]({target})")


def add_to_list(lines, first, last, label, target, bullet="-"):
    """Adds the entry between first and last, under its letter heading when the list has them.

    Returns how many lines were added."""
    before = len(lines)
    heads = [(i, m.group(1), m.group(2)) for i in range(first, last)
             for m in [LETTER.fullmatch(lines[i].strip())] if m]
    if not heads:
        insert_sorted(lines, first, last, label, target, bullet)
        return len(lines) - before
    marks, letter = heads[0][1], label[0].upper()
    start = next((i for i, _, h in heads if h == letter), None)
    if start is None:
        start = next((i for i, _, h in heads if h > letter), None)
        if start is None:
            start = last
            while start > first and not ENTRY.match(lines[start - 1]):
                start -= 1
            lines[start:start] = ["", f"{marks} {letter}"]
            start += 1
        else:
            lines[start:start] = [f"{marks} {letter}", ""]
        last += 2
    end = next((i for i in range(start + 1, last) if LETTER.fullmatch(lines[i].strip())), last)
    insert_sorted(lines, start + 1, end, label, target, bullet)
    return len(lines) - before


def update_database_page(folder, db, names, check):
    path = folder / f"database-{db}.md"
    if not path.exists():
        return []
    lines, newline, bom = read(path)
    listed = {m.group(2) for m in map(ENTRY.match, lines) if m}
    for target in sorted(listed):
        if "/" not in target and not (folder / f"{target}.md").exists():
            print(f"  warning: {path.relative_to(DOCS)} links to '{target}', which has no page")
    missing = [n for n in names if n not in listed]
    for name in missing:
        add_to_list(lines, 0, len(lines), name, name)
    if missing and not check:
        write(path, lines, newline, bom)
    return missing


def update_index(folder, pages, check):
    path = folder / INDEX_PAGE
    if not path.exists():
        return []
    lines, newline, bom = read(path)
    added = []
    for db, title in DATABASES.items():
        start = next(i for i, l in enumerate(lines) if l.strip() == f"## {title}")
        end = next(i for i in range(start, len(lines)) if lines[i].strip() == "</details>")
        listed = {m.group(2) for m in map(ENTRY.match, lines[start:end]) if m}
        first = next(i for i in range(start, end) if ENTRY.match(lines[i]) or LETTER.fullmatch(lines[i].strip()))
        for name in pages[db]:
            if name not in listed:
                end += add_to_list(lines, first, end, name, name)
                added.append(f"{title}: {name}")
    if added and not check:
        write(path, lines, newline, bom)
    return added


def update_dbc_index(folder, check):
    path = folder / DBC_INDEX_PAGE
    if not path.exists():
        return []
    lines, newline, bom = read(path)
    rows = [i for i, l in enumerate(lines) if ENTRY.match(l)]
    listed = {ENTRY.match(lines[i]).group(2) for i in rows}
    bullet = lines[rows[0]][0]
    back_link = re.compile(r"(?m)^\[[^\]]+\]\(%s\)\s*$" % re.escape(path.stem))
    added = []
    for page in sorted(folder.glob("*.md")):
        head = page.read_text(encoding="utf-8-sig", errors="replace").splitlines()[:15]
        if page.stem in listed or page.name.startswith("database-") or not back_link.search("\n".join(head)):
            continue
        title = next((l[2:].strip() for l in head if l.startswith("# ")), page.stem)
        title = re.sub(r"\.dbc$", "", title.replace("\\", ""))
        add_to_list(lines, rows[0], len(lines), title, page.stem, bullet)
        added.append(page.stem)
    if added and not check:
        write(path, lines, newline, bom)
    return added


def documented(text, dbc):
    if any(COMMENT.match(l) and not LOCALE_NOTE.search(l) for l in text):
        return True
    if dbc:
        return sum(1 for l in text if SECTION.match(l)) > 2
    end = next((i for i, l in enumerate(text) if l.startswith("|")), 3)
    while end < len(text) and text[end].startswith("|"):
        end += 1
    return any(l.strip() and not l.startswith(("#", "**", "<")) for l in text[end:])


def update_marks(folder, name, check):
    """Sets the link title that draws a dot (documented) or a diamond (columns only)."""
    path = folder / name
    if not path.exists():
        return []
    lines, newline, bom = read(path)
    changed = []
    for i, line in enumerate(lines):
        entry = ENTRY.match(line)
        page = folder / f"{entry.group(2)}.md" if entry else None
        if not page or not page.exists():
            continue
        mark = DOCUMENTED if documented(read(page)[0], name == DBC_INDEX_PAGE) else COLUMNS_ONLY
        new = f'{line[0]} [{entry.group(1)}]({entry.group(2)} "{mark}")'
        if new != line:
            lines[i] = new
            changed.append(f"{entry.group(2)} marked as {'columns only' if mark == COLUMNS_ONLY else 'documented'}")
    if changed and not check:
        write(path, lines, newline, bom)
    return changed


def update_dbc_count(folder, check):
    """Keeps the "246 DBC files" number on the two index pages equal to the DBC Index list."""
    index = folder / DBC_INDEX_PAGE
    if not index.exists():
        return []
    count = sum(1 for l in read(index)[0] if ENTRY.match(l))
    changed = []
    for name in (DBC_INDEX_PAGE, INDEX_PAGE):
        path = folder / name
        if not path.exists():
            continue
        lines, newline, bom = read(path)
        text = newline.join(lines)
        new = re.sub(r"\b\d+( client)? DBC files", lambda m: f"{count}{m.group(1) or ''} DBC files", text)
        if new != text:
            changed.append(f"{name[:-3]}: number of DBC files set to {count}")
            if not check:
                write(path, new.split(newline), newline, bom)
    return changed


def parse_arguments():
    parser = argparse.ArgumentParser(description="AzerothCore wiki table and DBC list updater")
    parser.add_argument("docs_dir", nargs="?", default=str(DOCS),
                        help="path to the docs folder (default: the docs folder of this repository)")
    parser.add_argument("--check", action="store_true", help="only report what is missing")
    parser.add_argument("--log", help="log file (default: tools/logs/update_table_lists-<date>.log)")
    return parser.parse_args()


def main():
    global DOCS
    args = parse_arguments()
    DOCS = Path(args.docs_dir).resolve()
    if not DOCS.is_dir():
        print(f"Error: Directory '{args.docs_dir}' does not exist.")
        return 1
    print(f"Docs directory: {DOCS}")
    check = args.check
    word = "missing" if check else "added"
    entries = []
    for language in LANGUAGES:
        folder = DOCS / language
        if not folder.is_dir():
            continue
        label = language or "en"
        pages = table_pages(folder)
        for db in DATABASES:
            for name in update_database_page(folder, db, pages[db], check):
                entries.append(f"[{label}] database-{db}: {word} - [{name}]({name})")
        for line in update_index(folder, pages, check):
            title, name = line.split(": ")
            entries.append(f"[{label}] {INDEX_PAGE[:-3]} ({title}): {word} - [{name}]({name})")
        for name in update_dbc_index(folder, check):
            entries.append(f"[{label}] {DBC_INDEX_PAGE[:-3]}: {word} {name}")
        for name in [DBC_INDEX_PAGE, INDEX_PAGE] + [f"database-{db}.md" for db in DATABASES]:
            for line in update_marks(folder, name, check):
                entries.append(f"[{label}] {name[:-3]}: {line}")
        for line in update_dbc_count(folder, check):
            entries.append(f"[{label}] {line}")
    for entry in entries:
        print("  " + entry)
    if not entries:
        print("Nothing to do: every table and DBC page is listed.")
    elif check:
        print(f"{len(entries)} lines are missing. Run without --check to add them.")
    else:
        print(f"Added {len(entries)} lines.")
    if args.log or (entries and not check):
        stamp = datetime.datetime.now()
        log = Path(args.log) if args.log else LOG_DIR / f"update_table_lists-{stamp:%Y%m%d-%H%M%S}.log"
        header = f"update_table_lists {stamp:%Y-%m-%d %H:%M:%S} | {'check only' if check else 'applied'} | {DOCS}"
        log.parent.mkdir(parents=True, exist_ok=True)
        log.write_text("\n".join([header, ""] + entries) + "\n", encoding="utf-8")
        print(f"Log written to {log}")
    return 1 if check and entries else 0


if __name__ == "__main__":
    sys.exit(main())
