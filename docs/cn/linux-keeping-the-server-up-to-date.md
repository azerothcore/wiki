# Linux 保持服务器最新

| 安装指南                                                                                                                             |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 6 步：服务器最终步骤](final-server-steps)                                                                                     | [第 8 步：客户端设置 >>](client-setup)                       |

## 保持源代码最新

```sh
cd ~/azerothcore/
git pull origin master
```

重新编译你拉取到的更改。

```sh
cd build
make -j$(nproc --all); make install
```
_你可以将 `-j$(nproc -all)` 替换为用于构建的核心数。例如：-j 2_

有时我们会向仓库中添加或移除文件。此时有必要重新编译服务器，方式与[首次在 Linux 核心安装中](linux-core-installation#configuring-for-compiling)安装时相同。

## 使用自动化服务器
如果你想使用 Jenkins、TeamCity 或类似工具更新 AzerothCore，以下步骤可能会对你有帮助。

将所需命令添加到 sudoers 文件中。下面的服务是在 [Linux 核心安装](linux-core-installation#optional-systemd-services)中创建的。
```sh
sudo visudo

%sudo ALL=NOPASSWD: /usr/sbin/service worldserver start
%sudo ALL=NOPASSWD: /usr/sbin/service authserver start
%sudo ALL=NOPASSWD: /usr/sbin/service worldserver stop
%sudo ALL=NOPASSWD: /usr/sbin/service authserver stop
%sudo ALL=NOPASSWD: /srv/azerothcore-wotlk/acore.sh compiler all
```

在 Jenkins/TeamCity 中运行命令
```sh
sudo service worldserver stop
sudo service authserver stop

cd /srv/azerothcore-wotlk
git pull origin master

sudo /srv/azerothcore-wotlk//acore.sh compiler all

sudo service worldserver start
sudo service authserver start
```


## 保持数据库最新

请阅读[数据库：保持服务器更新](database-keeping-the-server-up-to-date)

<br>

## 帮助

{% include help.html %}

| 安装指南                                                                                                                             |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 6 步：服务器最终步骤](final-server-steps)                                                                                     | [第 8 步：客户端设置 >>](client-setup)                       |
