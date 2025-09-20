# ChrRaces.dbc

[`Volver a:DBC`](dbc-index)

Éste archivo DBC alberga todas las razas existentes, algunas de las cuales no son utilizadas y por ende no están disponibles para los jugadores.

**Versión 3.3.5a**

[Cómo importar datos DBC a mi base de datos](how-to-import-dbc-data-in-db)

**Estructura**

| Columna | Campo                   | Tipo         | Notas                                                                                                                           |
|---------|-------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------|
| 1       | ID                      | Integer      |                                                                                                                                 |
| 2       | [Flags](#flags)         | Integer      |                                                                                                                                 |
| 3       | FactionID               | iRefID       | Identificador (ID) de la plantilla de facción. El orden de la pantalla en la creación del personaje depende de esto.            |
| 4       | Exploration             | iRefID       | Jugó en zonas en proceso de exploración con SMSG_EXPLORATION_EXPERIENCE.                                                        |
| 5       | MaleModel               | iRefID       | Sólo es usado en la pantalla de creación/selección de personajes. El servidor establece el modelo del jugador dentro del juego. |
| 6       | FemaleModel             | iRefID       | Sólo es usado en la pantalla de creación/selección de personajes. El servidor establece el modelo del jugador dentro del juego. |
| 7       | ClientPrefix            | String       | Una forma abreviada del nombre. Usado para modelos de cascos que posean los jugadores.                                          |
| 8       | BaseLanguage            | Integer      | 1 para la Horda, 7 para la Alianza y también para No Jugable.                                                                   |
| 9       | creatureType            | iRefID       | Siempre el valor 7 (Humanoide).                                                                                                 |
| 10      | ResSicknessSpellID      | Integer      | Siempre el valor 15007.                                                                                                         |
| 11      | SplashSoundID           | Integer      | 1090 para los enanos, 1096 para los demás. Estando almacenado en CGUnit de CGUnit::PostInit.                                    |
| 12      | clientFilestring        | String       | El mismo que se utiliza en las rutas de los archivos para los modelos.                                                          |
| 13      | cinematicSequenceID     | iRefID       | Identificador (ID) usado para la cinemática de inicio.                                                                          |
| 14      | alliance                | Integer      | Facción (0 para la Alianza, 1 para la Horda, 2 equivale a No Disponible)                                                        |
| 15-30   | RaceNameNeutral         | Loc          | Nombre a mostrar.                                                                                                               |
| 31      | NameLangMask            | Integer      | Marcadores en cadena, sin uso aparente.                                                                                         |
| 32-47   | RaceNameFemale          | Loc          | Sólo si es diferente del nombre anterior, de lo contrario no es usado. Siempre apunta a NULL para zhCN.                         |
| 48      | NameFemaleLangMask      | Integer      | Marcadores en cadena, sin uso aparente.                                                                                         |
| 49-64   | RaceNameMale            | Loc          | Sólo si es diferente del nombre anterior, de lo contrario no es usado. Siempre apunta a NULL para zhCN.                         |
| 65      | NameMaleLangMask        | Integer      | Marcadores en cadena, sin uso aparente.                                                                                         |
| 66      | facialHairCustomization | String       | Nombres internos para los rasgos faciales.                                                                                      |
| 67      | facialHairCustomization | String       | Los nombres en clave se encuentran en luas.                                                                                     |
| 68      | hairCustomization       | String       | Nombre interno para las personalizaciones del cabello. Cuernos para los tauren, normal para el resto.                           |
| 69      | required_expansion      | Integer      | 0 para Classic y No Jugable, 1 para Burning Crusade                                                                             |

### Contenido

| ID | Valor    | Nombre                  |
|----|----------|-------------------------|
| 1  | 1        | Humano                  |
| 2  | 2        | Orco                    |
| 3  | 4        | Enano                   |
| 4  | 8        | Elfo de la Noche        |
| 5  | 16       | No-Muerto               |
| 6  | 32       | Tauren                  |
| 7  | 64       | Gnomo                   |
| 8  | 128      | Trol                    |
| 9  | 256      | Goblin                  |
| 10 | 512      | Elfo de Sangre          |
| 11 | 1024     | Draenei                 |
| 12 | 2048     | Orco Vil                |
| 13 | 4096     | Naga                    |
| 14 | 8192     | Tábido                  |
| 15 | 16384    | Esqueleto               |
| 16 | 32768    | Vrykul                  |
| 17 | 65536    | Tuskarr                 |
| 18 | 131072   | Trol del bosque         |
| 19 | 262144   | Taunka                  |
| 20 | 524288   | Esqueleto de Rasganorte |
| 21 | 1048576  | Trol de hielo           |

### Flags

| Marcador | Descripción        |
|----------|--------------------|
| 1        | No jugable         |
| 2        | Pies descalzos     |
| 4        | Puede usar montura |
| 8        | Es calvo (¿XD?)    |


### Valores de Facción

Sólo para la Alianza = 1101;
Sólo para la Horda = 690;
Para ambas facciones = 1791 (0 también puede funcionar);


### ¿Cómo se obtienen los valores?

Si quieres aprender acerca de cómo funcionan realmente los bits puedes leer el artículo de [Tutorial de Bits y Bytes](Bit-and_bytes-tutorial) que puede ser hallado en esta misma página.