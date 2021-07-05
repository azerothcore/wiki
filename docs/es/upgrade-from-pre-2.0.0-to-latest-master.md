# Actualizaci�n de previa a 2.0.0 a la �ltima versi�n 

Este es el tutorial para actualizar cualquier servidor existente desde una versi�n anterior a la [versi�n 2.0.0](https://github.com/azerothcore/azerothcore-wotlk/releases/tag/v2.0.0) a la �ltima versi�n `master`.

**Nota**: siempre se recomienda hacer una copia de seguridad de su base de datos antes de realizar cualquier actualizaci�n.

### Paso 1. Actualiza a la �ltima confirmaci�n 2.0.0

Primero debe actualizar su servidor a [esta confirmaci�n](https://github.com/azerothcore/azerothcore-wotlk/commit/1fc22a74088e235e78fa02decbaf0864899477d7), ejecutando:

`git checkout 1fc22a74088e235e78fa02decbaf0864899477d7`

Ahora actualice su **base de datos** como [lo hace normalmente](Update#3-update-the-database).

### Paso 2. Actualiza a la versi�n master m�s reciente

Actualizar al �ltimo master:

`git checkout master; git pull;`

**Nota**: si est� utilizando su propio fork of AC, como de costumbre, debe [sincronizarla](Syncing-your-fork)

Ahora actualice su **n�cleo y base de datos** (nuevamente) como [lo hace normalmente](Update).
