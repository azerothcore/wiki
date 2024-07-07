# instance\_template

[<-Back-to:World](database-world)

**The \`instance\_template\` table**

This table has all the templates for every instance. When a group enters an instance, a new copy of that instance is made from the values in these fields.

If you want to change the spot you will start in when you enter/leave an instance, go to areatrigger\_teleport

**Table Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [map][1]        | INT          | UNSIGNED   |     | NO   | NULL    |       |         |
| [parent][2]     | BIGINT       | UNSIGNED   |     | NO   | 0       |       |         |
| [script][3]     | VARCHAR(128) | SIGNED     |     | NO   | NULL    |       |         |
| [allowMount][4] | tinyiny(1)   | SIGNED     |     | NO   | 0       |       |         |

[1]: #map
[2]: #parent
[3]: #script
[4]: #allowmount

**Description of the fields**

### map

The map ID of the instance. See Maps.dbc

### parent

If the instance is a subinstance of another instance, this field has the parent instance's map ID.

### script

The name of the instance script that the instance will use and apply (if any).

### allowMount

- 0 = you can not mount inside this instance
- 1 = you can mount inside this instance
