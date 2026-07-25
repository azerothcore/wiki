# chat\_filter

[<-Volver a:Characters](database-characters)

**Tabla `chat_filter`**

Esta tabla almacena las palabras reservadas que usa el filtro de chat del core. Cuando se encuentra una entrada coincidente, el mensaje se bloquea usando una coincidencia de subcadena insensible a mayúsculas y minúsculas.

El filtro se controla con las opciones `ChatFilter.Whisper`, `ChatFilter.Say`, `ChatFilter.Yell` y `ChatFilter.Emote` de `worldserver.conf`. Gestiona las entradas dentro del juego con `.chatfilter list`, `.chatfilter add`, `.chatfilter remove` y `.reload chat_filter`.

**Estructura**

| Field     | Type         | Attributes | Key | Null | Default | Extra          | Comment |
| --------- | ------------ | ---------- | --- | ---- | ------- | -------------- | ------- |
| [ID](#id) | INT          | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [Word](#word) | VARCHAR(255) | SIGNED     |     | NO   |         |                |         |

**Descripción de los campos**

### ID

Identificador único de la fila.

### Word

Palabra o frase reservada que comprueba el filtro de chat.
