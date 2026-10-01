# quest_template_addon

[<-Volver a: World](database-world)

**Tabla: quest_template_addon**

Contiene definiciones adicionales como enlazado de misiones, dependencias y requisitos para que las misiones definidas en la tabla [quest_template](quest_template) estén disponibles para el jugador.

**Estructura:**

| Field                                           | Type      | Attributes | Key | Null | Default | Extra | Comment                               |
| ----------------------------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------- |
| [ID](#id)                                       | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       | Unique ID linked to quest_template.ID |
| [MaxLevel](#maxlevel)                           | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |
| [AllowableClasses](#allowableclasses)           | INT       | UNSIGNED   |     | NO   |         |       |                                       |
| [SourceSpellID](#sourcespellid)                 | MEDIUMINT | UNSIGNED   |     | NO   |         |       |                                       |
| [PrevQuestID](#prevquestid)                     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [NextQuestID](#nextquestid)                     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [ExclusiveGroup](#exclusivegroup)               | MEDIUMINT |            |     | NO   |         |       |                                       |
| [BreadcrumbForQuestId](#breadcrumbforquestid)   | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |                                       |
| [RewardMailTemplateID](#rewardmailtemplateid)   | MEDIUMINT | UNSIGNED   |     | NO   |         |       |                                       |
| [RewardMailDelay](#rewardmaildelay)             | INT       | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredSkillID](#requiredskillid)             | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredSkillPoints](#requiredskillpoints)     | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMinRepFaction](#requiredminrepfaction) | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMaxRepFaction](#requiredmaxrepfaction) | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMinRepValue](#requiredminrepvalue)     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [RequiredMaxRepValue](#requiredmaxrepvalue)     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [ProvidedItemCount](#provideditemcount)         | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |
| [SpecialFlags](#specialflags)                   | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |

**Descripción de los campos:**

### ID

ID único de misión, que coincide con el mismo ID de misión en [quest_template.ID](quest_template#id)

### MaxLevel

Nivel máximo de jugador al que un personaje puede obtener la misión.

### AllowableClasses

Clases requeridas para obtener la misión. 0 significa que la misión está disponible para todas las clases.
Este campo es un bitmask, puedes combinar valores de clase. Ver [ChrClasses.dbc](chrclasses)

### SourceSpellID

El ID del hechizo lanzado sobre el jugador al iniciar la misión.

### PrevQuestID

- **si el valor > 0:** contiene el id de la misión anterior, que debe completarse antes de poder iniciar esta misión.
- **si el valor < 0:** contiene el id de la misión padre, que debe estar activa antes de poder iniciar esta misión.

### NextQuestID

Contiene el id de la siguiente misión, en caso de que el PrevQuestId de esa otra misión no sea suficiente.

### ExclusiveGroup

- **si ExclusiveGroup > 0**

Permite definir un grupo de misiones de las cuales solo una puede elegirse y completarse. P. ej., si de las misiones 1200, 1201 y 1202 solo debe permitirse elegir una, inserta 1200 en el ExclusiveGroup de las 3 misiones.

- **si ExclusiveGroup < 0**

Permite definir un grupo de misiones de las cuales todas deben completarse y recompensarse para iniciar la siguiente misión. P. ej., si la misión 1000 depende de una de las misiones 1200, 1201 y 1202 y todas estas misiones tienen el mismo grupo exclusivo negativo, entonces todas estas misiones deben completarse y recompensarse antes de poder iniciar la misión 1000.

Nota: Todas las misiones que usan un ExclusiveGroup también deben tener entradas en [pool_template](pool_template) y [pool_quest](quest_template#examples-dealing-with-quests) como ejemplos.

### BreadcrumbForQuestId

Si se establece, indica que esta misión es una migaja (breadcrumb) que conduce a la misión con el ID especificado. Las dos misiones pasan a ser mutuamente excluyentes:

- Esta misión (la migaja) deja de estar disponible si la misión objetivo se toma, se completa o se recompensa.
- La misión objetivo deja de estar disponible si esta misión está en progreso o completada (pero no si se recompensa — completar la migaja desbloquea la misión objetivo).

Este único campo reemplaza la necesidad de múltiples entradas de condición. `0` significa que no hay relación de migaja.

### RewardMailTemplateID

Si la misión da como recompensa un objeto de una posible lista de objetos, el ID aquí corresponde a la plantilla de botín adecuada en [quest_mail_loot_template](loot_template). Según las reglas de esa plantilla de botín, los objetos "saqueados" se enviarán por correo al completar la misión.

### RewardMailDelay

Cuántos segundos esperar hasta que se envíe el correo al personaje que entregó una misión que recompensa objetos de una plantilla de botín.

### RequiredSkillID

Habilidad que se requiere conocer para aceptar la misión. Ver [SkillLine.dbc](skillline)
0 significa que no se requiere ninguna habilidad.

### RequiredSkillPoints

Puntos de habilidad requeridos para poder aceptar la misión.

### RequiredMinRepFaction

ID de facción para el requisito de reputación. Ver [Faction.dbc](faction).

### RequiredMaxRepFaction

El ID de facción de la facción que controla el valor máximo de reputación que el jugador puede tener y aun así obtener la misión. Ver [Faction.dbc](faction).

### RequiredMinRepValue

Los jugadores deben tener esta reputación o superior para poder recibir la misión.

### RequiredMaxRepValue

El valor máximo de reputación que el jugador puede tener con una facción y aun así obtener la misión. Si el jugador tiene más reputación que el valor de este campo, la misión ya no podrá tomarse.

### ProvidedItemCount

Número de objetos entregados al jugador (insertados en las bolsas del jugador) al aceptar la misión.

### SpecialFlags

Este campo es un bitmask y sirve para controlar funciones de misión del lado del servidor. Blizzard mantiene estos datos del lado del servidor y no se envían al cliente, así que tenemos que rellenar el campo manualmente.

| Flag                                      | Value | Description                                                                                                                                                                                                                              |
| ----------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| QUEST_SPECIAL_FLAGS_NONE                  | 0     | Sin requisitos adicionales.                                                                                                                                                                                                             |
| QUEST_SPECIAL_FLAGS_REPEATABLE            | 1     | Hace la misión repetible.                                                                                                                                                                                                               |
| QUEST_SPECIAL_FLAGS_EXPLORATION_OR_EVENT  | 2     | Hace que la misión solo pueda completarse mediante algún evento externo (una entrada en [areatrigger_involvedrelation](areatrigger_involvedrelation), un efecto de hechizo de completar misión o una entrada en [spell_scripts](scripts) con el comando 7, como algunos ejemplos). |
| QUEST_SPECIAL_FLAGS_AUTO_ACCEPT           | 4     | Hace la misión de aceptación automática. A partir del parche 3.3.5a solo las misiones de la zona inicial necesitan este flag.                                                                                                          |
| QUEST_SPECIAL_FLAGS_DF_QUEST              | 8     | Solo se usa para misiones del Buscador de mazmorras (Dungeon Finder).                                                                                                                                                                  |
| QUEST_SPECIAL_FLAGS_MONTHLY               | 16    | Hace la misión mensual.                                                                                                                                                                                                                 |
| QUEST_SPECIAL_FLAGS_CAST                  | 32    | La misión requiere el killcredit de RequiredOrNpcGo (un lanzamiento de hechizo), pero NO la muerte real de un NPC. Esta acción normalmente implica matar a un NPC "bunny" invisible.                                                     |
| QUEST_SPECIAL_FLAGS_NO_REP_SPILLOVER      | 64    | Hace que la misión no comparta la reputación recompensada con otras facciones aliadas.                                                                                                                                                  |
| QUEST_SPECIAL_FLAGS_CAN_FAIL_IN_ANY_STATE | 128   | Permite que la misión falle en Player::FailQuest() independientemente de su estado actual, p. ej. relevante para misiones con tiempo que están 'completadas' desde el principio.                                                        |
| QUEST_SPECIAL_FLAGS_NO_LOREMASTER_COUNT   | 256   | Esta misión no debería contar para el logro Maestro Cronista (Loremaster).                                                                                                                                                              |
