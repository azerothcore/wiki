# Contribuir

Puedes contribuir de varias formas a AzerothCore:

- [comentando un problema abierto](Contribute#how-to-comment-an-issue)

- [abriendo un problema](Contribute#how-to-open-an-issue)

- [prueba de una solicitud de extracción](How-to-test-a-PR)

- [prueba de cambios solo de base de datos](How-to-test-DB-only-changes)

- [creando una solicitud de extracción](Contribute#how-to-create-a-pull-request)

- [mejorando nuestra wiki](Contribute#improve-the-wiki)
## Información general

Para contribuir, obviamente necesitas una cuenta de github.

## Cómo comentar un problema

Puede ayudar mucho revisando los [problemas](https://github.com/azerothcore/azerothcore-wotlk/issues) y uniéndose a sus discusiones.

Una cosa que puede hacer es actualizar su núcleo y verificar si el problema sigue siendo válido en su revisión, luego puede escribir un comentario **que incluya el hash de confirmación**.

## Cómo abrir un problema

osas importantes que hacer antes de informar un error:

**1) Actualice su núcleo a la última revisión de AzerothCore y compruebe si el error sigue ahí.**

**2) Busque entre los [problemas](https://github.com/azerothcore/azerothcore-wotlk/issues) para verificar si alguien ya informó el error, en ese caso solo tiene que comentar el problema para confirmar el error (incluida su revisión principal)**

Si **(y solo si)** el error aún no se ha informado, puede [abrir un problema](https://github.com/azerothcore/azerothcore-wotlk/issues/new) e incluir:

- La **descripción del error**, incluidos los **enlaces** útiles y **ID/GUID/nombres** de cualquier entidad relacionada (NPC, hechizos, objetos de juego, etc.)
- La **revisión del núcleo (hash de confirmación)** del AzerothCore en el que está ejecutando, **no escriba solo la "última versión"** incluso si acaba de actualizar su núcleo.
- Si se trata de un problema de compilación, sería útil conocer también su **sistema operativo** y **versión del compilador**.

## Cómo probar una solicitud de extracción

- Lea [Cómo probar un PR](How-to-test-a-PR).

## Cómo crear una solicitud de extracción

- Lea [Cómo crear un PR](How-to-create-a-PR).

### Dando crédito al autor del código

Si desea enviar un código escrito por otra persona, puede otorgarle créditos al autor cuando se comente:

`git commit --author="AuthorName <authoremail@address.com>" -am "Confirma el mensaje aquí"`

Actualización: desafortunadamente, al fusionar un PR aplastando el comentario, GitHub establece automáticamente al autor del compromiso resultante como la persona que abrió el PR. Por esta razón, mencione al autor original (y comprometa, si corresponde) en la descripción del PR.

## Mejora la Wiki

¿Quieres mejorar o agregar una página a nuestro wiki? ¡Bien! Discutámoslo usando [nuestro chat](https://discord.gg/PaqQRkd).
