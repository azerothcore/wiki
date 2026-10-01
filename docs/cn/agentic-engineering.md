# AzerothCore 的代理式工程（Agentic Engineering）

{% include important.html content="尽情使用 AI。但请保持控制：审查、理解、测试并为你提交的每一行代码负责。明显未经审查的 AI 生成 PR 可能会被直接关闭，而不会给出详细评审。" %}

## AzerothCore 与 AI

我们正经历着自互联网普及以来软件开发方式最大的变革之一。
AI 正在迅速改变开发者的工作方式，而且这种改变会一直持续下去。

在 AzerothCore，我们更愿意引导这场变革，而不是假装它没有发生。我们把 AI 视为一种工具，它能帮助我们更快地前进，*同时*构建出更好的软件。
一旦速度开始以牺牲质量为代价，我们就做错了。

你不需要信任 AI，你需要掌控它。本页展示的就是我们在这里如何做到这一点。

## 基本原则

我们欢迎 AI 辅助的贡献，它们与任何其他贡献遵循同样的标准。在提交 PR 之前：

1. **为自己的代码负责。** 提交之前，审查并理解每一行代码。评审过程中，回答问题的是你，而不是你的智能体。如果你无法解释某项改动，说明它还没准备好。
2. **真实地进行测试。** 编译它、运行它、在游戏中验证它。"能编译"不等于测试过。
3. **保持透明。** PR 模板会询问是否使用了 AI，请如实回答。
4. **听起来像个真人。** Issue、PR 描述和评审回复应该读起来像你自己写的。没有人喜欢面对一堵由生成文本堆成的墙。
5. **尊重评审者的时间。** 低质量的 AI 生成 PR 带来的工作量比它们节省的还多。明显未经审查的 AI 生成 PR 可能会被直接关闭，而不会给出详细评审。
6. **运行一次 [/self-review 会话](agentic-self-review)**，并把生成的报告包含在你的 PR 中。AC 团队可以拒绝任何未包含此类报告的 PR。

为什么如此明确？在过去，我们收到了一波由作者从未认真工程化、甚至从未理解的 AI 生成 PR。
我们感谢每一份贡献，但这会造成混乱，并给评审人员带来沉重负担。本页其余部分展示了一种更好的方式。

## 刚接触 AI？刚接触 C++？很好。

你并不孤单。从早期的 MaNGOS 时代到如今，开源模拟项目一直是学习型项目。
一个人们通过摆弄自己最喜欢的游戏来写下第一行代码的地方。
AI 并没有改变这一点。如果说有什么不同，那就是它进一步降低了入门门槛。

诀窍在于把智能体当作结对编程的伙伴，而不是一台自动售货机。让它解释自己在做什么以及为什么这么做。质疑它的选择。
**当有不清楚的地方时，请它用更简单的话重新解释。**
这样使用 AI，它会是你遇到过的最好的编程导师之一，而且每完成一个任务，你都会比之前更熟练一些。

## 结构化的代理式工程，而不是"氛围编码"（Vibe Coding）

把一个一句话的提示扔给智能体，然后把它输出的任何东西直接推上去，这就是你会陷入上述第 5 条规则的方式。
真正有效的是一个结构化的流程：由*你*来做决策，智能体负责具体执行。

