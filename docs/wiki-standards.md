# WIKI STANDARDS

## FILE NAMING:

DATABASE TABLES files are to be named exactly as it is in the database,

ALL OTHER FILES are to be named in `lowercase` and to use `-` (dashes) for spaces.

FILES SHOULD NOT contain special characters other than `-` (dashes). If we want a file named C++ we name it cpp.

ALL WIKI FILES should end with with `.md`.

## FILE ENCODING

ALL FILES must be UTF-8 encoded to work on the wiki.

## FILE LANGUAGE

TO ENSURE EASY MAINTENANCE, all files must be written in `markdown` format. HTML is not allowed!

## FILE HEADERS

THE FILE  SHOULD ALWAYS START WITH `# File Name`. (This is to display correct info in the browser tab.)

## DATABASE TABLE FILES:

ALL DATABASE TABLE FILES should be present in the correct DATABASE FILE.

When adding/removing a table it should also be updated in `database-auth` `database-characters` `database-world`

## LINKING WITHIN THE WIKI

When linking to a page in the wiki we use relative links. (`[home](home#overview)`).

When linking to a header on the same page in the wiki relative links. (`[withCapitalLetters](#withcapitalletters).`

It is important to note that only lowercase letters and no special characters are allowed in relative links. Otherwise, the links will be broken.

When linking to a page outside of the wiki we use absolute links. (`[Google](https://google.com)`).

## TRANSLATION

ALL TRANSLATIONS should be in a sub-directory of /docs/ with the shortened locale of the language. i.e./docs/es/. If there have been no translations prior, you need to allow the directory path in the config. See [this commit on how to do it](https://github.com/azerothcore/wiki/commit/8b897c3384298674e82108357ee5e655f788229f).

ALL FILES should be named the **exact same as the English versions**! Do not ever translate the file names, only the contents within.

## ARCHIVED PAGES: (Not yet implemented)

ALL ARCHIVED PAGES that could potentially have some some value should be added to the `archive` list and links to these pages should be removed from other places in the wiki.

They should also be moved into the /docs/archive/ folder.
