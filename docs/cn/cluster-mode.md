# 集群模式（Cluster Mode）

| 安装指南                                                                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击前面的链接在各步骤之间轻松切换。 |
| [<< 第 9 步：可选附加内容](optional-additions)                                                                                  |

{% include warning.html content="集群模式是 <b>实验性</b> 功能，仍在开发中。" %}

## 概述

集群模式允许多个 worldserver 共同服务**一个服务器**（realm），在它们之间分配玩家和地图。每个 worldserver 可以声明它愿意处理哪些地图；[ToCloud9](https://github.com/walkline/ToCloud9) 随后在集群中分配地图，并在玩家更换地图时将玩家重定向到正确的 worldserver。

AzerothCore 只提供集成点（配置、地图分配钩子、登录/重定向路径，以及 sidecar C API）。分布式逻辑位于 ToCloud9 中：服务发现、客户端连接的**网关（gateway）**、共享 GUID 池，以及 auth、characters、guild、mail、auction house、chat、group 和 matchmaking 服务。

有关架构及其设计理由，请参阅 [ToCloud9 README](https://github.com/walkline/ToCloud9#readme) 和 [AzerothCore 讨论](https://github.com/azerothcore/azerothcore-wotlk/discussions/16748)。

## 编译

AzerothCore 通过 **libsidecar** 与 ToCloud9 通信，libsidecar 是来自 ToCloud9 仓库的共享库。

默认情况下，核心会针对该库的**树内桩（stub）**进行编译，因此集群代码可以编译但不会执行任何操作。普通（非集群）构建不需要额外依赖，且不受影响。

要运行集群模式，你必须链接**真正的**库。受支持的实现是 **libsidecar-cpp**（原生 C++，相同的 C ABI）。

### 1. 编译 libsidecar-cpp

在 ToCloud9 的检出目录中：

```bash
cd game-server/libsidecar-cpp
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF
cmake --build . --config Release
```

在 Windows 上，请使用 **x64** 原生工具 / VS 生成器，例如：

```cmd
cmake .. -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF
cmake --build . --config Release
```

预编译的 Windows 二进制文件也发布在 [ToCloud9 releases](https://github.com/walkline/ToCloud9/releases) 页面（VS 2022 用 `libsidecar-cpp-windows-x64-v143`，VS 2019 用 `v142`）。

### 2. 将库安装到 AzerothCore 中

将产物放置到你的 AzerothCore 源码树的 `deps/libsidecar/` 下。CMake 期望共享库位于该目录的 `CMakeLists.txt` **旁边**（而不仅仅是嵌套的 `lib/` 下），C 头文件位于 `include/` 下。

在 **macOS** 和 **Linux** 上，libsidecar-cpp 以 `VERSION` / `SOVERSION` 构建，因此构建目录包含**三个**相关名称——一个真实二进制文件和两个符号链接。请**全部**复制并**保留符号链接**（不要将它们压平为三个完整副本）。

| 平台 | 构建目录中的典型文件 |
| -------- | ------------------------------------ |
| macOS | `libsidecar.0.0.1.dylib`（真实文件）<br>`libsidecar.0.dylib` → `libsidecar.0.0.1.dylib`<br>`libsidecar.dylib` → `libsidecar.0.dylib` |
| Linux | `libsidecar.so.0.0.1`（真实文件）<br>`libsidecar.so.0` → `libsidecar.so.0.0.1`<br>`libsidecar.so` → `libsidecar.so.0` |
| Windows | `libsidecar.dll` **和** `libsidecar.lib`（没有带版本的符号链接） |

AzerothCore 的 CMake 会查找不带版本的名称（`libsidecar.dylib` / `libsidecar.so` / `libsidecar.dll`）。加载器仍会沿符号链接链找到真实二进制文件，因此省略带版本的文件或破坏链接都会导致链接或运行时失败。

同时让头文件与你编译的库保持同步：

```text
deps/libsidecar/include/   ← 从 ToCloud9 game-server/libsidecar-cpp/include/ 复制
```

集群模式源码树已自带匹配的头文件；升级 libsidecar 时请替换它们。

示例（macOS / Linux，在 libsidecar-cpp 的 Release 构建之后）。使用 `cp -a` 以便两个符号链接保持为符号链接：

```bash
# macOS
cp -a game-server/libsidecar-cpp/build/libsidecar*.dylib /path/to/azerothcore/deps/libsidecar/
# Linux
# cp -a game-server/libsidecar-cpp/build/libsidecar.so* /path/to/azerothcore/deps/libsidecar/

cp game-server/libsidecar-cpp/include/*.h /path/to/azerothcore/deps/libsidecar/include/

# 运行时加载器也需要同样的三件套（真实文件 + 两个符号链接）：
sudo cp -a game-server/libsidecar-cpp/build/libsidecar*.dylib /usr/lib/   # macOS
# sudo cp -a game-server/libsidecar-cpp/build/libsidecar.so* /usr/lib/  # Linux
```

在 Windows 上，除 `deps/libsidecar/` 用于链接外，还要将 `libsidecar.dll` 复制到 `worldserver.exe` 旁边（或 `PATH` 中）。

### 3. 使用真实库配置 AzerothCore

配置核心时传入 [CMake 选项](cmake-options) **`-DUSE_REAL_LIBSIDECAR=ON`**。

CMake 摘要会以下列方式确认该选择：

```text
* Use stub for libsidecar         : No
```

如果那一行仍然显示 `Yes`，说明真实库未被选中，或者在 CMake 预期的位置未找到。

## 配置

相关选项位于 `worldserver.conf` 末尾的 `CLUSTER SETTINGS` 区块中。编辑前请参阅[如何使用配置文件](how-to-work-with-conf-files)。

| 设置 | 默认值 | 描述 |
| ------- | ------- | ----------- |
| `Cluster.Enabled` | `0` | 启用集群模式并初始化 libsidecar。 |
| `Cluster.AvailableMaps` | `""` | 此 worldserver 可以处理的以逗号分隔的地图 ID 列表，例如 `"0,1,573"`。空值表示任意地图；随后 ToCloud9 的 servers-registry 会在集群中分配一个子集。 |
| `Cluster.IsCrossrealm` | `0` | 启用跨服行为。需要连接到 MySQL 跨服反向代理（ToCloud9 `mysqlreverseproxy`）。 |

与 AzerothCore 的其他设置一样，这些设置可以用环境变量覆盖（`AC_CLUSTER_ENABLED`、`AC_CLUSTER_AVAILABLE_MAPS`、`AC_CLUSTER_IS_CROSSREALM`，以及相关的端口如 `AC_WORLD_SERVER_PORT`）。Sidecar 服务端点通过 ToCloud9 文档中描述的 `TC9_*` / 服务环境变量单独配置。

{% include important.html content="当 <code>Cluster.Enabled = 1</code> 时，ToCloud9 网关成为可信的认证边界。worldserver 随后会跳过会话密钥摘要验证、数据包加密、warden、IP/国家锁定、封禁和最低安全级别强制执行，以及登录时的角色所有权检查。worldserver 端口必须只能由网关访问，<b>绝不能直接暴露给玩家</b>。" %}

你还必须运行 ToCloud9 微服务（至少包括 servers-registry、guidserver、gateway、authserver，以及你依赖的 guild/mail/chat/group/auction/matchmaking 服务），并让 libsidecar 指向它们。使用 ToCloud9 auth 路径时，请**不要**为该服务器运行 AzerothCore 自带的 `authserver`。

## 运行集群

设置说明由 ToCloud9 仓库维护：

* [Docker Compose](https://github.com/walkline/ToCloud9#readme) — 启动完整集群的最快方式
* [Helm chart](https://github.com/walkline/ToCloud9/tree/master/chart) — Kubernetes
* [Windows + WSL，不使用 Docker](https://github.com/walkline/ToCloud9/blob/master/doc/RunNonDockerWinWSLAzerothCore.md)
* [Windows 原生，不使用 Docker](https://github.com/walkline/ToCloud9/blob/master/doc/RunNonDockerWindowsAzerothCore.md)（libsidecar-cpp）
* **不使用 Docker 的 Linux / macOS**：按上述方法编译 libsidecar-cpp，用 `-DUSE_REAL_LIBSIDECAR=ON` 配置核心，为 characters 数据库应用 ToCloud9 SQL 迁移，启动 ToCloud9 服务，然后运行一个或多个启用 `Cluster.Enabled = 1` 的 worldserver（每个进程使用不同的端口 / `TC9_GRPC_PORT` / `TC9_HEALTH_CHECK_PORT`）

最小的多 worldserver 示例（在服务启动之后）：

```bash
# worldserver A
AC_CLUSTER_ENABLED=1 AC_WORLD_SERVER_PORT=9601 ./worldserver

# worldserver B（覆盖 sidecar 端口以避免冲突）
AC_CLUSTER_ENABLED=1 AC_WORLD_SERVER_PORT=9602 \
  TC9_GRPC_PORT=9603 TC9_HEALTH_CHECK_PORT=9604 ./worldserver

# 可选：将进程固定到单个地图（例如冰冠堡垒）
AC_CLUSTER_ENABLED=1 AC_CLUSTER_AVAILABLE_MAPS=631 AC_WORLD_SERVER_PORT=9605 \
  TC9_GRPC_PORT=9606 TC9_HEALTH_CHECK_PORT=9607 ./worldserver
```

## 获取帮助

不属于 AzerothCore 侧的集群模式问题应提交到 [ToCloud9 问题跟踪器](https://github.com/walkline/ToCloud9/issues) 或其 [Discord 频道](https://discord.gg/QxfBD9uGbN)。
