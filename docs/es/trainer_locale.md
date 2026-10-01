# trainer_locale

[<-Volver a:World](database-world)

**Tabla \`trainer_locale\`**

Esta tabla contiene la localización de la plantilla del entrenador.

**Estructura**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |            | PRI | NO   |         |       |         |
| [Greeting_lang](#greetinglang)  | MEDIUMTEXT | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | 0       |       |         |

**Descripción de los campos**

### ID

[trainer.Id](trainer#id).

### locale

| Locale |
| ------ |
| koKR   |
| frFR   |
| deDE   |
| zhCN   |
| zhTW   |
| esES   |
| esMX   |
| ruRU   |

### Greeting_lang

[trainer.Greeting](trainer#greeting) localizado.

### VerifiedBuild

Este campo se usa para determinar si este gameobject procede de sniffs verificados.

Si el valor es 0 entonces aún no se ha parseado o se ha heredado de una BD más antigua o de otro Core.

Si el valor es mayor que 0 entonces se ha parseado con sniffs de esa build de cliente concreta.

Si el valor es -Client Build entonces se parseó con archivos WDB de esa build de cliente concreta y se editó manualmente después por alguna necesidad especial.
