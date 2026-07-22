# Instalación en Arch Linux
Esta página cubre la configuración de dependencias específicas de Arch Linux para AzerothCore. Está pensada para usarse junto con la guía de [Instalación clásica en Linux](classic-installation).

{% include warning.html content="El paquete AzerothCore en AUR está muy desactualizado y no se recomienda." %}

## Antes de empezar
- Esta guía no explica cómo instalar Arch Linux.
- Asegúrate de que tu sistema esté actualizado y de tener un usuario normal con privilegios `sudo`.
- La [Arch Wiki](https://wiki.archlinux.org/title/Installation_guide) es la mejor fuente para la instalación general de Arch y la gestión de paquetes.

Asegúrate de que tu sistema esté completamente actualizado y, si actualizas el kernel, reinicia con el nuevo kernel antes de continuar.
```sh
sudo pacman -Syu
```

## Paquetes requeridos
Instala los paquetes de desarrollo necesarios para compilar AzerothCore:

```sh
sudo pacman -Syu --needed base-devel git cmake clang boost
```

## MySQL en Arch Linux
AzerothCore requiere Oracle MySQL. Oracle MySQL no está disponible en los repositorios oficiales de Arch, por lo que esta guía lo instala desde AUR.

> {% include warning.html content="Confiar en llaves es siempre responsabilidad del usuario. Si tienes dudas o preocupaciones, detente aquí y utiliza otro método de instalación." %}

Importa la llave de firma de MySQL:

```sh
gpg --recv-keys B7B3B788A8D3785C
```

Construye e instala el paquete de AUR:

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

## Próximos pasos
Una vez que el servidor de base de datos esté instalado y funcionando, continúa con la guía de [Instalación clásica en Linux](classic-installation) para compilar AzerothCore y finalizar la configuración.
