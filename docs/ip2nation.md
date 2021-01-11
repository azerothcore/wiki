# ip2nation

[<-Back-to:Auth](database-auth.md)

**The \`ip2nation\` and \`ip2nationCountries\` tables**

## Structure

| Field        | Type    | Attributes | Key | Null | Default | Extra | Comment |
|--------------|---------|------------|-----|------|---------|-------|---------|
| [ip][1]      | int(11) | unsigned   | MUL | NO   | 0       |       |         |
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

They are not mantained by TrinityCore development team and **they require external data to perform their function**, which can be found at
[ip2nation](http://www.ip2nation.com/ip2nation/Download)

NOTE IF YOU EXPORT THIS DATABASE FROM WINDOWS ENVIROMENT AND IMPORT IT ON LINUX YOU WILL HAVE STARTUP ERROR BECAUSE  **ip2nationCountries** WILL BE RENAMED TO  **ip2nationcountries** IMPORT IT AGAIN FROM IP2NATION WEBPAGE TO FIX IT.
