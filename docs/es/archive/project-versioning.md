---
redirect_from: "/Project-Versioning"
---

## Versionado del proyecto

Usamos el estándar de versionado semántico:

http://semver.org/spec/v2.0.0.html

Por ejemplo, podemos tener: **1.5.1-dev.1** que corresponde a: **MAJOR.MINOR.PATCH-PRERELEASE**

Con más detalle:

* Versión **MAJOR** cuando haces cambios incompatibles en la API / estructura de la BD. En AzerothCore lanzamos una versión MAJOR de vez en cuando y a partir de entonces solo damos soporte a arreglos de seguridad (lee la sección de abajo). Por tanto, esta versión puede verse más como un Milestone. 

* Versión **MINOR** cuando añades funcionalidad de forma retrocompatible. Esto está mayormente sin usar en AC, ya que no importamos ninguna funcionalidad nueva después de lanzar una versión MAJOR.

* Versión **PATCH** cuando haces arreglos de bugs y de seguridad retrocompatibles.

* **PRERELEASE** esto es lo que se llama "metadata" en el estándar semver. Usamos esta parte del versionado mientras trabajamos en la rama **master**. Cada vez que se lanza una nueva funcionalidad o un cambio que rompe compatibilidad (tanto en código como en BD), este número se incrementa para notificarte sobre posibles acciones a realizar. Consulta [cómo usar el changelog](how-to-use-changelog).

### PRERELEASE primero

AzerothCore aún no se considera un software "completado", por lo que está constantemente en fase de desarrollo. El versionado descrito arriba se usará principalmente para proporcionar una forma sencilla de comprobar si un módulo, script o cualquier cosa conectada a AC es compatible o no con AC y qué hacer para actualizarlo.

Nuestra estrategia es (en orden de las acciones más comunes):

- no actualizar la versión cuando los cambios son solo pequeños arreglos/cambios de mantenimiento
- actualizar la versión prerelease `-dev.x` en master cuando tenemos cambios que rompen compatibilidad o nuevas funcionalidades
- subir la versión mayor cuando decidimos lanzar una nueva versión estable
- si se importa algún nuevo parche de seguridad o funcionalidad dentro de la versión mayor lanzada, esos incrementarán entonces la versión minor/patch, pero lo hacemos muy ocasionalmente.

## Fases de desarrollo

* **FASE 1: Fase de desarrollo**: durante la fase de desarrollo, usaremos la rama master, donde podemos hacer libremente cambios en la API, la BD y todo lo que pueda romper la compatibilidad con revisiones antiguas. 
Al inicio de cada fase de desarrollo, limpiaremos las carpetas sql/updates archivando los SQLs antiguos.

  N.B. 
  * Algunos trabajos grandes, como reescribir/implementar funcionalidades, podrían no estar listos para la siguiente revisión y eventualmente se planificarán para una futura, por lo que se mantendrán en ramas dedicadas en lugar de en master. 
  * Usando la rama master tendrás acceso inmediato a nuevas funcionalidades geniales, pero debes tener cuidado ya que algunos commits pueden romper la estabilidad en algunos casos raros.


* **FASE 2: Solo arreglos de estabilidad y seguridad**: en esta fase dejaremos de importar arreglos de mecánicas / contenido y ofreceremos soporte solo a problemas de seguridad y estabilidad. Por ejemplo: si una función genera un crash por un puntero nulo, lo arreglaremos.

  Podríamos eventualmente extender esta fase si muchas personas lo solicitan.

* **FASE 3: Fin de vida ( EOL )**: archivaremos esa release manteniendo, por supuesto, la documentación y la rama. Puedes seguir usándola/descargándola, pero no ofreceremos ningún soporte oficial de ningún tipo

## Lista de releases

NOTA: esto está desactualizado, consulta nuestras [releases](https://github.com/azerothcore/azerothcore-wotlk/releases) en github
  
| version/branch | codename  | description | current state | release data | end of support|
|     --         |    --     |      --     |           --  |       --     |      --       |
|     0.x        |  Sunwell|  small reworks for sunwell  |EOL|      2016 Q3 |      2017  Q1 |
|     1.x        |  Mimiron | first version to introduce the module system | EOL|     2017 Q1 |      2019  Q1 |
|     2.x        |  Gunship | Integrated CI/CD and tons of fixes  | Security & Stability   |     2019 Q1 |      ~ |
|     master (3.x)        |  ~ | ~ | developing |     ~ |      ~|
