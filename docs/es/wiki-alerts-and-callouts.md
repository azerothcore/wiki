# Alertas y callouts de la wiki

## Alertas

Las alertas se pueden añadir de la siguiente manera.

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

Si necesitas varios párrafos, introduce `<br/>`.

El include usa `markdown="span"` como atributo, lo que significa que GFM procesará todo el contenido como un span. No puedes usar elementos de bloque como `p`, `div` o `pre`. Si necesitas estos elementos, puedes rodear manualmente el contenido con el HTML del include, o puedes usar estas etiquetas:

{% raw %}
```
{{site.data.alerts.note}}
<p>Content</p>
<a href="http://azerothcore.org">Webpage</a>
{{site.data.alerts.end}}
```
{% endraw %}

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

El tipo puede ser uno de los siguientes
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
