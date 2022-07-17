---
redirect_from: "/Directory-Structure"
---

# Estructura del directorio

AzerothCore y nuestros módulos siguen la estructura de directorios estándar de hw-core:

[Estructura estándar del directorio](https://github.com/HW-Core/directory-structure/blob/master/README.md)

Esta estructura se ajusta a nuestra [arquitectura modular](The-Modular-Structure).

azerothcore/

├── [apps][1]<br/>
├── [bin][2]<br/>
├── [conf][3]<br/>
├── [data][4]<br/>
├── [deps][5]<br/>
├── [env][6]<br/>
├── [modules][7]<br/>
├── [src][8]<br/>
└── [var][9]<br/>

[1]: #apps
[2]: #bin
[3]: #conf
[4]: #data
[5]: #deps
[6]: #env
[7]: #modules
[8]: #src
[9]: #var

## Estructura del directorio de AzerothCore Wotlk en detalle:

### apps

Utilidades y aplicaciones con un nivel de conocimiento superior al de los módulos. Pueden actuar en las operaciones del ciclo de vida del proyecto como el CI, la instalación de módulos, la migración de la base de datos, etc.

Un ejemplo de aplicación es nuestro db_assembler que es capaz de crear y actualizar su instalación de base de datos.

### bin

Contiene los binarios/scripts de este proyecto. Esta carpeta puede ser colocada dentro de la variable envolvente PATH de tu sistema operativo, permitiéndote integrar los scripts CLI del proyecto con tu shell.

Un ejemplo es el script azerothcore dashboard, que le permite ejecutar directamente la aplicación de instalación, el db_assembler y las otras herramientas que vienen con el repo de azerothcore.

### conf

Los archivos de configuración que necesitan las apps/ y otras herramientas incluidas en nuestro repo. No es la carpeta donde se almacenan los archivos conf de worldserver y authserver porque la carpeta conf/ se utiliza sólo para el repositorio y no se compila.

Un ejemplo de archivo de configuración es el conf.sh.dist. Es un conf todo en uno utilizado por nuestras aplicaciones como el dashboard, el compilador, el db_assembler etc.

### data

Todos los datos estáticos no compilados con las fuentes.

Un ejemplo de datos son los archivos sql, los assets, etc.

Puede obtener más información sobre el Directorio SQL [aquí](sql-directory.md).

### deps

Se trata de una estructura de carpetas orientada al dominio. Por lo tanto, todas las carpetas definen un dominio empresarial específico. En este caso, cada carpeta representa un componente independiente que necesita el proyecto para funcionar. Todos los componentes se almacenan con una [estrategia monorepo](https://en.wikipedia.org/wiki/Monorepo). Todo el código que es genérico y no está relacionado con la lógica de Wotlk debe ser movido bajo un componente separado de la capa deps y manejado por un VCS apropiado.

La capa deps de AzerothCore puede ser utilizada y configurada para construir otras aplicaciones de servidor.

Un ejemplo de deps son las librerías de terceros como acelib y la libra g3dlite, pero también las librerías creadas por la organización azerothcore para un propósito genérico.

### modules

Se trata de una estructura de carpetas orientada al dominio. De hecho, la principal ventaja de esta estructura es su modularidad. Cada carpeta representa un [módulo](The-Modular-Structure) /plugin independiente que es opcional y puede ser usado para extender las funcionalidades del núcleo. Todos los módulos se almacenan con una estrategia multi-repo y son ignorados por git por defecto.

Un ejemplo de módulo son los transmog, el autobalance, los crossbattlegrounds, etc.

### env

Esta carpeta se utiliza para el entorno de distribución por defecto. Por defecto, el compilador generará los binarios, los archivos de configuración y todo lo necesario para la aplicación del servidor dentro de la carpeta /env/dist. Sin embargo, como se explica en el estándar de estructura de directorios, esta carpeta se puede utilizar para crear cualquier tipo de entornos encapsulados anidados.

### src

Todas las fuentes estrictamente relacionadas con esta aplicación/proyecto y la versión del servidor wotlk. Sigue una estructura de carpetas orientada a los roles. Esta es una estructura de directorios clásica vista en muchos frameworks. Los archivos están organizados por sus roles (juego, scripts, herramientas, etc.). Su principal beneficio es obtener rápidamente la imagen de todos los archivos para roles específicos.

### var

Es una carpeta cuyo contenido es ignorado por git. La carpeta var contiene datos volátiles como los archivos temporales de construcción. Nota: La carpeta var no se utiliza para almacenar los registros de worldserver/authserver, aunque sean datos volátiles, porque esos datos no están relacionados con el ciclo de vida del repositorio y residen dentro del **entorno de aplicación** (/env/dist).

![AC Layers](https://docs.google.com/drawings/d/e/2PACX-1vQDBXPZMAq2HSszx8BGxloxQ5cqDULLC2tCgCmO2uyAF6HH3s9RkDFZxbQVsmFY8xM8Y18rIQJg1mBU/pub?w=1413&h=945)
