# points\_of\_interest\_locale

[<-Back-to:World](database-world)

**The \`locales\_points\_of\_interest\` table**

Translations of the names in [points\_of\_interest](points_of_interest).

**Table Structure**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |            |     |      |         |       |         |
| [Name](#name)                   | TEXT       |            |     | YES  | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | NULL    |       |         |

**Description of the fields**

### ID

The point of interest. See [points\_of\_interest.ID](points_of_interest#id).

### locale

The locale of the translation, for example `deDE`.

### Name

The translated name of the point.

### VerifiedBuild

This field is used to determine if the data originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
