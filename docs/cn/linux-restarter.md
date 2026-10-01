## 简介
本教程将指导你在使用 Linux 服务器时，创建一个在关闭、重启或崩溃后重启 AzerothCore 的脚本。

设置重启器的最简单方法是使用我们的[集成脚本或 docker](how-to-restart-and-debug)。

不过，下面将向你展示如何从零开始创建你自己的重启器。

## 创建脚本
#### 前置条件
- 确认你的 Linux 服务器已安装 screen 和 nano。

```sh
sudo apt-get update && sudo apt-get install screen nano
```

- 安装好 screen 和 nano 后，继续下一步。

#### 脚本创建
- 进入你的服务器 bin 目录 `~/azeroth-server/bin`，然后输入 `nano auth.sh`
- 在新建的 nano 界面中，输入以下脚本：

```sh
#!/bin/sh
while :; do
./authserver
sleep 20
done
```

- 输入完成后，按 Ctrl + O，按 Enter 确认，然后按 Ctrl + X。这将保存新脚本并返回终端。我们刚刚创建了 Authserver 重启脚本。接下来创建 Worldserver 脚本。
- 输入 `nano world.sh`
- 在新建的 nano 界面中，输入以下脚本：

```sh
while :; do
./worldserver
sleep 20
done
```

- 输入完成后，按 Ctrl + O，按 Enter 确认，然后按 Ctrl + X。这将保存新脚本并返回终端。我们刚刚创建了 Worldserver 重启脚本。接下来创建一个同时启动 Authserver 和 Worldserver 重启脚本的脚本。
- 输入 `nano restarter.sh`

```sh
#!/bin/bash
screen -AmdS auth ./auth.sh
screen -AmdS world ./world.sh
```

- 输入完成后，按 Ctrl + O，按 Enter 确认，然后按 Ctrl + X。最后，让我们创建服务器关闭脚本。
- 输入 `nano shutdown.sh`

```sh
#!/bin/bash
screen -X -S "world" quit
screen -X -S "auth" quit
```

- 输入完成后，按 Ctrl + O，按 Enter 确认，然后按 Ctrl + X。接下来，让我们启动服务器。

## 服务器管理
#### 服务器启动
- 要使用这些脚本启动服务器，请确保你位于服务器 bin 目录 `~/azeroth-server/bin` 中。
- 我们将通过输入以下命令 `./restarter.sh` 来启动重启脚本。
- 补充说明：如果你希望在启动服务器的同时看到 worldserver 控制台，请使用以下命令 `./restarter.sh; screen -r world`。

#### 服务器监控
- 访问并查看 Authserver 或 Worldserver 控制台：
-- Authserver：`screen -r auth`
-- Worldserver：`screen -r world`
- 当你想退出 screen 并返回终端时，按 Ctrl + A，然后按 D。

#### 服务器关闭
- 要终止重启器并关闭服务器，请确保你位于服务器 bin 目录 `~/azeroth-server/bin` 中。
- 输入 `./shutdown.sh`，脚本将关闭，你的服务器也会随之终止。
