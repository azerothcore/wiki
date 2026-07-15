# quest_greeting_locale

[<-Volver a: World](database-world)

**Tabla \`quest_greeting_locale\`**

Esta tabla añade un comportamiento de saludo (greeting) a un NPC o un Gameobject.

**Estructura**

| Field              | Type       | Attributes | Key | NULL | Default | Comment |
| ------------------ | ---------- | ---------- | --- | ---- | ------- | ------- |
| [ID][1]            | MEDIUMINT  | UNSIGNED   | Yes | NO   | 0       |         |
| [Type][2]          | TINYINT    | UNSIGNED   | Yes | NO   | 0       |         |
| [locale][3]        | VARCHAR(4) |            | NO  | NO   |         |         |
| [Greeting][5]      | TEXT       |            | NO  | YES  | NULL    |         |
| [VerifiedBuild][6] | SMALLINT   | SIGNED     | NO  | NO   | 0       |         |

[1]: #id
[2]: #type
[3]: #greetemotetype
[4]: #greetemotedelay
[5]: #greeting
[6]: #verifiedbuild

**Descripción de los campos:**

### ID

ID único ([creature_template.entry](creature_template#entry) o [gameobject\_template.entry](gameobject_template#entry))

### Type

-   0=Creature (el ID apunta a creature\_template.entry)
-   1=GameObject (el ID apunta a gameobject\_template.entry)

### locale

Locale del cliente

### Greeting

Texto a mostrar

### VerifiedBuild

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB.

- Si el valor es 0, entonces aún no ha sido parseada.
- Si el valor es mayor que 0, entonces ha sido parseada con archivos WDB de esa build de cliente específica.
- Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren datos adecuados en los WDB.
- Si el valor es -Client Build, entonces fue parseada con archivos WDB de esa build de cliente específica y editada manualmente después por alguna necesidad especial.
