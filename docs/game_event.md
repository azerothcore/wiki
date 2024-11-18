# game_event

[<-Back-to:World](database-world)

**The \`game_event\` table**

**Table Structure**

This table holds definitions for all game events that are activated or deactivated automatically by the Game Event System in the core.

| Field                        | Type         | Attributes | Key | Null | Default | Extra  | Comment                                                                                                                              |
| ---------------------------- | ------------ | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| [eventEntry](#evententry)    | TINYINT      | UNSIGNED   | PRI | NO   |         | Unique | Entry of the game event                                                                                                              |
| [start_time](#starttime)     | TIMESTAMP    |            |     | YES  | NULL    |        | Absolute start date, the event will never start before                                                                               |
| [end_time](#endtime)         | TIMESTAMP    |            |     | YES  | NULL    |        | Absolute end date, the event will never start after; if NULL it will be implicitly set to 2 years in the future on each server start |
| [occurrence](#occurrence)    | BIGINT       | UNSIGNED   |     | NO   |         |        | Delay in minutes between occurrences of the event                                                                                    |
| [length](#length)            | BIGINT       | UNSIGNED   |     | NO   |         |        | Length in minutes of the event                                                                                                       |
| [holiday](#holiday)          | MEDIUMINT    | UNSIGNED   |     | NO   |         |        | Client side holiday id (from dbc)                                                                                                    |
| [holidayStage](holidaystage) | TINYINT      | UNSIGNED   |     | NO   |         |        |                                                                                                                                      |
| [description](#description)  | VARCHAR(255) | SIGNED     |     | YES  | NULL    |        | Description of the event displayed in console                                                                                        |
| [world_event](#worldevent)   | TINYINT      | UNSIGNED   |     | NO   |         |        | 0 if normal event, 1 if world event                                                                                                  |
| [announce](#announce)        | TINYINT      | UNSIGNED   |     | YES  | 2       |        | 0 dont announce, 1 announce, 2 value from config                                                                                     |

**Field Descriptions**

### eventEntry

Entry of the event. Keep it as low as possible and prevent making holes in the list. Higher the max id is, the more memory will be used to store the event data.

### start_time

Absolute start date of the event. The event will start occurring only if the local time at the server is after the one set here.

### end_time

Absolute end date of the event. The event will stop occurring if the local time at the server is after the one set here.

### occurrence

Number of minutes between 2 occurrences of the event. (2880 = 2 days, 1440 = 1 day, etc)

{% include warning.html content="Value can't be 0 or the server will crash." %}

### length

Number of minutes the event will last after the start of the occurrence. (2880 = 2 days, 1440 = 1 day, etc)
This value must be lower than occurrence one or the event will never stop.


### holiday

Holiday ID from  [Holidays DBC file](holidays). This is sent to the client to update the calender.

### description

String containing the name of the event displayed in console each time it starts or stops.

### world_event

This is a boolean field that determines if this game event is a world event or not. 0 = normal event, 1 = world event. For the world event to work, you need to at a minimum, populate [game_event_condition](game_event_condition) and [game_event_quest_condition](game_event_quest_condition).

### announce

| Value | Description                                        |
| ----- | -------------------------------------------------- |
| 0     | Don't announce the Event                           |
| 1     | Announce the description of the Event to the world |
| 2     | Use the `event.announce` settings from the config  |

### Database Content

<details>

<summary>Click me to see the contents of the table (18/11/2024)</summary>

| eventEntry | start_time       | end_time         | occurence | length  | holiday | holidayStage | description                                      | world_event | announce |
| ---------- | ---------------- | ---------------- | --------- | ------- | ------- | ------------ | ------------------------------------------------ | ----------- | -------- |
| 1          | 22/06/2021 00:01 | 31/12/2030 12:00 | 525600    | 20160   | 341     | 1            | Midsummer Fire Festival                          | 0           | 2        |
| 2          | 16/12/2021 01:00 | 31/12/2030 12:00 | 525600    | 25920   | 141     | 1            | Winter Veil                                      | 0           | 2        |
| 3          | 05/01/2020 06:01 | 31/12/2030 12:00 | 131040    | 10079   | 376     | 2            | Darkmoon Faire (Terokkar Forest)                 | 0           | 2        |
| 4          | 07/09/2014 06:01 | 31/12/2030 12:00 | 131040    | 10079   | 374     | 2            | Darkmoon Faire (Elwynn Forest)                   | 0           | 2        |
| 5          | 05/10/2014 06:01 | 31/12/2030 12:00 | 131040    | 10079   | 375     | 2            | Darkmoon Faire (Mulgore)                         | 0           | 2        |
| 6          | 01/01/2021 07:00 | 31/12/2030 12:00 | 525600    | 120     | 0       | 0            | New Year's Eve                                   | 0           | 2        |
| 7          | 24/01/2021 00:01 | 31/12/2030 12:00 | 525600    | 20160   | 327     | 1            | Lunar Festival                                   | 0           | 2        |
| 8          | 08/02/2021 00:01 | 31/12/2030 12:00 | 525600    | 20160   | 423     | 1            | Love is in the Air                               | 0           | 2        |
| 9          | 13/04/2021 00:01 | 31/12/2030 12:00 | 525600    | 10080   | 181     | 1            | Noblegarden                                      | 0           | 2        |
| 10         | 01/05/2021 00:01 | 31/12/2030 12:00 | 525600    | 10080   | 201     | 1            | Children's Week                                  | 0           | 2        |
| 11         | 29/09/2021 00:01 | 31/12/2030 12:00 | 525600    | 10080   | 321     | 1            | Harvest Festival                                 | 0           | 2        |
| 12         | 19/10/2021 00:00 | 31/12/2030 12:00 | 525600    | 20160   | 324     | 1            | Hallow's End                                     | 0           | 2        |
| 13         | 01/01/2000 14:00 | 01/01/2000 14:00 | 525600    | 1       | 0       | 0            | Elemental Invasions                              | 0           | 2        |
| 14         | 29/10/2016 00:00 | 31/12/2030 07:00 | 10080     | 1440    | 0       | 0            | Stranglethorn Fishing Extravaganza Announce      | 0           | 2        |
| 15         | 30/10/2016 14:00 | 31/12/2030 07:00 | 10080     | 120     | 301     | 0            | Stranglethorn Fishing Extravaganza Fishing Pools | 0           | 2        |
| 16         | 05/08/2007 10:00 | 31/12/2030 12:00 | 180       | 120     | 0       | 0            | Gurubashi Arena Booty Run                        | 0           | 2        |
| 17         | 01/01/2000 14:00 | 01/01/2000 14:00 | 525600    | 1       | 0       | 0            | Scourge Invasion                                 | 0           | 2        |
| 18         | 07/05/2010 13:00 | 31/12/2030 12:00 | 60480     | 6240    | 283     | 1            | Call to Arms: Alterac Valley!                    | 0           | 2        |
| 19         | 02/04/2010 13:00 | 31/12/2030 12:00 | 60480     | 6240    | 284     | 1            | Call to Arms: Warsong Gulch!                     | 0           | 2        |
| 20         | 23/04/2010 13:00 | 31/12/2030 12:00 | 60480     | 6240    | 285     | 1            | Call to Arms: Arathi Basin!                      | 0           | 2        |
| 21         | 30/04/2010 13:00 | 31/12/2030 12:00 | 60480     | 6240    | 353     | 1            | Call to Arms: Eye of the Storm!                  | 0           | 2        |
| 22         | 01/01/2000 14:00 | 01/01/2000 14:00 | 525600    | 1       | 0       | 0            | AQ War Effort                                    | 0           | 2        |
| 23         | 04/09/2014 06:01 | 31/12/2030 12:00 | 131040    | 4320    | 374     | 1            | Darkmoon Faire Building (Elwynn Forest)          | 0           | 2        |
| 24         | 20/09/2021 03:00 | 31/12/2030 13:00 | 525600    | 21600   | 372     | 2            | Brewfest                                         | 0           | 2        |
| 25         | 29/07/2015 21:00 | 31/12/2030 12:00 | 1440      | 540     | 0       | 0            | Pyrewood Village                                 | 0           | 2        |
| 26         | 23/11/2021 01:00 | 31/12/2030 12:00 | 525600    | 10080   | 404     | 1            | Pilgrim's Bounty                                 | 0           | 2        |
| 27         | 24/03/2008 12:00 | 31/12/2030 12:00 | 86400     | 21600   | 0       | 0            | Edge of Madness, Gri'lek                         | 0           | 2        |
| 28         | 07/04/2008 12:00 | 31/12/2030 12:00 | 86400     | 21600   | 0       | 0            | Edge of Madness, Hazza'rah                       | 0           | 2        |
| 29         | 21/04/2008 12:00 | 31/12/2030 12:00 | 86400     | 21600   | 0       | 0            | Edge of Madness, Renataki                        | 0           | 2        |
| 30         | 05/05/2008 12:00 | 31/12/2030 12:00 | 86400     | 21600   | 0       | 0            | Edge of Madness, Wushoolay                       | 0           | 2        |
| 31         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Tournament                                 | 0           | 2        |
| 32         | 31/07/2008 12:00 | 05/08/2008 12:00 | 60        | 5       | 0       | 0            | L70ETC BlizzCon Concert                          | 0           | 2        |
| 33         | 22/03/2011 06:10 | 31/12/2030 12:00 | 30        | 5       | 0       | 0            | Dalaran: Minigob                                 | 0           | 2        |
| 34         | 01/10/2021 00:01 | 31/12/2030 12:00 | 525600    | 44640   | 0       | 0            | Brew of the Month October                        | 0           | 2        |
| 35         | 01/11/2021 00:01 | 31/12/2030 12:00 | 525600    | 43200   | 0       | 0            | Brew of the Month November                       | 0           | 2        |
| 36         | 01/12/2021 00:01 | 31/12/2030 12:00 | 525600    | 44640   | 0       | 0            | Brew of the Month December                       | 0           | 2        |
| 37         | 01/01/2021 00:01 | 31/12/2030 12:00 | 525600    | 44640   | 0       | 0            | Brew of the Month January                        | 0           | 2        |
| 38         | 01/02/2021 00:01 | 31/12/2030 12:00 | 525600    | 40320   | 0       | 0            | Brew of the Month February                       | 0           | 2        |
| 39         | 01/03/2021 00:01 | 31/12/2030 12:00 | 525600    | 44640   | 0       | 0            | Brew of the Month March                          | 0           | 2        |
| 40         | 01/04/2021 00:01 | 31/12/2030 12:00 | 525600    | 43200   | 0       | 0            | Brew of the Month April                          | 0           | 2        |
| 41         | 01/05/2021 00:01 | 31/12/2030 12:00 | 525600    | 44640   | 0       | 0            | Brew of the Month May                            | 0           | 2        |
| 42         | 01/06/2021 00:01 | 31/12/2030 12:00 | 525600    | 43200   | 0       | 0            | Brew of the Month June                           | 0           | 2        |
| 43         | 01/07/2021 00:01 | 31/12/2030 12:00 | 525600    | 44640   | 0       | 0            | Brew of the Month July                           | 0           | 2        |
| 44         | 01/08/2021 00:01 | 31/12/2030 12:00 | 525600    | 44640   | 0       | 0            | Brew of the Month August                         | 0           | 2        |
| 45         | 01/09/2021 00:01 | 31/12/2030 12:00 | 525600    | 44640   | 0       | 0            | Brew of the Month September                      | 0           | 2        |
| 46         | 08/09/2008 12:00 | 24/09/2008 12:00 | 1051897   | 23040   | 0       | 0            | Spirit of Competition                            | 0           | 2        |
| 47         | 31/07/2008 12:00 | 05/08/2008 12:00 | 5184000   | 7200    | 0       | 0            | BlizzCon 2007                                    | 0           | 2        |
| 48         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Wintergrasp Alliance Defence                     | 5           | 2        |
| 49         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Wintergrasp Horde Defence                        | 5           | 2        |
| 50         | 19/09/2021 01:01 | 31/12/2030 12:00 | 525600    | 1440    | 398     | 1            | Pirates' Day                                     | 0           | 2        |
| 51         | 01/11/2021 02:00 | 31/12/2030 12:00 | 525600    | 2820    | 409     | 1            | Day of the Dead                                  | 0           | 2        |
| 52         | 25/12/2021 06:00 | 31/12/2030 12:00 | 525600    | 11700   | 0       | 0            | Winter Veil: Gifts                               | 0           | 2        |
| 53         | 09/04/2010 13:00 | 31/12/2030 12:00 | 60480     | 6240    | 400     | 1            | Call to Arms: Strand of the Ancients!            | 0           | 2        |
| 54         | 16/04/2010 13:00 | 31/12/2030 12:00 | 60480     | 6240    | 420     | 1            | Call to Arms: Isle of Conquest!                  | 0           | 2        |
| 55         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Season 3                                   | 0           | 2        |
| 56         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Season 4                                   | 0           | 2        |
| 57         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Season 5                                   | 0           | 2        |
| 58         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Season 6                                   | 0           | 2        |
| 59         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Season 7                                   | 0           | 2        |
| 60         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Season 8                                   | 0           | 2        |
| 61         | 07/09/2010 06:00 | 10/10/2010 06:00 | 9999999   | 47520   | 0       | 0            | Zalazane's Fall                                  | 0           | 2        |
| 62         | 30/10/2016 13:00 | 31/12/2030 07:00 | 10080     | 240     | 0       | 0            | Stranglethorn Fishing Extravaganza - The Crew    | 0           | 2        |
| 63         | 22/03/2014 13:00 | 31/12/2030 12:00 | 10080     | 180     | 0       | 0            | Kalu'ak Fishing Derby Turn-ins                   | 0           | 2        |
| 64         | 22/03/2014 14:00 | 31/12/2030 12:00 | 10080     | 60      | 424     | 0            | Kalu'ak Fishing Derby Fishing Pools              | 0           | 2        |
| 65         | 01/01/2000 14:00 | 31/12/2030 12:00 | 5184000   | 2592000 | 0       | 0            | Venture Bay Alliance Defence                     | 5           | 2        |
| 66         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Venture Bay Horde Defence                        | 5           | 2        |
| 67         | 02/01/2010 06:40 | 31/12/2030 12:00 | 60        | 5       | 0       | 0            | AT Event Trigger (Tirion Speech)                 | 0           | 2        |
| 68         | 02/01/2010 06:55 | 31/12/2030 12:00 | 60        | 5       | 0       | 0            | AT Event Trigger (Horde Event)                   | 0           | 2        |
| 69         | 02/01/2010 06:10 | 31/12/2030 12:00 | 60        | 5       | 0       | 0            | AT Event Trigger (Alliance Event)                | 0           | 2        |
| 70         | 17/09/2021 03:00 | 31/12/2030 12:00 | 525600    | 4320    | 0       | 0            | Brewfest Building (Iron Forge)                   | 0           | 2        |
| 71         | 06/01/2013 07:01 | 31/12/2030 12:00 | 131040    | 4320    | 375     | 1            | Darkmoon Faire Building (Mulgore)                | 0           | 2        |
| 72         | 04/07/2024 06:00 | 31/12/2030 12:00 | 525600    | 1080    | 62      | 0            | Fireworks Spectacular                            | 0           | 2        |
| 73         | 01/01/2010 01:00 | 01/01/2030 01:00 | 60        | 1       | 0       | 0            | Hourly Bells                                     | 0           | 2        |
| 74         | 01/01/2022 07:00 | 01/01/2030 08:00 | 1440      | 60      | 0       | 0            | Children of Goldshire                            | 0           | 2        |
| 75         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Season 1                                   | 0           | 2        |
| 76         | 01/01/2000 14:00 | 01/01/2000 14:00 | 5184000   | 2592000 | 0       | 0            | Arena Season 2                                   | 0           | 2        |
| 77         | 06/11/2016 02:01 | 31/12/2030 07:00 | 131040    | 4320    | 376     | 1            | Darkmoon Faire Building (Terokkar Forest)        | 0           | 2        |
| 78         | 20/03/2021 07:00 | 31/12/2030 07:00 | 525600    | 262800  | 0       | 0            | Summer seasonal fish                             | 0           | 2        |
| 79         | 28/10/2018 12:00 | 31/12/2030 18:00 | 1440      | 360     | 0       | 0            | Diurnal fishing event                            | 0           | 2        |
| 80         | 28/10/2018 00:00 | 31/12/2030 06:00 | 1440      | 360     | 0       | 0            | Nocturnal fishing event                          | 0           | 2        |
| 81         | 02/01/2008 08:00 | 31/12/2030 06:00 | 1440      | 15      | 0       | 0            | L70ETC Grim Guzzler Concert                      | 0           | 2        |
| 82         | 02/01/2008 01:55 | 31/12/2030 06:00 | 240       | 15      | 0       | 0            | L70ETC World's End Tavern Concert                | 0           | 2        |
| 85         | 22/03/2011 01:00 | 31/12/2030 07:00 | 5184000   | 35      | 0       | 0            | Stitches Event                                   | 0           | 2        |
| 86         | 02/01/2008 11:55 | 31/12/2030 06:00 | 240       | 15      | 0       | 0            | Perry Gatner                                     | 0           | 2        |
| 87         | 02/01/2008 11:55 | 31/12/2030 06:00 | 5184000   | 90      | 0       | 0            | Scarlet Oracle                                   | 0           | 2        |
| 88         | 28/10/2016 18:00 | 30/12/2030 23:00 | 1440      | 720     | 0       | 0            | Evening                                          | 0           | 2        |
| 89         | 28/10/2016 20:00 | 30/12/2030 23:00 | 1440      | 600     | 0       | 0            | Leprithus                                        | 0           | 2        |
| 90         | 30/10/2016 14:00 | 31/12/2030 07:00 | 10080     | 180     | 0       | 0            | Stranglethorn Fishing Extravaganza - Turn-ins    | 0           | 2        |

</details>
