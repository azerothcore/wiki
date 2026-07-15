# Cómo usar el changelog

Todos los cambios que rompen compatibilidad/notables de este proyecto se documentarán en el archivo `/docs/changelog/master`.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto se adhiere al [Versionado Semántico](project-versioning).

**Este changelog debería proporcionar una forma sencilla para que los desarrolladores actualicen su propio código que está conectado a AzerothCore** (p. ej. módulos, APIs, scripts, etc.)
No es una forma de llevar un registro de TODOS los cambios realizados (para eso tenemos el historial de git). Por tanto, solo 2 reglas de oro a seguir:

- **SÍ ESCRIBE** en el changelog cuando hayas añadido cambios que rompen compatibilidad, arreglos de seguridad o nuevas funcionalidades importantes que otras personas puedan usar.
- **NO ESCRIBAS** en el changelog cuando estés añadiendo pequeños arreglos o mejoras menores.

## Cómo crear un changelog

La creación de un changelog para un PR es similar a la creación de un nuevo archivo sql.
En la carpeta `doc/changelog/pendings` encontrarás un script `create.sh`.

Ejecuta este script para crear un nuevo archivo de changelog en la misma carpeta que se llamará automáticamente `changes_<timestamp>.md`.

Una vez que el PR se integre, nuestro pipeline fusionará tu archivo en `doc/changelog/master` creando automáticamente una nueva sección dentro de ese archivo.
Esta sección se titulará con el nuevo número de versión basado en el anterior del archivo `acore.json` que puedes encontrar en la carpeta raíz.

Así, por ejemplo:

si la versión actual es `1.0.0-dev.1`, después de que tu PR se integre se cambiará a `1.0.0-dev.2` automáticamente dentro de `acore.json` y se creará una nueva sección 
llamada `## 1.0.0-dev.2` bajo el changelog `master`.

Este enfoque también es bastante útil para que los módulos lleven un registro de la compatibilidad

## Cómo escribir un changelog

Es obligatorio usar el formato "[Keep a Changelog](https://keepachangelog.com/en/1.0.0/)", usando correctamente los siguientes tipos de títulos de sección:

- Added para nuevas funcionalidades.
- Changed para cambios en funcionalidad existente.
- Deprecated para funcionalidades que pronto serán eliminadas.
- Removed para funcionalidades ya eliminadas.
- Security en caso de vulnerabilidades.

Tienes que crear una nueva sección H3 ( `###` en markdown) para cada tipo diferente de cambios.

Por ejemplo:

```
### Added

- new hooks X, Y
- new formula for Z

### Changed

- return value for hook X, now it's boolean instead of void
```

### Documentar cómo actualizar

Después de las secciones anteriores tienes que describir los pasos necesarios para actualizar el código. Esta es la **parte más importante** y es particularmente útil para los autores de módulos para arreglar su código basándose en lo que cambiaste sin tener que leer con dificultad toneladas de commits y buscar información por ahí.

Para ello, puedes usar la sección ```### How to upgrade``` generada por nuestro `create.sh`. 
Por favor, sé lo más detallado posible. 
Si las directrices son muy largas y requieren más de unas pocas líneas (una página wiki entera, por ejemplo), puedes simplemente enlazar esa página.

Ejemplo:

```
### How to upgrade

- The hook OnCheck of the Achievement script class now returns a boolean instead of a void. Add `return true` to your methods if you don't want to change the original behaviour. 
```

## Cómo lanzar una nueva versión mayor

Este es un proceso manual. Cada vez que lanzamos una nueva versión mayor (4.0.0, 5.0.0, etc.) necesitamos mover el `master` a la carpeta `doc/changelog/previous-versions` y renombrarlo usando este formato: `v[major].x`. Después de eso tenemos que crear un nuevo archivo `master` vacío
