# gameobject_questitem

[<-Volver a: World](database-world)

**Tabla \`gameobject_questitem\`**

**Estructura**

| Field                               | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [GameObjectEntry](#gameobjectentry) | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Idx](#idx)                         | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ItemId](#itemid)                   | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild)     | INT  | UNSIGNED   |     | YES  | NULL    |       |         |

**Descripción de los campos**

### GameObjectEntry

[gameobject_template.entry](gameobject_template#entry).

### Idx

Índice 0-3

### ItemId

[item_template.entry](item_template#entry).

### VerifiedBuild

Este campo se usaba para determinar si los datos han sido verificados a partir de archivos WDB.

Si el valor es 0, entonces aún no han sido parseados.

Si el valor es mayor que 0, entonces han sido parseados con archivos WDB de esa build de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren datos adecuados en los WDB.

Si el valor es -Client Build, entonces fue parseado con archivos WDB de esa [build de cliente](realmlist#gamebuild) específica y editado manualmente después por alguna necesidad especial.
