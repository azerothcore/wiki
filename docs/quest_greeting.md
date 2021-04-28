# quest\_greeting

**Table: quest\_greeting**

This table add greeting behavior to an NPC or an Gameobject.

| Field                | Type      | Attributes | Key | NULL | Default | Comment                                                          |
|----------------------|-----------|------------|-----|------|---------|------------------------------------------------------------------|
| [ID][1]              | MEDIUMINT | Unsigned   | Yes | NO   | 0       | Unique ID (creature_template.entry or gameobject_template.entry) |
| [Type][2]            | TINYINT   | Unsigned   | Yes | NO   | 0       | 0=Creature 1=GameObject                                          |
| [GreetEmoteType][3]  | SMALLINT  | Unsigned   | NO  | NO   | 0       | Quest NPC Emote                                                  |
| [GreetEmoteDelay][4] | INT       | Unsigned   | NO  | NO   | 0       | Emote delay in milliseconds                                      |
| [Greeting][5]        | text      |            | NO  | YES  | NULL    | Text to show                                                     |
| [VerifiedBuild][6]   | SMALLINT  | Signed     | NO  | NO   | 0       | Game client Build number or manually set value                   |

[1]: #id
[2]: #type
[3]: #greetemotetype
[4]: #greetemotedelay
[5]: #greeting
[6]: #verifiedbuild

**Description of the fields:**

### ID

Unique ID ([creature\_template.entry](https://trinitycore.atlassian.net/wiki/display/tc/creature_template#creature_template-entry) or [gameobject\_template.entry](https://trinitycore.atlassian.net/wiki/display/tc/gameobject_template#gameobject_template-entry))

### Type

-   0=Creature (The ID is point to creature\_template.entry)
-   1=GameObject (The ID is point to gameobject\_template.entry)

### GreetEmoteType

Quest NPC [Emote](https://trinitycore.atlassian.net/wiki/display/tc/Emotes)

### GreetEmoteDelay

Emote delay in milliseconds

### Greeting

Text to show

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

- If value is 0 then it has not been parsed yet.
- If value is above 0 then it has been parsed with WDB files from that specific client build.
- If value is -1 then it is just a place holder until proper data are found on WDBs.
- If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