我们推荐的工作流被称为 [**RPAC（Refine-Plan-Act-Consolidate，细化-计划-执行-整合）**](https://medium.com/engineering-in-the-age-of-ai/the-refine-plan-act-pattern-for-agentic-ai-coding-59ee013e4427)：把工作拆分成多个阶段，每个阶段产出一份小文档，你在继续之前先阅读、修正并批准它。
每个阶段都在一个全新的、专注的会话中运行，这会带来更好的输出，同时消耗更少的 token（下面会详细说明）。

## 选择你的智能体

本页的所有内容都与具体的智能体无关。

我们的大多数开发者使用 CLI 工具，例如 **Claude Code**，但也有一些更便宜的替代方案，使用开源模型，例如 [**Kimi Code**](https://www.kimi.com/code)、[OpenCode](https://opencode.ai/) 等。

## agent-toolkit

[agent-toolkit](https://github.com/eai-org/agent-toolkit/) 是一个小型开源技能与规则集合，实现了这套工作流。
它由 AC 的创始人与外部维护者共同维护，并且位于 AC GitHub 组织之外，因为其他项目也会使用它。
它已经过 Claude Code 的实战考验，并且设计为可与任何智能体配合使用；如果某些东西在你的智能体上无法正常工作，请[提交 bug 报告](https://github.com/eai-org/agent-toolkit/issues)。

用一条命令安装它：

```bash
git clone https://github.com/eai-org/agent-toolkit.git && cd agent-toolkit && ./install.sh
```

保持它最新：

```bash
cd agent-toolkit && git pull && ./install.sh
```

其他安装方式（Claude Code 插件市场、[skills.sh](https://www.skills.sh/)、[agentwheel](https://www.nestdev.it/agentwheel/)）列在 [README](https://github.com/eai-org/agent-toolkit/#how-to-install) 中。

## 演练：从 ticket 到 PR

假设你想处理一个跟踪于 `https://github.com/azerothcore/azerothcore-wotlk/issues/XXXXX` 的 bug 或功能（把 `XXXXX` 替换为实际的 ticket 编号）。

**1. 获取 ticket。** 打开一个新会话并输入：

```
/fetch-ticket https://github.com/azerothcore/azerothcore-wotlk/issues/XXXXX
```

这会下载 ticket 及其附带的任何有用信息（评论、相关 ticket）到一个规划目录：

```
.claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.TICKET.md
```

如果你使用不同的智能体，不用担心目录名：它只是一个文件夹。
如果你的任务没有 GitHub ticket，可以在相同位置手动创建一个类似的 `md` 文件。

**2. 细化：确定*做什么*。** 运行 `/clear`，然后：

```
/refine-ticket .claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.TICKET.md
```

这会启动一个交互式会话：智能体会检查代码并向你提问，以确定 ticket 的目标，然后在旁边写出一份 `REQUIREMENTS.md`。

**3. 计划：确定*怎么做*。** 运行 `/clear`，然后：

```
/create-implementation-plan .claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.REQUIREMENTS.md
```

又是一个交互式会话，这次是关于实现细节的，最终产出一份 `PLAN.md`。

可选地，`/create-manual-test-instructions` 可以从 ticket 或需求中推导出逐步测试说明，方便你自己进行游戏内测试，也方便评审者使用。

**4. 执行：执行计划。** 运行 `/clear`，然后：

```
Execute the plan `.claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.PLAN.md`
```

如果你想要额外的评审轮次，可以把它串联起来：

```
Execute the plan `.claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.PLAN.md` then run /fresh-eyes-review and address the feedback where it makes sense
```

（也可以在后面的提示中运行评审。）

**5. 用 /self-review 让 AI 审查你的代码**：

选择一个**强大的模型**（例如 Fable、Opus 或类似的）。这一步**不要**使用便宜的模型。

```
/self-review
```

这会启动一个交互式评审流程，它会给出建议，并让你选择要应用哪些。

**仔细**阅读这些问题，并选择你认为必要的改动。

流程结束时，它会生成一份 `<slug>.SELF-REVIEW.md` 文档，你必须逐字复制粘贴到你 PR 的评论中，以便维护者审阅。

**这一步是强制性的，请勿跳过。**

**6. 打开 PR。** 当你准备好时，智能体可以帮你填写 AC 的 PR 模板：

```
/generate-pr-description
```

然后做智能体做不了的部分：在游戏中测试你的改动，从头到尾通读最终的 diff，然后打开 PR。

别忘了把上一步生成的 `<slug>.SELF-REVIEW.md` 文件内容复制粘贴进去。

**7. 处理评审。** 当评论到来时，`/fetch-pr-review` 会把它们收集到一份文档中，`/refine-pr-review` 会带你逐条处理（采纳、部分采纳或提出异议），并给出草拟的回复。

## 值得养成的习惯

### 保持上下文精炼

你可能注意到我们一直在运行 `/clear`。一个全新、专注的上下文会让智能体明显更好*而且*更便宜：更少的杂乱意味着更高质量的输出和更少的 token 浪费。

如果你使用 Claude Code，我们建议启用上下文使用量指示器，这样你随时都知道窗口有多满：

![Claude Code context usage indicator](https://miro.medium.com/v2/resize:fit:640/format:webp/1*NlQRpqFBz7FTlY01QG-B8Q.png)

它的配置在[这里](https://gist.github.com/FrancescoBorzi/ac9d6afd5dbb2ef3dd0499cd7caba5dc)可用。

### 把 token 花在关键处

如果你的订阅额度有限，可以根据阶段切换模型（在 Claude Code 中：`/model model-name`）：

- **获取（Fetch）：** 便宜的模型（例如 Haiku 或 Sonnet）就足够了
- **细化与计划（Refine and plan）：** 使用智能模型（例如 Fable 或 Opus）；质量在这里决定
- **执行（Execute）：** 当计划足够好时，较便宜的模型（例如 Sonnet）通常就能胜任

### 不要时刻盯着你的智能体

智能体会话可能会运行一段时间，每分钟都切出去看一眼会毁掉你的专注力。[ai-notify](https://github.com/Helias/ai-notify) 是一个由 [Helias](https://github.com/Helias) 编写的小型跨平台脚本，当你的智能体完成工作或需要你的输入时它会通知你，但前提是你当前没有在盯着那个终端。
它支持 Claude Code、Codex、OpenCode 等。

额外加分：你可以把它配置成用**魔兽争霸 3** 苦工那句"Work, work"作为通知音效，在这里简直再合适不过了。

## 更进一步

### 协助 PR 评审

评审其他人的 PR 是为项目做贡献并同时学习的最佳方式之一。这个技能可以协助你：

```
/review-code-assistant https://github.com/azerothcore/azerothcore-wotlk/pull/XXXXX
```

它会扫描改动并建议一列评审意见。**不要盲目复制粘贴**：逐条阅读，确保你理解每条意见背后的理由，遇到不明白的地方就请智能体用更简单的话解释。
只发布那些你真心认为能帮助作者改进代码的意见。

这也是加深你自己编程技能的绝佳方式，你甚至可以在打开 PR 之前对自己分支运行它。

### 保持本地环境健康

- **[context-checkup](https://github.com/eai-org/agent-toolkit/blob/main/skills/context-checkup/SKILL.md)**：审计有哪些内容会自动加载进会话上下文，找出可以精简以降低启动 token 消耗的部分。
- **[memory-doctor](https://github.com/eai-org/agent-toolkit/blob/main/skills/memory-doctor/SKILL.md)**：清理智能体不断积累的记忆，把相关内容移动到正确的位置。关于 memory-doctor 的更多细节见[这里](https://medium.com/engineering-in-the-age-of-ai/keep-your-ai-agents-memory-clean-and-organized-with-memory-doctor-a79f7174f257)。

### 编写新的文档和技能，让你的智能体从错误中学习

- **[compact-docs-writer](https://github.com/eai-org/agent-toolkit/blob/main/skills/compact-docs-writer/SKILL.md)**：以最大 token 效率编写文档。
- **[compact-skill-creator](https://github.com/eai-org/agent-toolkit/blob/main/skills/compact-skill-creator/SKILL.md)**：创建或编辑技能，保持精简高效。
- **[self-improve](https://github.com/eai-org/agent-toolkit/blob/main/skills/self-improve/SKILL.md)**：每当你的智能体犯错时，先纠正它，然后在同一个会话中运行此技能。教训会被永久存储在正确的技能或文档中，这样错误就不会重演。

### AzerothCore MCP

[azerothMCP](https://github.com/blinkysc/azerothMCP) 由 [Blinky](https://github.com/blinkysc) 创建，它让你的智能体可以只读访问 AzerothCore 的数据库和 wiki 文档。这意味着它可以直接查阅生物脚本、SmartAI 逻辑、数据库模式和游戏机制，而不是靠猜。

## 延伸阅读

本页介绍的工作流和习惯在以下文章中有更深入的阐述：

- [Keep your AI agent's context window sharp](https://medium.com/engineering-in-the-age-of-ai/keep-your-ai-agents-context-window-sharp-7255d83a8949)：为什么 `/clear` 和精简的上下文如此重要
- [An approach to agentic skills](https://medium.com/engineering-in-the-age-of-ai/my-approach-to-agentic-skills-e08dc6c0d1cd)：self-improve 以及持续教导你的智能体背后的理念
- [Context-aware notifications for multi-tasking developers](https://medium.com/engineering-in-the-age-of-ai/ai-notify-context-aware-notifications-for-multi-tasking-developers-3614635398ec)：ai-notify 背后的故事
- [Keep your AI agent’s memory clean and organized with memory-doctor](https://medium.com/engineering-in-the-age-of-ai/keep-your-ai-agents-memory-clean-and-organized-with-memory-doctor-a79f7174f257)
- 代理式的 **Refine-Plan-Act-Consolidate**（RPAC）模式：[理论](https://medium.com/engineering-in-the-age-of-ai/the-refine-plan-act-pattern-for-agentic-ai-coding-59ee013e4427) 与[实践](https://medium.com/engineering-in-the-age-of-ai/how-i-use-ai-agents-to-solve-programming-tasks-daily-2a68a5828b8e)两方面的讲解
- [Use AI to assist you with both sides of code reviews](https://medium.com/engineering-in-the-age-of-ai/let-ai-speed-up-both-sides-of-your-code-reviews-while-you-stay-in-full-control-3b059506ef39)

## 总结

AI 并不会取代对代码库的理解；它只会回报那些理解代码库的人。配合上面的工作流使用，它会让贡献 AzerothCore 变得更快、更有趣，而且老实说，它是作为开发者升级的最好的方式之一。

有问题、想法或反馈？来 Discord 找我们聊聊。本页会持续演进，任何改进建议都始终欢迎。

## 给不说英语的人

使用[这条规则](https://github.com/eai-org/agent-toolkit/blob/main/docs/use-my-mothertongue-rule.md)让智能体用你自己的语言与你交流，同时仍然用英语生成产物。

你只需把那个链接给你的 AI 智能体，说出你的母语，然后请智能体安装它即可。
