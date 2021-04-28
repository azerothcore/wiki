# ip2nationCountries

[<-Back-to:Auth](database-auth.md)

**The \`ip2nationCountries\` table**

## Structure

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
|------------------|--------------|------------|-----|------|---------|-------|---------|
| [code][1]        | varchar(4)   |            | PRI | NO   |         |       |         |
| [iso_code_2][2]  | varchar(2)   |            |     | NO   |         |       |         |
| [iso_code_3][3]  | varchar(3)   |            |     | YES  |         |       |         |
| [iso_country][4] | varchar(255) |            |     | NO   |         |       |         |
| [country][5]     | varchar(255) |            |     | NO   |         |       |         |
| [lat][6]         | FLOAT        |            |     | NO   | 0       |       |         |
| [lon][7]         | FLOAT        |            |     | NO   | 0       |       |         |

[1]: #code
[2]: #iso_code_2
[3]: #iso_code_3
[4]: #iso_country
[5]: #country
[6]: #lat
[7]: #lon

## Description of the fields

### code

### iso_code_2

### iso_code_3

### iso_country

### country

### lat

### lon

### Example

| code | iso_code_2 | iso_code_3 | iso_country          | country              | lat   | lon    |
|------|------------|------------|----------------------|----------------------|-------|--------|
| 01   |            |            |                      | Private              | 0     | 0      |
| ad   | AD         | AND        | Andorra              | Andorra              | 42.3  | 1.3    |
| ae   | AE         | ARE        | United Arab Emirates | United Arab Emirates | 24    | 54     |
| af   | AF         | AFG        | Afghanistan          | Afghanistan          | 33    | 65     |
| ag   | AG         | ATG        | Antigua and Barbuda  | Antigua and Barbuda  | 17.03 | -61.48 |

They are not mantained by AzerothCore development team and **they require external data to perform their function**, which can be found at
[ip2nation](http://www.ip2nation.com/ip2nation/Download) or via this module [mod-ip2natioon-ip2nationcountries](https://github.com/azerothcore/mod-ip2nation-ip2nationcontries)

