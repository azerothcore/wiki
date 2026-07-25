# trainer_spell

[<-Volver a:World](database-world)

**Tabla \`trainer_spell\`**

Esta tabla contiene las entradas de spells del entrenador.

**Estructura**

| Field                           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TrainerId](#trainerid)         | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [SpellId](#spellid)             | INT     | UNSIGNED   | PRI | NO   | 2       |       |         |
| [MoneyCost](#moneycost)         | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqSkillLine](#reqskillline)   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqSkillRank](#reqskillrank)   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility1](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility2](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility3](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqLevel](#reqlevel)           | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT     |            |     | YES  | 0       |       |         |

**Descripción de los campos**

### TrainerId

[trainer.Id](trainer#id).

### SpellId

El ID del spell a enseñar.

### MoneyCost

El coste en cobre para aprender el spell.

### ReqSkillLine

El [SkillLine ID](skillline) que el jugador debe conocer para aprender el spell.

| ID  | Name           |
| --- | -------------- |
| 129 | First Aid      |
| 164 | Blacksmithing  |
| 165 | Leatherworking |
| 171 | Alchemy        |
| 182 | Herbalism      |
| 185 | Cooking        |
| 186 | Mining         |
| 197 | Tailoring      |
| 202 | Engineering    |
| 333 | Enchanting     |
| 356 | Fishing        |
| 393 | Skinning       |
| 633 | Lockpicking    |
| 755 | Jewelcrafting  |
| 773 | Inscription    |
| 776 | Runeforging    |

### ReqSkillRank

El nivel mínimo de puntos de skill en [ReqSkillLine](#reqskillline) requerido para aprender el spell.

### ReqAbility

El ID del spell requerido que el jugador necesita para aprender el spell.

### ReqLevel

El nivel de jugador requerido para aprender este spell.

### VerifiedBuild

Este campo se usa para determinar si este gameobject procede de sniffs verificados.

Si el valor es 0 entonces aún no se ha parseado o se ha heredado de una BD más antigua o de otro Core.

Si el valor es mayor que 0 entonces se ha parseado con sniffs de esa build de cliente concreta.

Si el valor es -Client Build entonces se parseó con archivos WDB de esa build de cliente concreta y se editó manualmente después por alguna necesidad especial.
