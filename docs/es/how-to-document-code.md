# Cómo documentar su código

Merece la pena consultar el extenso [Manual de Doxygen](https://www.doxygen.nl/manual/docblocks.html). Doxygen proporciona una amplia variedad de opciones para documentar el código y puede ser adaptado para la documentación general también. Esta página le llevará a través de algunas de las características más utilizadas en la documentación de AzerothCore.

Los bloques de comentarios de Doxygen son fáciles de crear. Para el comentario de línea sólo hay que insertar una triple barra diagonal.

```cpp
///Esta línea se incluirá en los comentarios Doxygen para esta función/clase/archivo
```

Comentar varias líneas es igual de fácil.

```cpp
/**
Estas líneas siguientes formarán un bloque de comentarios
Para empezar un nuevo párrafo añada una línea vacía
Para terminar el bloque de comentarios, escriba asterisco y luego barra diagonal.
*/
```

Si te tomas unos minutos mientras escribes tu código para escribir bloques de comentarios, puedes indicar a los futuros desarrolladores lo que pretendías y hacerles la vida más productiva y fácil.

Este es un ejemplo de un [Hook documentado](hooks-script.md) en nuestro `ScriptMgr.h`:

```cpp
/**
 * @brief Este hook se ejecuta antes de enviar el mensaje de salida durante la cola de arena, lo que permite ejecutar operaciones adicionales o desactivar el mensaje de salida
 *
 * @param queue Contiene información sobre la cola de la Arena
 * @param ginfo Contiene información sobre el grupo de la cola
 * @return True si quiere seguir enviando el mensaje, false si quiere desactivar el mensaje
 */
[[nodiscard]] virtual bool OnBeforeSendExitMessageArenaQueue(BattlegroundQueue* /*queue*/, GroupQueueInfo* /*ginfo*/) { return true; }
```

## Etiquetas comunes de Doxygen

### Etiquetas comunes de los documentos fuente

`@brief`

Esta etiqueta proporciona una breve descripción de una función para las páginas doxygen. Este mensaje debe decir lo que sucede en la función. Por convención en AzerothCore todas las funciones deben tener etiquetas breves. Estas se incluyen en el archivo de cabecera junto con la declaración de las funciones.

`@details`

Esta etiqueta proporciona una descripción más detallada. Este mensaje debería dar al usuario una idea de cuándo es válido llamar a esta función (es decir, qué debe ser cierto para que la función funcione), cómo la función lleva a cabo su función, y qué será cierto cuando la función regrese. Por convención en AzerothCore todas las funciones deben tener etiquetas de detalles. Éstas se colocan con la definición de la función.

`@param`

Esta etiqueta puede utilizarse para documentar el propósito y el significado de los parámetros de las funciones. Se puede especificar la naturaleza del parámetro como entrada salida o ambos de la siguiente manera:

- `@param[in]`
- `@param[out]`
- `@param[in/out]`
- `@class`

Esta etiqueta informa a doxygen de que el bloque de comentarios debe estar asociado a la clase. Este bloque debe explicar el propósito de la clase, las consideraciones de diseño y la relación con otras clases. También proporciona cualquier información que otros programadores puedan encontrar útil para usar las clases.

`@example`

Esta etiqueta le permite insertar fragmentos de código que se recogen en la página de ejemplos. De este modo, puede indicar a la gente cómo utilizar su código directamente en el archivo con la definición de su clase.

`@return`

Esta etiqueta permite describir lo que la función devuelve.

### Etiquetas comunes de las páginas de Doxygen

`@page`

Esta etiqueta indica a Doxygen que se trata de una página flotante y permite a doxygen nombrar la página para que otras páginas puedan hacer referencia y enlazar con ella.

`@page describing_awesome_mode_by_james This Page describes James' Awesome Mode`

La primera palabra después de `@page` es la palabra que tendrá que escribirse en un comando `@ref` para enlazar la página. Doxygen reemplazará cualquier referencia a la página con la cadena que aparece después de la palabra. Así que en el caso anterior Doxygen reemplazaría "describiendo_el_modo_alucinante_de_james" por "Esta página describe el modo alucinante de James" en la documentación generada. Generalmente en html como mínimo los enlaces se muestran en azul. Tenga en cuenta que he tenido problemas para incluir las letras mayúsculas en la "palabra" que da nombre a la página. A veces funciona como se ha descrito anteriormente, pero otras veces falla al sustituir la "palabra" por la "cadena" para los enlaces de otras ubicaciones.

`@ref`

Este comando le dice a Doxgyen que inserte un enlace a la página especificada en esta sección. Así que siguiendo con el comando `@page` anterior, si quisiera insertar un enlace a la página que describe el modo impresionante de James, escribiría:

`///// @ref describing_awesome_mode_by_james`

`@image`

Una imagen a veces vale más que mil palabras, o al menos eso dice el refrán. Esta etiqueta permite insertar una imagen en la documentación. Doxygen requiere diferentes formatos de imagen para los diferentes tipos de salida. A continuación muestro cómo insertar imágenes para que aparezcan tanto en html como en pdf generados por latex. Tenga en cuenta que los archivos de imagen deben ser colocados en una ubicación reconocida por Doxygen. Esto se establece mediante la variable IMAGE_PATH en el archivo Doxygen. Actualmente el doc/images está indexado. Así que colocar los archivos de imagen en esa ubicación debería permitir a Doxygen encontrarlos.

`///// @image html special_image.png`

`///// @image latex special_image.eps "Special Image label" width=5cm`

`@section`

`@subsection`

A menudo es útil dividir una página doxygen en secciones y subsecciones. Esto sirve para dos propósitos. Uno es crear cabeceras. En segundo lugar se puede crear una referencia a través de la página para enlazar con la sección. Esta página se compone de secciones y enlaces a secciones. La lista de secciones al principio de la página se implementa usando el comando `@section`. De forma similar al comando `@page`, se puede proporcionar un nombre de enlace y una cadena.

`///// @section common_doxygen_tags_used Common Doxygen Tags`

`///// @subsection common_page_tags Common Doxygen Page Tags`

## Documentación de la construcción

Si doxygen se encuentra en su ruta, simplemente emita el comando

`doxygen`
