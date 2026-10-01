---
redirect_from: "/cn/Live-e2e"
---

# 在线端到端测试

AzerothCore 可以在真实的 3.3.5a 服务器上运行**在线端到端测试**。它们是协议客户端，不是核心的桩代码，也不是 worldserver 的预演（dry-run）。

这些机器人来自 [AzerothGhost](https://github.com/azerothcore/AzerothGhost)。它们通过 auth 登录，进入世界，并驱动与正式客户端相同的操作码（登录、传送、施法、战斗、任务、拾取等）。断言会检查协议、对象缓存，有时还会检查角色数据库。

这**不能**替代[在游戏中测试 PR](how-to-test-a-pr)。它是对在线堆栈的额外覆盖，主要目的是防止 PR 在某个玩家可见的路径已经损坏的情况下被合并。

## CI 做了什么

针对 `azerothcore/azerothcore-wotlk` 的拉取请求（不包括 fork，也不包括草稿 PR），以及每次推送到 `master` 时：

1. 常规的 `nopch-build` 任务会编译真实的 `authserver` 和 `worldserver`（不使用 PCH），并上传这些二进制文件。
2. `e2e full` 任务启动 MySQL，并应用常规的 AC 数据库和客户端数据设置。
3. 它启动**那些相同的二进制文件**。`worldserver` 监听 8085 端口，`authserver` 监听 3724 端口。该任务会一直等待直到两个端口都能接受连接。
4. 它从 `e2e/` 目录运行 `go test -tags=e2e` 来针对该服务器进行测试。

因此，流水线会从这些二进制文件运行一个**完整**的 AC 堆栈，然后像客户端一样与它通信。不存在部分 worldserver，也没有模拟的战斗。

工作流中关于 "dry-run" 的注释只涉及 CMake/编译路径。测试本身总是针对一个运行中的进程。

`master` 上运行的是相同的完整测试套件，而不是冒烟子集。这样可以捕获偶发问题，以及旧 PR 在旧 `master` 上通过、但落地到后续提交后却失败的情况。

你也可以通过 `workflow_dispatch`（`scope=full` 或 `scope=smoke`）手动启动测试套件。

## 这些测试是什么

它们位于 AzerothCore 仓库的 `e2e/` 目录下（`smoke/` 和 `suites/`）。它们从 [AzerothGhost](https://github.com/azerothcore/AzerothGhost)（`e2e/e2eharness`）导入测试框架。

典型流程：

1. 创建一个 GM 测试账号和一个角色。
2. 登录并等待会话进入世界。
3. 放置机器人（命名传送、垫子，或 `.go creature`）。
4. 可选地准备战斗（`.gm off`、作弊、PvP 标记）。
5. 驱动一个真实的客户端动作（施法、拉怪、交易、重新登录……）。
6. 断言玩家会看到的结果（光环消失、生命值下降、仍然在桥上、下一波没有提前、世界仍然存活）。

设置过程可以使用 GM 命令。判定标准应该是玩家可见的结果，而不是"GM 命令返回了"。

未解决的核心 bug 会通过 `OPEN(e2e)` 和问题链接保持注释状态。它们不会被编译，因此不可能"软通过"。

## 如何在本地运行

你需要一个正在运行的 authserver、worldserver 和 MySQL，以及 Go 1.26+。

```bash
cd e2e
cp .env.example .env   # 编辑 auth 地址 + DSN
set -a; source .env; set +a
go test -tags=e2e ./... -count=1 -v -timeout 120m -parallel 1 -p 1
```

如果不加 `-tags=e2e`，`go test ./...` 会跳过这些包。

请保持 `-parallel 1 -p 1`，除非你确定每个并发包都有自己的隔离垫。共享一个垫会让机器人互相干扰。

编写细节：核心仓库中的 `e2e/README.md`，以及 AzerothGhost 的 [`LLM_GUIDE.md`](https://github.com/azerothcore/AzerothGhost/blob/main/e2e/LLM_GUIDE.md) 和 [`EXAMPLES.md`](https://github.com/azerothcore/AzerothGhost/blob/main/e2e/EXAMPLES.md)。
