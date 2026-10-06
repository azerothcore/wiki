# AzerothCore Wiki

Read in: [English :gb:](README.md) | [Español :es:](README_es.md)

Welcome to the AzerothCore Wiki! This repository provides comprehensive documentation for setting up, configuring, and customizing the AzerothCore WoW emulator. The live site is at [azerothcore.org/wiki](https://www.azerothcore.org/wiki/home).

If you want to contribute to the wiki please open a PR in the /docs/ directory.

Any problems? [Open an issue](https://github.com/azerothcore/wiki/issues/new).

## Running it locally

### With Docker

1. Install [Docker](https://docs.docker.com/get-docker/).
2. Run `docker compose up github-wiki-theme`
3. Open `http://localhost:4000/home`

### Without Docker

Requires [Ruby](https://jekyllrb.com/docs/installation/) and Bundler (`gem install bundler`).

> [!NOTE]
> These steps were tested on:
>
> - Windows 11 25H2 (OS Build 26200.9457) with Ruby 3.3.11 and Bundler 4.0.12
> - Ubuntu 24.04.3 LTS (kernel 6.8.0-90-generic, x86_64, systemd 255) with Ruby 3.3.0 and Bundler 4.0.19

#### With the test script

- Windows: double-click `wiki.bat` in the `tools` folder, or open a command prompt in `tools` and run `wiki build`
- Linux and macOS: in the `tools` folder run `./wiki.sh build`

The script installs the gems if needed, stops any old server still running on port 4000, and serves the site. Then open `http://localhost:4000/wiki/home`.

The first run can be slow, because Jekyll has to generate more than 500 pages (see [Build times](#build-times)). `--verbose` is enabled by default, so each page is printed as it is built and you can see that Jekyll has not hung. If you would rather not see the build progress, remove `--verbose` from the last line of the script.

##### Options

Add these words after the script name. They can be combined, in any order. In PowerShell write `.\wiki` instead of `wiki`.

| Option  | What it does |
| :------ | :----------- |
| `build` | Builds the English pages only, reusing the previous build. This is the fast, everyday mode, and what the script does when no option is given. |
| `all`   | Also builds the Spanish and Chinese translations. That is about 1,500 pages, so it takes much longer. |
| `clean` | Throws away the previous build and the downloaded theme, and rebuilds everything. Use it if a page looks stale or wrong, or after changing the sidebar, a layout or `_config.yml`. |

Without `clean`, the script reuses the previous build and only renders the pages that changed. For that it keeps the theme in the `.theme-cache` folder, which is not committed.

Windows, from the `tools` folder:

```
wiki build
wiki build all
wiki clean
wiki clean all
```

Linux and macOS, from the `tools` folder:

```bash
./wiki.sh build
./wiki.sh build all
./wiki.sh clean
./wiki.sh clean all
```

##### Build times

When the build finishes, the script prints how long it took and which options were used. These are the times measured so far:

| System | Command | Pages | Time |
| :----- | :------ | :---- | :--- |
| Windows 11 | `wiki clean` | about 560 (English only) | about 6 minutes |
| Windows 11 | `wiki clean all` | about 1,500 (English and 2 translations) | about 40 minutes |
| Ubuntu 24.04 | `./wiki.sh clean` | about 560 (English only) | about 8 minutes |
| Ubuntu 24.04 | `./wiki.sh clean all` | about 1,500 (English and 2 translations) | about 54 minutes |

After the first build, saving a page only rebuilds that page, which takes about 10 seconds.

The site is served on `127.0.0.1`, so only your own computer can open it. To let other devices on your network reach it, set `JEKYLL_HOST=0.0.0.0` before running the script:

Windows:

```
set "JEKYLL_HOST=0.0.0.0"
wiki build
```

Linux and macOS:

```bash
JEKYLL_HOST=0.0.0.0 ./wiki.sh build
```

Local previews do not create the redirects from old page addresses, because on Windows and macOS those would overwrite the real pages.

#### Manually

Copy `.env-files/Gemfile.github` to the root of the repository and name it `Gemfile`. Jekyll only loads the theme and the GitHub Pages plugins when the Gemfile is there. The copy is git-ignored. Then run:

```bash
bundle install
bundle exec jekyll serve --baseurl /wiki
```

Then open `http://localhost:4000/wiki/home`. Jekyll watches the files and rebuilds on save, so just refresh the browser.

The `--baseurl /wiki` part makes the sidebar links work: they point to `/wiki/...` like on the live site.

## Tools

The `tools` folder has the scripts used to preview and maintain the wiki. The Python scripts need Python 3 and are run from the wiki folder.

| Script | What it does |
| :----- | :----------- |
| `wiki.bat`, `wiki.sh` | Builds and serves the wiki locally. See [With the test script](#with-the-test-script). |
| `update_table_lists.py` | Adds new table and DBC pages to the lists and indexes. |
| `update_gm_commands.py` | Updates the GM Commands page from a database. |
| `local_theme_cache.rb` | Loaded by the build scripts to keep the theme between builds. It is not run by hand. |

A script that changes pages writes a log of what it changed to `tools/logs`, which is not committed. `--log file.log` writes it to another file.

### Table and DBC lists

Run it after adding a database table page or a DBC page:

```
python tools/update_table_lists.py --check
python tools/update_table_lists.py
```

`--check` only reports what is missing. Without it, the script:

- adds new table pages to `database-auth`, `database-characters` or `database-world` and to the Database Index, under the right letter. The database is read from the back link at the top of the page.
- adds new DBC pages to the DBC Index.
- sets the bullet of each entry: a dot for a page with descriptions, a diamond for a page that only has column names and types.
- keeps the number of DBC files on the index pages correct.

The languages and databases it works on are set at the top of the script. Another docs folder can be given as the first argument: `python tools/update_table_lists.py path/to/docs`.

### GM Commands page

The script reads the `command` table of a running AzerothCore database and updates `docs/gm-commands.md`:

```
python tools/update_gm_commands.py
python tools/update_gm_commands.py -y
python tools/update_gm_commands.py --check
python tools/update_gm_commands.py --host 10.0.0.5 --user root --password secret
```

Without options it asks for the connection, and Enter keeps a default (`acore` / `acore` on `127.0.0.1:3306`, databases `acore_world` and `acore_auth`). `-y` uses the defaults without asking.

| Option | What it does |
| :----- | :----------- |
| `--check` | Only reports what would change. |
| `--host`, `--port`, `--user`, `--password`, `--world-db`, `--auth-db` | Connection settings. |
| `--no-rbac` | Does not read the RBAC tables. |
| `--replace-rbac` | Also replaces the RBAC column of commands that are already on the page. |
| `--remove-missing` | Deletes commands that are no longer in the database, instead of flagging them for review. |
| `--page` | Path to another `gm-commands.md`. |

Security and Syntax come from the database. Descriptions that are already on the page are kept, and a new command gets the help text of the database as its description. It needs PyMySQL, mysql-connector-python or the `mysql` command line client.

## Project structure

- `docs/` - the wiki pages, one Markdown file per page. `docs/es/` and `docs/cn/` hold the translations, `docs/archive/` the archived pages.
- `_includes/` - shared HTML: the sidebar (`azerothcore/sidebar.html`) and the notice boxes.
- `_layouts/`, `_sass/`, `assets/` - page templates, styling and scripts.
- `images/` - images used in the pages.
- `_config.yml` - the Jekyll configuration.
- `.env-files/`, `docker-compose.yml`, `tools/` - what is needed to run the site locally.

## Adding content

- Read the [Wiki Standards](https://www.azerothcore.org/wiki/wiki-standards) first.
- **New or changed page**: add or edit a Markdown file in `docs/`. `docs/my-page.md` is published as `/wiki/my-page`.
- **Database table page**: follow the [Database Table Template](https://www.azerothcore.org/wiki/database-table-template). Then run `python tools/update_table_lists.py` to add it to the lists (see [Tools](#tools)).
- **Sidebar**: edit `_includes/azerothcore/sidebar.html`.

## Deployment

The site is built and published from the `master` branch. There is no manual deploy step.
