# AzerothCore WIKI

Leer en: [Ingles :gb:](README.md) | [Español :es:](README_es.md)

Wiki para el proyecto AzerothCore disponible aquí: http://azerothcore.github.io/wiki/es

## Cómo instalar localmente (desarrollo)

### Con [docker-compose](https://docs.docker.com/compose/install/)

1. Instalar [docker-compose](https://docs.docker.com/compose/install/)
2. Ejecutar `docker-compose up github-wiki-theme`
3. El sitio web estará listo el `http://127.0.0.1:4000/`

### Sin docker compose

En primer lugar, instale el [entorno de desarrollo ruby](https://jekyllrb.com/docs/installation/) utilizando [esta guía](https://jekyllrb.com/docs/installation/).

Después de eso, instale `bundler` usando la gema y ejecute `bundler install`:

```
$ gem install bundler
$ bundle install
```

Pues bien, ahora puedes ejecutar localmente la aplicación utilizando:

```
bundle exec jekyll serve
```

Si todo ha ido bien, puedes visitar tu aplicación web en `http://127.0.0.1:4000/`.

¿Algún problema? [Abrir una incidencia](https://github.com/azerothcore/wiki/issues/new).
