# 分诊（Triaging）指南

## 简介

本指南旨在概述 AzerothCore 项目的 bug 分诊。它将涵盖目标、分诊流程、工具和来源的摘要，以及其他有用的链接。

## 目标

我们的目标是获取提交到 ChromieCraft issue 跟踪器的 bug 报告，并及时、准确、有记录地判断它是否是有效的报告。如果是，我们就将其连同补充的注释和文档一起转发到 AzerothCore issue 跟踪器。

那么，什么决定了有效的 bug 报告？如果一份 bug 报告展示了 AzerothCore 中与零售版暴雪 WoW 服务器在 “巫妖王之怒”（Wrath of the Lich King）时代的表现不一致的行为，那么它就是有效的。以下是一些有助于判断的日期：
- Wrath 于 2008 年 10 月 14 日随 3.02 补丁发布。
- 最后一个 Wrath 补丁是 3.3.5a，于 2010 年 6 月 29 日发布。
- Wrath 于 2010 年 10 月 12 日随着《大灾变》（Cataclysm）的发布而结束。

## 如何进行分诊

### 1. 选择一个 issue
你首先要进入 ChromieCraft issue 跟踪器：https://github.com/chromiecraft/chromiecraft/issues
选择一个带有橙色 ‘Needs Triage’（需要分诊）标签的 issue。

### 2. 检查重复项
选定一个 issue 后，首先搜索是否有重复项——任务名称、角色名称，甚至单个游戏对象的 GUID 都可以检查，以确保它们没有被报告过。在一个拥有如此庞大且不断增长的玩家基础的项目中，许多已报告的 issue 之前都已经被看到过。它们可能已被检查并认定不是 bug，也可能已经在某个尚未部署到 CC 的补丁中被修复。此外，找到其他相关的 issue（即使不是重复项）也有助于你更好地理解某个问题。

### 3. 验证 issue
现在我们已经确认这是一个新 bug，接下来要判断这究竟是明显错误的行为，还是可能由对游戏的误解、误读或无知造成的。这通常是通过对照下面列出的来源进行检查，以确定它到底是不是一个 bug。一些表面上的 bug 其实是预期行为，而另一些报告则是由游戏改动引起的——例如，在香草时代（Vanilla）正确的行为，由于平衡性调整，在 Wrath 中可能就是不正确的。

### 4. 尝试复现它
如果这是一个真正的问题，请尝试按照用户的说明去复现它。你可以在 CC PTR 或你自己的 AC 本地服务器上进行。如果用户没有提供足够的信息来复现问题，你总是可以请他们澄清，并在 CC 跟踪器上给该 issue 打上 “Waiting for Feedback”（等待反馈）标签。

如果你无法在自己的服务器上复现该行为，请注意，纯净的 AC 服务器并不总是与 ChromieCraft 服务器的行为方式相同。CC 上有大量的 mod 和其他自定义内容，可能会产生不可预测的影响，因此无法在纯净 AC 服务器上复现的 bug 被报告的情况相当常见。

#### 与 CC mod 和进度系统相关的 bug
Chromie 为了玩家的便利运行着许多 mod。这些包括 CFBG（跨阵营战场 mod）、跨阵营地下城、决斗重置 mod、低等级竞技场等等。这些故障虽然并不罕见，但与 AC 项目没有直接关系。如果你确定某份 bug 报告源自 CC mod，应尽可能向该 mod 自己的 GitHub issues 页面报告。你可以通过搜索 GitHub 找到它。

特别是，如果某个 issue 涉及不应在某个等级范围内可用的物品（例如，当 CC 当前的内容区间是 40-49 级时，商人却在出售 60 级的装备），那么这是一个进度系统（progression system）问题，可以在这里报告：https://github.com/azerothcore/progression-system

#### 客户端问题
请注意，Wow 客户端远非完美，工具提示和角色统计等内容的用户界面显示有时可能不准确。如果是这种情况，首先检查用户是否在运行 enUS 客户端，因为 enGB 客户端更容易出现这类问题。如果他们运行的是正确的客户端，那么请尝试确认问题只是显示方面的，而不是真实的。例如，有一个已知的客户端问题：一些低级物品出售时看起来是 0 铜币。如果你实际检查出售情况，会发现该物品是以正确的价格出售的，用户也获得了正确金额的钱，但界面上没有显示出来。这类问题属于客户端问题，最终无法由 AC 项目修复。

