{% include warning_es.html content="Esta guía está desactualizada porque hace referencia a MariaDB, que ya no recibe soporte." %}

## Introduction

Este tutorial te guiará por todo el proceso de configuración del servidor AzerothCore y te ayudará a familiarizarte con Debian y las interfaces de línea de comandos (CLI). En este tutorial, repasaremos lo siguiente:
- Analizamos diversas herramientas que pueden ayudarle a poner en funcionamiento su servidor, como clientes MySQL, clientes SSH, clientes SFTP y potentes editores de archivos.
- Configurar un Droplet en DigitalOcean desde cero
- Construyendo el núcleo
- Cargando la base de datos

Hay un video de YouTube paso a paso que te guía a través de todo el proceso. Te recomendamos seguirlo y usar este tutorial como guía de referencia.

[![Tutorial Video](https://img.youtube.com/vi/lenMiDtbHhs/0.jpg)](https://www.youtube.com/watch?v=lenMiDtbHhs)

## Aplicaciones de PC que podrías necesitar:
#### Clientes MySQL:
- [HeidiSQL](https://www.heidisql.com/)
- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [SQLYog](https://www.webyog.com/product/sqlyog) (Paid)

#### Clientes SSH:
- Consola de DigitalOcean
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [Termius](https://termius.com/) (Paid)

#### Clientes FTP:
- [Filezilla](https://filezilla-project.org/)
- [Terminus](https://termius.com/) (Paid)

#### Editores de archivos:
- [Visual Studio Code](https://code.visualstudio.com/)
- [Notepad++](https://notepad-plus-plus.org/)

## Eligiendo nuestra Droplet
#### Configurar nuevo Droplet
- 8 GB de RAM / 4 núcleos
- Debian 9
- Elija región
- Habilitar la monitorización
- Contraseña de un solo uso
- Nombra la Droplet como quieras, en este tutorial la llamaremos "AzerothCore".

## Configuración inicial de Droplet
#### Cambiar su zona horaria
- Ingrese el comando `timedatectl` para confirmar que el Droplet esté configurado en hora UTC (00:00).
- Antes de configurar la zona horaria, primero debemos averiguar el código correspondiente. Introduce el comando `timedatectl list-timezones` para ver una lista de todas las zonas horarias. Pulsa Intro hasta encontrar tu zona horaria y anótala. Pulsa *Control+C* una vez que hayas terminado de buscar zonas horarias.
- Una vez que esté nuevamente en la línea de comando, ingrese `sudo timedatectl set-timezone YOUR_TIME_ZONE`
- Verifique que la zona horaria esté configurada correctamente ingresando `timedatectl`

#### Agregar un nuevo usuario
- Se recomienda no usar el usuario *root* para las aplicaciones. Por ello, crearemos un usuario responsable de todas las actividades de AzerothCore. Introduce `adduser azcore` para crear un nuevo usuario.
- A continuación, asegurémonos de que este usuario tenga permisos de sudo. Para obtenerlos, use el siguiente comando: `usermod -aG sudo azcore`

#### Verificar el acceso a Sudo para el nuevo usuario
- Inicie sesión como nuestro nuevo usuario `sudo su azcore`
- Ingrese `sudo whoami` y luego ingrese la contraseña que eligió para este usuario (puede ser diferente de su contraseña de root).
- Si dice *root*, ¡listo! Ingresa el comando `exit` para volver a tu usuario root y continuar con los siguientes pasos.

#### Instalación de bibliotecas clave y aplicaciones adicionales
- A continuación, necesitamos instalar varias bibliotecas, aplicaciones y herramientas importantes para Azerothcore. Ejecuta el siguiente comando:
```
sudo apt-get update && sudo apt-get install git make gcc g++ clang default-libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev g++-7
```
- Seleccione 'Y' para cualquier solicitud que solicite espacio adicional para la instalación.
- Actualicemos nuestra lista de aplicaciones una vez más antes de continuar con `sudo apt-get update`
- Instalemos Screen, una aplicación que nos permitirá tener múltiples aplicaciones abiertas a la vez y persistir después de cerrar sesión en la consola `sudo apt-get install screen`
- El siguiente es curl: lo usaremos para obtener VMAP, MMAP y otros datos necesarios para el servidor `sudo apt install curl`
- Instalemos la utilidad de descompresión para que podamos descomprimir los archivos de datos `sudo apt install unzip`
- Finalmente, terminemos con `sudo apt install`

#### Instalación de CMake
- Asegurémonos de que no exista ninguna versión de CMake eliminando cualquier instalación previa de CMake. `sudo apt remove --purge --auto-remove cmake`
- A continuación, comenzaremos el proceso de instalación de CMake. Copia este bloque completo y pégalo en tu terminal. Si deseas instalar una versión diferente de CMake, puedes actualizar la versión y el número de compilación a una versión diferente de CMake, que puedes encontrar en https://cmake.org/download/
```
version=3.16
build=2
mkdir ~/temp
cd ~/temp
wget https://cmake.org/files/v$version/cmake-$version.$build.tar.gz
tar -xzvf cmake-$version.$build.tar.gz
cd cmake-$version.$build/
```
- Después de escribir un montón de texto, presione “Retorno” o “Enter” una vez en su teclado.
- Ahora, instalemos CMake. Copia este bloque completo y pégalo en tu terminal.
```
./bootstrap
make -j$(nproc)
sudo make install
```
- Una vez finalizada la construcción (y obtengas nuevamente la línea de comando), presiona "Retorno" o "Enter" una vez en tu teclado para instalar CMake.
- Verifiquemos que esté ejecutando la versión correcta de CMake con el comando `cmake --version`. Nota: Si la versión de CMake no funciona, cierre la terminal, vuelva a conectarse y vuelva a intentar el comando `version`.
- Regrese a su directorio principal escribiendo "cd".
- Limpiemos la instalación de CMake con `rm -rf temp`. Ahora veamos cómo configurar la base de datos.

#### Completar la instalación segura de MariaDB
- Comencemos el proceso `sudo mysql_secure_installation`
- Para las siguientes indicaciones, responda `[no pasa]/N/Y/Y/Y/Y`
- Una vez que estemos nuevamente en la línea de comandos, escriba `sudo mysql` para ingresar a la consola MariaDB
- Una vez en la consola MariaDB, creemos nuestro Usuario:
```
GRANT ALL ON *.* TO 'dbadmin'@'%' IDENTIFIED BY 'password1' WITH GRANT OPTION;
```
- Elige el nombre de usuario que quieras; puede ser cualquiera, no necesariamente `dbadmin`. Además, asegúrate de elegir una contraseña muy segura, ya que `password1` *NUNCA* debe usarse.
- Actualicemos los permisos para MariaDB `Flush Privileges;`
- Regresar a la consola principal de Debian `exit`

#### Configurar conexiones remotas a MariaDB
- Navegue hasta la carpeta que contiene el archivo que necesitamos `cd /etc/mysql/mariadb.conf.d`
- Inicie el editor de archivos nano para el archivo de configuración `nano 50-server.cnf`
- Navegue hasta la dirección de enlace y actualícela a: `0.0.0.0`
- Para guardar los cambios, presione *Ctrl + X*, luego *Y* y, finalmente, *Ctrl + T*. Luego, use las flechas para seleccionar `50-server.cnf`.
- Ahora que hemos actualizado un archivo de configuración clave de MariaDB, debemos reiniciar el proceso de MariaDB. Introduzca `sudo /etc/init.d/mysql restart`.

#### Configurar el firewall no complicado (UFW)
- Actualicemos nuestro catálogo de aplicaciones `sudo apt update`
- Instalemos UFW `sudo apt install ufw`
- A continuación, bloquearemos todas las conexiones entrantes. Este es un paso importante para proteger su servidor. Abriremos los puertos en los siguientes pasos: `sudo ufw default deny incoming`
- A continuación, vamos a habilitar todas las conexiones salientes. Esto debería permitir que su servidor realice llamadas sin problemas. `sudo ufw default allow outgoing`
- We need to make sure we don't get locked out of the Console, so we need to unblock port 22, which is the port SSH uses. To do this, enter `sudo ufw allow ssh`
- Permitamos que el puerto MariaDB acepte conexiones entrantes `sudo ufw allow 3306`
- Habilitemos el servidor de autenticación para que acepte conexiones entrantes `sudo ufw allow 3724`
- Y ahora el puerto Worldserver `sudo ufw allow 8085`
- Verifique que haya habilitado todos los puertos anteriores y luego active UFW con esto: `sudo ufw enable`

## Instalación de AzerothCore
#### Clonemos el Git de AzerothCore
- Inicie sesión como nuestro usuario sudo `sudo su azcore`
- Navega a nuestro directorio de inicio `cd`
- Descarguemos y clonemos la última versión de AzerothCore `git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore`
- Una vez que se complete la clonación, naveguemos a la carpeta de nivel superior del directorio git `cd azerothcore`
- Necesitamos crear una carpeta llamada *build* `mkdir build`
- Vaya a la nueva carpeta de compilación `cd build`
- Ahora ejecutamos el comando cmake, este es el paso de precompilación para garantizar que se tengan en cuenta todos los archivos cpp antes de compilar y le dice al compilador qué compilar.
```
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DTOOLS=0 -DSCRIPTS=static
```
- Ahora compilamos AzerothCore. Esto puede tardar un poco dependiendo de la cantidad de núcleos de CPU que tenga tu Droplet. Este tutorial se basa en el Droplet de 4 núcleos de CPU, que se compila en aproximadamente 8 minutos. Introduce el siguiente comando para compilar el núcleo y colocar los elementos ensamblados en su nuevo lugar:
```
MTHREADS=`grep -c ^processor /proc/cpuinfo`; MTHREADS=$(($MTHREADS + 2));
make -j $MTHREADS;
make install -j $MTHREADS;
```
- Después de que la terminal diga `make install -j $MTHREADS` luego de compilar, presione 'Retorno' o 'Enter' en su teclado para instalar y finalizar el proceso de compilación.

#### Archivos de datos
- Como usuario `azcore`, regresemos al directorio de inicio `cd`
- Ahora necesitamos ir a la carpeta del servidor de compilación `cd azeroth-server`
- Necesitamos crear una carpeta para nuestros archivos de datos y navegar hasta ella `mkdir data;cd data`
- Descarguemos los archivos de datos necesarios. `curl https://wow.heyaapl.com/data.zip --output data.zip`
- Descomprimamos el directorio de datos principal `unzip data.zip`

#### Configurar los archivos de configuración del servidor
- Usando SFTP, navegue a `/home/azcore/azeroth-server/etc` y descargue authserver.conf.dist y worldserver.conf.dist a su máquina local.
- Cambie el nombre de los archivos en su máquina local para eliminar la extensión .dist del nombre del archivo.
- Actualice la información de la base de datos en los archivos de configuración de Authserver y Worldserver con el editor de archivos. Use el nombre de usuario y la contraseña que creó en los pasos anteriores para actualizar la información de conexión a la base de datos.
- En la configuración de Worldserver, configure la carpeta DataDir en: `"/home/azcore/azeroth-server/data"`
- Cargue los archivos .conf nuevamente al directorio etc usando su cliente SFTP.

#### Configuración y carga inicial de la base de datos
- De forma similar a lo que se hizo con Authserver.conf y Worldserver.conf, necesitamos actualizar el archivo de configuración de importación de la base de datos. Mediante SFTP, navegue a `/home/azcore/azerothcore/conf/dist/` y busque `config.sh`. Descárguelo en su equipo local.
- Abra `config.sh` en un editor y localice la sección *CONFIGURACIONES DEL EXPORTADOR/IMPORTADOR DE DB*.
- Reemplace la información de inicio de sesión de la base de datos, que comienza en la línea 153, con el nombre de usuario y la contraseña que configuró anteriormente en este tutorial. Repita este proceso para las secciones de configuración de la base de datos Auth, Character y World (que comienzan en las líneas 153, 158 y 163, respectivamente).
- Guarde `config.sh` y vuelva a cargarlo al directorio `/home/azcore/azerothcore/conf/`.
- Necesitamos estar en el directorio git para poder ejecutar el script de importación, así que ingrese el siguiente comando `cd /home/azcore/azerothcore`
- Inicie el script de importación de la base de datos con el siguiente comando: `bash apps/db_assembler/db_assembler.sh`. Necesitamos configurar todas las bases de datos, por lo que debemos seleccionar *Import-all: Ensamblar e Importar Todo*. Escriba `import-all` y presione Enter. Esto puede generar un error después de cada ejecución, pero no importa: importa todas las bases de datos correctamente. Repita este paso hasta que se cargue la base de datos World. Escriba `quit` una vez importada la base de datos World.

## Inicio del servidor
#### Configuración final
- Conéctese a su base de datos con su cliente MySQL. La dirección IP de su servidor DigitalOcean es el nombre de host, el nombre de usuario es el nombre de usuario de su base de datos y la contraseña es la contraseña de su base de datos. El puerto predeterminado debería ser 3306. Conéctese.
- Vaya a la base de datos `acore_auth` y abra la tabla `realmlist`. Visualice los datos de la tabla.
- Actualice el valor de `address` a la dirección IP de su servidor. Aquí puede actualizar el nombre del dominio de su servidor si así lo desea.

#### Poner en marcha su servidor
- En su terminal SSH, ingrese el siguiente comando `cd /home/azcore/azeroth-server/bin`
- Ahora, activemos el servidor de autenticación. Usamos Screens para tener abiertos tanto el servidor de autenticación como el servidor mundial simultáneamente. Vamos a etiquetar la pantalla del servidor de autenticación como "auth". Introduzca el siguiente comando para iniciarlo: `screen -AmdS auth ./authserver`. Introduzca `screen -r auth` para verificar que se haya iniciado correctamente. Presione *Ctrl + A, seguido de D* para salir de la pantalla de autenticación. Para cerrar la pantalla por completo, presione *Ctrl + C*. Esto finalizará el proceso, así que úselo solo al apagar el servidor de autenticación.
- Ahora, activemos el servidor mundial. Vamos a etiquetar su pantalla como "world". Para iniciarlo, introduzca el siguiente comando: `screen -AmdS world ./worldserver`. Introduzca `screen -r world` para verificar que se haya iniciado correctamente. Presione *Ctrl + A, seguido de D* para salir de la pantalla del mundo. Para cerrar la pantalla por completo, presione *Ctrl + C*. Esto finalizará el proceso, así que úselo solo al apagar el servidor mundial.
- Nota al margen: si desea obtener más información sobre por qué pasamos `AmdS` al inicializar Screens, o para ver si hay otros argumentos que desea pasar, [aquí hay una excelente referencia](https://linux.die.net/man/1/screen) sobre lo que significa cada letra y por qué se utilizan.

#### Crea tu cuenta en el juego
- Navegue a la pantalla mundial escribiendo `screen -r world`
- Ingrese el siguiente comando para crear su nueva cuenta `account create [nombre de cuenta] [contraseña]`
- A continuación, hagamos que su nueva cuenta sea una cuenta de administrador `account set gmlevel [accountname] 3 -1`

#### Actualiza tu lista de reinos
- Configura tu realmlist.wtf con tu IP de DigitalOcean, que se encuentra en `[Directorio WoW]/data/enUS`. ¡Edítalo con tu editor e inicia sesión!
