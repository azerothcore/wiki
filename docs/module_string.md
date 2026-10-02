# module\_string

[<-Back-to:World](database-world)

**The module_string table**

This table holds information of string entries for modules.

**Table: module\_string's Structure**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment                      |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ---------------------------- |
| [module](#module) | VARCHAR(255) |            | PRI | NO   |         |       | module dir name, eg mod-cfbg |
| [id](#id)         | INT          | UNSIGNED   | PRI | NO   |         |       |                              |
| [string](#string) | TEXT         |            |     | NO   |         |       |                              |

**Description of the table's fields**

### module

Module identifier

### id

String id

### string

The English text
