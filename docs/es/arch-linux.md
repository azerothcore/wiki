# Instalación en Arch Linux
Esta página cubre la configuración de dependencias específicas de Arch Linux para AzerothCore. Está pensada para usarse junto con la guía de [Instalación clásica en Linux](classic-installation).

Hay dos formas de instalar AzerothCore: mediante la instalación manual o mediante el paquete experimental de AUR.

## Instalación manual del núcleo

### Antes de comenzar
- Esta guía no explica cómo instalar Arch Linux.
- Asegúrate de que tu sistema esté actualizado y de tener un usuario normal con privilegios `sudo`.
- La [Arch Wiki](https://wiki.archlinux.org/title/Installation_guide) es la mejor fuente para la instalación general de Arch y la gestión de paquetes.

Asegúrate de que tu sistema esté completamente actualizado y, si actualizas el kernel, reinicia con el nuevo kernel antes de continuar.
```sh
sudo pacman -Syu
```

### Paquetes requeridos
Instala los paquetes de desarrollo necesarios para compilar AzerothCore:

```sh
sudo pacman -Syu --needed base-devel git cmake clang boost
```

### MySQL en Arch Linux
AzerothCore requiere Oracle MySQL. Oracle MySQL no está disponible en los repositorios oficiales de Arch, por lo que esta guía lo instala desde AUR.

> {% include warning.html content="Confiar en llaves es siempre responsabilidad del usuario. Si tienes dudas o preocupaciones, detente aquí y utiliza otro método de instalación." %}

Importa la llave de firma de MySQL:

```sh
gpg --recv-keys B7B3B788A8D3785C
```

Construye e instala el paquete de MySQL de AUR:

> {% include note.html content="Este paquete compila MySQL desde el código fuente. Probablemente necesitarás al menos 4 gigabytes de memoria para que la compilación tenga éxito." %}

```sh
mkdir -p ~/AUR
cd ~/AUR
git clone https://aur.archlinux.org/mysql.git
cd mysql
makepkg -si
```

Después de la instalación, habilita e inicia MySQL:

```sh
sudo systemctl enable --now mysql.service
```

### Próximos pasos
Una vez que el servidor de base de datos esté instalado y funcionando, continúa con la guía de [Instalación clásica en Linux](classic-installation) para compilar AzerothCore y finalizar la configuración.

## Instalación desde AUR (Experimental)

{% include warning.html content="El paquete de AzerothCore en AUR ha sido reescrito y está siendo probado por usuarios. Envía tus comentarios por Discord." %}

Debes tener especial cuidado para que Arch no intente instalar MariaDB como sustituto de MySQL.

Los ejemplos siguientes utilizan `yay` para instalar las dependencias, pero puedes usar otro ayudante de AUR. Estas instrucciones están pensadas para funcionar con cualquiera de los dos métodos.

Ten en cuenta que `acore.sh` no se distribuye con este método de instalación, ya que muchas de las tareas que gestiona se realizan de otra forma.

Los siguientes ejecutables, instalados con el paquete, gestionan distintas partes de la instalación:

* `acore_setup`: Inicializa AzerothCore, configura un usuario nuevo, realiza la población inicial de la base de datos y habilita el acceso remoto al indicador `AC>` desde el servicio en segundo plano. Se ejecuta en localhost de forma predeterminada.
* `acore_mod`: Compila y despliega automáticamente los módulos ubicados en una carpeta, o los elimina si ya no existen.
* `attach-world`: Inicia una sesión de conexión remota al servidor para que puedas acceder al indicador `AC>` y desconectarte mientras el servidor continúa ejecutándose.

### Instalación de MySQL
Debido a las definiciones de los paquetes y para permitir la resolución automática de dependencias, debemos usar el paquete específico de MySQL 8.4 en lugar del más reciente, que es la versión 9.

```sh
yay -S libmysqlclient84 mysql-clients84 mysql84
```

A continuación, inicializa MySQL. Puedes cambiar los directorios y usuarios según sea necesario.

Ten en cuenta que este comando mostrará una contraseña temporal que debes recordar o guardar para usarla más adelante.
```sh
sudo mysqld --initialize --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

Ahora inicia el servicio de MySQL:
```sh
sudo systemctl enable --now mysqld
```

A continuación, configura el primer usuario ejecutando los scripts de inicialización de MySQL:
```sh
sudo mysql_secure_installation
```

En este script, selecciona lo siguiente:

1. Cambiar la contraseña de root: Establece la que quieras. La contraseña inicial es la contraseña aleatoria mostrada anteriormente.
1. Aplicar una política estricta de contraseñas: No (interferirá con las credenciales predeterminadas que creará AzerothCore).
1. Eliminar usuarios anónimos: Sí
1. Deshabilitar el inicio de sesión remoto: Sí (esto solo elimina las cuentas root remotas; no deshabilita el acceso remoto de otros usuarios ni cambia la dirección de enlace del servidor). Responde Sí de forma predeterminada. Si necesitas acceso remoto a la base de datos, configura por separado usuarios dedicados sin privilegios de root y el acceso de red.
1. Eliminar la base de datos de prueba: Sí
1. Recargar las tablas de privilegios: Sí

### Instalar AzerothCore
El núcleo está dividido en dos paquetes: el núcleo y los datos del cliente/mapas.

Si quieres extraer los datos de los mapas por tu cuenta, el paquete clientdata no es necesario y puedes omitirlo. Sin embargo, AzerothCore espera encontrar los datos de los mapas en `/usr/share/azerothcore/data`.

```sh
yay -S azerothcore-wotlk-git azerothcore-clientdata
```

### Inicializar AzerothCore
Este paquete instala un script auxiliar llamado `acore_setup`.

```sh
sudo acore_setup
```

Este script realizará parte de la configuración, te preguntará por el usuario de MySQL, iniciará el servidor para rellenar previamente la base de datos y, cuando el servidor esté activo, te pedirá crear una cuenta con:

```sh
AC> account create <username> <password>
```

Nota: ¡Esta cuenta tendrá privilegios de Game Master!

Después de estos pasos, el servidor se apagará automáticamente. Puedes iniciarlo todo habilitando e iniciando los servicios:

```sh
sudo systemctl enable --now acore-auth-server acore-world-server
```

### Conectarse a AzerothCore
Puedes conectarte al servidor local en ejecución con:

```sh
attach-world
```

Después, introduce tu nombre de usuario y contraseña de administrador de AzerothCore. Puedes salir en cualquier momento pulsando `Ctrl+C`.

> {% include note.html content="¡Ctrl+C _no_ apagará el servidor!" %}

### Gestión de módulos
> {% include warning.html content="Este paquete de AUR no debe utilizarse con el módulo PlayerBots. Existe otra bifurcación del núcleo para ese módulo y este paquete no la admite." %}

Para gestionar módulos, clona los repositorios en `/usr/src/acore-modules`.

Cuando los hayas clonado y estés listo para desplegarlos, ejecuta:
```sh
acore_mod
```

Esto hará lo siguiente:

1. Crear un enlace simbólico desde el código fuente del módulo hasta la ubicación donde se encuentra el código fuente de AzerothCore.
1. Realizar una compilación incremental para recompilar AzerothCore con los módulos.
1. Empaquetar los archivos SQL para reinstalarlos con el nuevo paquete y guardarlos en el directorio de instalación de AzerothCore.
1. Instalar el paquete.
1. Reiniciar los servicios.

> {% include warning.html content="Si tu módulo tiene un archivo de configuración o ajustes que deban añadirse a archivos de configuración existentes, tendrás que hacerlo manualmente. Después de actualizar la configuración, reinicia el servicio world." %}

### Comentarios
Este trabajo está en curso y todavía no he probado muchos módulos. Si encuentras problemas, publícalos en Discord. Beck es el usuario que mantiene este paquete.
