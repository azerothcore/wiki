# player_shapeshift_model

[<-Back-to:World](database-world)

**The \`player_shapeshift_model\` table**

This table holds the information on what values are used for the druid shapeshift models, based on the shapeshift, race, character customisation and their gender.

**Table Structure**

| Field                              | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| ShapeshiftID (#shapeshiftid)       | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| RaceID (#raceid)                   | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| CustomizationID (#customizationid) | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| GenderID (#genderid)               | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| ModelID (#modelid)                 | INT     | UNSIGNED   |     | NO   |         |       |         |

**Description of the fields**

### ShapeshiftID

| FormID |   Description    |
| :----: | :--------------: |
|   1    |     Cat Form     |
|   5    |    Bear Form     |
|   8    |  Dire Bear Form  |
|   27   | Epic Flight Form |
|   29   |   Flight Form    |

### RaceID

| RaceID | Description |
| :----: | :---------: |
|   4    |  Night Elf  |
|   6    |   Tauren    |

You also may refer to [chrraces](chrraces) "ID" column.

### CustomizationID

If you're a Night Elf it's works by using the [haircolor](characters#haircolor) as the value.

Example below:

| ShapeshiftID | RaceID | CustomizationID [[haircolor](characters#haircolor)] | GenderID | ModelID |                    Comment                    |
| :----------: | :----: | :-------------------------------------------------: | :------: | :-----: | :-------------------------------------------: |
|      5       |   4    |                          6                          |    2     |  29414  | Night Elf, any gender, bear colour: Dark Blue |

If you're a Tauren it's works by using the [skin](characters#skin) as the value.

| ShapeshiftID | RaceID | CustomizationID [[skin](characters#skin)] | GenderID | ModelID |                 Comment                 |
| :----------: | :----: | :---------------------------------------: | :------: | :-----: | :-------------------------------------: |
|      5       |   6    |                     0                     |    0     |  29418  | Tauren, male, bear colour: Dark (Black) |
|      5       |   6    |                     2                     |    1     |  29419  |   Tauren, female, bear colour: White    |

### GenderID

| [GenderID](characters#gender) | Description |
| :---------------------------: | :---------: |
|               0               |    Male     |
|               1               |   Female    |
|               2               |   Unknown   |

### ModelID

Refer to [creature_model_info](#creature_model_info#displayid)

### Default Values

From the Pull request: [refactor(Core): Use database tables for Shaman totems and Druid shapeshift forms. (#22104)](https://github.com/azerothcore/azerothcore-wotlk/pull/22104)

| ShapeshiftID | RaceID | CustomizationID | GenderID | ModelID |       Comment        |
| :----------: | :----: | :-------------: | :------: | :-----: | :------------------: |
|      1       |   4    |        0        |    2     |  29407  |        Green         |
|      1       |   4    |        1        |    2     |  29407  |     Light Green      |
|      1       |   4    |        2        |    2     |  29407  |      Dark Green      |
|      1       |   4    |        3        |    2     |  29406  |      Light Blue      |
|      1       |   4    |        4        |    2     |  29408  |        White         |
|      1       |   4    |        7        |    2     |  29405  |        Violet        |
|      1       |   4    |        8        |    2     |  29405  |        Violet        |
|      1       |   4    |       255       |    2     |   892   |      Dark Blue       |
|      1       |   6    |       12        |    0     |  29409  |        White         |
|      1       |   6    |       13        |    0     |  29409  |        White         |
|      1       |   6    |       14        |    0     |  29409  |        White         |
|      1       |   6    |       18        |    0     |  29409  |   Completely White   |
|      1       |   6    |        9        |    0     |  29410  |     Light Brown      |
|      1       |   6    |       10        |    0     |  29410  |     Light Brown      |
|      1       |   6    |       11        |    0     |  29410  |     Light Brown      |
|      1       |   6    |        6        |    0     |  29411  |        Brown         |
|      1       |   6    |        7        |    0     |  29411  |        Brown         |
|      1       |   6    |        8        |    0     |  29411  |        Brown         |
|      1       |   6    |        0        |    0     |  29412  |         Dark         |
|      1       |   6    |        1        |    0     |  29412  |         Dark         |
|      1       |   6    |        2        |    0     |  29412  |         Dark         |
|      1       |   6    |        3        |    0     |  29412  |      Dark Grey       |
|      1       |   6    |        4        |    0     |  29412  |      Dark Grey       |
|      1       |   6    |        5        |    0     |  29412  |      Dark Grey       |
|      1       |   6    |       255       |    0     |  8571   |         Grey         |
|      1       |   6    |       10        |    1     |  29409  |        White         |
|      1       |   6    |        6        |    1     |  29410  |     Light Brown      |
|      1       |   6    |        7        |    1     |  29410  |     Light Brown      |
|      1       |   6    |        4        |    1     |  29411  |        Brown         |
|      1       |   6    |        5        |    1     |  29411  |        Brown         |
|      1       |   6    |        0        |    1     |  29412  |         Dark         |
|      1       |   6    |        1        |    1     |  29412  |         Dark         |
|      1       |   6    |        2        |    1     |  29412  |         Dark         |
|      1       |   6    |        3        |    1     |  29412  |         Dark         |
|      1       |   6    |       255       |    1     |  8571   |         Grey         |
|      5       |   4    |        0        |    2     |  29413  |    Green (29415?)    |
|      5       |   4    |        1        |    2     |  29413  | Light Green (29415?) |
|      5       |   4    |        2        |    2     |  29413  | Dark Green (29415?)  |
|      5       |   4    |        6        |    2     |  29414  |      Dark Blue       |
|      5       |   4    |        4        |    2     |  29416  |        White         |
|      5       |   4    |        3        |    2     |  29417  |      Light Blue      |
|      5       |   4    |       255       |    2     |  2281   |        Violet        |
|      8       |   4    |        0        |    2     |  29413  |    Green (29415?)    |
|      8       |   4    |        1        |    2     |  29413  | Light Green (29415?) |
|      8       |   4    |        2        |    2     |  29413  | Dark Green (29415?)  |
|      8       |   4    |        6        |    2     |  29414  |      Dark Blue       |
|      8       |   4    |        4        |    2     |  29416  |        White         |
|      8       |   4    |        3        |    2     |  29417  |      Light Blue      |
|      8       |   4    |       255       |    2     |  2281   |        Violet        |
|      5       |   6    |        0        |    0     |  29418  |     Dark (Black)     |
|      5       |   6    |        1        |    0     |  29418  |     Dark (Black)     |
|      5       |   6    |        2        |    0     |  29418  |     Dark (Black)     |
|      5       |   6    |        3        |    0     |  29419  |        White         |
|      5       |   6    |        4        |    0     |  29419  |        White         |
|      5       |   6    |        5        |    0     |  29419  |        White         |
|      5       |   6    |       12        |    0     |  29419  |        White         |
|      5       |   6    |       13        |    0     |  29419  |        White         |
|      5       |   6    |       14        |    0     |  29419  |        White         |
|      5       |   6    |        9        |    0     |  29420  |   Light Brown/Grey   |
|      5       |   6    |       10        |    0     |  29420  |   Light Brown/Grey   |
|      5       |   6    |       11        |    0     |  29420  |   Light Brown/Grey   |
|      5       |   6    |       15        |    0     |  29420  |   Light Brown/Grey   |
|      5       |   6    |       16        |    0     |  29420  |   Light Brown/Grey   |
|      5       |   6    |       17        |    0     |  29420  |   Light Brown/Grey   |
|      5       |   6    |       18        |    0     |  29421  |   Completely White   |
|      5       |   6    |       255       |    0     |  2289   |        Brown         |
|      8       |   6    |        0        |    0     |  29418  |     Dark (Black)     |
|      8       |   6    |        1        |    0     |  29418  |     Dark (Black)     |
|      8       |   6    |        2        |    0     |  29418  |     Dark (Black)     |
|      8       |   6    |        3        |    0     |  29419  |        White         |
|      8       |   6    |        4        |    0     |  29419  |        White         |
|      8       |   6    |        5        |    0     |  29419  |        White         |
|      8       |   6    |       12        |    0     |  29419  |        White         |
|      8       |   6    |       13        |    0     |  29419  |        White         |
|      8       |   6    |       14        |    0     |  29419  |        White         |
|      8       |   6    |        9        |    0     |  29420  |   Light Brown/Grey   |
|      8       |   6    |       10        |    0     |  29420  |   Light Brown/Grey   |
|      8       |   6    |       11        |    0     |  29420  |   Light Brown/Grey   |
|      8       |   6    |       15        |    0     |  29420  |   Light Brown/Grey   |
|      8       |   6    |       16        |    0     |  29420  |   Light Brown/Grey   |
|      8       |   6    |       17        |    0     |  29420  |   Light Brown/Grey   |
|      8       |   6    |       18        |    0     |  29421  |   Completely White   |
|      8       |   6    |       255       |    0     |  2289   |        Brown         |
|      5       |   6    |        0        |    1     |  29418  |     Dark (Black)     |
|      5       |   6    |        1        |    1     |  29418  |     Dark (Black)     |
|      5       |   6    |        2        |    1     |  29419  |        White         |
|      5       |   6    |        3        |    1     |  29419  |        White         |
|      5       |   6    |        6        |    1     |  29420  |   Light Brown/Grey   |
|      5       |   6    |        7        |    1     |  29420  |   Light Brown/Grey   |
|      5       |   6    |        8        |    1     |  29420  |   Light Brown/Grey   |
|      5       |   6    |        9        |    1     |  29420  |   Light Brown/Grey   |
|      5       |   6    |       10        |    1     |  29421  |   Completely White   |
|      5       |   6    |       255       |    1     |  2289   |        Brown         |
|      8       |   6    |        0        |    1     |  29418  |     Dark (Black)     |
|      8       |   6    |        1        |    1     |  29418  |     Dark (Black)     |
|      8       |   6    |        2        |    1     |  29419  |        White         |
|      8       |   6    |        3        |    1     |  29419  |        White         |
|      8       |   6    |        6        |    1     |  29420  |   Light Brown/Grey   |
|      8       |   6    |        7        |    1     |  29420  |   Light Brown/Grey   |
|      8       |   6    |        8        |    1     |  29420  |   Light Brown/Grey   |
|      8       |   6    |        9        |    1     |  29420  |   Light Brown/Grey   |
|      8       |   6    |       10        |    1     |  29421  |   Completely White   |
|      8       |   6    |       255       |    1     |  2289   |        Brown         |
|      27      |   4    |       255       |    2     |  21243  |                      |
|      27      |   6    |       255       |    2     |  21244  |                      |
|      29      |   4    |       255       |    2     |  20857  |                      |
|      29      |   6    |       255       |    2     |  20872  |                      |
