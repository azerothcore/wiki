# character\_stats

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_stats\`**

La tabla alberga información acerca de todas las estadísticas relativas al personaje. Es usada comunmente para aplicaciones externas, como en sitios web.
Véase worldserver.conf: PlayerSave.Stats.\*

**Estructura**

| Field                   | Type  | Attributes | Key | Null | Default | Extra | Comment                            |
| ----------------------- | ----- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]               | INT   | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [maxhealth][2]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower1][3]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower2][4]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower3][5]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower4][6]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower5][7]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower6][8]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower7][9]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [strength][10]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [agility][11]           | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [stamina][12]           | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [intellect][13]         | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [spirit][14]            | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [armor][15]             | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resHoly][16]           | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resFire][17]           | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resNature][18]         | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resFrost][19]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resShadow][20]         | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resArcane][21]         | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [blockPct][22]          | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [dodgePct][23]          | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [parryPct][24]          | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [critPct][25]           | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [rangedCritPct][26]     | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [spellCritPct][27]      | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [attackPower][28]       | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [rangedAttackPower][29] | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [spellPower][30]        | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resilience][31]        | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |

[1]: #guid
[2]: #maxhealth
[3]: #maxpower
[4]: #maxpower
[5]: #maxpower
[6]: #maxpower
[7]: #maxpower
[8]: #maxpower
[9]: #maxpower
[10]: #strength
[11]: #agility
[12]: #stamina
[13]: #intellect
[14]: #spirit
[15]: #armor
[16]: #resholy
[17]: #resfire
[18]: #resnature
[19]: #resfrost
[20]: #resshadow
[21]: #resarcane
[22]: #blockpct
[23]: #dodgepct
[24]: #parrypct
[25]: #critpct
[26]: #rangedcritpct
[27]: #spellcritpct
[28]: #attackpower
[29]: #rangedattackpower
[30]: #spellpower
[31]: #resilience

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### maxhealth

Cantidad máxima de salud que posée el personaje actualmente.

### maxpower

| Valor | Descripción  |
| ----- | ------------ |
| 1     | Maná         |
| 2     | Ira          |
| 3     | Focus        |
| 4     | Energía      |
| 5     | Felicidad    |
| 6     | Runas        |
| 7     | Poder rúnico |

### strength

Valor actual de la Fuerza del personaje.

### agility

Valor actual de la Agilidad del personaje.

### stamina

Valor actual del Aguante del personaje.

### intellect

Valor actual del Intelecto del personaje.

### spirit

Valor actual del Espíritu del personaje.

### armor

Valor actual de la Armadura del personaje.

### resHoly

Valor actual de la Resistencia a lo Sagrado del personaje.

### resFire

Valor actual de la Resistencia al Fuego del personaje.

### resNature

Valor actual de la Resistencia a la Naturaleza del personaje.

### resFrost

Valor actual de la Resistencia a la Escarcha del personaje.

### resShadow

Valor actual de la Resistencia a las Sombras del personaje.

### resArcane

Valor actual de la Resistencia a lo Arcano del personaje.

### blockPct

Probabilidad de Bloqueo actual del personaje.

El valor debe ser >=0 (mayor o igual a cero). Si el valor no cumple la condición, la sentencia SQL fallará en `character_stats_chk_1`.

### dodgePct

Probabilidad de Esquivar actual del personaje.

El valor debe ser >=0 (mayor o igual a cero). Si el valor no cumple la condición, la sentencia SQL fallará en `character_stats_chk_1`.

### parryPct

Probabilidad de Parar actual del personaje.

El valor debe ser >=0 (mayor o igual a cero). Si el valor no cumple la condición, la sentencia SQL fallará en `character_stats_chk_1`.

### critPct

Probabilidad de Golpe Crítico actual del personaje.

El valor debe ser >=0 (mayor o igual a cero). Si el valor no cumple la condición, la sentencia SQL fallará en `character_stats_chk_1`.

### rangedCritPct

Probabilidad de Golpe Crítico a distancia actual del personaje.

El valor debe ser >=0 (mayor o igual a cero). Si el valor no cumple la condición, la sentencia SQL fallará en `character_stats_chk_1`.

### spellCritPct

Probabilidad de Golpe Crítico de hechizos actual del personaje.

El valor debe ser >=0 (mayor o igual a cero). Si el valor no cumple la condición, la sentencia SQL fallará en `character_stats_chk_1`.

### attackPower

Poder de Ataque actual del personaje

### rangedAttackPower

Poder de Ataque a distancia actual del personaje

### spellPower

Poder de hechizos actual del personaje

### resilience

Valor actual del Temple del personaje.