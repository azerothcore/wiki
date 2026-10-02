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

- Windows: double-click `test_locally.bat`
- Linux and macOS: run `bash test_locally.sh`

The script installs the gems if needed, stops any old server still running on port 4000, and serves the site. Then open `http://localhost:4000/wiki/home`.

The first run can be slow, because Jekyll has to generate more than 500 pages. `--verbose` is enabled by default, so each page is printed as it is built and you can see that Jekyll has not hung. If you would rather not see the build progress, remove `--verbose` from the last line of the script.

The script uses `_config.local.yml` on top of `_config.yml`. That file leaves out the translations to keep the build short; remove `docs/es` and `docs/cn` from its `exclude` list to build them too.

Run it with `clean` (`test_locally.bat clean`) to throw away the previous build and rebuild everything. Do this if a page looks stale or wrong.

Local previews do not create the redirects from old page addresses, because on Windows and macOS those would overwrite the real pages.

The site is served on `127.0.0.1`, so only your own computer can open it. Set `JEKYLL_HOST=0.0.0.0` before running the script if other devices on your network need to reach it.

#### Manually

Copy `.env-files/Gemfile.github` to the root of the repository and name it `Gemfile`. Jekyll only loads the theme and the GitHub Pages plugins when the Gemfile is there. The copy is git-ignored. Then run:

```bash
bundle install
bundle exec jekyll serve --baseurl /wiki
```

Then open `http://localhost:4000/wiki/home`. Jekyll watches the files and rebuilds on save, so just refresh the browser.

The `--baseurl /wiki` part makes the sidebar links work: they point to `/wiki/...` like on the live site.

## Project structure

- `docs/` - the wiki pages, one Markdown file per page. `docs/es/` and `docs/cn/` hold the translations, `docs/archive/` the archived pages.
- `_includes/` - shared HTML: the sidebar (`azerothcore/sidebar.html`) and the notice boxes.
- `_layouts/`, `_sass/`, `assets/` - page templates, styling and scripts.
- `images/` - images used in the pages.
- `_config.yml` - the Jekyll configuration.
- `.env-files/`, `docker-compose.yml` - what is needed to run the site locally.

## Adding content

- Read the [Wiki Standards](https://www.azerothcore.org/wiki/wiki-standards) first.
- **New or changed page**: add or edit a Markdown file in `docs/`. `docs/my-page.md` is published as `/wiki/my-page`.
- **Database table page**: follow the [Database Table Template](https://www.azerothcore.org/wiki/database-table-template).
- **Sidebar**: edit `_includes/azerothcore/sidebar.html`.

## Deployment

The site is built and published from the `master` branch. There is no manual deploy step.
