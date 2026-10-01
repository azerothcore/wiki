---
tableofcontents: 1
---

# 如何为你的代码编写文档

详尽的 [Doxygen 手册](https://www.doxygen.nl/manual/docblocks.html)非常值得一读。Doxygen 为编写代码文档提供了多种多样的选项，也可以适用于一般性文档。本页面将带你了解 AzerothCore 文档中一些常用的功能。

Doxygen 注释块很容易创建。对于单行注释，只需插入三个正斜杠。

```cpp
///This line will be included in the Doxygen comments for this function/class/file
```

多行注释也同样简单。

```cpp
/**
These next few lines will form a comment block
To start a new paragraph add an empty line
To end the comment block type asterik and then forward slash.
*/
```

在你编写代码时花几分钟编写注释块，就能告诉未来的开发者你的意图，让他们的工作更高效、更轻松。

这是我们的 `ScriptMgr.h` 中一个已记录文档的 [Hook](hooks-script) 示例：

```cpp
/**
 * @brief This hook runs before sending the exit message during the arena queue, allowing you to run extra operations or disabling the exit message
 *
 * @param queue Contains information about the Arena queue
 * @param ginfo Contains information about the group of the queue
 * @return True if you want to continue sending the message, false if you want to disable the message
 */
[[nodiscard]] virtual bool OnBeforeSendExitMessageArenaQueue(BattlegroundQueue* /*queue*/, GroupQueueInfo* /*ginfo*/) { return true; }
```

## 常用的 Doxygen 标签

### 常用的源码文档标签

`@brief`

该标签为 doxygen 页面提供函数的一句话简介。这条信息应说明函数内部发生了什么。按照 AzerothCore 的惯例，所有函数都必须有 brief 标签。这些标签包含在头文件中函数声明的旁边。

`@details`

该标签提供更详细的描述。这条信息应让用户了解何时调用该函数是有效的（即函数正常工作必须满足什么条件）、函数如何执行其功能，以及函数返回后哪些条件会成立。按照 AzerothCore 的惯例，所有函数都必须有 details 标签。这些标签放在函数定义的位置。

`@param`

该标签可用于记录函数参数的目的和含义。你可以用以下方式指定参数的性质是输入、输出还是两者皆是。

`@param[in]`

`@param[out]`

`@param[in/out]`

`@class`

该标签告知 doxygen 该注释块应与该类关联。该注释块应解释类的用途、设计考虑以及与其他类的关系。同时提供其他程序员在使用该类时可能有用的任何信息。

`@example`

该标签允许你插入代码片段，这些代码片段随后会被收集到示例页面上。这样你就可以直接在类定义所在的文件中告诉人们如何使用你的代码。

`@return`

该标签允许你描述函数返回的内容。

### 常用的 Doxygen 页面标签

`@page`

该标签告知 Doxygen 这是一个自由浮动的页面，并允许 doxygen 为页面命名，以便其他页面可以引用并链接到该页面。

`@page describing_awesome_mode_by_james This Page describes James' Awesome Mode`

`@page` 后面的第一个词，是需要在 `@ref` 命令中输入的用于链接该页面的词。Doxygen 会用这个词后面的字符串替换对页面的任何引用。因此在上面的例子中，Doxygen 会在生成的文档中用 “This Page describes James' Awesome Mode” 替换 “describing_awesome_mode_by_james”。通常在 html 中链接至少会以蓝色显示。请注意，我在命名页面的“词”中包含大写字母时遇到过麻烦。有时它能如上所述正常工作，但有时它会无法用“字符串”替换“词”来生成来自其他位置的链接。

`@ref`

该命令告知 Doxygen 在本节中插入一个指向指定页面的链接。因此，接续上面的 `@page` 命令，如果我想插入一个链接指向描述 James 的 awesome mode 的页面，我会输入

`///// @ref describing_awesome_mode_by_james`

`@image`

一幅图片有时胜过千言万语，至少这句谚语是这样说的。该标签允许在文档中插入图片。Doxygen 针对不同的输出类型要求不同的图片格式。下面我将展示如何插入图片，使其同时出现在 html 和由 latex 生成的 pdf 中。请注意，图片文件必须放置在 Doxygen 可识别的位置。这由 Doxygen 文件中的 IMAGE_PATH 变量设置。目前 doc/images 已被索引。因此将图片文件放在该位置应该能让 Doxygen 找到它们。

`///// @image html special_image.png`

`///// @image latex special_image.eps "Special Image label" width=5cm`

`@section`

`@subsection`

将 doxygen 页面划分为多个部分和子部分通常很有用。这有两个目的。一是创建标题。二是可以通过页面创建指向该部分的引用链接。本页面就使用了部分和指向部分的链接。页面开头的内容列表就是使用 `@section` 命令实现的。与 `@page` 命令类似，可以提供链接名称和字符串。

`///// @section common_doxygen_tags_used Common Doxygen Tags`

`///// @subsection common_page_tags Common Doxygen Page Tags`

## 构建文档

如果 doxygen 在你的 PATH 中，只需执行命令

`doxygen`
