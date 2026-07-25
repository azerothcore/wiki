# module_string

[<-Volver a:World](database-world)

**Tabla module_string**

Esta tabla contiene información de las entradas de cadenas (strings) para los módulos.

**Estructura**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment                      |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ---------------------------- |
| [module](#module) | VARCHAR(255) |            | PRI | NO   |         |       | module dir name, eg mod-cfbg |
| [id](#id)         | INT          | UNSIGNED   | PRI | NO   |         |       |                              |
| [string](#string) | TEXT         |            |     | NO   |         |       |                              |

**Descripción de los campos**

### module

Identificador del módulo

### id

Id de la cadena

### string

El texto en inglés
