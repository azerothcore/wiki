# trainer

[<-Volver a:World](database-world)

**Tabla \`trainer\`**

Esta tabla contiene la plantilla única del entrenador (trainer).

**Estructura**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Type](#type)                   | TINYINT    | UNSIGNED   |     | NO   | 2       |       |         |
| [Requirement](#requirement)     | MEDIUMINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Greeting](#greeting)           | MEDIUMTEXT |            |     | NO   |         |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | 0       |       |         |

**Descripción de los campos**

### ID

ID único del entrenador

### Type

| Type | Description |
| ---- | ----------- |
| 0    | Class       |
| 1    | Mount       |
| 2    | Tradeskill  |
| 3    | Pet         |

### Requirement

Deja 0 para que no haya requisito.

| Type       | Requirement                              | Description                                              |
| ---------- | ---------------------------------------- | ------------------------------------------------------- |
| Class      | [ChrClasses.Content](chrclasses#content) | El jugador necesita ser de esta clase para entrenar con el entrenador. |
| Mount      | [ChrRaces](chrraces#content)             | El jugador necesita ser de esta raza para entrenar con el entrenador.  |
| TradeSkill | Spell ID                                 | El jugador debe conocer este spell para entrenar con este entrenador. |
| Pet        | [ChrClasses.Content](chrclasses#content) | El jugador necesita ser de esta clase para entrenar con el entrenador. |

### Greeting

El texto que se muestra al abrir la ventana del entrenador.

Esto no es texto de gossip.

### VerifiedBuild

Este campo se usa para determinar si este gameobject procede de sniffs verificados.

Si el valor es 0 entonces aún no se ha parseado o se ha heredado de una BD más antigua o de otro Core.

Si el valor es mayor que 0 entonces se ha parseado con sniffs de esa build de cliente concreta.

Si el valor es -Client Build entonces se parseó con archivos WDB de esa build de cliente concreta y se editó manualmente después por alguna necesidad especial.
