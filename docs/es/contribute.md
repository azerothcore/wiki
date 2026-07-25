---
redirect_from: "/Contribute"
---

# Contribuir

Puedes contribuir de varias formas a AzerothCore:

- [Comentar un issue abierto](#how-to-comment-an-issue)

- [Abrir un issue](#how-to-open-an-issue)

- [Probar un pull request](#how-to-test-a-pull-request)

- [Probar cambios solo de base de datos](how-to-test-db-only-changes)

- [Crear un pull request](#how-to-create-a-pull-request)

- [Mejorar nuestra wiki](#improve-the-wiki)

## Información general

Para contribuir, obviamente necesitas una cuenta de github.

## Cómo comentar un issue {#how-to-comment-an-issue}

Puedes ayudar mucho revisando los [issues](https://github.com/azerothcore/azerothcore-wotlk/issues) y uniéndote a sus discusiones.

Una cosa que puedes hacer es actualizar tu core y comprobar si el issue sigue siendo válido en tu revisión; luego puedes escribir un comentario **incluyendo el hash del commit**.

## Cómo abrir un issue {#how-to-open-an-issue}

Cosas importantes que hacer antes de reportar un bug:

**1) Actualiza tu core a la última revisión de AzerothCore y comprueba si el bug sigue estando presente**

**2) Busca entre los [issues](https://github.com/azerothcore/azerothcore-wotlk/issues) para verificar si alguien ya reportó el bug; en ese caso solo tienes que comentar el issue para confirmar el bug (incluyendo tu revisión del core)**

Si **(y solo si)** el bug aún no ha sido reportado, puedes [abrir un issue](https://github.com/azerothcore/azerothcore-wotlk/issues/new) e incluir:

- la **descripción del bug**, incluidos cualquier **enlace** útil e **IDs/GUIDs/nombres** de cualquier entidad relacionada (NPCs, hechizos, gameobjects, etc.)
- la **revisión del core (hash del commit)** del AzerothCore en el que lo estás ejecutando, **no escribas solo "la última versión"** aunque acabes de actualizar tu core
- si se trata de un problema de build, sería útil conocer también tu **sistema operativo** y **versión del compilador**

## Cómo probar un Pull Request {#how-to-test-a-pull-request}

- Lee [Cómo probar un PR](how-to-test-a-pr).

## Cómo crear un Pull Request {#how-to-create-a-pull-request}

- Lee [Cómo crear un PR](how-to-create-a-pr).
- Alternativamente, también puedes consultar [este tutorial más simple](how-to-create-a-db-pr) sobre cómo abrir pull requests que contienen código SQL a través de GitHub.

### Dando crédito al autor del código

Si quieres enviar código escrito por otra persona, puedes dar créditos al autor cuando haces el commit:

`git commit --author="AuthorName <authoremail@address.com>" -am "Commit message here"`

Actualización: desafortunadamente, al fusionar un PR mediante squash del commit, GitHub establece automáticamente como autor del commit resultante a la persona que abrió el PR. Por este motivo, menciona al autor original (y al commit, si corresponde) en la descripción del PR.

## Mejora la Wiki {#improve-the-wiki}

¿Quieres mejorar o agregar una página a nuestra wiki? ¡Bien! Discutámoslo usando [nuestro chat](https://discord.gg/PaqQRkd).
