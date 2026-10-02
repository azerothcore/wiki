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

THE ONLY EXCEPTIONS are listed under [HTML EXCEPTIONS](#html-exceptions) below.

## HTML EXCEPTIONS

HTML IS ALLOWED ONLY in the cases below. Everywhere else use markdown: `**bold**`, not `<b>bold</b>`.

### Notice boxes

A NOTICE BOX is added with an include. There are four alerts and one callout:

{% raw %}
```
{% include note.html content="Extra information the reader may want." %}
{% include tip.html content="An optional shortcut or a better way to do something." %}
{% include important.html content="Something the reader must know before going on." %}
{% include warning.html content="Something that can break the server or lose data." %}
{% include callout.html content="A highlighted block without a label." type="primary" %}
```
{% endraw %}

Preview:

{% include note.html content="Extra information the reader may want." %}
{% include tip.html content="An optional shortcut or a better way to do something." %}
{% include important.html content="Something the reader must know before going on." %}
{% include warning.html content="Something that can break the server or lose data." %}
{% include callout.html content="A highlighted block without a label." type="primary" %}


THE CALLOUT `type` is one of `danger`, `default`, `primary`, `success`, `info` or `warning`. See [Wiki Alerts and Callouts](wiki-alerts-and-callouts) for how each one looks.

THE TEXT in `content` is HTML, not markdown. Markdown written there is shown as plain characters, for example `**bold**` shows the asterisks. Use these tags instead:

| To get       | Write                                   |
| ------------ | --------------------------------------- |
| Bold         | `<b>text</b>`                           |
| Inline code  | `<code>text</code>`                     |
| A link       | `<a href='page-name'>text</a>`          |
| A line break | `<br/>`                                 |

THE `content` VALUE is wrapped in double quotes, so it must not contain a double quote. Use single quotes for HTML attributes (`href='...'`) and `&quot;` for a quotation mark in the text.

ONLY INLINE TAGS work in `content`. Paragraphs, lists, tables and code blocks do not. If a box needs them, use the long form described in [Wiki Alerts and Callouts](wiki-alerts-and-callouts).

KEEP EACH INCLUDE on one line, with an empty line before and after it.

### Version requirements box

A LIST OF REQUIRED VERSIONS, as at the top of each requirements page, is an `info` callout with one requirement per line. End every line except the last with `<br/>`. This is the one include that may span several lines:

{% raw %}
```
{% include callout.html content="Windows ≥ 10<br/>
Boost ≥ 1.78<br/>
MySQL ≥ 8.0 (Recommended 8.4)<br/>
CMake ≥ 3.16" type="info" %}
```
{% endraw %}

Preview:

{% include callout.html content="Windows ≥ 10<br/>
Boost ≥ 1.78<br/>
MySQL ≥ 8.0 (Recommended 8.4)<br/>
CMake ≥ 3.16" type="info" %}


DO NOT USE a table for this list.

### The help list

THE STANDARD "still having problems" LIST is added with an include that takes no content:

{% raw %}
```
{% include help.html %}
```
{% endraw %}

Preview:

{% include help.html %}


### Line breaks in tables

A TABLE CELL cannot contain a new line, so use `<br>` to break a line inside a cell.

### Collapsible sections

LONG OUTPUT OR OPTIONAL STEPS can be folded away with `<details>` and `<summary>`. Leave an empty line after the `<summary>` line and before `</details>`, so the markdown between them is rendered:

```
<details>
<summary>Click to show the full log</summary>

The folded content, written in markdown.

</details>
```

Preview:

<details>
<summary>Click to show the full log</summary>

The folded content, written in markdown.

</details>

### Images with a size

USE MARKDOWN for images (`![description](url)`). Use `<img>` only when the image needs a fixed width or height, and always give it an `alt` text:

```
<img src="url" alt="description" width="400">
```

## FILE HEADERS

THE FILE  SHOULD ALWAYS START WITH `# File Name`. (This is to display correct info in the browser tab.)

## DATABASE TABLE FILES:

ALL DATABASE TABLE FILES should be present in the correct DATABASE FILE.

When adding/removing a table it should also be updated in `database-auth` `database-characters` `database-world` and in `database-index`

ALL DATABASE TABLE FILES should follow the [Database Table Template](database-table-template), and every column should have a description.

## INSTALLATION GUIDE PAGES

EVERY STEP of the installation guide has the same navigation at the top and at the bottom of the page: one sentence, then the previous and the next step.

```markdown
# Server Setup

This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps.

| [<< Step 2: Core Installation](core-installation) | [Step 4: Database Installation >>](database-installation) |
| :-- | --: |
```

Preview:

This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps.

| [<< Step 2: Core Installation](core-installation) | [Step 4: Database Installation >>](database-installation) |
| :-- | --: |

THE NAVIGATION comes directly after the title. Notice boxes and everything else go below it, so the navigation is in the same place on every step.

ON A STEP PAGE THAT ONLY LINKS to the Linux, macOS and Windows pages, those three links come directly after the navigation, and notice boxes go below the links. That keeps the links in the same place when moving from one step to the next.

ON THE LINUX, macOS AND WINDOWS PAGES of a step, the previous and next links stay on the same operating system (Windows Core Installation goes back to Windows Requirements). Add a middle link, `[Choose another OS](step-page)`, that goes to the step's own page, and use `| :-- | :-: | --: |` so it is centred. On the first step there is no previous page for the operating system, so its previous link goes to the step's own page and no middle link is needed.

THE TWO LINKS are a table with a header row only. The wiki shows such a table at full width with two equal halves. The second row sets the alignment: `:--` is left, `--:` is right and `:-:` is centre. Leave a cell empty when there is no previous or no next step.

## COMMUNITY-MADE GUIDES

EVERY GUIDE listed under "Community made" on the [Installation Guide](installation) starts with this note, directly after the title. On a page with step navigation, the note comes directly after the navigation. If the guide has several pages, put it on each page:

{% raw %}
```
{% include note.html content="This guide is community-made. It may not be up to date and is not officially supported." %}
```
{% endraw %}

Preview:

{% include note.html content="This guide is community-made. It may not be up to date and is not officially supported." %}


WHEN YOU ADD a community-made guide, add this note to it and list the guide under "Community made" on the Installation Guide.

## LINKING WITHIN THE WIKI

When linking to a page in the wiki we use relative links. (`[home](home#overview)`).

When linking to a header on the same page in the wiki relative links. (`[withCapitalLetters](#withcapitalletters).`

It is important to note that only lowercase letters and no special characters are allowed in relative links. Otherwise, the links will be broken.

When linking to a page outside of the wiki we use absolute links. (`[Google](https://google.com)`).

## TRANSLATION

ALL TRANSLATIONS should be in a sub-directory of /docs/ with the shortened locale of the language. i.e./docs/es/. If there have been no translations prior, you need to allow the directory path in the config. See [this commit on how to do it](https://github.com/azerothcore/wiki/commit/8b897c3384298674e82108357ee5e655f788229f).

ALL FILES should be named the **exact same as the English versions**! Do not ever translate the file names, only the contents within.

## ARCHIVED PAGES:

ALL ARCHIVED PAGES that could potentially have some some value should be added to the [archive](archive) list and links to these pages should be removed from other places in the wiki.

They should also be moved into the /docs/archive/ folder. Translations of an archived page are moved into the archive folder of their own locale, i.e. /docs/es/archive/, keeping the exact same file name as the English version.

Pages in an archive folder keep the url they had before they were archived, so links from outside the wiki do not break, and they automatically get an archive notice at the top of the page.

If a locale gets its first archived page, you need to allow the directory path in `_config.yml`, the same way it is done for translations.
