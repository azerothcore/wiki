# Cómo probar los cambios en la base de datos

## Introducción

La guía principal sobre [Cómo probar un PR](How-to-test-a-PR) servirá para todo tipo de PR.

Sin embargo, es común tener PRs que sólo hacen cambios en la base de datos (típicamente la base de datos `world`).

Para estos PRs hay una forma más sencilla de probarlos, que se explicará en esta página.

**Consejo**: La lista completa de los PR que deben ser examinados está disponible [aquí].(https://github.com/azerothcore/azerothcore-wotlk/pulls?q=is%3Apr+is%3Aopen+label%3A%22Waiting+to+be+tested%22).

## Requisitos

Este tutorial asume que usted:

- Tiene una versión **reciente** de AzerothCore instalada en tu sistema (ya sea usando la [instalación tradicional](Installation) o la [instalación Docker](Install-with-Docker)). Recomendamos utilizar la última versión de `master`.
- Tiene una cuenta en GitHub, puede [registrar una aquí](https://github.com/join) de forma gratuita.
- Tiene un cliente de base de datos como [HeidiSQL](https://www.heidisql.com/), Navicat o similar.

## Comprobar si un PR sólo tiene cambios en la BD

Abra la página de PR (pull request) y haga clic en la pestaña "Cambios de archivo" (File Changes):

![File Changes](https://user-images.githubusercontent.com/75517/52176720-ea4da900-27b6-11e9-8459-d58adf7fd50c.png)

- Si ves cambios en los archivos `*.cpp`, `*.h`, entonces sigue [esta guía](How-to-test-a-PR) en su lugar.

- Si sólo ves cambios en `*.sql`, sigue leyendo.

## Importe los cambios a su base de datos

El PR tendrá algunos archivos sql (normalmente sólo uno) dentro de las carpetas `pending_db_xxxxx` donde `xxxxx` es el nombre de la base de datos (normalmente `world`).

Básicamente, sólo hay que importar esos cambios a la base de datos correspondiente (normalmente `acore_world`).

Para ello, haga clic en el botón "Ver archivo" en la pestaña "Cambios en el archivo" de la página de PR. Puede descargar todo el archivo o simplemente copiar manualmente todo el código SQL.

A continuación, abre tu cliente de base de datos (por ejemplo, HeidiSQL), selecciona la base de datos adecuada (por ejemplo, `acore_world`) y ejecuta el código SQL.

Por ejemplo, en HeidiSQL **selecciona primero** la base de datos de la columna de la izquierda, luego abre la pestaña "Consulta", pega allí el código SQL y pulsa F9 para ejecutarlo:

![HeidiSQL import example](https://user-images.githubusercontent.com/75517/52532889-e4624580-2d2b-11e9-8325-aa587c2d080d.png)

## Reflejar los cambios en el juego

Una forma rápida de hacer que su servidor cargue los nuevos cambios es simplemente reiniciando el proceso `worldserver`.

**Consejo**: Si está usando AC con Docker, puede simplemente reiniciar su contenedor de base de datos usando `docker-compose restart ac-worldserver`.

**Consejo avanzado**: A veces los cambios sólo afectan a las tablas que se pueden recargar directamente en el juego mediante el comando `.reload tablename`.

¡Ahora puedes probar los cambios y publicar tus resultados como comentario en la página de github del PR!

## Volver a un estado limpio

Después de probar los cambios, tiene que volver en un estado limpio (como estaba antes de aplicar esos cambios a su DB).

- En una configuración **tradicional**, puedes eliminar tu base de datos `acore_world` y utilizar el ensamblador de BD para generar una nueva

- En una configuración de **docker**, puedes destruir y recrear tus contenedores usando `docker-compose down` y `docker-compose up`.

## Informes

Para obtener instrucciones sobre lo que hay que probar, cómo informar de los resultados de las pruebas y ejemplos de otros informes, lea [esta parte](How-to-test-a-PR#what-needs-to-be-tested) de la guía principal del PR.
