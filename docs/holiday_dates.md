# holiday\_dates

[<-Back-to:World](database-world)

**The \`holiday\_dates\` table**

`table-no-description`

**Table Structure**

| Field            | Type    | Attribute | Key | Null | Default | Extra | Comment |
|:-----------------|---------|-----------|-----|------|---------|-------|---------|
| id               | INT     | UNSIGNED  | PRI | NO   |         |       |         |
| date_id          | TINYINT | UNSIGNED  | PRI | NO   |         |       |         |
| date_value       | INT     | UNSIGNED  |     | NO   |         |       |         |
| holiday_duration | INT     | UNSIGNED  |     | NO   | 0       |       |         |

**Description of fields:**

### id

Holiday id from Holidays.dbc

### date_id

Unique id.

### date_value

Start date in blizztime. Use [https://github.com/The-Cataclysm-Preservation-Project/Packet-BlizzTime-tool](https://github.com/The-Cataclysm-Preservation-Project/Packet-BlizzTime-tool) to get the correct value.

### holiday_duration

`field-no-description|4`
