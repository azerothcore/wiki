# phase\_area

[Back-to:World](World)

# Tables**:** phase\_area

## General

PhaseIds added to player by zone/area events. 
Each line holds one Zone or Area with one phaseId and a description.  Each line is active by default. With the table [conditions](conditions)you can edit the working range of the phase.

## Structure

| Field        | Type    | Null | Key | Default | Extra |
|--------------|---------|------|-----|---------|-------|
| [AreaId][1]  | int     | No   | PRI | 0       |       |
| [PhaseId][2] | int     | No   | PRI | 0       |       |
| [Comment][3] | VARCHAR |      |     |         |       |

[1]: #areaid
[2]: #phaseid
[3]: #comment

## Description of the fields

### AreaId

This is the Zone or Area identifier, see [AreaTrigger.dbc](DBC-AreaTrigger)

### PhaseId

This is the connected PhaseId 

### Comment

A free description.

### Examples

As Demo we look at Kezan, Startarea Goblin.

The Player-Character is starting with PhaseId 378 and change on Quest Reward 14109 to Phase 379.

So first we set the definition of both phaseIds to table phase\_area

| AreaId | PhaseId | Comment         |
|--------|---------|-----------------|
| 4737   | 378     | Kezan startarea |
| 4737   | 379     | Kezan startarea |

Now we must declare the Quest-Range by using conditions. Note: we starting from start in phase 378, so we need no start-range, only the end range

| SourceTypeOrReferenceId | SourceGroup | SourceEntry | ConditionTypeOrReference | ConditionValue1 | NegativeCondition | Comment                                            |
|-------------------------|-------------|-------------|--------------------------|-----------------|-------------------|----------------------------------------------------|
| 26                      | 378         | 4737        | 8                        | 14109           | 1                 | Kezan Set in Phase 378 from start to -Reward 14109 |

Next we declare the following range for phase 379 starting with reward on quest 10109 and end on reward quest 14153

| SourceTypeOrReferenceId | SourceGroup | SourceEntry | ConditionTypeOrReference | ConditionValue1 | NegativeCondition | Comment                                  |
|-------------------------|-------------|-------------|--------------------------|-----------------|-------------------|------------------------------------------|
| 26                      | 379         | 4737        | 8                        | 14109           | 0                 | Kezan Set in Phase 379 from reward 14109 |
| 26                      | 379         | 4737        | 8                        | 14153           | 1                 | Kezan Set in Phase 379 to reward 14153   |

And so on....

Note: The quest 14109/14110 14113/14153 are Required Gender Quest.
