# La estructura modular

Basado en nuestra [estructura de directorios](Directory-Structure) modular basada en dominios, el proyecto AzerothCore te permite añadir y ampliar las características del juego añadiendo módulos aislados personalizados, sin necesidad de parchear el núcleo directamente.

El resultado es tener siempre un núcleo limpio que es fácil de mantener y mantenerlo sincronizado con las últimas actualizaciones de AzerothCore.

## Hooks

### Script hooks

Para cambiar las características del juego, los módulos utilizan **script hooks**, que son una colección de funciones [implementadas en el núcleo: ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h) y son capaces de operar desde el principio del servidor (tan pronto como comienza la inicialización del Mundo).

La lista de los hooks de scripts está disponible [aquí](Hooks-Script).

A veces necesitas añadir nuevos hooks para tu módulo personalizado, es absolutamente posible añadirlos al núcleo. Sólo hay unos pocos pasos necesarios para crear un nuevo hook, por favor, siga esta guía [aquí](hooks-script) para aprender cómo.

Cuando añadas nuevos hooks, no olvides [crear un PR](http://www.azerothcore.org/wiki/How-to-create-a-PR) con ellos. De esta manera, serán revisados por los desarrolladores de AzerothCore e incluidos en el repositorio oficial.

### Cmake hooks

Los hooks de CMake permiten a los módulos ejecutar operaciones durante la fase de compilación de AzerothCore. Esto puede utilizarse, por ejemplo, para instalar y cargar archivos `*.conf` personalizados durante el inicio del servidor.

Así, los módulos pueden tener sus propios archivos de configuración y puedes **evitar parchear** el archivo `worldserver.conf.dist`.

La lista de los hooks de CMake está disponible [aquí](hooks-cmake).

### Bash hooks

Los hooks Bash permiten que los módulos interactúen con la consola bash de AzerothCore. Con él, puedes añadir operaciones automatizadas cada vez que se añada o elimine el módulo mediante la consola bash de AzerothCore.

Esto se puede utilizar, por ejemplo, para ejecutar automáticamente el código SQL que añadiría tablas adicionales en la DB cuando se instala un módulo, y eliminarlas cuando se desinstala.

Para interactuar con nuestro sistema bash, crea y utiliza `include.sh` en tu directorio raíz.

La lista de los hooks de CMake está disponible [aquí](hooks-bash).

## Cómo crear un módulo

Puedes empezar a crear tu primer módulo leyendo [cómo crear un módulo](Create-a-Module).
