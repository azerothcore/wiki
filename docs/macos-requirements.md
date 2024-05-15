# macOS Requirements

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](classic-installation.md) | [Step 2: Core Installation >>](macos-core-installation.md) |

| |
| :- |
| MacOS ≥ 11 |
| OpenSSL ≥ 3.0 |
| Boost ≥ 1.70 |
| MySQL ≥ 5.7.0 |
| CMake ≥ 3.16 |

- Install XCode using the App Store, then open the terminal and type:

```sh
xcode-select --install
```

- Install the package manager [Homebrew](http://brew.sh/)

Use brew it to install the required packages:

```sh
brew update
```

```sh
brew install openssl@3 readline cmake boost coreutils bash bash-completion coreutils
```

This will install bash 5+, you might need to restart your terminal.
Make sure you are using bash 5 or newer by typing `bash --version`.

Now install mysql:

```sh
brew install mysql
```

You will be prompted some instructions to complete the `mysql` installation, for example to properly set a password. Just follow the instructions and properly configure mysql. **This step is important, do not skip it.**

To verify that mysql has been properly installed, try accessing it using either the command line (e.g. `mysql -u root -p`) or using DB client managers with a UI like Sequel Ace.

You can install Sequel Ace with:

```sh
brew install --cask sequel-ace
```

<br>

## Help

If you are still having problems, check:

* [FAQ](faq.md)

* [Common Errors](common-errors.md)

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](classic-installation.md) | [Step 2: Core Installation >>](macos-core-installation.md) |
