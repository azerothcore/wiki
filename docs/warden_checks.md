# warden\_checks

 

**Table: warden\_checks**

This table contains data related to the use of the anti-cheat tool Warden, which can be enabled in Worldserver.conf

 

| Field                             | Type        | Attributes        | Key | NULL | Default         | Comment                                   |
|-----------------------------------|-------------|-------------------|-----|------|-----------------|-------------------------------------------|
| [id](#warden_checks-id)           | SMALLINT | UNSIGNED          | PRI | NO   | auto\_increment | Unique ID, automatically incremented by 1 |
| [type](#warden_checks-type)       | TINYINT  | UNSIGNED          |     | YES  | NULL            |                                           |
| [data](#warden_checks-data)       | VARCHAR(48) | utf8\_general\_ci |     | YES  | NULL            |                                           |
| [str](#warden_checks-str)         | VARCHAR(20) | utf8\_general\_ci |     | YES  | NULL            |                                           |
| [address](#warden_checks-address) | INT     | UNSIGNED          |     | YES  | NULL            |                                           |
| [length](#warden_checks-length)   | TINYINT  | UNSIGNED          |     | YES  | NULL            |                                           |
| [result](#warden_checks-result)   | VARCHAR(24) | utf8\_general\_ci |     | YES  | NULL            |                                           |
| [comment](#warden_checks-comment) | VARCHAR(50) | utf8\_general\_ci |     | YES  | NULL            |                                           |

 

**Description of the fields:**

 

### id

Unique ID, automatically incremented by 1

### type

(ToDo: insert useful description here)

### data

(ToDo: insert useful description here)

### str

(ToDo: insert useful description here)

### address

(ToDo: insert useful description here)

### length

(ToDo: insert useful description here)

### result

(ToDo: insert useful description here)

### comment

(ToDo: insert useful description here)

 
