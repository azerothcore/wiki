# 代理式自我评审（Agentic Self Review）

在 AzerothCore，我们追求高质量的代码，正因如此我们有一套流程，要求所有提交 AI 辅助 PR 的贡献者认真运行一次 `/self-review` 会话。

这一步的目标是确保你的 PR 不会引入任何回归或非预期的副作用，从而保持整体代码质量。

**这会耗费你额外的时间和 token。** 比起更多低质量的 AI 凑数 PR，我们更希望有更少但质量更高的 PR。

## 给贡献者：如何运行自我评审流程

### 安装技能

`/self-review` 技能是 [agent-toolkit](https://github.com/eai-org/agent-toolkit) 开源工具集的一部分。

你可以这样快速安装：

```
git clone https://github.com/eai-org/agent-toolkit.git && cd agent-toolkit && ./install.sh
```

并记得定期用以下命令保持更新：

```
cd agent-toolkit && git pull && ./install.sh
```

### 选择一个强大的模型

自我评审必须使用强大的模型，例如 Claude Fable、GPT Sol，或者至少是 Claude Opus 或同级别的领先模型。

**不要使用便宜的模型**，因为它们无法产出高质量的结果。

**不要试图作弊**：维护者随时可以在你的 PR 上运行同样的流程并比较结果。

### 运行它，然后等待

在本地检出你 PR 的分支，打开你的 AI 智能体，然后运行：

```
/self-review
```

这会花费一些时间。请耐心等待。

### 处理发现的问题

检查完你的代码后，智能体会提出发现的问题，并给出哪些应该处理的建议。**由你来决定**。

请仔细检查：不要盲目接受你不确定的改动。如果有任何不清楚的地方，请智能体进一步解释。

评审会持续进行，直到没有需要处理的发现为止。

### 发布结果

自我评审会生成一个 `<slug>.SELF-REVIEW.md` 产物（位于 `.agents/plans/<slug>/` 目录），其内容可以直接**逐字**复制粘贴到你的 PR 评论中。

请勿手动修改该产物的内容，也请勿将该产物文件本身提交到你的 PR 中。

团队保留关闭任何未提供此类产物的 PR 的权利。

就是这样。

## 给维护者：如何引导自我评审流程

`/self-review` 技能的行为由两部分定义：

- [技能源代码](https://github.com/eai-org/agent-toolkit/blob/main/skills/self-review/SKILL.md)及其依赖，存放在 [agent-toolkit 仓库](https://github.com/eai-org/agent-toolkit)中，它定义了该技能在所有项目中的通用行为
- AzerothCore 项目特有的规则，技能始终被指示遵循这些规则，它们存放在 AC 主仓库的 [.agents/docs/self-review-rules.md](https://github.com/azerothcore/azerothcore-wotlk/blob/master/.agents/docs/self-review-rules.md) 文件中

另外请记住，技能被指示检查 AzerothCore 仓库中的任何相关治理文档，例如 [.agents/docs/](https://github.com/azerothcore/azerothcore-wotlk/blob/master/.agents/docs/) 下的其他文档，当然还有 [AGENTS.md](https://github.com/azerothcore/azerothcore-wotlk/blob/master/AGENTS.md) 文件。

要对这些内容进行修改，请始终调用以下技能：

- 修改任何 `*.md` 文件时使用 `/compact-docs-writer`
- 修改技能时使用 `/compact-skill-creator`
