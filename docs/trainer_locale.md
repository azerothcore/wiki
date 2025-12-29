# trainer_locale

[<-Back-to:World](database-world)

**The \`trainer_locale\` table**

This table hold the locale of the trainer template.

**Table Structure**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |            | PRI | NO   |         |       |         |
| [Greeting_lang](#greetinglang)  | MEDIUMTEXT | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | 0       |       |         |

**Description of the fields**

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

[trainer.Greeting](trainer#greeting) localized.

### VerifiedBuild

This field is used to determine if this gameobject originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
