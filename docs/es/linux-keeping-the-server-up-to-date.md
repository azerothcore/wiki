# Linux: mantener el servidor actualizado

| Guía de Instalación                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 6: Pasos finales del servidor](final-server-steps)                                                                                  | [Paso 8: Configuración del cliente >>](client-setup) |

## Mantener la fuente actualizada

```sh
cd ~/azerothcore/
git pull origin master
```

Reconstruya los cambios que realizó.

```sh
cd build
make -j$(nproc --all); make install
```
_Puedes reemplazar `-j$(nproc -all)` con el número de núcleos que se usarán para la compilación. Por ejemplo: -j 2_

A veces añadimos o eliminamos archivos del repositorio. En ese momento, es necesario recompilar el servidor, tal como se instaló la primera vez [en la instalación de Linux Core](linux-core-installation#configuring-for-compiling).

## Usando el servidor de automatización
Si desea actualizar AzerothCore usando Jenkins, Teamcity o una herramienta similar, los siguientes pasos pueden ayudarlo.

Agregue los comandos necesarios al archivo sudoers. Los servicios a continuación se crearon [en la instalación de Linux Core](linux-core-installation#optional-systemd-services)

```sh
sudo visudo

%sudo ALL=NOPASSWD: /usr/sbin/service worldserver start
%sudo ALL=NOPASSWD: /usr/sbin/service authserver start
%sudo ALL=NOPASSWD: /usr/sbin/service worldserver stop
%sudo ALL=NOPASSWD: /usr/sbin/service authserver stop
%sudo ALL=NOPASSWD: /srv/azerothcore-wotlk/acore.sh compiler all
```

Ejecutar comandos en Jenkins/Teamcity
```sh
sudo service worldserver stop
sudo service authserver stop

cd /srv/azerothcore-wotlk
git pull origin master

sudo /srv/azerothcore-wotlk//acore.sh compiler all

sudo service worldserver start
sudo service authserver start
```


## Mantener la base de datos actualizada

Leer [Base de datos: Manteniendo el servidor actualizado](database-keeping-the-server-up-to-date)

<br>

## Ayuda

{% include help.html %}

| Guía de instalación                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 6: Pasos finales del servidor](final-server-steps)                                                                                  | [Paso 8: Configuración del cliente >>](client-setup) |