还有相当多的用户运行客户端 mod 来更改模型、贴图等，而且他们几乎从不提及这一点。但如果你看到某个看起来像客户端图形问题的问题（即这个 NPC 看起来很奇怪/模型错误/不可见），记得询问报告者是否运行了任何图形 mod。

### 5. 描述并记录该 issue
如果该 bug 是真实且有效的，如果原始报告者遗漏了任何重要细节，你可以补充其描述。在描述物体和生物时，尽量提供额外的有用信息，如数据库 ID 和出生点 GUID。

简单地注明该 bug 报告已被确认通常就足够了。然而，如果你想让证据尽可能清晰，那么截图或录制错误行为的视频通常是个好方法。战斗日志的截图尤其有用。对于视频，我发现 [OBS Studio](https://obsproject.com/download) 非常适合屏幕录制，而 [Shotcut](https://www.shotcut.org/) 是处理录制结果的好视频编辑器。（而且这两者都是 FOSS（自由开源软件），作为同样开源的项目，支持其他开源项目是件好事。）

### 6. 记录如何复现它
展示如何复现问题，最好使用 GM 命令。因此，不要写“接受任务 “Kill Ten Foozles””，而应写 `.quest add 1234`。命令 `.go c XXXX` 和 `.go o XXXX`（分别用于前往生物和物体）在这里很有用，因为它们可以让你直接传送到问题所在之处。`.additem [itemname]` 也很方便。

请记住，当有人提交 PR 来修复这个 issue 时，修复者和 PR 的测试者都会依赖你在这里提供的信息来简化他们的工作。

### 7. 复制到 AC 跟踪器并附上指向 CC 的链接
现在你已经确认这是一个有效的 bug，你可以把它移到 AzerothCore issue 跟踪器。操作方式是[在这里](https://github.com/azerothcore/azerothcore-wotlk/issues/new?assignees=&labels=&template=)创建一个新的空白 issue。然后你可以从原始 CC 工单中复制数据。你可以点击报告文本框右上角的三个水平点并选择 Edit（编辑）来完成此操作。然后你可以复制工单文本，将该信息粘贴到 AC 工单中，再添加你自己的评论和发现，生成最终的工单。

为它起一个合适的标题——清晰且一致是最好的。然后添加上报给 ChromieCraft 的原始 issue 的链接（“Originally reported LINK-TO-CHROMIECRAFT-ISSUE”）。GitHub 会自动关联这两个报告。

你还应该检查 CC 报告是否包含服务器版本哈希。（版本哈希是一小串随机数字和字母，例如 `3d4befd`。）如果不包含，AC 跟踪器会发出提示。如果由于某种原因缺失了，当前的 ChromieCraft 版本信息可以在[这里](https://github.com/chromiecraft/azerothcore-wotlk)找到；或者如果你在自己的测试服务器上复现了该问题，你可以使用你自己的哈希。这可以在你正在运行的 AC world server 的 `AC>` 命令提示符下输入 `server info` 来找到。

### 8. 为 AC 和 CC 的 issue 添加标签
现在你可以为你创建的新 AC issue 和你一直在处理的 CC issue 添加相关标签。合理添加标签——‘Generic’（通用）是最后的手段，用于影响广泛等级范围的问题。否则，根据 issue 发生的区域等级，或它影响的 quest 或 NPC 的等级来添加标签。如果你不确定某个区域的等级，可以[在这里](https://wowpedia.fandom.com/wiki/Zones_by_level_(original))找到按等级划分的 Wrath 时代区域列表。

对于 AC issue，如果你正在从 CC 复制某个 issue，你可以添加 ‘Confirmed’（已确认）标签。也可以随意添加其他相关标签，如 ‘Quest’、‘Loot’、‘DB’、‘PVP’，或某个职业相关的标签。

对于 CC issue，你可以给它打上 ‘Confirmed’、‘Linked to AC’（已链接到 AC）标签，以及一个表示等级范围或（如果不适用）Generic 的标签。同样，如果有其他相关标签，如 ‘Class Issue’（职业问题），请随意添加。

如果你拥有相应的权限，还可以将新的 AC issue 添加到相关的项目（project）中，通常是与该 issue 的等级范围匹配的那个。

## 准则
- **运用你的判断力。** 我们的职责是发挥最好的判断力，而不只是当复印机。我们拥有大多数玩家没有的工具和信息，因此我们应该能够比他们更深入地看透问题并据此做出决定。
- **推广问题。** 尝试推广或拓宽问题。如果某一种不寻常的物品、NPC 或法术不能正常工作，请尝试检查同类型其他物品是否也坏了。理想情况下，我们希望捕捉到尽可能广泛范围的错误。
- **保持怀疑。** 用户对这些问题的感受可能非常强烈。你经常会看到诸如“它一直就是这样”或“我从香草时代就玩这个职业，它就应该是这样”的说法。这些没有其他证据支持的断言，应该以适当的怀疑态度对待。有经验的玩家可能比你更了解他们的职业，但这并不意味着他们的话应该在没有其他证据的情况下被当作事实接受。
- **合并相似的问题。** 如果在搜索时发现相关的问题，考虑用一条注释把两者联系起来。（可以简单到“另见 <ticket URL>.”。这会通过告知相似的问题，帮助最终修复该 issue 的人。）
- **尝试确定优先级。** 更严重的 bug 优先于次要的，频繁出现的 bug 优先于罕见的。与直觉相反，较新的 issue 可能需要优先于较旧的，理由是：如果一个 bug 长期存在却一直没有被修复，那么它很可能不太重要。
- 如果你找不到任何来源，至少也要说出来，而不是什么都不说。
- **要有礼貌。** 当有人提交 bug 报告时，他们是在帮我们的忙。他们花时间创建 GitHub 账号并撰写 bug 报告来帮助我们。我们至少应该以专业和礼貌的态度回报他们。

## 来源

> [!IMPORTANT]
> 我们的目标是模拟 3.3.5 的行为。经核实和验证的原始 3.3.5 来源在可用时具有优先权。
> 在没有此类来源或来源相互冲突时，我们会运用自己的判断和专业知识，去分析和验证最准确的来源。

以下是对我们可以用来判断 bug 是否有效的来源的总体（绝非详尽）介绍。它们包括：

- [TBC Wowhead](http://tbc.wowhead.com/) 或 [Current Wowhead](https://www.wowhead.com/) - Wowhead 是一个重要但存在缺陷的数据来源，一方面是因为网站自身的数据，另一方面是因为用户在其上的评论。Wowhead 的评论可能是我们所拥有的关于单个任务和物品的最大单一信息集，这也是为什么其中那么多都是彻头彻尾的废话实在令人遗憾。
    然而，我们很容易陷入 Wowhead 数据正确且完整的假设中，而实际上并非如此。Wowhead 的数据来自用户提交，因此其掉落率等数据自身也存在问题。它的数据还被一些提交私人服务器数据的人污染了。因此，尽管 Wowhead 看似权威，但如果不加甄别地解读，其数据可能是零散、不完整且具有误导性的。
	注意这里列出的两个版本。TBC Wowhead 通常更有用，但当前在线版本的 Wowhead 确实也包含 Wrath 时代的用户评论，而 TBC WH 没有。

- [Wowpedia](https://wowpedia.fandom.com/wiki/Special:Search) - Wowpedia 可以是一个相当不错的来源，因为它有历史功能，可以查看一篇文章在 WotLK 时代的样子。要访问它，请进入相关文章，查看文章标题右侧。在 ‘View Source’ 旁边你会看到三个垂直排列的点。点击它就可以访问该文章的 History（历史）。你通常需要的是 2010 年 10 月 12 日（Cata 的发布日期）之前写的最后一篇文章。

    Wowpedia 经常汇总与某个天赋或技能相关的补丁说明，这通常很有用。它还经常记录任务文本和任务给予者的对话，因此对于这类内容来说是一个方便的来源。请注意，较早的 Wrath 时代内容也可以在其姊妹网站 [WowWiki](https://wowwiki-archive.fandom.com/wiki/Wiki) 上找到。

- Sniffs 数据 - ‘Sniffs’ 是玩家在玩零售版 Wow 时捕获的拦截数据包。它们的优点在于使用真实的零售数据，并将其以 SQL 形式提供，因此可以被广泛使用。缺点是 sniff 数据只包含客户端可见的数据，往往不完整且有缺失，而且通常很难通过其他方式验证。
    关于利用这些数据的一个有用网站，请参阅 Discord 上 @Efymer 制作的 [AzerothCore SpeedChecker](https://azerothcore-speedchecker.web.app/)——如果你想验证生物的移动速度或其他标志与抓取的零售数据是否一致，它可以帮你做到。

- YouTube - 可以是一个极好的信息来源，因为有很多人在 Classic/TBC 中做任务的视频。遗憾的是，来自原始 WotLK 时代的视频很少。YT 的另一个问题是，不只是零售玩家会上传 Wow 视频。其他私人服务器的玩家也会制作视频（要特别留意一个叫 Bue 的人，在 YouTube 上搜索某个任务时，他经常排在搜索结果顶部）。这些私人服务器视频作为正确的暴雪式行为的来源，当然基本毫无用处。

- [TrinityCore](https://github.com/TrinityCore/TrinityCore/issues) - Trinity 比 AC 更古老也更大，他们自己的 bug 跟踪器和 issue 数据库也相应地比我们的大。因此，当 AC 跟踪器没有结果时，它往往是检查某个问题其他报告的好地方。你也经常能在那里找到问题的解决方案。请注意，TC 有多个分支，其中只有一个以 3.3.5a 为目标。

- [Wayback Machine/Internet Archive](https://web.archive.org/) - 如果你真的找不到同时代的来源，需要查看某个网站在 2010 年的状态，那么 Wayback Machine 很不错，前提是你知道你想查看的网站的 URL。例如，他们有猎人宠物网站 Petopia 的 2010 年快照，偶尔会有用。

- 魔兽世界自己的[论坛](https://us.forums.blizzard.com/en/wow/) - 当讨论 vanilla 或 TBC 问题时，Wow 论坛偶尔会有用，但通常充满了互相反驳和互喷的人，因此作为来源并不可靠。

- 同样，[MMO Champion](https://www.mmo-champion.com/forum.php) 的论坛可能有用，因为它们自 Wrath 之前就已存在，且基本没有变化。这意味着你有时可以在那里找到有用的第一手信息。然而，和大多数论坛一样，从随机的糟粕中筛选出有用信息可能很困难。

- [WowGaming](https://wowgaming.altervista.org/aowow/) - 这个网站充当我们自己的 AC 数据库快照的前端。因此，它可以让你快速了解当前版本 AzerothCore 的详细信息。

- [World of Warcraft WotLK Database](https://wotlkdb.com/) - 另一个 Wrath 时代数据的第三方快照，尽管其数据质量偶尔存疑。不是主要来源。

- 分诊 Discord 的 #need-help 频道在这里非常有用。

## 工具
- AC 服务器/测试环境。这是基本的测试工具。尽量让你的 AC 服务器保持尽可能新。每天更新是个好主意，你不应该超过一周不更新。

- [GM 命令](gm-commands)和宏 - 你至少要熟悉各种作弊功能（无伤害、加速、飞行）、`.go`、`.additem`、`.quest add` 等等。在你的测试账号上设置各种作弊和增强宏也很有用，这样你就可以立即创建并训练一个新角色。在测试各种职业和种族问题时，你会发现自己需要创建然后删除大量不同的角色，因此用宏来自动化新角色的创建可以很快收回投入的时间。

- [Keira3](https://www.azerothcore.org/Keira3/) - 这是分诊必不可少的工具。用 Keira 五分钟就能省下在开放世界中跑上一个小时的时间。它内置了一个 SQL 编辑器，可以运行自定义查询。它还在大多数数据字段上提供了内置工具提示，有助于理解你正在查看的内容。你还可以用它生成修复问题的 SQL，尽管它生成的 SQL 只能作为起点。这是因为它通常不符合 PR 在查询去重方面所偏好的 SQL 规范。

- 一个通用的 SQL 编辑器，如 [HeidiSQL](https://www.heidisql.com/)（注意，仅限 Windows），也很有用。Keira 并不能访问 AC 数据库中的每一张表，只访问最常用的那些，因此像 Heidi 这样能让你查看所有内容的工具，对于更生僻的表会很好用。

- [AC Wiki 表](database-world)，尤其是那些涉及 world 数据库的表。它们为你提供了关于数据库结构和字段的重要信息。如果你对某件事应该如何运作或某个标志的含义感到困惑，答案通常在这里。

- [有用的 SQL 片段](useful-sql) - 这些旨在成为从数据库中获取各种潜在问题信息的快速、易用的工具。

- 学会过滤 GitHub issues：
    - `type:issue label:"Needs Triage"` - 查找所有打开的 issues
    - `author:Username` - 查找作者创建的所有 issues
    - `involves:Username` - 查找他们发起或评论过的所有 issues。

## 其他链接
- [当前 ChromieCraft 版本](https://github.com/chromiecraft/azerothcore-wotlk)
- [ChromieCraft mods](https://github.com/chromiecraft/chromiecraft/blob/main/.github/CC_SERVER_INFO.md)
- [如何分诊](https://github.com/chromiecraft/chromiecraft#for-contributors-how-to-triagereport-bugs)
