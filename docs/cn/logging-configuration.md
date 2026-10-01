---
tableofcontents: 1
---

# 日志配置（类似 log4j）

## 在核心中设置日志

```cpp
LOG_TYPE("appender", "LOG MESSAGE {}", var);

// 示例
LOG_ERROR("sql.sql", "Unable to load creature entry {} and spawnId {}", entry, guid);
```

要在 LOG MESSAGE 中传入任何参数，请使用花括号，它使用 FMT 格式来接收任意参数并将其传入日志。

| 类型  |
| :---- |
| FATAL |
| ERROR |
| WARN  |
| INFO  |
| DEBUG |
| TRACE |

## 日志记录器（Logger）与附加器（Appender）

日志系统由两个组件组成：日志记录器（logger）和附加器（appender）。这两类组件使用户能够根据消息类型和级别记录日志，并在运行时控制它们在何处输出。

### 日志记录器（Logger）

该系统最主要的好处在于能够禁用某些日志语句，同时让其他日志语句不受阻碍地输出。

这一能力的前提是，日志记录器是根据某种由开发者选择的规则进行分类的。

日志记录器是命名实体。日志记录器的名称区分大小写，并遵循层级命名规则：

如果一个日志记录器的名称后面加一个点后，成为另一个日志记录器名称的前缀，那么前者被称为后者的祖先。如果在一个日志记录器和其派生日志记录器之间不存在其他祖先，那么前者被称为后者的父级。

例如，名为 "entities.player" 的日志记录器是名为 "entities.player.character" 的日志记录器的父级。同样，"entities" 是 "entities.player" 的父级，并且是 "entities.player.character" 的祖先。

日志记录器可以被分配级别。可用的级别有 TRACE、DEBUG、INFO、WARN、ERROR 和 FATAL，也可以使用 DISABLED 级别来禁用。

根据定义，打印方法决定了日志请求的级别。例如，LOG_INFO(...) 是一个级别为 INFO 的日志请求。

如果日志请求的级别高于或等于其日志记录器的级别，则该请求被视为启用；否则，该请求被视为禁用。没有分配级别的日志记录器会从层级中继承一个级别。

示例：

| Logger 名称 | 分配的级别 | 继承的级别 |
| :---------- | :------------- | :-------------- |
| root        | Proot          | Proot           |
| server      | None           | Proot           |

由于 "server" 未定义，它使用 root 日志记录器及其日志级别。

FATAL < ERROR < WARN < INFO < DEBUG < TRACE。

### 附加器（Appender）

根据日志记录器有选择地启用或禁用日志请求只是其中一部分功能。该系统允许日志请求输出到多个目的地。一个输出目的地被称为附加器（appender）。

当前系统为控制台、文件和数据库定义了附加器，但可以轻松扩展到远程套接字服务器、NT 事件日志、syslog 守护进程或任何其他系统。

一个日志记录器可以挂载多个附加器。针对某个日志记录器的每个启用的日志请求都会被转发到该日志记录器的所有附加器。

### 配置

系统会读取所有带有 "Logger." 和 "Appender." 前缀的配置元素，并配置日志系统。如果 "root" 无法被正确配置，核心将移除所有日志记录器和附加器，并创建一组默认配置：

- 日志级别为 Error 的 Logger "root"
- 日志级别为 Info 的 Logger "server"
- 用于记录到控制台的 Appender "Console"

附加器的配置行遵循以下格式：

> Type,LogLevel,Flags,optional1,optional2

它是一个用逗号分隔的元素列表，其中每个元素都有自己的含义。

```
Type: 附加器的类型

1 - (Console)
2 - (File)
3 - (DB)

LogLevel: 日志级别

0 - (Disabled)
1 - (Fatal)
2 - (Error)
3 - (Warning)
4 - (Info)
5 - (Debug)
6 - (Trace)

Flags: 定义对日志消息所做的一些额外修改

1 - 在文本前添加时间戳前缀
2 - 在文本前添加日志级别前缀
4 - 在文本前添加日志过滤器类型前缀
8 - 在日志文件名后附加时间戳。格式：YYYY-MM-DD_HH-MM-SS（仅用于 Type = 2）
16 - 在覆盖前备份现有文件（仅用于 Mode = w）
```

根据类型的不同，元素 optional1 和 optional2 会有不同的含义。

```
Colors（当 Type = Console 时作为 optional1 读取）

格式："fatal error warn info debug trace"
0 - BLACK
1 - RED
2 - GREEN
3 - BROWN
4 - BLUE
5 - MAGENTA
6 - CYAN
7 - GREY
8 - YELLOW
9 - LRED
10 - LGREEN
11 - LBLUE
12 - LMAGENTA
13 - LCYAN
14 - WHITE
示例："1 9 3 6 5 8"

File：文件名（当 Type = File 时作为 optional1 读取）
允许使用一个 "%u" 来创建动态文件

Mode：打开文件的模式（当 Type = File 时作为 optional2 读取）

a - (Append)
w - (Overwrite)
```

