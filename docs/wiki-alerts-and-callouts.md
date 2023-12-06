# Wiki Alerts and Callouts

## Alerts

Alerts can be added as following.

{% raw %}
```
{% include note.html content="Add content between quotes" %}
{% include tip.html content="Add content between quotes" %}
{% include important.html content="Add content between quotes" %}
{% include warning.html content="Add content between quotes" %}
```
{% endraw %}

{% include note.html content="Add content between quotes" %}
{% include tip.html content="Add content between quotes" %}
{% include important.html content="Add content between quotes" %}
{% include warning.html content="Add content between quotes" %}

If you need multiple paragraphs, enter `<br/>`.

The include uses `markdown="span"` as an attribute, which means GFM will process the entire content as a span. You can’t use block elements such as `p` or `div` or `pre`. If you need these elements, you can either manually surround the content with the HTML from the include, or you can use these tags:

```
{{site.data.alerts.note}}
<p>Content</p>
<a href="http://azerothcore.org">Webpage</a>
{{site.data.alerts.end}}
```

{{site.data.alerts.note}}
<p>Content</p>
<a href="http://azerothcore.org">Webpage</a>
{{site.data.alerts.end}}

## Callouts

{% raw %}
```
{% include callout.html content="Add content between quotes" type="primary" %}
```
{% endraw %}

{% include callout.html content="Add content between quotes" type="primary" %}

The type can be one of the following
| Type    |
| ------- |
| danger  |
| default |
| primary |
| success |
| info    |
| warning |

{% include callout.html content="This is a <b>danger</b> callout." type="danger" %}
{% include callout.html content="This is a <b>default</b> callout." type="default" %}
{% include callout.html content="This is a <b>primary</b> callout." type="primary" %}
{% include callout.html content="This is a <b>success</b> callout." type="success" %}
{% include callout.html content="This is a <b>info</b> callout." type="info" %}
{% include callout.html content="This is a <b>warning</b> callout." type="warning" %}
