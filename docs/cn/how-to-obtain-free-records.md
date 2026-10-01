---
redirect_from: "/cn/How-to-obtain-free-records"
---

# 如何获取空闲的记录

在某些情况下，我们需要获取或了解那些值尚未被占用的记录。

无论是因为我们想插入一个新值，还是因为过了一段时间后想重构我们的表。

要做到这一点，你可以使用以下脚本：

```sql
SELECT t.id + 1
FROM Table1 t
WHERE NOT EXISTS (
    SELECT * 
    FROM Table1 t2
    WHERE t2.id = t.id + 1
)
LIMIT 1
```

我们必须替换表的名称，以及我们正在查找的属性。

现在让我们看一个例子。假设我们想在 `creature` 中搜索第一个空闲记录。

首先我们必须确定它的主键：`guid`

```sql
SELECT t.`guid` + 1
FROM `creature` t
WHERE NOT EXISTS (
    SELECT * 
    FROM `creature` t2
    WHERE t2.`guid` = t.`guid` + 1
)
LIMIT 1
```

运行查询后，在这种情况下我们会得到数字 **15** 作为结果。

{% include note.html content="目前这个值已经改变，现在不一样了。但在当时它是数字 15。" %}

我们现在必须做的是通过一个 `SELECT` 来检查这个值是否未被使用：

```sql
SELECT * FROM `creature` WHERE `guid`=15;
```

为了验证信息是否正确，我把前 16 条记录留给你看。

| guid | id    | map | zoneId |
|------|-------|-----|--------|
| 1    | 2843  | 0   | 0      |
| 2    | 7853  | 0   | 0      |
| 3    | 2499  | 0   | 0      |
| 4    | 2838  | 0   | 0      |
| 5    | 2839  | 0   | 0      |
| 6    | 2626  | 0   | 0      |
| 7    | 2482  | 0   | 0      |
| 8    | 8123  | 0   | 0      |
| 9    | 9459  | 0   | 0      |
| 10   | 9520  | 0   | 0      |
| 11   | 1215  | 0   | 0      |
| 12   | 1218  | 0   | 0      |
| 13   | 30140 | 571 | 0      |
| 14   | 30156 | 571 | 0      |
| 16   | 32442 | 571 | 0      |

如你所见，数字 15 是可用的。

{% include note.html content="该表还有很多其他属性，但我们只展示了一部分，以免表格过于冗长。" %}
