# macOS Requirements

| Installation Guide                                                                                                                   |                                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Start: Installation Guide](classic-installation)                                                                                 | [Step 2: Core Installation >>](macos-core-installation) |

|               |
| :------------ |
| MacOS ≥ 11    |
| OpenSSL ≥ 3.0 |
| Boost ≥ 1.74  |
| MySQL ≥ 8.0.0 |
| CMake ≥ 3.16  |

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

{% include help.html %}

| Installation Guide                                                                                                                   |                                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Start: Installation Guide](classic-installation)                                                                                 | [Step 2: Core Installation >>](macos-core-installation) |
