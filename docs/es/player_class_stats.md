# player_class_stats

[<-Volver a:World](database-world)

**Tabla \`player_class_stats\`**

Esta tabla contiene información sobre qué valores se aplican a las estadísticas de los personajes conforme suben de nivel. Todos los valores de esta tabla representan únicamente las estadísticas base de una clase en un nivel concreto.

**Estructura**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Class][1]     | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Level][2]     | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [BaseHP][3]    | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [BaseMana][4]  | INT     | UNSIGNED   |     | NO   | 1       |       |         |
| [Strength][5]  | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Agility][6]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Stamina][7]   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Intellect][8] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Spirit][9]    | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #Class
[2]: #Level
[3]: #BaseHP
[4]: #BaseMana
[5]: #Strength
[6]: #Agility
[7]: #Stamina
[8]: #Intellect
[9]: #Spirit

**Descripción de los campos**

### Class

La clase del personaje. Este campo define qué valores aplicar a las estadísticas de un personaje. Este valor se toma de [`ChrClasses.dbc`](chrclasses).

### Level

El nivel al que deberían aplicarse las estadísticas.

### BaseHP

Los puntos de vida base que se aplican a un personaje. Se aplican antes de las bonificaciones de aguante.

### BaseMana

El maná base que se aplica a un personaje. Se aplica antes de las bonificaciones de intelecto.

### Strength

La fuerza base que se aplica a un personaje.

### Agility

La agilidad base que se aplica a un personaje.

### Stamina

El aguante base que se aplica a un personaje.

### Intellect

El intelecto base que se aplica a un personaje.

### Spirit

El espíritu base que se aplica a un personaje.

### Examples

| Class | Level | BaseHP | BaseMana | Strength | Agility | Stamina | Intellect | Spirit |
| ----- | ----- | ------ | -------- | -------- | ------- | ------- | --------- | ------ |
| 1     | 1     | 20     | 0        | 23       | 20      | 22      | 20        | 20     |
| 2     | 1     | 28     | 60       | 22       | 20      | 22      | 20        | 21     |
| 3     | 1     | 46     | 65       | 20       | 23      | 21      | 20        | 21     |
| 4     | 1     | 25     | 0        | 21       | 23      | 21      | 20        | 20     |
| 5     | 1     | 52     | 73       | 20       | 20      | 20      | 22        | 23     |
| 6     | 55    | 1359   | 0        | 108      | 73      | 99      | 29        | 42     |
| 7     | 1     | 40     | 85       | 21       | 20      | 21      | 21        | 22     |
| 8     | 1     | 32     | 100      | 20       | 20      | 20      | 23        | 22     |
| 9     | 1     | 23     | 90       | 20       | 20      | 21      | 22        | 22     |
| 11    | 1     | 44     | 60       | 21       | 20      | 20      | 22        | 22     |

**Relación con [\`player_race_stats\`](player_race_stats)**

Esta tabla por sí sola no define las estadísticas de un personaje en ningún nivel. Los valores de esta tabla se combinan con los valores de la tabla `player_race_stats` para aplicar las estadísticas finales a un personaje en cualquier nivel.

La estadística final se puede calcular así: toma la estadística base de esta tabla y súmale el modificador para esa estadística de `player_race_stats`.

Por ejemplo, un druida de nivel cuarenta tiene una fuerza base de cuarenta y seis. Combinándola con el modificador de fuerza de un elfo de la noche de menos cuatro, obtienes un valor final de cuarenta y dos.
