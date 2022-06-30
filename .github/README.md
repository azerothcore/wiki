# AzerothCore WIKI

Read in: [English :gb:](README.md) [Spanish :es:](README_es.md)

Wiki for the AzerothCore Project available here: http://azerothcore.github.io/wiki

## How to install locally (development)

### With [docker-compose](https://docs.docker.com/compose/install/)

1. install [docker-compose](https://docs.docker.com/compose/install/)
2. run `docker-compose up github-wiki-theme`
3. the website will be ready on `http://127.0.0.1:4000/`

### Without docker compose

First of all install the [ruby development environment](https://jekyllrb.com/docs/installation/) using [this guide](https://jekyllrb.com/docs/installation/).

After that install `bundler` using gem and run `bundler install`:

```
$ gem install bundler
$ bundle install
```

Well, now you can run locally the app using:

```
bundle exec jekyll serve
```

If everything succeds, you can visit your web app at `http://127.0.0.1:4000/`.

Any problems? [Open a issue](https://github.com/azerothcore/wiki/issues/new).
