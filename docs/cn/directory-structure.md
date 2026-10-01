---
redirect_from: "/cn/Directory-Structure"
---

# 目录结构

AzerothCore 及其模块遵循 hw-core 的目录结构标准：

<a href="https://github.com/HW-Core/directory-structure/blob/master/README" target="_blank">标准目录结构</a>

此结构符合我们的[模块化架构](the-modular-structure)。

azerothcore/

├── [apps][1]<br/>
├── [bin][2]<br/>
├── [conf][3]<br/>
├── [data][4]<br/>
├── [deps][5]<br/>
├── [env][6]<br/>
├── [modules][7]<br/>
├── [src][8]<br/>
└── [var][9]<br/>

[1]: #apps
[2]: #bin
[3]: #conf
[4]: #data
[5]: #deps
[6]: #env
[7]: #modules
[8]: #src
[9]: #var

##  AzerothCore Wotlk 目录结构详解：

### apps
  与模块相比，具有更高层级意识的实用程序和应用程序。它们可以参与项目的生命周期操作，例如 CI、模块安装、数据库迁移等。
  
  app 的一个示例是我们的 db_assembler，它能够创建和升级你的数据库安装。

### bin  
  包含此项目的二进制文件/脚本。此文件夹可以放置在你操作系统的 PATH 环境变量中，从而让你将项目的 CLI 脚本集成到你的 shell 中。
  
  一个示例是 azerothcore dashboard 脚本，它允许你直接运行安装程序 app、db_assembler 以及随 azerothcore 仓库附带的其他工具。

### conf  
  apps/ 和我们仓库中包含的其他工具所需的配置文件。它并不是存放 worldserver 和 authserver conf 文件的文件夹，因为 conf/ 文件夹仅用于仓库本身，不会被编译。
  
  配置文件的一个示例是 conf.sh.dist。它是一个一体化的 conf，供我们的 app（如 dashboard、编译器、db_assembler 等）使用。

### data 
  所有不与源代码一起编译的静态数据。
  
  data 的示例包括 sql 文件、assets 等。
  
  你可以[在这里](sql-directory)了解更多关于 SQL 目录的信息。
    
### deps
  这是一个面向领域的文件夹结构。因此，所有文件夹都定义了一个特定的业务领域。在这种情况下，每个文件夹都代表项目运行所需的一个独立组件。所有组件都按照[monorepo 策略](https://en.wikipedia.org/wiki/Monorepo)存储。所有通用且与 Wotlk 逻辑无关的代码都应移到 deps 层的一个独立组件下，并由相应的 VCS 管理。
  AzerothCore 的 deps 层可以被使用和配置来构建其他服务器应用程序。

  deps 的示例包括第三方库，如 acelib 和 g3dlite 库，以及由 azerothcore 组织为通用目的创建的库。

### modules
  这是一个面向领域的文件夹结构。事实上，此结构的主要好处就在于它的模块化。每个文件夹都代表一个独立的可选[模块](the-modular-structure)/插件，可用于扩展核心功能。所有模块都采用多仓库策略存储，并且默认被 git 忽略。
  
  模块的示例包括 transmog、autobalance、crossbattlegrounds 等。

### env
  此文件夹用于默认的发布环境。默认情况下，编译器会在 /env/dist 文件夹内生成服务器应用程序所需的二进制文件、配置文件以及所有内容。不过，正如 directory-structure 标准中所解释的那样，此文件夹可用于创建任何类型的嵌套封装环境。

### src  
  所有与本应用程序/项目及 wotlk 服务器版本严格相关的源代码。它遵循面向角色的文件夹结构。这是许多框架中常见的经典目录结构。文件按其角色（game、scripts、tools 等）组织。其主要好处是可以快速了解特定角色的所有文件。
  
### var  
  此文件夹中的内容会被 git 忽略。var 文件夹包含易变数据，例如临时的构建文件。注意：var 文件夹不用于存储 worldserver/authserver 日志，尽管它们也是易变数据，因为这些数据与仓库生命周期无关，并且位于**应用程序环境**（/env/dist）中。
  
  
![AC Layers](https://docs.google.com/drawings/d/e/2PACX-1vQDBXPZMAq2HSszx8BGxloxQ5cqDULLC2tCgCmO2uyAF6HH3s9RkDFZxbQVsmFY8xM8Y18rIQJg1mBU/pub?w=1413&h=945)
