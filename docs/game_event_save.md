# game\_event\_save

[<-Back-to:Characters](database-characters)

**The \`game\_event\_save\` table**

Stores the saved state and next start time of world events, the game events that progress through conditions.

**Table: game\_event\_save's Structure**

| Field                     | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [eventEntry](#evententry) | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [state](#state)           | TINYINT | UNSIGNED | NO   |     | 1       |       |         |
| [next_start](#nextstart)  | INT     | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### eventEntry

The game event. See [game\_event.eventEntry](game_event#evententry).

### state

The state of a world event:

| Value | State                      | Description                                                    |
| ----- | -------------------------- | -------------------------------------------------------------- |
| 0     | GAMEEVENT_NORMAL           | Standard game event.                                           |
| 1     | GAMEEVENT_WORLD_INACTIVE   | Not started yet.                                               |
| 2     | GAMEEVENT_WORLD_CONDITIONS | Waiting for its conditions to be met.                          |
| 3     | GAMEEVENT_WORLD_NEXTPHASE  | Conditions are met, waiting for the next event to start.       |
| 4     | GAMEEVENT_WORLD_FINISHED   | The next events have started.                                  |
| 5     | GAMEEVENT_INTERNAL         | Never handled by the event update.                             |

### next\_start

The time the event moves to its next state, in Unix time. 0 if not set.
