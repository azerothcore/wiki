# Sistema BASH

AzerothCore utiliza un sistema bash avanzado que nos permite automatizar procesos como la **compilación de fuentes, la instalación de módulos, la configuración de la base de datos, etc.**

Por ahora, estamos usando bash en lugar de Python para reducir las dependencias externas, ya que BASH es un lenguaje de scripting multiplataforma que ya está incluido con **OSX, Linux y Windows** (a través de GIT BASH que le pedimos que instale en nuestros requisitos).

Puede leer la documentación oficial de bash aquí: https://tldp.org/LDP/abs/html/index.html

## Panel ACORE 

Nuestros scripts de bash relacionados con azerothcore se pueden encontrar dentro de la carpeta /app, pero también creamos un script llamado **acore.sh** dentro de la carpeta raíz.
Este script ejecuta un panel que contiene los comandos para ejecutar todos los scripts relacionados con la carpeta /app.

Ejecute `./acore.sh --help` para obtener la lista completa de comandos disponibles.

### Configuración

La carpeta /conf disponible en el directorio raíz de nuestro proyecto se utiliza para darle la posibilidad de cambiar las configuraciones de todos nuestros scripts bash.

### Modo interactivo

ejecute `./acore.sh`  y puede usar el panel en modo interactivo: puede navegar dentro del menú y submenú del panel y ejecutar el comando que necesita.

### Argumentos de comando

Puede utilizar los comandos del panel como argumentos del script ./acore.sh. Por ejemplo:

`./acore.sh compiler configure` ejecutará el proceso de configuración de nuestro compilador c++

Todos los comandos vienen con un alias más corto. Por ejemplo, `./acore.sh c configure` ejecutará la configuración del compilador, pero también `./acore.sh 5 3` lo hará.

## Dependencias

Nuestro sistema bash utiliza bibliotecas bash externas que son genéricas y no están relacionadas con el propio azerothcore, esas bibliotecas han sido creadas por nosotros y se han colocado en la carpeta / deps

## GANCHOS:

Interno [Sistema de gancho para bash](hooks-bash)

## Otros recursos

- Comando bash único para instalar azerothcore: [Video + secuencia de comandos en la descripción](https://www.youtube.com/watch?v=j1HI6pLZZvM)
