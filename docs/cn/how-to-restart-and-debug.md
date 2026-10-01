---
tableofcontents: 1
---

# 如何重启和调试

AzerothCore 由两个服务组成：authserver 和 worldserver。
Authserver 仅充当认证器和领域路由器，将你已认证的客户端连接重定向到所选领域的地址。
而 worldserver 则处理所有与游戏机制相关的连接，并且是单个领域所有相关事物的唯一权威来源。

Authserver 和 worldserver 可以部署在不同的环境中。不过，在下面的指南中，我们将说明如何在同一个环境中一起运行它们。

## `startup-scripts` 引擎

我们引入了一套新的启动脚本，提供了一种强大且统一的方式来运行、管理和调试你的服务器。对于所有非 Docker 安装，这现在是处理 `authserver` 和 `worldserver` 进程的推荐方式。

这些脚本提供了高级功能，例如通过 systemd 或 PM2 自动重启、会话管理（使用 `tmux` 或 `screen`），以及用于崩溃分析的集成 GDB 调试。

有关如何使用和配置新启动脚本的完整指南，请参阅官方的 **[startup-scripts 目录中的 README.md](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/startup-scripts/README.md)**。

### 基本用法

使用新系统最简单的方式是通过 acore.sh 仪表盘：

```bash
# 使用新引擎运行 worldserver
./acore.sh run-worldserver

# 使用新引擎运行 authserver
./acore.sh run-authserver
```

### 配置和调试

要启用 GNU 调试器（GDB）并生成崩溃报告，你需要编辑服务的配置文件。例如，对于名为 `ac-world-1` 的服务，你可以编辑类似 ac-world-1-run-engine.conf 的文件并设置 `GDB_ENABLED=1`。

```properties
// ...existing code...
# Enable/disable GDB execution
export GDB_ENABLED=1
// ...existing code...
```

如果在启用 GDB 后服务器崩溃，你会在 `apps/startup-scripts/logs/crashes/` 目录中找到崩溃转储文件（例如 `gdb-YYYY-MM-DD-HH-MM-SS.txt`）。<b>请记住，你必须使用以下编译类型之一来编译代码：`Debug` 或 `RelWithDebInfo`，否则 GDB 将无法生成有意义的报告。</b>

## 使用 Docker（跨平台）

我们的 Docker 设置集成了 `startup-scripts` 引擎。这意味着在 Docker 环境中启用 GDB 和管理重启也同样可以无缝工作。此外，我们的 docker-compose.yml 使用了 [restart-policy 功能](https://docs.docker.com/config/containers/start-containers-automatically/) 在崩溃或系统重启后自动保持容器运行。

更多信息请参阅 [使用 Docker 安装](https://www.azerothcore.org/wiki/Install-with-Docker) 文档。你还会在那里找到如何使用 VSCode 结合其 Remote Docker 扩展来调试代码的指南。
