# Arch Linux Install
If you are an Arch Linux user you can  install  it from AUR ([Arch User Repository](https://wiki.archlinux.org/index.php/Arch_User_Repository))

## Install dependencies

### Install *base-devel*
All you need to install AUR packages is [*base-devel*](https://www.archlinux.org/groups/x86_64/base-devel/) and [*git*](https://www.archlinux.org/packages/?name=git), you can install them with *pacman*:
```
$ sudo pacman -S base-devel git
```

### Install *ACE*
Then you need to install [*ACE*](https://aur.archlinux.org/packages/ace/) package from AUR:
```
git clone https://aur.archlinux.org/ace.git
cd ace
makepkg -si
```
## Install *AzerothCore*
After that you can install [azeroth-core](https://aur.archlinux.org/packages/azeroth-core/) package:

```
git clone https://aur.archlinux.org/azeroth-core.git
cd azeroth-core
makepkg -si
```
Moreover, if you want you can use [*yay*](https://github.com/Jguer/yay) as AUR package manager to install AUR packages.
