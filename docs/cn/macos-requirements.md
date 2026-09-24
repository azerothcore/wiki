# macOS 环境要求

{% include important.html content="<b>MySQL 26.x.x</b> 不受支持。请改用 <b>MySQL 8.4 LTS</b>。" %}

| 安装指南                                                                                                                             |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 开始：经典安装](classic-installation)                                                                                            | [第 2 步：核心安装 >>](macos-core-installation)              |

|               |
| :------------ |
| MacOS ≥ 11    |
| OpenSSL ≥ 3.0 |
| Boost ≥ 1.74  |
| MySQL ≥ 8.0.0 |
| CMake ≥ 3.16  |

- 使用 App Store 安装 XCode，然后打开终端并输入：

```sh
xcode-select --install
```

- 安装软件包管理器 [Homebrew](http://brew.sh/)

使用 brew 安装所需的软件包：

```sh
brew update
```

```sh
brew install openssl@3 readline cmake boost coreutils bash bash-completion coreutils
```

这将安装 bash 5+，你可能需要重启你的终端。
通过输入 `bash --version` 确保你使用的是 bash 5 或更高版本。

现在安装 mysql：

```sh
brew install mysql
```

系统会提示你完成 `mysql` 安装的一些说明，例如正确设置密码。请按照说明操作并正确配置 mysql。**这一步很重要，不要跳过。**

要验证 mysql 是否已正确安装，请尝试使用命令行（例如 `mysql -u root -p`）或使用像 Sequel Ace 这样带界面的数据库客户端管理器进行访问。

你可以通过以下命令安装 Sequel Ace：

```sh
brew install --cask sequel-ace
```

<br>

## 帮助

{% include help.html %}

| 安装指南                                                                                                                             |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 开始：经典安装](classic-installation)                                                                                            | [第 2 步：核心安装 >>](macos-core-installation)              |
