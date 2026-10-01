# 如何处理 Conf 文件

## 配置文件是如何组成的

所有配置文件都在 2 个宏组下加载它们的属性（你的配置文件头部必须包含其中一个）：

[authserver] -> 用于 authserver 配置

[worldserver] -> 用于 worldserver 配置

一个属性由名称和值组成，它们将在服务器启动/配置重载时被加载到一个对象中。

## 配置文件是如何加载的？

所有配置属性都可以在 .conf.dist 文件中找到，但是这个文件永远不会被读取。

在服务器启动时，我们首先读取 .conf 文件，并将所有属性加载到 sConfig 对象下。任何 .conf 文件中不存在的值，将使用核心中的默认值。

这允许你创建一个更小的 .conf 文件，**不需要**你拥有 .conf.dist 文件中的全部配置属性。因为默认值将从核心中定义的值中获取。

例如，如果你想保留所有默认配置，但只需要更改数据库属性，你可以创建一个只包含以下内容的 worldserver.conf 文件：

```
[worldserver]
LoginDatabaseInfo     = "127.0.0.1;3306;root;root;azerothcore_test_auth"
WorldDatabaseInfo     = "127.0.0.1;3306;root;root;azerothcore_test_world"
CharacterDatabaseInfo = "127.0.0.1;3306;root;root;azerothcore_test_chars"
```

## 从环境变量加载配置值

可以从环境变量加载配置值，这在[这里](config-overrides-with-env-var)有说明。

## 模块配置

在普通的 `.conf` 和 `.conf.dist` 文件被加载之后，你可以使用脚本/模块 API 加载无限数量的配置文件。它们的行为与上面描述的相同。

{% include note.html content="我们不建议你覆盖服务器的配置属性，因为你可能会与其他也使用这些属性的模块产生并发问题。相反，请<b>创建新的带命名空间的属性</b>。" %}

例如，如果你想在你的模块中修改"禁用水中呼吸"（disable water breath）功能。与其使用 `worldserver.conf.dist` 中现有的属性：

```
DisableWaterBreath = x
```

不如使用一个命名空间，例如：

`MyModuleName.DisableWaterBreath = x`

然后使用它。

## 我可以在配置文件中使用相对路径吗？

可以，但不推荐。每个路径都是相对于你启动 authserver/worldserver 的目录的，无论你是手动启动还是通过脚本启动。所以如果你这样做（Linux 示例）：

```bash
cd /tmp/test
./path/to/worldserver
```

并且你在 worldserver.conf 中有类似 `LogsDir = "../logs/worldserver/"` 的相对路径，
它将在 `/logs/worldserver` 下创建日志。

## 结论

配置文件将按照以下流程加载：

```
1. Env vars（环境变量）
2. authserver.conf
3. worldserver.conf
4. modules *.conf
5. Core default values（核心默认值）
```
