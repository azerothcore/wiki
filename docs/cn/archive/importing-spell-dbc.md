# 向 spell_dbc 表导入数据

## 简介

[spell_dbc](spell_dbc) 包含关于服务端技能的数据，这些技能在客户端 DBC 文件中找不到，同时它也包含用于改进或修复技能的 DBC **覆盖（override）**。

为了在 `spell_dbc` 表中为某个技能添加覆盖，你首先需要从客户端 DBC 文件中导入该技能的基础数据（除非该技能已经被导入过）。

客户端 DBC 文件中有大约 5 万个技能，你可以将单个技能或全部技能导入到本地 AC 数据库的 `spell_dbc` 表中，以便对它们进行操作并添加你的覆盖。

当你从 DBC 导入技能时，会得到一个包含所有默认值的 `INSERT IGNORE` 查询。请将此查询保存在某个地方，提交 PR 修复时你会需要它。导入技能后，你可以使用 [Keira3](https://www.azerothcore.org/Keira3/) 等工具轻松获得包含你覆盖内容的 `UPDATE` 查询。

当提交针对某个技能的 `spell_dbc` 修复 PR 时，如果该技能之前不存在于 `spell_dbc` 表中，你必须在 PR 中同时包含 `INSERT IGNORE` 和 `UPDATE` 查询。

## 如何将 DBC 文件中的技能导入到 spell_dbc 表

要从 Spell.dbc 向我们的 spell_dbc 表导入数据，你可以参考关于[如何从 DBC 文件导入数据](how-to-import-dbc-data-in-db)的通用指南。你只需遵循同样的指南，改用 Spell.dbc 文件即可。
