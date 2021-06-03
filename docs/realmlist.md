# realmlist

[<-Back-to:Auth](database-auth.md)

**The \`realmlist\` table**

This table sets up information on all available realms. Each row controls a different realm.

**Structure**

| Field                      | Type         | Attributes | Key | Null | Default       | Extra          | Comment |
|----------------------------|--------------|------------|-----|------|---------------|----------------|---------|
| [id][1]                    | INT      | UNSIGNED   | PRI | NO   |               | AUTO_INCREMENT |         |
| [name][2]                  | VARCHAR(32)  |            | UNI | NO   |               |                |         |
| [address][3]               | VARCHAR(255) |            |     | NO   | 127.0.0.1     |                |         |
| [localAddress][4]          | VARCHAR(255) |            |     | NO   | 127.0.0.1     |                |         |
| [localSubnetMask][5]       | VARCHAR(255) |            |     | NO   | 255.255.255.0 |                |         |
| [port][6]                  | SMALLINT  | UNSIGNED   |     | NO   | 8085          |                |         |
| [icon][7]                  | TINYINT   | UNSIGNED   |     | NO   | 0             |                |         |
| [flag][8]                  | TINYINT   | UNSIGNED   |     | NO   | 2             |                |         |
| [timezone][9]              | TINYINT   | UNSIGNED   |     | NO   | 0             |                |         |
| [allowedSecurityLevel][10] | TINYINT   | UNSIGNED   |     | NO   | 0             |                |         |
| [population][11]           | FLOAT        | UNSIGNED   |     | NO   | 0             |                |         |
| [gamebuild][12]            | INT      | UNSIGNED   |     | NO   | 12340         |                |         |

[1]: #id
[2]: #name
[3]: #address
[4]: #localaddress
[5]: #port
[6]: #icon
[7]: #flag
[8]: #timezone
[9]: #allowedsecuritylevel
[10]: #population
[11]: #gamebuild

**Description of the fields**

### id

The realm ID. This number is unique for every realm and it MUST correlate with the RealmID configuration value in worldserver.conf.

Value must be >=0. If the value does not meet the condition the SQL will fail on `realmlist_chk_1`.

### name

The name of the realm. This will appear in the realm selection list as well as in the character selection screen.

### address

The public (WAN) or LAN IP address of the world server. Use 127.0.0.1 in this field if only you is connecting to the server (and it runs on the same machine as your client).

Alternatively you can use a domain name like *example.com.*

### localAddress

Mostly 127.0.0.1

### port

The port that the world server is running on. If all world servers are on the same machine, they will all need to use a different port.

### icon

The icon of the realm.

| Icon | Type   |
|------|--------|
| 0    | Normal |
| 1    | PvP    |
| 4    | Normal |
| 6    | RP     |
| 8    | RP PvP |

### flag

Realmflag of this realm.

| Flag | Hex value | Description  |
|------|-----------|--------------|
| 0    | 0x0       | None         |
| 1    | 0x1       | Invalid      |
| 2    | 0x2       | Offline      |
| 4    | 0x4       | SpecifyBuild |
| 8    | 0x8       | Medium       |
| 16   | 0xF       | Medium       |
| 32   | 0x10      | New Players  |
| 64   | 0x20      | Recommended  |
| 128  | 0x40      | Full         |

### timezone

The realm timezone, it will be displayed in the tabs of the realmlist

| timezone | displayed name     |
|----------|--------------------|
| 1        | Development        |
| 2        | United States      |
| 3        | Oceanic            |
| 4        | Latin America      |
| 5        | Tournament         |
| 6        | Korea              |
| 7        | Tournament         |
| 8        | English            |
| 9        | German             |
| 10       | French             |
| 11       | Spanish            |
| 12       | Russian            |
| 13       | Tournament         |
| 14       | Taiwan             |
| 15       | Tournament         |
| 16       | China              |
| 17       | CN1                |
| 18       | CN2                |
| 19       | CN3                |
| 20       | CN4                |
| 21       | CN5                |
| 22       | CN6                |
| 23       | CN7                |
| 24       | CN8                |
| 25       | Tournament         |
| 26       | Test Server        |
| 27       | Tournament         |
| 29       | CN9                |
| 30       | Test Server 2      |
| 31       | CN10               |
| 32       | CTC                |
| 33       | CNC                |
| 34       | CN1/4              |
| 35       | CN/2/6/9           |
| 36       | CN3/7              |
| 37       | Russian Tournament |
| 38       | CN5/8              |
| 39       | CN11               |
| 40       | CN12               |
| 41       | CN13               |
| 42       | CN14               |
| 43       | CN15               |
| 44       | CN16               |
| 45       | CN17               |
| 46       | CN18               |
| 47       | CN19               |
| 48       | CN20               |
| 49       | Brazil             |
| 50       | Italian            |
| 51       | Hyrule             |
| 52       | QA2 Test           |
| 53       |                    |
| 54       |                    |
| 55       | Recommended Realm  |
| 56       | Test               |
| 57       | Recommended Realm  |
| 58       |                    |
| 59       | Future Test        |

### allowedSecurityLevel

The minimum account gmlevel required for accounts to log in to this realm. Changing this value will automatically update the visible in-game realm list, but the Worldserver must be restarted for it to truly take effect.

### population

This field is automatically updated at regular intervals and will have the current population. The formula to calculate the value in this field is: playerCount / maxPlayerCount \* 2. In the realm list in-game, the thresholds for low, medium, and high population are 0.5, 1.0, and 2.0 respectively.

### gamebuild

Accepted Client version for the realm.

| Build Version | Client Patch |
|---------------|--------------|
| 5875          | 1.12.1       |
| 6005          | 1.12.2       |
| 8606          | 2.4.3        |
| 9947          | 3.1.3        |
| 10146         | 3.2.0        |
| 10505         | 3.2.2a       |
| 10571         | 3.3.0        |
| 11159         | 3.3.0a       |
| 11403         | 3.3.2        |
| 11623         | 3.3.3        |
| 11723         | 3.3.3a       |
| 12340         | 3.3.5a       |
