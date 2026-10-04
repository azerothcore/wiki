# warden\_checks

[<-Back-to:World](database-world)

**The \`warden\_checks\` table**

This table contains data related to the use of the anti-cheat tool Warden, which can be enabled in Worldserver.conf

**Table: warden\_checks's Structure**

| Field               | Type         |          | Null | Key | Default | Extra          | Comment                                   |
| :------------------ | :----------- | :------- | :--: | :-: | :-----: | :------------: | :---------------------------------------- |
| [id](#id)           | SMALLINT     | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT | Unique ID, automatically incremented by 1 |
| [type](#type)       | TINYINT      | UNSIGNED | YES  |     | NULL    |                |                                           |
| [data](#data)       | VARCHAR(48)  |          | YES  |     | NULL    |                |                                           |
| [str](#str)         | VARCHAR(170) |          | YES  |     | NULL    |                |                                           |
| [address](#address) | INT          | UNSIGNED | YES  |     | NULL    |                |                                           |
| [length](#length)   | TINYINT      | UNSIGNED | YES  |     | NULL    |                |                                           |
| [result](#result)   | VARCHAR(24)  |          | YES  |     | NULL    |                |                                           |
| [comment](#comment) | VARCHAR(50)  |          | YES  |     | NULL    |                |                                           |

**Description of the table's fields**

### id

Unique ID, automatically incremented by 1

### type

| Value | Check          | Description                                          |
| ----- | -------------- | ---------------------------------------------------- |
| 87    | TIMING_CHECK   | Checks that the tick count function is not detoured. |
| 113   | DRIVER_CHECK   | Checks that a driver is not loaded.                  |
| 126   | PROC_CHECK     | Checks that a function is not detoured.              |
| 139   | LUA_EVAL_CHECK | Runs a Lua check in the client.                      |
| 152   | MPQ_CHECK      | Checks that an MPQ file is not modified.             |
| 178   | PAGE_CHECK_A   | Scans all memory pages for a hash.                   |
| 191   | PAGE_CHECK_B   | Scans the memory pages of modules for a hash.        |
| 217   | MODULE_CHECK   | Checks that a module is not injected.                |
| 243   | MEM_CHECK      | Checks that a piece of memory is not modified.       |

### data

Data for the check as a hex string, for example the seed and hash of a page or module check.

### str

String for the check, for example the module, file or driver name, or the Lua code.

### address

Memory address the check reads from.

### length

Number of bytes the check reads.

### result

The expected result as a hex string. The check fails if the client returns something else.

### comment

A description of the check.
