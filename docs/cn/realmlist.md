# realmlist

[<-返回至:Auth](database-auth)

**`realmlist` 表**

此表设置所有可用服务器的信息。每一行控制一个不同的服务器。

**表结构**

| Field                      | Type         | Attributes | Key | Null | Default       | Extra          | Comment |
| -------------------------- | ------------ | ---------- | --- | ---- | ------------- | -------------- | ------- |
| [id][1]                    | INT          | UNSIGNED   | PRI | NO   |               | AUTO_INCREMENT |         |
| [name][2]                  | VARCHAR(32)  | SIGNED     | UNI | NO   | ''            |                |         |
| [address][3]               | VARCHAR(255) | SIGNED     |     | NO   | 127.0.0.1     |                |         |
| [localAddress][4]          | VARCHAR(255) | SIGNED     |     | NO   | 127.0.0.1     |                |         |
| [localSubnetMask][5]       | VARCHAR(255) | SIGNED     |     | NO   | 255.255.255.0 |                |         |
| [port][6]                  | SMALLINT     | UNSIGNED   |     | NO   | 8085          |                |         |
| [icon][7]                  | TINYINT      | UNSIGNED   |     | NO   | 0             |                |         |
| [flag][8]                  | TINYINT      | UNSIGNED   |     | NO   | 2             |                |         |
| [timezone][9]              | TINYINT      | UNSIGNED   |     | NO   | 0             |                |         |
| [allowedSecurityLevel][10] | TINYINT      | UNSIGNED   |     | NO   | 0             |                |         |
| [population][11]           | FLOAT        | SIGNED     |     | NO   | 0             |                |         |
| [gamebuild][12]            | INT          | UNSIGNED   |     | NO   | 12340         |                |         |

[1]: #id
[2]: #name
[3]: #address
[4]: #localaddress
[5]: #port
[6]: #icon
[7]: #flag
[8]: #timezone
[9]: #allowedsecuritylevel
[10]: #population
[11]: #gamebuild

**字段说明**

### id

服务器 ID。此数字对每个服务器都是唯一的，并且必须与 worldserver.conf 中的 RealmID 配置值一致。

值必须 >=0。如果值不满足条件，SQL 将在 `realmlist_chk_1` 处失败。

### name

服务器的名称。它将显示在服务器选择列表以及角色选择界面中。

### address

世界服务器（world server）的公网（WAN）或局域网（LAN）IP 地址。如果只有你自己连接服务器（并且服务器与你的客户端运行在同一台机器上），请在此字段中使用 127.0.0.1。这是客户端用来连接世界服务器（worldserver）的地址。

或者，你也可以使用域名，例如 *example.com*。

### localAddress

对于本地或简单安装，通常为 127.0.0.1。

当客户端连接时，如果客户端地址与 `localAddress` 处于同一子网（根据 `localSubnetMask` 判断），则该客户端将获得 `localAddress` 来连接世界服务器，而不是 `address`。这在解决某些问题时很有用，例如局域网客户端连接被路由到外部再回到你的网络，例如某些 NAT 实现不擅长为非外部连接处理端口转发的情况。

### localSubnetMask

采用 `255.255.255.0` 这类格式的子网掩码。与 `localAddress` 配合使用。

### port

世界服务器（world server）运行所用的端口。如果所有世界服务器都在同一台机器上，则它们都需要使用不同的端口。

### icon

服务器的图标。

| Icon | Type   |
| ---- | ------ |
| 0    | Normal |
| 1    | PvP    |
| 4    | Normal |
| 6    | RP     |
| 8    | RP PvP |

### flag

此服务器的服务器标志（Realmflag）。

| Flag | Hex value | Description  |
| ---- | --------- | ------------ |
| 0    | 0x0       | None         |
| 1    | 0x1       | Invalid      |
| 2    | 0x2       | Offline      |
| 4    | 0x4       | SpecifyBuild |
| 8    | 0x8       | Medium       |
| 16   | 0xF       | Medium       |
| 32   | 0x10      | New Players  |
| 64   | 0x20      | Recommended  |
| 128  | 0x40      | Full         |

### timezone

服务器时区，它将显示在服务器列表的标签页中。

| timezone | displayed name     |
| -------- | ------------------ |
| 1        | Development        |
| 2        | United States      |
| 3        | Oceanic            |
| 4        | Latin America      |
| 5        | Tournament         |
| 6        | Korea              |
| 7        | Tournament         |
| 8        | English            |
| 9        | German             |
| 10       | French             |
| 11       | Spanish            |
| 12       | Russian            |
| 13       | Tournament         |
| 14       | Taiwan             |
| 15       | Tournament         |
| 16       | China              |
| 17       | CN1                |
| 18       | CN2                |
| 19       | CN3                |
| 20       | CN4                |
| 21       | CN5                |
| 22       | CN6                |
| 23       | CN7                |
| 24       | CN8                |
| 25       | Tournament         |
| 26       | Test Server        |
| 27       | Tournament         |
| 29       | CN9                |
| 30       | Test Server 2      |
| 31       | CN10               |
| 32       | CTC                |
| 33       | CNC                |
| 34       | CN1/4              |
| 35       | CN/2/6/9           |
| 36       | CN3/7              |
| 37       | Russian Tournament |
| 38       | CN5/8              |
| 39       | CN11               |
| 40       | CN12               |
| 41       | CN13               |
| 42       | CN14               |
| 43       | CN15               |
| 44       | CN16               |
| 45       | CN17               |
| 46       | CN18               |
| 47       | CN19               |
| 48       | CN20               |
| 49       | Brazil             |
| 50       | Italian            |
| 51       | Hyrule             |
| 52       | QA2 Test           |
| 53       |                    |
| 54       |                    |
| 55       | Recommended Realm  |
| 56       | Test               |
| 57       | Recommended Realm  |
| 58       |                    |
| 59       | Future Test        |

### allowedSecurityLevel

账号登录此服务器所需的最低账号 gmlevel。更改此值会自动更新游戏中可见的服务器列表，但必须重启 Worldserver 才能真正生效。

### population

此字段会定期自动更新，保存当前的人口数量。该字段值的计算公式为：playerCount / maxPlayerCount \* 2。在游戏内的服务器列表中，低、中、高人口的阈值分别为 0.5、1.0 和 2.0。

### gamebuild

服务器接受的客户端版本。

| Build Version | Client Patch |
| ------------- | ------------ |
| 5875          | 1.12.1       |
| 6005          | 1.12.2       |
| 8606          | 2.4.3        |
| 9947          | 3.1.3        |
| 10146         | 3.2.0        |
| 10505         | 3.2.2a       |
| 10571         | 3.3.0        |
| 11159         | 3.3.0a       |
| 11403         | 3.3.2        |
| 11623         | 3.3.3        |
| 11723         | 3.3.3a       |
| 12340         | 3.3.5a       |
