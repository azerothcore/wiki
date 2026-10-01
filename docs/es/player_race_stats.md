# player\_race\_stats

[<-Volver a:World](database-world)

**Tabla \`player\_race\_stats\`**

Esta tabla contiene información sobre los modificadores de los valores de estadísticas que se aplican a los personajes. Todos los valores de esta tabla representan únicamente los modificadores del valor de estadística basados en la raza de un personaje.

**Estructura**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Race][1]      | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Strength][2]  | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Agility][3]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Stamina][4]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Intellect][5] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Spirit][6]    | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #Race
[2]: #Strength
[3]: #Agility
[4]: #Stamina
[5]: #Intellect
[6]: #Spirit

**Descripción de los campos**

### Race

La raza del personaje. Este campo define qué valores aplicar a las estadísticas de un personaje. Este valor se toma de [`ChrRaces.dbc`](chrraces).

### Strength

El modificador de fuerza que se aplica a la estadística base de un personaje.

### Agility

El modificador de agilidad que se aplica a la estadística base de un personaje.

### Stamina

El modificador de aguante que se aplica a la estadística base de un personaje.

### Intellect

El modificador de intelecto que se aplica a la estadística base de un personaje.

### Spirit

El modificador de espíritu que se aplica a la estadística base de un personaje.

**Relación con [\`player\_class\_stats\`](player_class_stats)**

Esta tabla por sí sola no define las estadísticas de un personaje. Los valores de esta tabla se combinan con los valores de la tabla `player\_class\_stats` para aplicar las estadísticas finales a un personaje en cualquier nivel.

La estadística final se puede calcular así: toma la estadística base de `player\_class\_stats` y súmale el modificador para esa estadística de esta tabla.

Por ejemplo, un druida de nivel cuarenta tiene una fuerza base de cuarenta y seis. Combinándola con el modificador de fuerza de un elfo de la noche de menos cuatro, obtienes un valor final de cuarenta y dos.
