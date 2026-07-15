# creature\_text

# Tabla: creature\_text

**Descripción breve:**

Esta tabla contiene todo el texto de habla (susurro, decir, gritar, texto de emote en burbujas de habla y en la ventana de chat) que se usa en la tabla [SMART\_SCRIPTS](http://www.azerothcore.org/wiki/smart_scripts) y en los scripts del core.

**Descripción detallada:**

¿Alguna vez te has preguntado cómo se scriptea un jefe como ***Sindragosa*** (→ [wowhead](http://www.wowhead.com/npc=36853/sindragosa))? No hace falta que te lo preguntes, ¡puedes verlo por ti mismo! (→ [Archivo de script de Sindragosa](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/scripts/Northrend/IcecrownCitadel/boss_sindragosa.cpp))

Lo sé, lo sé; esto parece increíblemente complejo, ¡más de 1600 líneas de código! Sin embargo, no hace falta entenderlo todo de una vez. Centrémonos en algo simple, pero aun así muy importante, ¿de acuerdo?

Si miras el principio del código, encontrarás un *enum* llamado Texts que está compuesto de 12 elementos (números del 0 al 11); miremos más de cerca el primer elemento de este *enum*:

**boss\_sindragosa.cpp**  Expand source

```cpp
 enum Texts
 {
     SAY_AGGRO = 0, // You are fools to have come to this place! The icy winds of Northrend will consume your souls!
     ...
 };
```

Puedes verificar en el juego por ti mismo que ***Sindragosa*** gritará esto cuando empieces un combate contra ella.
¿Notaste algo interesante? El texto real está colocado después de un // lo que significa que esta información es un comentario
y nuestro compilador lo ignorará. Por otro lado, vemos claramente que ella está gritando ese texto, ¿cómo es posible?

## ¿Dónde se almacena esta información? ¿Cómo puedo encontrarla?

Podrías decir: bueno, esto tiene más de 1600 líneas de largo, seguro que hay algo, simplemente aún no lo hemos encontrado.
Te aseguro que no encontrarás nada; si no me crees, usa el atajo CTRL+F y diviértete buscando.

¿No hay nada? Es una lástima, pero quizá, quizá tuviste la oportunidad de descubrir algo.

**boss\_sindragosa.cpp**  Expand source

```cpp
 void EnterCombat(Unit* victim) override
 {
     ...
     Talk(SAY_AGGRO); // interesting!
 }
```

¿Ves la última línea de esta función? ¡Están usando algo que no debería funcionar!
Podemos concluir que esta función se llamará cuando ***Sindragosa*** entre en combate (¡mira el nombre de la función!), así que
ahora vemos por qué grita al inicio.

Todavía hay una pregunta fundamental: ¿dónde se almacena la información sobre este texto? La respuesta es
más simple de lo que podrías pensar. ¡Se almacena en la tabla **CREATURE\_TEXT**!

*continuará...*

## Estructura

| Field                 | Type         | Attributes      | Key | Null | Default | Extra | Comment                 |
|-----------------------|--------------|-----------------|-----|------|---------|-------|-------------------------|
| [CreatureID][1]       | MEDIUMINT | UNSIGNED        | PRI | NO   |         |       | creature_template entry |
| [GroupID][2]          | TINYINT   | UNSIGNED        | PRI | NO   |         |       |                         |
| [ID][3]               | TINYINT   | UNSIGNED        | PRI | NO   |         |       |                         |
| [Text][4]             | longtext     | utf8_general_ci |     | YES  | NULL    |       |                         |
| [Type][5]             | TINYINT   | UNSIGNED        |     | NO   |         |       |                         |
| [Language][6]         | TINYINT   | UNSIGNED        |     | NO   |         |       |                         |
| [Probability][7]      | FLOAT        | SIGNED          |     | NO   |         |       |                         |
| [Emote][8]            | MEDIUMINT | UNSIGNED        |     | NO   |         |       |                         |
| [Duration][9]         | MEDIUMINT | UNSIGNED        |     | NO   |         |       |                         |
| [Sound][10]           | MEDIUMINT | UNSIGNED        |     | NO   |         |       |                         |
| [BroadcastTextId][11] | MEDIUMINT | SIGNED          |     | NO   |         |       |                         |
| [TextRange][12]       | TINYINT   | UNSIGNED        |     | NO   |         |       |                         |
| [comment][13]         | VARCHAR(255) | utf8_general_ci |     | YES  | NULL    |       |                         |

[1]: #creatureid
[2]: #groupid
[3]: #id
[4]: #text
[5]: #type
[6]: #language
[7]: #probability
[8]: #emote
[9]: #duration
[10]: #sound
[11]: #broadcasttextid
[12]: #textrange
[13]: #comment

## Descripción de los campos

### CreatureID

Este es el [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry) al que está vinculado el script.

### GroupID

Si hay más de uno del mismo entry (más de un texto que la criatura dice), esta columna se usa para elegir si es un decir aleatorio o una lista ordenada. Si una criatura tiene más de un texto de decir que se muestra en un orden dado, debe incrementarse por cada nueva entrada coincidente (ej. 0, 1, 2, 3...). Si solo hay una entrada o un solo grupo, este valor debe ser 0. Si hay varios grupos de textos, este valor permanece igual dentro del grupo mientras el id se incrementa dentro del mismo grupo.

Ejemplo del Guardia de la Ciudad de Ventormenta, criatura 68:

| CreatureID | GroupID | ID  | Text                                                                                                                       |
|------------|---------|-----|----------------------------------------------------------------------------------------------------------------------------|
| 68         | 0       | 0   | Taste blade, mongrel!                                                                                                      |
| 68         | 0       | 1   | Please tell me that you didn't just do what I think you just did. Please tell me that I'm not going to have to hurt you... |
| 68         | 0       | 2   | As if we don't have enough problems, you go and create more!                                                               |
| 68         | 2       | 0   | %s throws a rotten apple at $n.                                                                                            |
| 68         | 3       | 0   | %s throws rotten banana on $n.                                                                                             |
| 68         | 4       | 0   | %s spits on $n.                                                                                                            |
| 68         | 5       | 0   | Monster!                                                                                                                   |
| 68         | 5       | 1   | Murderer!                                                                                                                  |
| 68         | 5       | 2   | GET A ROPE!                                                                                                                |
| 68         | 5       | 3   | How dare you set foot in our city!                                                                                         |
| 68         | 5       | 4   | You disgust me.                                                                                                            |
| 68         | 5       | 5   | Looks like we're going to have ourselves an execution.                                                                     |
| 68         | 5       | 6   | Traitorous dog.                                                                                                            |
| 68         | 5       | 7   | My family was wiped out by the Scourge! MONSTER!                                                                           |

### ID

Entrada para cada grupo de textos. Este es el identificador único cuando el entry (criatura) es el mismo y el groupid no cambia; debe incrementarse (ej. 0, 1, 2, 3...). Un decir de la criatura se seleccionará aleatoriamente de esta lista según el groupid al que pertenece.

### Text

El texto que dirá la criatura.

### Type

| Value | Old value | Localization | Picture Example                               |
|-------|-----------|--------------|-----------------------------------------------|
| 12    | 0         | Say          | ![Say](assets/images/Say.png)                 |
| 14    | 1         | Yell         | ![Yell](assets/images/Yell.png)               |
| 16    | 2         | Emote        | ![Emote](assets/images/Emote.png)             |
| 41    | 3         | Boss Emote   | ![BossEmote](assets/images/BossEmote.png)     |
| 15    | 4         | Whisper      | ![Whisper](assets/images/Whisper.png)         |
| 42    | 5         | Boss Whisper | ![BossWhisper](assets/images/BossWhisper.png) |

### Language

Valor de [Languages.dbc](languages) (+ la tabla wiki del archivo dbc). Cuando se pone a 0, se usará el idioma por defecto actual.

### Probability

Un valor de 1-100 que representa el porcentaje de probabilidad de que este texto se ejecute.

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `creature_text_chk_1`.

### Emote

El emote que la criatura reproduce cuando se ejecuta el texto. El valor a usar en este campo se puede obtener de [emote.dbc](emotes)

### Duration

Tiempo en ms para ver el texto.
0 es el valor por defecto y lo calcula el core.

### Sound

La entrada de sonido que esta criatura reproducirá al mismo tiempo que se ejecuta el texto. Los sonidos se encuentran en SoundEntries.dbc.

### BroadcastTextId

Id del texto equivalente que se encuentra en [broadcast\_text](broadcast_text)

### TextRange

| Value | Range          |
|-------|----------------|
| 0     | Normal/Default |
| 1     | Area           |
| 2     | Zone           |
| 3     | Map            |
| 4     | World          |

### comment

Este campo te permite etiquetar una entrada de texto.
