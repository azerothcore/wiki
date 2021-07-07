# Instalación de Arch Linux
Si es un usuario de Arch Linux, puede instalarlo desde AUR ([Arch User Repository](https://wiki.archlinux.org/index.php/Arch_User_Repository))

## Instalar dependencias

### Instalar  *base-devel*
Todo lo que necesita para instalar los paquetes AUR es [*base-devel*](https://www.archlinux.org/groups/x86_64/base-devel/) and [*git*](https://www.archlinux.org/packages/?name=git), puede instalarlos con *pacman*:
```
$ sudo pacman -S base-devel git
```

### Instalar *ACE*
Debe instalar el paquete [*ACE*](https://aur.archlinux.org/packages/ace/) de AUR:
```
git clone https://aur.archlinux.org/ace.git
cd ace
makepkg -si
```
## Instalar *AzerothCore*
Después de eso, puedes instalar el paquete [azerothcore](https://aur.archlinux.org/packages/azerothcore/) :

```
git clone https://aur.archlinux.org/azerothcore.git
cd azerothcore
makepkg -si
```
Además, si lo desea, puede usar [*yay*](https://github.com/Jguer/yay) como administrador de paquetes AUR para instalar paquetes AUR.
