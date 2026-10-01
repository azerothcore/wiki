# 维基提示与提示框

## 提示（Alerts）

提示可以按如下方式添加。

{% raw %}
```
{% include note.html content="在引号之间添加内容" %}
{% include tip.html content="在引号之间添加内容" %}
{% include important.html content="在引号之间添加内容" %}
{% include warning.html content="在引号之间添加内容" %}
```
{% endraw %}

{% include note.html content="在引号之间添加内容" %}
{% include tip.html content="在引号之间添加内容" %}
{% include important.html content="在引号之间添加内容" %}
{% include warning.html content="在引号之间添加内容" %}

如果需要多个段落，请输入 `<br/>`。

该 include 使用 `markdown="span"` 作为属性，这意味着 GFM 会将整个内容当作一个 span 来处理。你不能使用 `p`、`div` 或 `pre` 等块级元素。如果你需要这些元素，可以手动用 include 中的 HTML 将内容包裹起来，也可以使用以下标签：

{% raw %}
```
{{site.data.alerts.note}}
<p>内容</p>
<a href="http://azerothcore.org">网页</a>
{{site.data.alerts.end}}
```
{% endraw %}

{{site.data.alerts.note}}
<p>内容</p>
<a href="http://azerothcore.org">网页</a>
{{site.data.alerts.end}}

## 提示框（Callouts）

{% raw %}
```
{% include callout.html content="在引号之间添加内容" type="primary" %}
```
{% endraw %}

{% include callout.html content="在引号之间添加内容" type="primary" %}

type 可以是以下值之一
| Type    |
| ------- |
| danger  |
| default |
| primary |
| success |
| info    |
| warning |

{% include callout.html content="这是一个 <b>danger</b> 提示框。" type="danger" %}
{% include callout.html content="这是一个 <b>default</b> 提示框。" type="default" %}
{% include callout.html content="这是一个 <b>primary</b> 提示框。" type="primary" %}
{% include callout.html content="这是一个 <b>success</b> 提示框。" type="success" %}
{% include callout.html content="这是一个 <b>info</b> 提示框。" type="info" %}
{% include callout.html content="这是一个 <b>warning</b> 提示框。" type="warning" %}
