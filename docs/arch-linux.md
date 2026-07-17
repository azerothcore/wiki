# Arch Linux Install
This guide assumes you will follow the Linux Classic Installation guide. This page will get all the dependencies you will need to compelete that setup.

{% include warning.html content="The AzerothCore package in the AUR is very out of date and not reccommended" %}

## Installing Arch
This is not meant to be a comprehensive guide on how to install Arch, and you should refer to the fantastic guides at [Arch Wiki](https://wiki.archlinux.org/title/Installation_guide).

## Install dependencies

### Install *base-devel*
All you need to install AUR packages is [*base-devel*](https://www.archlinux.org/groups/x86_64/base-devel/) and [*git*](https://www.archlinux.org/packages/?name=git), you can install them with *pacman*:
```
$ sudo pacman --needed -S base-devel git cmake clang boost
```

## Installing MySQL
You cannot directly install mysql through pacman, so we will utilize the AUR for this step. You can use a helper of your choice if you would like to, but these instructions will just directly invoke and install the package.

In order to install the mysql package, we will need to import the signing key of Oracle first.
{% include warning.html content="Trusting keys is always up to the user to verify that the key being trusted should be. If you have any doubts or concerns, stop here and use a different installation method." %}
```
gpg --recv-keys B7B3B788A8D3785C
```

Now we can install MySQL

```
mkdir ~/AUR
cd ~/AUR
git clone https://aur.archlinux.org/mysql.git
cd mysql
makepkg -si
```

## Install *AzerothCore*
After that you can install [azerothcore](https://aur.archlinux.org/packages/azerothcore/) package:

```
git clone https://aur.archlinux.org/azerothcore.git
cd azerothcore
makepkg -si
```
