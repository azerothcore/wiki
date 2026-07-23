# Instalación en Arch Linux

Esta página trata la configuración de dependencias específicas de Arch Linux para AzerothCore. Está pensada para usarse junto con la guía [Instalación clásica en Linux](classic-installation).

{% include warning.html content="El paquete AzerothCore en el AUR está muy desactualizado y no se recomienda." %}

## Antes de comenzar

- Esta guía no explica cómo instalar Arch Linux en sí.
- Asegúrate de que tu sistema esté actualizado y de tener un usuario normal con privilegios de `sudo`.
- La [Arch Wiki](https://wiki.archlinux.org/title/Installation_guide) es la mejor fuente para la instalación general de Arch y la gestión de paquetes.

Asegúrate de que tu sistema esté completamente actualizado; si actualizas el kernel, reinicia en el nuevo kernel antes de continuar.

```sh
sudo pacman -Syu
```

## Paquetes requeridos

Instala los paquetes básicos de desarrollo necesarios para compilar AzerothCore:

```sh
sudo pacman -Syu --needed base-devel git cmake clang boost
```

## MySQL en Arch Linux

AzerothCore requiere Oracle MySQL. Oracle MySQL no está disponible en los repositorios oficiales de Arch, por lo que esta guía lo instala desde el AUR.

> {% include warning.html content="Confiar en claves es siempre responsabilidad del usuario; verifica que la clave que se confía sea la correcta. Si tienes dudas o preocupaciones, detente aquí y usa otro método de instalación." %}

Importa la clave de firma de MySQL:

```sh
gpg --recv-keys B7B3B788A8D3785C
```

Construye e instala el paquete del AUR:

Antes de compilar, comprueba si hay paquetes MariaDB instalados que puedan entrar en conflicto con Oracle MySQL:

```sh
pacman -Qs mariadb || true
```

Si están presentes paquetes MariaDB (o relacionados), elimínalos antes de continuar para evitar conflictos:

```sh
sudo pacman -Rns mariadb
```

> {% include note.html content="Este paquete construye MySQL desde el código fuente. Probablemente necesitarás al menos 4 Gigabytes de memoria para que la compilación tenga éxito." %}

```sh
mkdir -p ~/AUR
cd ~/AUR
git clone https://aur.archlinux.org/mysql.git
cd mysql
makepkg -si
```

Después de la instalación, inicializa MySQL:

```sh
sudo mysqld --initialize --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

Esto imprimirá una contraseña temporal. Toma nota de ella para el usuario root para más adelante al configurar el servidor.

```sh
sudo systemctl enable --now mysqld
```

MySQL ahora está inicializado y listo para su configuración.

## Siguientes pasos

Una vez que tu servidor de base de datos esté instalado y en funcionamiento, continúa con la guía [Instalación clásica en Linux](classic-installation) para compilar AzerothCore y finalizar la configuración.
