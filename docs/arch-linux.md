# Arch Linux Install
This page covers Arch Linux-specific dependency setup for AzerothCore. It is intended to be used together with the [Linux Classic Installation](classic-installation) guide.

{% include warning.html content="The AzerothCore package in the AUR is very out of date and not recommended." %}

## Before you begin
- This guide does not explain how to install Arch Linux itself.
- Make sure your system is up to date and you have a normal user with `sudo` privileges.
- The [Arch Wiki](https://wiki.archlinux.org/title/Installation_guide) is the best source for general Arch installation and package management.

Make sure your system is fully up to date, and if you update the kernel, please reboot into the new kernel before continuing.
```sh
sudo pacman -Syu
```

## Required packages
Install the core development packages needed to build AzerothCore:

```sh
sudo pacman -Syu --needed base-devel git cmake clang boost
```

## MySQL on Arch Linux
AzerothCore requires Oracle MySQL. Oracle MySQL is not available from the official Arch repositories, so this guide installs it from the AUR.

> {% include warning.html content="Trusting keys is always up to the user to verify that the key being trusted should be. If you have any doubts or concerns, stop here and use a different installation method." %}

Import the MySQL signing key:

```sh
gpg --recv-keys B7B3B788A8D3785C
```

Build and install the AUR package:

> {% include note.html content="This pacakge builds MySQL from source. You will likely need at least 4 Gigabytes of memory for the compile to succeed." %}


```sh
mkdir -p ~/AUR
cd ~/AUR
git clone https://aur.archlinux.org/mysql.git
cd mysql
makepkg -si
```

After installation, enable and start MySQL:

```sh
sudo systemctl enable --now mysql.service
```

## Next steps
Once your database server is installed and running, continue with the [Linux Classic Installation](classic-installation) guide to compile AzerothCore and finish configuration.
