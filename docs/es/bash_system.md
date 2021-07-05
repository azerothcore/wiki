# Sistema BASH

AzerothCore utiliza un sistema bash avanzado que nos permite automatizar procesos como la **compilaci�n de fuentes, la instalaci�n de m�dulos, la configuraci�n de la base de datos, etc.**

Por ahora, estamos usando bash en lugar de Python para reducir las dependencias externas, ya que BASH es un lenguaje de scripting multiplataforma que ya est� incluido.
con ** OSX, Linux y Windows ** (a trav�s de GIT BASH que le pedimos que instale en nuestros requisitos).

Puede leer la documentaci�n oficial de bash aqu�: https://tldp.org/LDP/abs/html/index.html

## Panel ACORE 

Nuestros scripts de bash relacionados con azerothcore se pueden encontrar dentro de la carpeta /app, pero tambi�n creamos un script llamado **acore.sh** dentro de la carpeta ra�z.
Este script ejecuta un panel que contiene los comandos para ejecutar todos los scripts relacionados con la carpeta /app.

run `./acore.sh --help` para ver la lista completa de los comandos disponibles.

### Configuraci�n

La carpeta /conf disponible en el directorio ra�z de nuestro proyecto se utiliza para darle la posibilidad de cambiar las configuraciones de todos nuestros scripts bash.

### Modo interactivo

ejecute `./acore.sh`  y puede usar el panel en modo interactivo: puede navegar dentro del men� y submen� del panel y ejecutar el comando que necesita

### Argumentos de comando

Puede utilizar los comandos del panel como argumentos del script ./acore.sh. Por ejemplo:

`./acore.sh compiler configure` ejecutar� el proceso de configuraci�n de nuestro compilador c++

Todos los comandos vienen con un alias m�s corto. Por ejemplo, `./acore.sh c configure` ejecutar� la configuraci�n del compilador, pero tambi�n `./acore.sh 5 3` lo har�.

## Dependencias

Nuestro sistema bash utiliza bibliotecas bash externas que son gen�ricas y no est�n relacionadas con el propio azerothcore, esas bibliotecas han sido creadas por nosotros y se han colocado en la carpeta / deps

## GANCHOS:

Interno [Sistema de gancho para bash](hooks-bash.md)

## Otros recursos

- Comando bash �nico para instalar azerothcore: [Video + secuencia de comandos en la descripci�n](https://www.youtube.com/watch?v=j1HI6pLZZvM)
