# 退出代码（Exit Codes）

AzerothCore 有 3 个默认的退出代码，当您关闭、重启或崩溃服务器时会调用它们。

```cpp
enum ShutdownExitCode
{
    SHUTDOWN_EXIT_CODE = 0,
    ERROR_EXIT_CODE    = 1,
    RESTART_EXIT_CODE  = 2,
};
```

当您使用 **.server shutdown**、**.server idleshutdown**、**.server exit** 命令时，或在 Windows 下当 [m_serviceStatus == 0](https://github.com/azerothcore/azerothcore-wotlk/blob/a594bf5b290e5476c61bab29809a079e93c5daa2/src/server/worldserver/Main.cpp#L575-L581) 时，会调用 SHUTDOWN_EXIT_CODE。

当您使用 **.server restart** 和 **.server idlerestart** 命令时，会调用 RESTART_EXIT_CODE。

当服务器崩溃时，会调用 ERROR_EXIT_CODE。这可能是由于 guid/id/entry 溢出、[Network.Threads](https://github.com/azerothcore/azerothcore-wotlk/blob/a594bf5b290e5476c61bab29809a079e93c5daa2/src/server/worldserver/worldserver.conf.dist#L2909-L2913) 小于等于 0，或服务器无法初始化网络所致。

了解所有退出代码在何处被调用的最佳方法是在源代码中查找它们。

## 命令

```
.server idleshutdown #delay [#exit_code]
.server idlerestart #delay [#exit_code]
.server shutdown #delay [#exit_code]
.server restart #delay [#exit_code]
```

**.server shutdown/restart**、**.server idleshutdown/restart** 命令都有 **[#exit_code]** 参数。

如果参数留空，shutdown 的默认退出代码始终为 0，restart 的默认退出代码始终为 2。

该参数可以取 0 - 125 之间的值，这样您可以输出除默认值之外的自定义退出代码。

## 包含退出代码的脚本

Worldserver 发送退出代码使您可以创建外部脚本，当脚本读取到显示的特定退出代码时即可采取相应操作。

例如，可以编写一个脚本，当 Worldserver 发送 RESTART_EXIT_CODE 时自动重启。

您可以查看[此](https://github.com/azerothcore/azerothcore-exitcode-script) Windows 批处理脚本，了解退出代码的用法。
