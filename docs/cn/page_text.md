# page\_text

[<-返回至:World](database-world)

**`page_text` 表**

该表保存信件类物品的文本，或任何当鼠标悬停时光标变为放大镜、右键点击后会打开一个可阅读信件内容的窗口的物品文本。

**表结构**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Text][2]          | LONGTEXT  | SIGNED     |     | NO   |         |       |         |
| [NextPageID][3]    | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild][4] | INT       | SIGNED     |     | YES  | NULL    |       |         |

[1]: #id
[2]: #text
[3]: #nextpageid
[4]: #verifiedbuild

## 字段说明

### ID

唯一标识符

### Text

实际文本。此字段中的消息将作为页面上的文本显示。

### NextPageID

下一页的 ID。[page_text.id](#id)。

### VerifiedBuild
