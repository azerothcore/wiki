# spell\_area

[<-Volver a: World](database-world)

**Tabla \`spell\_area\`**

Esta tabla se usa para aplicar un aura de hechizo específica al jugador dentro de un área del juego. Cuando cualquier jugador entra en esta área o interactúa de algún modo con una misión, esta aura se manejará en consecuencia.

**Estructura**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell][1]              | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [area][2]               | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [quest_start][3]        | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [quest_end][4]          | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [aura_spell][5]         | MEDIUMINT | SIGNED     | PRI | NO   |         |       |         |
| [racemask][6]           | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [gender][7]             | TINYINT   | UNSIGNED   | PRI | NO   |         |       |         |
| [flags][8]              | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [quest_start_status][9] | INT       | UNSIGNED   |     | NO   |         |       |         |
| [quest_end_status][10]  | INT       | UNSIGNED   |     | NO   |         |       |         |

[1]: #spell
[2]: #area
[3]: #quest_start
[4]: #quest_end
[5]: #aura_spell
[6]: #racemask
[7]: #gender
[8]: #flags
[9]: #quest_start_status
[10]: #quest_end_status

**Descripción de los campos**

### spell

El ID del hechizo a lanzar sobre el jugador. Ver [Spell.dbc](spell).

### area

El ID del área. Escribe ".gps" en el juego y busca el número "Area:" a usar en esta celda. Ver también AreaTable.dbc.

### quest\_start

El entry de la misión que el jugador debe tener en el estado definido por **quest\_start\_status**. Ver [quest\_template.id](quest_template#id).

### quest\_end

El entry de la misión que el jugador NO debe tener en el estado definido por **quest\_end\_status**. Ver [quest\_template.id](quest_template#id). Poner tanto **quest\_start** como **quest\_end** al mismo valor es inútil.

### aura\_spell

Si se establece, este valor (más o menos el ID de aura de hechizo de Spell.dbc) impone una condición adicional.

El valor tiene el siguiente efecto:

- **< 0**  (valores negativos) Si el jugador tiene el aura **-aura\_spell** entonces el [spell](#spell_area-spell) no se activará.
-   **0**   esta columna se ignora.
- **> 0**  (valores positivos) Si el jugador no tiene el aura **aura\_spell** entonces el [spell](#spell_area-spell) no se activará.

### racemask

Este ID se llama automáticamente desde [ChrRaces.dbc](chrraces). El bitmask se introduce aquí.

- 0, 1791 = Todas las razas
- 690 (2 + 16 + 32 + 128 + 512) = Solo Horda
- 1101 (1 + 4 + 8 + 64 + 1024 ) = Solo Alianza

### gender

El tipo de género al que se aplica esta entrada. 0 = Masculino, 1 = Femenino, 2 = Cualquiera.

### flags

| Flag | Value | Name                          | Comment                                                                                                                   |
| ---- | ----- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1    | 0x01  | SPELL\_AREA\_FLAG\_AUTOCAST   | Si el hechizo debe aplicarse automáticamente cuando el personaje entra en el área. También impide que el usuario lo elimine. |
| 2    | 0x02  | SPELL\_AREA\_FLAG\_AUTOREMOVE | Si el hechizo debe eliminarse automáticamente cuando el personaje está **dentro** del área (solo funciona con actualizaciones de misión) |

Nota: El hechizo siempre se elimina al salir del área, SPELL\_AREA\_FLAG\_AUTOREMOVE no afecta a esto.

Ejemplo:

- flags = 0 : El hechizo no se añade al entrar (debe añadirse manualmente), no se elimina automáticamente al actualizar la misión, pero se elimina al salir.
- flags = 1 : El hechizo se aplica automáticamente al entrar, no se elimina automáticamente al actualizar la misión, pero se elimina al salir.
- flags = 2 : El hechizo no se añade al entrar (debe añadirse manualmente), se elimina automáticamente al actualizar la misión y se elimina al salir.
- flags = 3 : (Por defecto) El hechizo se aplica automáticamente al entrar, se elimina automáticamente al actualizar la misión y se elimina al salir.

### quest\_start\_status, quest\_end\_status

Dentro de **quest\_start\_status**, puedes definir la máscara del estado de misión requerido para **quest\_start**.

Dentro de **quest\_end\_status**, puedes definir la máscara del estado de misión requerido para **quest\_end**. 

Ejemplo:

El área 257 es una caverna en Teldrassil. Lo que queremos es simple: cuando el jugador toma la misión 28725, tiene el aura en la caverna. Cuando termina la misión 28727, el aura desaparece.

Deberías tener el hechizo 92237 al entrar en la caverna SI:

- La misión de inicio 28725 está incompleta, completa o recompensada (2 | 8 | 64 = 74) 
- La misión de fin 28727 no está tomada (none), está incompleta o completa PERO no recompensada (1 | 2 | 8 = 11)

Aquí está el SQL para este ejemplo: 

```sql
INSERT INTO `spell_area` (`spell`, `area`, `quest_start`, `quest_end`, `autocast`, `quest_start_status`, `quest_end_status`) VALUES 
(92237, 257, 28725, 28727, 1, 74, 11);
```

| Quest Status                       | Flag          | Explanation                                                                         |
| ---------------------------------- | ------------- | ----------------------------------------------------------------------------------- |
| QUEST\_STATUS\_NONE = 0            | 1             | El jugador no tiene ni ha tenido la misión en absoluto. Podría aceptarla, pero no lo ha hecho (todavía). |
| QUEST\_STATUS\_COMPLETE = 1        | 2             | El jugador cumplió los objetivos, pero aún no la ha entregado.                       |
| ~~QUEST\_STATUS\_UNAVAILABLE = 2~~ | 4 (NOT USED)  | (Sin usar)                                                                          |
| QUEST\_STATUS\_INCOMPLETE = 3      | 8             | El jugador aún no cumplió los objetivos                                             |
| ~~QUEST\_STATUS\_AVAILABLE = 4~~   | 16 (NOT USED) | (Sin usar)                                                                          |
| QUEST\_STATUS\_FAILED = 5          | 32            | El jugador falló al cumplir los objetivos por cualquier motivo, p. ej. límite de tiempo |
| QUEST\_STATUS\_REWARDED = 6        | 64            | El jugador entregó la misión y esto es una especie de interacción post-misión       |

Ejemplo para un SQL

 Para un \`quest\_end\_status\` que debe contener QUEST\_STATUS\_NONE (1), QUEST\_STATUS\_COMPLETE (2) y QUEST\_STATUS\_INCOMPLETE (8):

``` sql
-- equivalente a `quest_end_status`= 11
UPDATE `spell_area` SET `quest_end_status`= (1|2|8) WHERE `spell`=XXXXX AND `area`=YYYY;
```

Algunos ejemplos:

- Un área podría pacificar a todos los jugadores (hechizo 39331)
- Otra área podría curar por completo cada 1 segundo (hechizo 48591)
- Teletransportar al jugador fuera de un área (hechizo 53141)
- Buffs específicos de facción, p. ej. en la Ciudadela de la Corona de Hielo:
- "Hellscream's Warsong" (hechizo 73822) para la horda 
- "Strength of Wrynn" (hechizo 73828) para la alianza
- Incluso buffs basados en región, como el área 440 - Tanaris.
