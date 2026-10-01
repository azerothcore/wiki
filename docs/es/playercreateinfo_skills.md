# playercreateinfo\_skills

[<-Volver a:World](database-world)

# Tabla playercreateinfo\_skills

Esta tabla contiene información sobre qué skills debería tener un personaje recién creado al empezar. Un personaje en esta tabla se define por su combinación de raza y clase.

## Estructura

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [racemask][1]  | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [classmask][2] | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [skill][3]     | SMALLINT     | UNSIGNED   | PRI | NO   |         |       |         |
| [rank][4]      | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment][5]   | VARCHAR(255) |            |     | YES  |         |       |         |

[1]: #racemask
[2]: #classmask
[3]: #spell
[4]: #rank
[5]: #comment

## Descripción de los campos

### racemask

Una o más razas del personaje. Ver [ChrRaces.dbc](chrraces).

### classmask

Una o más clases del personaje. Ver [ChrClasses.dbc](chrclasses).

### Spell

Id de skill. Ver [Skill.dbc](skillline)

### Rank

Rango de la skill.

### Comment

Una descripción de la skill.
