# quest_greeting_locale

[<-Back-to:World](database-world)

**The \`quest_greeting_locale\` table**

This table add greeting behavior to an NPC or an Gameobject.

**Table Structure**

| Field              | Type       | Attributes | Key | NULL | Default | Comment |
| ------------------ | ---------- | ---------- | --- | ---- | ------- | ------- |
| [ID][1]            | MEDIUMINT  | UNSIGNED   | Yes | NO   | 0       |         |
| [Type][2]          | TINYINT    | UNSIGNED   | Yes | NO   | 0       |         |
| [locale][3]        | VARCHAR(4) |            | NO  | NO   |         |         |
| [Greeting][5]      | TEXT       |            | NO  | YES  | NULL    |         |
| [VerifiedBuild][6] | SMALLINT   | SIGNED     | NO  | NO   | 0       |         |

[1]: #id
[2]: #type
[3]: #greetemotetype
[4]: #greetemotedelay
[5]: #greeting
[6]: #verifiedbuild

**Description of the fields:**

### ID

Unique ID ([creature_template.entry](creature_template#entry) or [gameobject\_template.entry](gameobject_template#entry))

### Type

-   0=Creature (The ID is point to creature\_template.entry)
-   1=GameObject (The ID is point to gameobject\_template.entry)

### locale

Client Locale

### Greeting

Text to show

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

- If value is 0 then it has not been parsed yet.
- If value is above 0 then it has been parsed with WDB files from that specific client build.
- If value is -1 then it is just a place holder until proper data are found on WDBs.
- If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
