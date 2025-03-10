# spell\_linked\_spell

[<-Back-to:World](database-world)

**The \`spell\_linked\_spell\` table**

This table provides data for spell linking system, telling it which spells trigger what, and under which conditions.

**Table Structure**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell_trigger][1] | MEDIUMINT | SIGNED     |     | NO   |         |       |         |
| [spell_effect][2]  | MEDIUMINT | SIGNED     |     | NO   |         |       |         |
| [type][3]          | SMALLINT  | UNSIGNED   |     | NO   |         |       |         |
| [comment][4]       | text      |            |     | NO   |         |       |         |

[1]: #spelltrigger
[2]: #spelleffect
[3]: #type
[4]: #comment

**Description of the fields**

### spell\_trigger

The spell, which when cast, will trigger the spell listed in [spell\_effect](#spell_effect)

### spell\_ effect

The spell that you want to be triggered. How this spell acts is determined by the [type](#type) field.

### type

Three values are possible (0,1,2). See below.

### comment

Optional comment to explain the link.

# **Description of the linking effects**

### type 0 (CAST)

**Trigger mode**

- \***spell\_trigger > 0:** "When *spell\_trigger* is cast..."
- \***spell\_trigger < 0:** "When the aura due to *spell\_trigger* is removed..."

**Effect**

- \***spell\_effect > 0:** *spell\_effect* is also cast (with triggered flag) on the same targets, on the caster if *spell\_trigger* has no target.
- \***spell\_effect < 0:** Auras due to *spell\_effect* are removed.

### type 1 (HIT)

**Trigger mode**

- \***spell\_trigger > 0:** "Effect is executed when *spell\_trigger* hits a target. I suppose that if the *spell\_trigger* hits more than one target, the effect is executed for each target hit.

**Effect**

- \***spell\_effect > 0:** *spell\_effect* is cast (with triggered flag) on the same target.
- \***spell\_effect < 0:** Auras due to *spell\_effect* are removed.

### type 2 (AURA)

**Trigger mode**

- \***spell\_trigger > 0:** "Effect is executed when the aura *spell\_trigger* is applied **AND** when it is removed from a target.

**Effect**

\***spell\_effect > 0 (ADD/REMOVE AURA)**

-   ON APPLY: Adds aura *spell\_effect* on the same target.
-   ON REMOVE: Removes aura *spell\_effect*on the same target.

\***spell\_effect < 0 (IMMUNITY)**

-   ON APPLY: Makes the target immune to *spell\_effect*.
-   ON REMOVE: Clears target immunity to *spell\_effect*.