示例：

```
Appender.Console1=1,5,6
```

创建一个新的附加器，将任何级别为 DEBUG 或更高的消息记录到控制台，并在消息前加上日志类型和级别前缀。

```
Appender.Console2=1,2,1,"1 9 3 6 5 8"
```

创建一个新的附加器，将任何级别为 ERROR 或更高的消息记录到控制台，并使用彩色文本在消息前加上时间戳前缀。

```
Appender.File=2,5,7,Auth.log,w
```

创建一个新的附加器，将任何级别为 DEBUG 或更高的消息记录到文件 "Auth.log" 中，并在消息前加上时间戳、类型和级别前缀。

在示例中，让两个不同的日志记录器都记录到控制台是完全合法的，但有些冗余。

一旦我们有了要读取的日志记录器列表，系统就会尝试根据其配置行配置一个新的日志记录器。日志记录器的配置行遵循以下格式：

> LogLevel,AppenderList

它是一个用逗号分隔的元素列表，其中每个元素都有自己的含义。

```
LogLevel

0 - (Disabled)
1 - (Fatal)
2 - (Error)
3 - (Warning)
4 - (Info)
5 - (Debug)
6 - (Trace)

AppenderList: 链接到日志记录器的附加器列表
（使用空格作为分隔符）。
```

## 示例

### 示例 1

将错误日志输出到控制台，以及一个名为 server.log 且只包含本次服务器运行日志的文件。文件应在消息前加上时间戳、类型和日志级别前缀。控制台应在消息前加上类型和日志级别前缀。

```
Appender.Console=1,2,6
Appender.Server=2,2,7,Server.log,w
Logger.root=2,Console Server
```

让我们跟踪系统如何记录两条不同的消息：

1. LOG_ERROR("guild", "Guild 1 created");

系统将尝试查找类型为 GUILD 的日志记录器，由于没有为 GUILD 配置日志记录器，它将使用 Root 日志记录器。由于消息的日志级别等于或高于日志记录器的日志级别，该消息会被发送到日志记录器中配置的附加器："Console" 和 "Server"。

Console 将写入："ERROR [GUILD] Guild 1 created"

Server 将写入文件："2012-08-15 ERROR [GUILD] Guild 1 created"

2. LOG_INFO("entities.player.character", "Player Name Logged in");

系统将尝试查找类型为 "character" 的日志记录器，由于没有为 "character" 配置日志记录器，它将使用 Root 日志记录器。由于消息的日志级别不等于或高于日志记录器的日志级别，该消息被丢弃。

### 示例 2

与上面相同的示例，但现在我想在文件中看到所有级别为 INFO 的消息，并且服务器文件应在创建时附加时间戳。

```
Appender.Console=1,2,6
Appender.Server=2,4,15,Server.log
Logger.root=3,Console Server
```

让我们跟踪系统如何记录两条不同的消息：

1. LOG_ERROR("guild", "Guild 1 created");

与示例 1 完全一致。

2. LOG_INFO("entities.player.character", "Player Name Logged in");

系统将尝试查找类型为 "character" 的日志记录器，由于没有为 "character" 配置日志记录器，它将使用 Root 日志记录器。由于消息的日志级别等于或高于日志记录器的日志级别，该消息会被发送到日志记录器中配置的附加器："Console" 和 "Server"。

Console 将丢弃该消息，因为日志级别不高于或等于此附加器的级别。

Server 将写入文件："2012-08-15 INFO [CHARACTER] Player Name Logged in"

### 示例 3

作为一名开发者，在尝试修复某些问题时，我可能只对记录核心的某个特定部分感兴趣。所以……我想以最高级别调试 "guild"，并在一定程度上记录一些 "character" 事件。此外，我正在检查一些路径点（Waypoints），所以我希望 "sql.dev" 无前缀地记录到文件。所有其他消息应只记录到控制台，"guild" 记录到 TRACE，"character" 记录到 INFO。

```
Appender.Console=1,6
Appender.SQLDev=2,5,0,SQLDev.log
Logger.guild=6,Console
Logger.entities.player.character=4,Console
Logger.sql.dev=4,SQLDev
```

使用此配置，任何日志类型不是 "guild"、"character" 或 "sql.dev" 的消息都会被忽略，因为我们没有定义 Root 日志记录器，系统创建了默认的 Root（已禁用）。Appender Console 的日志级别应被定义为允许其日志记录器的所有可能消息，在本例中 "guild" 使用 TRACE（6），因此 Appender 应允许它。Logger Characters 会将其自身消息限制为 INFO（4）。
