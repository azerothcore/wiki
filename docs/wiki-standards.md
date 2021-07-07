# WIKI STANDARDS

## FILE NAMING:

DATABASE TABLES files are to be named exactly as it is in the database,

ALL OTHER FILES are to be named in `lower case` and to use `-` (dashes) for spaces.

FILES SHOLD NOT contain any special characters other than `-` (dashes). If we want a file named C++ we name it cpp.

ALL WIKI FILES should end with with `.md`.

## FILE ENCODING

ALL FILES must be UTF-8 encoded to work on the wiki.

## FILE HEADERS

THE FILE  SHOULD ALWAYS START WITH `# File Name`. (This is to display correct info in the tab.)

## DATABASE TABLE FILES:

ALL DATABASE TABLE FILES should be present in the correct DATABASE FILE.

When adding/removing a table it should also be updated in `database-auth.md` `database-characters.md` `database-world.md`

## TRANSLATION

ALL TRANSLATIONS should be in a sub directory of /docs/ with the shortened locale of the language. i.e /docs/es/. If there has been no translations prior, you need to allow the directory path in the config. See [this commit on how to do it](https://github.com/azerothcore/wiki/commit/8b897c3384298674e82108357ee5e655f788229f).

ALL FILES should be named the **exact same as the English versions**! Do not ever translate the file names, only the contents within.

## ARCHIVED PAGES: (Not yet implemented)

ALL ARCHIVED PAGES that could potentially have some sort of value should be added in the `archive.md` list and links to these pages should be removed from other places in the wiki.

They should also be moved into the /docs/archive/ folder.
