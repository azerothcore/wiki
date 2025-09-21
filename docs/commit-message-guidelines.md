# Commit Message Guidelines

# 📌 Title
**Type(Scope/Subscope):** _Commit ultra short explanation_

| ✅ Examples (max 50 characters) |
|--------------------------------|
| fix(DB/SAI): Missing spell to NPC Hogger |
| fix(Scripts/Raid): Phase 2 of Ragnaros |
| feat(Core/Players): Implement missing player flags |

**Pay attention to not leave broken commit messages (e.g. random spaces)**

---

# 📖 Description
Explain **why** this change is being made and **what** it fixes.

| ✅ Examples (max 72 chars per line) |
|-------------------------------------|
| Hogger (id: 492) was not charging player when being engaged. |

---

# ✍️ Co-Author(s)
If there are more authors, they can be mentioned like this:
```

Co-authored-by: Name [name@example.com](mailto:name@example.com)

```

**If you are cherry-picking commits, it is mandatory to refer the original author in your commit.**

When you create a commit (using the GIT Bash terminal), type:

``` 
git commit --author="John Doe <john@example.com>" -m "Your commit message"
```

✔️ This sets the Author field in the commit to John Doe <john@example.com>
✔️ Your normal Git config user.name and user.email will still be used for the Committer field.

If you are using GitHub Desktop, you may fill the co-author field, underneath the commit description box.

---

# 📌 Extra Infos

# ✅ Types
- **feat**: new feature
- **fix**: bug fix  
- **refactor**: refactoring production code (no change to functionality expected)
- **style**: formatting, missing semicolons, etc; no code change
- **docs**: changes to documentation
- **chore**: updating bash scripts, git files etc; no production code change

**Remember:**
- ✅ Capitalize the subject line
- ✅ Use the **imperative mood** in the subject line
- ✅ Do not end the subject line with a period  
- ✅ Separate subject from body with a blank line
- ✅ Use the body to explain **what** and **why** rather than **how**
- ✅ Can use multiple lines with `-` for bullet points in body

**More info:** [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)

---

# 📦 Scope and 🔧 Subscope
Scope defines the main area affected:

- Core (core related, framework files)
- Scripts (core related, script files)
- DB (database related, SQL)

Follow the file names or content type:

- fix(Scripts/Ulduar): Mimiron rocket barrage targeting

- fix(DB/SAI): Add missing spells to Howling Prowler

👉 For SQL commits:
If the content is mixed, choose the most predominant table type.
Example: if most edits are in smart_scripts, use SAI.
If the changes are too diluted, use a general sub-scope like Misc.

For example:
```
fix(Scripts/Ulduar): Mimiron rocket barrage targeting
```

Or

```
fix(DB/SAI): Add missing spells to Howling Prowler
```
