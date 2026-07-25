{% include warning.html content="This guide is out-dated as it refers to MariaDB, which is no longer supported." %}

## Introducción

Este tutorial te guiará por todo el proceso de configuración del servidor de AzerothCore, y te ayudará a familiarizarte con el uso de Debian y las interfaces de línea de comandos (CLI). En este tutorial, cubriremos lo siguiente:
- Ver varias herramientas para ayudarte a poner en marcha tu servidor, como clientes MySQL, clientes SSH, clientes SFTP y potentes editores de archivos. 
- Configurar un Droplet en DigitalOcean desde cero
- Compilar el Core
- Cargar la base de datos

Hay un vídeo de YouTube paso a paso que te guía por todo este proceso. Se recomienda que sigas ese vídeo, usando este tutorial como guía de referencia.

[![Tutorial Video](https://img.youtube.com/vi/lenMiDtbHhs/0.jpg)](https://www.youtube.com/watch?v=lenMiDtbHhs)

## Apps de PC que puedes necesitar:
#### Clientes MySQL:
- [HeidiSQL](https://www.heidisql.com/)
- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [SQLYog](https://www.webyog.com/product/sqlyog) (De pago)

#### Clientes SSH:
- La consola de DigitalOcean
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [Termius](https://termius.com/) (De pago)

#### Clientes FTP:
- [Filezilla](https://filezilla-project.org/)
- [Terminus](https://termius.com/) (De pago)

#### Editores de archivos:
- [Visual Studio Code](https://code.visualstudio.com/)
- [Notepad++](https://notepad-plus-plus.org/)

## Elegir nuestro Droplet
#### Configurar un nuevo Droplet
- 8GB RAM / 4 Cores
- Debian 9
- Elige la región
- Activa la monitorización
- Contraseña de un solo uso
- Nombra el Droplet como quieras; en este tutorial lo llamamos `AzerothCore`

## Configuración inicial del Droplet
#### Cambia tu zona horaria
- Introduce el comando `timedatectl` para confirmar que el Droplet está configurado en hora UTC (00:00).
- Antes de poder establecer la zona horaria, primero necesitamos averiguar cuál es el código de tu zona horaria. Introduce el comando `timedatectl list-timezones` para ver una lista de todas las zonas horarias. Pulsa Enter hasta encontrar tu zona horaria, y anótala. Pulsa *Control+C* una vez que hayas terminado de buscar zonas horarias.
- Una vez que vuelvas a la línea de comandos, introduce `sudo timedatectl set-timezone YOUR_TIME_ZONE`
- Verifica que la zona horaria se estableció correctamente introduciendo `timedatectl`

#### Añade un nuevo usuario
- Es una buena práctica no usar el usuario *root* para las aplicaciones. Por eso, vamos a crear un usuario que será responsable de todas las actividades de AzerothCore. Introduce `adduser azcore` para crear un nuevo usuario.
- A continuación, asegurémonos de que este usuario tenga permisos de sudo. Otorga esos permisos usando el siguiente comando `usermod -aG sudo azcore`

#### Verifica el acceso sudo del nuevo usuario
- Iniciemos sesión como nuestro nuevo usuario `sudo su azcore`
- Introduce `sudo whoami` y luego introduce la contraseña que elegiste para este usuario (puede ser diferente de tu contraseña de root).
- Si dice *root*, ¡entonces está todo listo! Introduce el comando `exit` para volver a tu usuario root para los siguientes pasos.

#### Instalar librerías clave y apps adicionales
- A continuación necesitamos instalar un montón de librerías, aplicaciones y herramientas importantes necesarias para AzerothCore. Ejecuta el siguiente comando: 
```
sudo apt-get update && sudo apt-get install git make gcc g++ clang default-libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev g++-7
```
- Elige 'Y' para cualquier prompt que pida espacio adicional para la instalación.
- Refresquemos nuestra lista de apps una vez más antes de continuar `sudo apt-get update`
- Instalemos Screen, una aplicación que nos permitirá tener varias aplicaciones abiertas a la vez y que persistan después de cerrar la sesión de la consola `sudo apt-get install screen`
- Lo siguiente es curl; lo usaremos para obtener los VMAP, MMAP y otros datos requeridos para el servidor `sudo apt install curl`
- Instalemos la utilidad unzip, para poder descomprimir los archivos de datos `sudo apt install unzip`
- Finalmente, terminemos con `sudo apt install`

#### Instalar CMake
- Asegurémonos de que no exista ninguna versión de CMake eliminando cualquier instalación previa de CMake. `sudo apt remove --purge --auto-remove cmake`
- A continuación, comenzaremos el proceso para instalar CMake. Copia todo este bloque y pégalo en tu terminal. Si deseas instalar una versión diferente de CMake, puedes actualizar la versión y el número de build a una versión de CMake diferente, que se puede encontrar en https://cmake.org/download/
```
version=3.16
build=2
mkdir ~/temp
cd ~/temp
wget https://cmake.org/files/v$version/cmake-$version.$build.tar.gz
tar -xzvf cmake-$version.$build.tar.gz
cd cmake-$version.$build/
```
- Después de un montón de texto, pulsa 'Return' o 'Enter' una vez en tu teclado.
- Ahora instalemos CMake. Copia todo este bloque y pégalo en tu terminal.
```
./bootstrap
make -j$(nproc)
sudo make install
```
- Después de que la compilación se complete (y recuperes la línea de comandos), pulsa 'Return' o 'Enter' una vez en tu teclado para instalar CMake
- Verifiquemos que estás ejecutando la versión correcta de CMake usando el comando `cmake --version`. Nota: si CMake Version no funciona, cierra tu terminal, reconéctate e intenta el comando version de nuevo.
- Vuelve a tu directorio principal escribiendo `cd`.
- Limpiemos la instalación de CMake con `rm -rf temp`. Ahora echemos un vistazo a la configuración de la base de datos.

#### Completar la instalación segura de MariaDB
- Comencemos el proceso `sudo mysql_secure_installation`
- Para los siguientes prompts, responde `[no pass]/N/Y/Y/Y/Y`
- Una vez que volvamos a la línea de comandos, escribe `sudo mysql` para entrar en la consola de MariaDB
- Una vez en la consola de MariaDB, creemos nuestro usuario: 
```
GRANT ALL ON *.* TO 'dbadmin'@'%' IDENTIFIED BY 'password1' WITH GRANT OPTION;
```
- Elige el nombre de usuario que quieras; puede ser cualquier cosa, no tiene que ser `dbadmin`. Además, por favor asegúrate de elegir una contraseña muy segura, ya que `password1` *NUNCA* debería usarse.
- Refresquemos los permisos de MariaDB `Flush Privileges;`
- Vuelve a la consola principal de Debian `exit`

#### Configurar conexiones remotas a MariaDB
- Navega a la carpeta que contiene el archivo que necesitamos `cd /etc/mysql/mariadb.conf.d`
- Abre el editor de archivos nano para el archivo de configuración `nano 50-server.cnf`
- Navega hasta la Bind Address, y actualízala a: `0.0.0.0`
- Para guardar tus cambios, pulsa *Ctrl + X*, luego *Y*, seguido de *Ctrl + T*. Luego usa tus teclas de flecha para seleccionar `50-server.cnf`
- Ahora que hemos actualizado un archivo de configuración clave de MariaDB, necesitamos reiniciar el proceso de MariaDB. Introduce `sudo /etc/init.d/mysql restart`

#### Configurar el Uncomplicated Firewall (UFW)
- Refresquemos nuestro catálogo de apps `sudo apt update`
- Instalemos UFW `sudo apt install ufw`
- A continuación, vamos a bloquear en bloque todas las conexiones entrantes. Este es un paso importante para proteger tu servidor. Abriremos puertos en los siguientes pasos `sudo ufw default deny incoming`
- A continuación, permitamos en bloque todas las conexiones salientes. Esto debería permitir que tu servidor haga peticiones sin problemas. `sudo ufw default allow outgoing`
- Necesitamos asegurarnos de no quedarnos bloqueados fuera de la consola, así que necesitamos desbloquear el puerto 22, que es el puerto que usa SSH. Para hacer esto, introduce `sudo ufw allow ssh`
- Permitamos que el puerto de MariaDB acepte conexiones entrantes `sudo ufw allow 3306`
- Habilitemos que el servidor de autenticación acepte conexiones entrantes `sudo ufw allow 3724`
- Y ahora el puerto del Worldserver `sudo ufw allow 8085`
- Verifica que has habilitado todos los puertos anteriores, y luego activa UFW con esto: `sudo ufw enable`

## Instalación de AzerothCore
#### Clonemos el Git de AzerothCore
- Inicia sesión como nuestro usuario sudo `sudo su azcore`
- Navega a nuestro directorio home `cd` 
- Descarguemos y clonemos la última versión de AzerothCore `git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore`
- Una vez que el clonado se complete, naveguemos a la carpeta de nivel superior del directorio git `cd azerothcore`
- Necesitamos crear una carpeta llamada *build* `mkdir build`
- Navega a la nueva carpeta build `cd build`
- Ahora ejecutamos el comando cmake; este es el paso de pre-compilación para asegurar que todos los archivos cpp estén contabilizados antes de compilar, y le dice al compilador qué compilar. 
```
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DTOOLS=0 -DSCRIPTS=static
```
- Ahora compilamos AzerothCore; esto puede tardar un tiempo dependiendo del número de núcleos de CPU que tenga tu Droplet. Este tutorial está basado en el Droplet de 4 núcleos de CPU, que compila en unos 8 minutos. Introduce el siguiente comando para compilar el core y colocar los elementos ensamblados en su nuevo hogar:
```
MTHREADS=`grep -c ^processor /proc/cpuinfo`; MTHREADS=$(($MTHREADS + 2));
make -j $MTHREADS;
make install -j $MTHREADS;
```
- Después de que la terminal diga `make install -j $MTHREADS` tras compilar, pulsa 'Return' o 'Enter' en tu teclado para instalar y finalizar el proceso de compilación.

#### Archivos de datos
- Como usuario `azcore`, volvamos al directorio home `cd`
- Ahora necesitamos ir a la carpeta del servidor compilado `cd azeroth-server`
- Necesitamos crear una carpeta para nuestros archivos de datos y navegar a ella `mkdir data;cd data`
- Descarguemos los archivos de datos requeridos. `curl https://wow.heyaapl.com/data.zip --output data.zip`
- Descomprimamos el directorio de datos principal `unzip data.zip`

#### Configurar los archivos de configuración del servidor
- Usando SFTP, navega a `/home/azcore/azeroth-server/etc` y descarga authserver.conf.dist y worldserver.conf.dist a tu máquina local.
- Renómbralos en tu máquina local para quitar el .dist del nombre del archivo. 
- Actualiza la información de la base de datos tanto en el archivo de configuración del Authserver como en el del Worldserver usando tu editor de archivos para editarlos. Usa el nombre de usuario y la contraseña que creaste en los pasos anteriores para actualizar la información de conexión a la base de datos.
- En la configuración del Worldserver, configura la carpeta DataDir a: `"/home/azcore/azeroth-server/data"`
- Sube los archivos .conf de vuelta al directorio etc usando tu cliente SFTP.

#### Configuración inicial y carga de la base de datos
- De forma similar a lo que se hizo con Authserver.conf y Worldserver.conf, necesitamos actualizar el archivo de configuración de importación de la base de datos. Usando SFTP, navega a `/home/azcore/azerothcore/conf/dist/` y encuentra el `config.sh`. Descárgalo a tu máquina local.
- Abre `config.sh` en un editor y localiza la sección *DB EXPORTER/IMPORTER CONFIGURATIONS*.
- Reemplaza la información de login de la base de datos que empieza en la línea 153 con el nombre de usuario y la contraseña de la base de datos que estableciste antes en este tutorial. Haz esto para las secciones de configuración de las bases de datos Auth, Character y World (empezando en las líneas 153, 158 y 163 respectivamente).
- Guarda `config.sh` y súbelo de vuelta al directorio `/home/azcore/azerothcore/conf/`.
- Necesitamos estar en el directorio git para ejecutar el script de importación, así que introduce el siguiente comando `cd /home/azcore/azerothcore`
- Inicia el script de importación de la base de datos introduciendo el siguiente comando `bash apps/db_assembler/db_assembler.sh`. Necesitamos configurar todas las bases de datos, así que necesitamos elegir *Import-all: Assemble & Import All*. Escribe `import-all` y pulsa enter. Esto puede dar error tras cada ejecución, pero está bien: importa cada base de datos con éxito. Repite todo este paso hasta que se cargue la base de datos World. Escribe `quit` una vez que la base de datos World se haya importado.

## Arranque del servidor
#### Configuración final
- Usando tu cliente MySQL, conéctate a tu base de datos. La dirección IP de tu servidor de DigitalOcean es el hostname, el nombre de usuario es tu nombre de usuario de la base de datos, y la contraseña es tu contraseña de la base de datos. El puerto debería estar por defecto en 3306. Conéctate.
- Navega a la base de datos `acore_auth`, y abre la tabla llamada `realmlist`. Mira los datos de la tabla. 
- Actualiza el valor `address` a la dirección IP de tu servidor. Aquí es donde puedes actualizar el nombre del realm de tu servidor si así lo deseas.

#### Inicia tu servidor
- En tu terminal SSH, introduce el siguiente comando `cd /home/azcore/azeroth-server/bin`
- Ahora, encendamos el Authserver. Estamos usando Screens para poder tener el Authserver y el Worldserver abiertos al mismo tiempo. Vamos a etiquetar el Screen del Authserver como 'auth'. Introduce el siguiente comando para iniciarlo `screen -AmdS auth ./authserver`. Introduce `screen -r auth` para verificar que se inició con éxito. Pulsa *Ctrl + A, seguido de D* para salir del screen de auth. Para cerrar el screen por completo, pulsa *Ctrl + C*. Esto matará el proceso, así que usa esto solo al apagar el Authserver.
- Ahora, encendamos el Worldserver. Vamos a etiquetar el Screen del Worldserver como 'world'. Introduce el siguiente comando para iniciarlo `screen -AmdS world ./worldserver`. Introduce `screen -r world` para verificar que se inició con éxito. Pulsa *Ctrl + A, seguido de D* para salir del screen de world. Para cerrar el screen por completo, pulsa *Ctrl + C*. Esto matará el proceso, así que usa esto solo al apagar el Worldserver.
- Nota al margen: si quieres aprender más sobre por qué pasamos `AmdS` al inicializar los Screens, o para ver si hay otros argumentos que quieras pasar, [aquí tienes una gran referencia](https://linux.die.net/man/1/screen) sobre lo que significa cada letra y por qué se usan.

#### Crea tu cuenta dentro del juego
- Navega al screen de world escribiendo `screen -r world`
- Introduce el siguiente comando para crear tu nueva cuenta `account create [accountname] [password]`
- A continuación, hagamos que tu nueva cuenta sea una cuenta de administrador `account set gmlevel [accountname] 3 -1`

#### Actualiza tu Realmlist
- Configura tu realmlist.wtf con tu IP de DigitalOcean, que se puede encontrar en `[WoW Directory]/data/enUS`. Edítalo con tu editor, ¡e inicia sesión!
