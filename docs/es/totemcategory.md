# TotemCategory

[`Volver a:DBC`](dbc-index)

**TotemCategory.dbc**
**Version is : 3.3.5a**

## Estructura

| Columna | Campo        | Tipo         | Notas                                                                                                 |
|---------|--------------|--------------|-------------------------------------------------------------------------------------------------------|
| 1       | ID           | Integer      |                                                                                                       |
| 2-18    | sRefName     | String + Loc | Icluye todo tipo de componentes... no sólo tótems                                                     |
| 19      | Category     | Integer      | A qué tipo de categoría pertenece la herramienta (1 para tótems, 3 para varas de encantamiento, etc.) |
| 20      | CategoryBits | BitMask      | Con cual herramienta de la categoría puede ser usada.                                                 |

### Por ejemplo, en el caso de los tótems:

| Bit | Descripción |
|-----|-------------|
| 0   | Tierra      |
| 1   | Aire        |
| 2   | Fuego       |
| 3   | Agua        |

El Tótem Maestro posée la 'Máscara de Bits' 1111b, lo que significa que éste valor puede usarse en lugar de los cuatro tótems normales ya mencionados.

## **Contenido**

| ID  | Nombre                              |
|-----|-------------------------------------|
| 1   | Cuchillo para desollar (OLD)        |
| 2   | Tótem de tierra                     |
| 3   | Tótem de aire                       |
| 4   | Tótem de fuego                      |
| 5   | Tótem de agua                       |
| 6   | Vara rúnica de cobre                |
| 7   | Vara rúnica de plata                |
| 8   | Vara rúnica de oro                  |
| 9   | Vara rúnica de veraplata            |
| 10  | Vara rúnica de arcanita             |
| 11  | Pico de minería (OLD)               |
| 12  | Piedra filosofal                    |
| 13  | Martillo de herrero (OLD)           |
| 14  | Llave de tuerca arcoluz             |
| 15  | Microajustador giromático           |
| 21  | Tótem maestro                       |
| 41  | Vara rúnica de hierro vil           |
| 62  | Vara rúnica de adamantita           |
| 63  | Vara rúnica de eternio              |
| 81  | Pluma hueca                         |
| 101 | Vara rúnica de azurita              |
| 121 | Juego de caligrafía de virtuoso     |
| 141 | Tambores                            |
| 161 | Navaja gnómica                      |
| 162 | Martillo de herrero                 |
| 165 | Pico de minería                     |
| 166 | Cuchillo para desollar              |
| 167 | Martillo pico                       |
| 168 | Hacha pico afilada                  |
| 169 | Sílex y yesca                       |
| 189 | Vara rúnica de cobalto (DO NOT USE) |
| 190 | Vara rúnica de titanio              |
