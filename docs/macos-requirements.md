# macOS Requirements

This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps.

| [<< Step 1: Requirements](requirements) | [Step 2: Core Installation >>](macos-core-installation) |
| :-- | --: |

{% include important.html content="<b>MariaDB</b> (any version) and <b>MySQL versions 5.7 and 8.1</b> are <b>not supported</b> by AzerothCore." %}

{% include important.html content="<b>MySQL 26.x.x</b> is <b>not supported</b>. Use <b>MySQL 8.4 LTS</b> instead." %}

{% include callout.html content="MacOS ≥ 11<br/>
OpenSSL ≥ 3.0<br/>
Boost ≥ 1.74<br/>
MySQL ≥ 8.0.0<br/>
CMake ≥ 3.16" type="info" %}

- Install XCode using the App Store, then open the terminal and type:

```sh
xcode-select --install
```

- Install the package manager [Homebrew](http://brew.sh/)

Use brew to install the required packages:

```sh
brew update
```

```sh
brew install openssl@3 readline cmake boost coreutils bash bash-completion
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

## Help

{% include help.html %}

This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps.

| [<< Step 1: Requirements](requirements) | [Step 2: Core Installation >>](macos-core-installation) |
| :-- | --: |
