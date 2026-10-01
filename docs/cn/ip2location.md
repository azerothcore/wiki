# IP2LOCATION

使用 IP2LOCATION，我们可以通过 `.pinfo <player>` 命令大致看到玩家可能来自哪个国家。

要能够使用此系统，你必须向你的 Authserver 提供 **ip2location lite 数据库**。

从 https://download.ip2location.com/lite/ 下载 **IP2LOCATION-LITE-DB1.CSV**

解压该文件并将其放在你选择的目录中。

在 authserver.conf 和 worldserver.conf 中，你需要在 IPLocationFile 下设置包含 .CSV 的完整目录路径。

在 Auth 和 Worldserver 启动时，你将能够在日志中看到 .CSV 文件被加载。
