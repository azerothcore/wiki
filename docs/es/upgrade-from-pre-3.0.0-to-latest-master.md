# Actualización de la versión anterior a la 3.0.0 al último master

Este es el tutorial para actualizar cualquier servidor existente desde una versión anterior a la [versión 3.0.0](https://github.com/azerothcore/azerothcore-wotlk/releases/tag/v3.0.0) a la última versión `master`.

**Nota**: siempre se recomienda hacer una copia de seguridad de su base de datos antes de realizar CUALQUIER actualización.

### Paso 1. Actualiza a la última confirmación 3.0.0

Primero debe actualizar su servidor a [esta confirmación](https://github.com/azerothcore/azerothcore-wotlk/commit/2d609e9e48b2e516e4a555015b2662cab15b0c38), ejecutando:

```
git pull; git checkout 2d609e9e48b2e516e4a555015b2662cab15b0c38
```

Ahora actualice su **base de datos** como lo hace habitualmente (por ejemplo, usando el db-ensambler)

### Paso 2. Actualiza a la versión master más reciente

Actualizar al último master:

`git checkout master; git pull;`

** Nota **: si está utilizando su propio fork de AC, como de costumbre, debe [sincronizarla](Syncing-your-fork)

Ahora actualice su **núcleo y base de datos** (nuevamente) como [lo hace normalmente](Update).
