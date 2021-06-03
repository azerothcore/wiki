# ip2nation

[<-Back-to:Auth](database-auth.md)

**The \`ip2nation\` and \`ip2nationCountries\` tables**

## Structure

| Field        | Type    | Attributes | Key | Null | Default | Extra | Comment |
|--------------|---------|------------|-----|------|---------|-------|---------|
| [ip][1]      | INT | UNSIGNED   | MUL | NO   | 0       |       |         |
| [country][2] | char(2) |            |     | NO   |         |       |         |

[1]: #ip
[2]: #country

# Description of the fields

### ip

### country

### Example

| ip        | country |
|-----------|---------|
| 0         | us      |
| 687865856 | za      |
| 689963008 | eg      |
| 691011584 | za      |
| 691617792 | zw      |
| 691621888 | lr      |

These tables allow to see approximately which country a player might be from when doing **.pinfo <player>** command.

They are not mantained by AzerothCore development team and **they require external data to perform their function**, which can be found at
[ip2nation](http://www.ip2nation.com/ip2nation/Download) or via this module [mod-ip2natioon-ip2nationcountries](https://github.com/azerothcore/mod-ip2nation-ip2nationcontries)
