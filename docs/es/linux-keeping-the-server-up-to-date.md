# Linux: mantener el servidor actualizado

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 6: Pasos finales del servidor](es/final-server-steps) | [Paso 8: Configuración del cliente >>](es/client-setup) |

## Mantener el código fuente actualizado

```sh
cd ~/azerothcore/
git pull origin master
```

Reconstruye los cambios que descargaste.

```sh
cd build
make -j$(nproc --all); make install
```
_Puedes reemplazar `-j$(nproc -all)` con el número de cores con los que compilar. Por ejemplo: -j 2_

A veces añadimos o eliminamos archivos del repositorio. En ese momento es necesario recompilar el servidor, tal como se instaló la primera vez [en la Instalación del Core en Linux](es/linux-core-installation#configuring-for-compiling).

## Usar un servidor de automatización

Si quieres actualizar AzerothCore usando Jenkins, Teamcity o una herramienta similar, los siguientes pasos pueden ayudarte.

Añade los comandos necesarios al archivo sudoers. Los servicios de abajo se crearon [en la Instalación del Core en Linux](es/linux-core-installation#optional-systemd-services)
```sh
sudo visudo

%sudo ALL=NOPASSWD: /usr/sbin/service worldserver start
%sudo ALL=NOPASSWD: /usr/sbin/service authserver start
%sudo ALL=NOPASSWD: /usr/sbin/service worldserver stop
%sudo ALL=NOPASSWD: /usr/sbin/service authserver stop
%sudo ALL=NOPASSWD: /srv/azerothcore-wotlk/acore.sh compiler all
```

Ejecuta los comandos en Jenkins/Teamcity
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

Lee [Base de datos: mantener el servidor actualizado](es/database-keeping-the-server-up-to-date)

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 6: Pasos finales del servidor](es/final-server-steps) | [Paso 8: Configuración del cliente >>](es/client-setup) |
