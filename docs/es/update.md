# Cómo actualizar AzerothCore a la última versión estable

## Verifica que estás en la última versión

1. Escriba `.server debug` en su consola.
  
    1. Si muestra `Using World DB: ACDB 335.4-dev` entonces puede proceder a [Actualizar su fuente local](#update-your-local-source).
  
    1. Si genera algo más para `Using World DB:` entonces primero debe seguir [esta guía sobre la actualización al último master](upgrade-from-pre-3.0.0-to-latest-master.md).

También recomendamos encarecidamente seguir el canal de #announcements  en el discord de AzerothCore para que sepa sobre cualquier otro cambio importante en AzerothCore.

## Actualiza tu fuente local

Vaya a su directorio de fuentes de AzerothCore.

- Si tienes tu propio fork de AzerothCore, necesitas [sincronizarlo](Syncing-your-fork).

- De lo contrario, si clonó AzerothCore directamente desde el repositorio principal, debe hacer un  `git pull` para actualizarlo.

## Recompilar

Vuelva a compilar sus fuentes, este paso es el mismo que el [Paso de compilación durante la instalación](Installation#3-compiling), pero generalmente puede omitir la parte de CMake a menos que esté agregando nuevos módulos.

Por ejemplo, en Linux/Mac sólo tiene que hacer `cd build;` y ejecutar `make -j 8; make install`. Por supuesto, puede cambiar el valor del parámetro `-j` de acuerdo con su CPU.

## Actualizar la base de datos

**Si está actualizando su entorno de producción, ¡HAGA UNA COPIA DE SEGURIDAD de sus bases de datos ANTES de actualizarlas!**

Debe importar los **nuevos** archivos de actualización de sql (ubicados en https://github.com/azerothcore/azerothcore-wotlk/tree/master/data/sql/updates) a cada base de datos.

Para automatizar este proceso, puede utilizar el script bash db-assembler `bash apps/db_assembler/db_assembler.sh`.

Si es la primera vez que lo usa [LEA ESTO PRIMERO](database-installation.md) y configure correctamente su archivo `conf/config.sh`.

![](https://user-images.githubusercontent.com/75517/50738699-6912ee80-11d7-11e9-95ea-667baa0bda70.png)
