# points\_of\_interest\_locale

[<-Back-to:World](database-world)

**The \`points\_of\_interest\_locale\` table**

Translations of the names in [points\_of\_interest](points_of_interest).

**Table: points\_of\_interest\_locale's Structure**

| Field                           | Type       |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                       | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [Name](#name)                   | TEXT       |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

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
