---
redirect_from: "/Upgrade-from-pre-2.0.0-to-latest-master"
---

# Actualización de previa a 2.0.0 a la última versión 

Este es el tutorial para actualizar cualquier servidor existente desde una versión anterior a la [versión 2.0.0](https://github.com/azerothcore/azerothcore-wotlk/releases/tag/v2.0.0) a la última versión `master`.

**Nota**: siempre se recomienda hacer una copia de seguridad de su base de datos antes de realizar cualquier actualización.

### Paso 1. Actualiza a la última confirmación 2.0.0

Primero debe actualizar su servidor a [esta confirmación](https://github.com/azerothcore/azerothcore-wotlk/commit/1fc22a74088e235e78fa02decbaf0864899477d7), ejecutando:

`git checkout 1fc22a74088e235e78fa02decbaf0864899477d7`

Ahora actualice su **base de datos** como [lo hace normalmente](Update#3-update-the-database).

### Paso 2. Actualiza a la versión master más reciente

Actualizar al último master:

`git checkout master; git pull;`

**Nota**: si está utilizando su propio fork of AC, como de costumbre, debe [sincronizarla](Syncing-your-fork)

Ahora actualice su **núcleo y base de datos** (nuevamente) como [lo hace normalmente](Update).
