# achievement\_criteria\_data

[<-Volver a: World](database-world)

**La tabla \`achievement\_criteria\_data\`**

Esta tabla contiene la información que un jugador necesita obtener / completar para alcanzar cierto logro.

**Estructura**

| Campo            | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ---------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [criteria_id][1] | MEDIUMINT |           | PRI   | NO   |             |       |            |
| [type][2]        | TINYINT   | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [value1][3]      | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |            |
| [value2][4]      | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |            |
| [ScriptName][5]  | char(64)  |           |       | NO   |             |       |            |

[1]: #criteria_id
[2]: #type
[3]: #value1
[4]: #value2
[5]: #scriptname

**Descripción de los campos**

### criteria\_id

Esta es la ID de[Achievement\_Criteria.dbc](Achievement+Criteria).

### type

Dpendiendo de este valor, será determinado cómo son usados value1 y value2.

| Tipo | Nombre                    |
| ---- | ------------------------- |
| 0    | TYPE_NONE                 |
| 1    | TYPE_T_CREATURE           |
| 2    | TYPE_T_PLAYER_CLASS_RACE  |
| 3    | TYPE_T_PLAYER_LESS_HEALTH |
| 4    | TYPE_T_PLAYER_DEAD        |
| 5    | TYPE_S_AURA               |
| 6    | TYPE_S_AREA               |
| 7    | TYPE_T_AURA               |
| 8    | TYPE_VALUE                |
| 9    | TYPE_T_LEVEL              |
| 10   | TYPE_T_GENDER             |
| 11   | TYPE_SCRIPT               |
| 12   | TYPE_MAP_DIFFICULTY       |
| 13   | TYPE_MAP_PLAYER_COUNT     |
| 14   | TYPE_T_TEAM               |
| 15   | TYPE_S_DRUNK              |
| 16   | TYPE_HOLIDAY              |
| 17   | TYPE_BG_LOSS_TEAM_SCORE   |
| 18   | TYPE_INSTANCE_SCRIPT      |
| 19   | TYPE_S_EQUIPED_ITEM       |
| 20   | TYPE_MAP_ID               |
| 21   | TYPE_S_PLAYER_CLASS_RACE  |
| 22   | TYPE_NTH_BIRTHDAY         |
| 23   | TYPE_S_KNOWN_TITLE        |

### value1

**TYPE\_T\_CREATURE**

-   El objetivo debe ser una entrada valida de creature\_template

**TYPE\_T\_PLAYER\_CLASS\_RACE**

-   El objetivo acá es un clase valida de (paste class list). value2 debe ser establecido también.

**TYPE\_T\_PLAYER\_LESS\_HEALTH**

-   El porcentaje de salud (hp) que el objetivo debe alcanzar 

**TYPE\_T\_PLAYER\_DEAD**

-   La facción del jugador objetivo, (debe coincidir con el jugador intentando alcanzar el logro).

**TYPE\_S\_AURA**

-   La ID del hechizo que debe tener activo el jugador. value2 debe estar establecido también.

**TYPE\_S\_AREA**

-   ID de area de AreaTable.dbc

**TYPE\_T\_AURA**

-   El hechizo del aura que el objetivo debe tener. value2 debe estar establecido también.

**TYPE\_VALUE**

-   Valor de comparación necesario para alcanzar el logro. Este valor se utiliza junto con otro tipo. (Ver valor2 para el tipo de comparación) 

**TYPE\_T\_LEVEL**

-   El nivel minimo que el objetivo puede ser.

**TYPE\_T\_GENDER**

-   Género: 0=Masculino, 1=Femenino

**TYPE\_SCRIPT**

-   Usado para deshabilitar un logro si todos los requisitios no son definididos. Se usaría si no todos los requisitios son conocidos.

**TYPE\_MAP\_DIFFICULTY**

-   Dificultad del mapa: (Mazmorras)
    - Normal = 0
    - Heroic = 1
-   Dificultad del mapa: (Bandas)
    - 10 Man Normal = 0
    - 25 Man Normal = 1
    - 10 Man Heroic = 2
    - 25 Man Heroic = 3

**TYPE\_MAP\_PLAYER\_COUNT**

-   El número de otros jugadores que tienen que estar en la zona. (No es seguro si es un mínimo o un máximo).

**TYPE\_T\_TEAM**

-   El objetivo debe estar en estas facciones: Alianza = 469, Horda = 67

**TYPE\_S\_DRUNK**

-   Quétan borracho debe estar el objetivo:
    - DRUNKEN\_SOBER = 0
    - DRUNKEN\_TIPSY = 1
    - DRUNKEN\_DRUNK = 2
    - DRUNKEN\_SMASHED = 3

**TYPE\_HOLIDAY** 

-   Holiday ID de Holiday.dbc y game\_event. Tiene que ser un festivo activo.

**TYPE\_BG\_LOSS\_TEAM\_SCORE**

-   El equipo del jugador gana la BG y el equipo contrario tiene un puntaje dentro del rango // Puntaje min.

**TYPE\_INSTANCE\_SCRIPT**

-   Hace que el script de la instancia revise que los criterios se ajusten.
**TYPE\_S\_EQUIPED\_ITEM**

-   Item level

**TYPE\_MAP\_ID**

-   El jugador debe estar en mapId.

**TYPE\_S\_PLAYER\_CLASS\_RACE**

-   La fuente acá es una clase válida (paste class list). El value2 debe estar establecido también.
 
**TYPE\_NTH\_BIRTHDAY**

-   Numero de cumpleaños.

**TYPE\_S\_KNOWN\_TITLE**

-   El valor acá es un titleId válido. Veáse: CharTitles.dbc

### value2

**TYPE\_T\_PLAYER\_CLASS\_RACE**
**TYPE\_S\_PLAYER\_CLASS\_RACE**

-   El valor acá es un ID válidod de raza. Véase ChrRaces.dbc

**TYPE\_S\_AURA**

-   Effect Index del aura

**TYPE\_T\_AURA**

-   Effect Index del aura

**TYPE\_BG\_LOSS\_TEAM\_SCORE**

-   Max. puntaje

**TYPE\_S\_EQUIPED\_ITEM**

-   Calidad del item

**TYPE\_VALUE**

| ComparisationType        |
| ------------------------ |
| COMP\_TYPE\_EQ = 0       |
| COMP\_TYPE\_HIGH = 1     |
| COMP\_TYPE\_LOW = 2      |
| COMP\_TYPE\_HIGH\_EQ = 3 |
| COMP\_TYPE\_LOW\_EQ = 4  |

### ScriptName

EL nombre del script (ScriptName) para cuando se haga scripting en el core.
Esto quiza sea 'SmartTrigger'. Usaría  [SmartAI](smart_scripts) entonces.
