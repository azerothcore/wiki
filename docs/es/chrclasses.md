# ChrClasses.dbc

[`Volver a:DBC`](dbc-index)

Éste archivo DBC contiene todas las clases jugables existentes dentro del juego.

**Versión 3.3.5a**

### Estructura

| Columna | Nombre                                         | Tipo    | Notas                                                                                                              |
|---------|------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------|
| 1       | ID                                             | Integer |                                                                                                                    |
| 2       | Unknown                                        | Integer | 1 para Cazador, Pícaro y Chamán, 9 para Caballero de la Muerte, 0 para el resto de clases. Removido en Cataclismo. |
| 3       | PowerType                                      | Integer | 0 para Maná, 1 para Ira, 2 para Focus, 3 = Energía, 4 = Felicidad, 6 = Runas. 2 y 4 sin uso aparente.              |
| 4       | m_petNameToken                                 | String  | Tipo de mascota. 101 para los demonios del brujo, 1 para el resto de mascotas.                                     |
| 5-20    | Name                                           | Loc     | Nombre a mostrar.                                                                                                  |
| 21      | NameLangMask                                   | Integer | Marcadores en cadena, sin uso aparente.                                                                            |
| 22-37   | Name_female                                    | Loc     | En caso de llegar a ser diferente del nombre inicial, de lo contrario no tiene un uso.                             |
| 38      | NameFemaleLangMask                             | Integer | Marcadores en cadena, sin uso aparente.                                                                            |
| 39-54   | Name_male                                      | Loc     | En caso de llegar a ser diferente del nombre inicial, de lo contrario no tiene un uso.                             |
| 55      | NameMaleLangMask                               | Integer | Marcadores en cadena, sin uso aparente.                                                                            |
| 56      | fileName                                       | String  | Nombre en inglés.                                                                                                  |
| 57      | [spellClassSet](#spellclassset)                | Integer |                                                                                                                    |
| 58      | [Flags](#flags)                                | Integer | Sin un uso aparente.                                                                                               |
| 59      | Camera                                         | iRefID  | Usado para el inicio de cinemáticas de clase. 165 para el Caballero de la Muerte, 0 para el resto de clases.       |
| 60      | required_expansion                             | Integer | 0 = Classic, 1 = Burning Crusade, 3 = Wrath of The Lich King.                                                      |

### Contenido

| ID | Valor | Nombre                 |
|----|-------|------------------------|
| 1  | 1     | Guerrero               |
| 2  | 2     | Paladín                |
| 3  | 4     | Cazador                |
| 4  | 8     | Pícaro                 |
| 5  | 16    | Sacerdote              |
| 6  | 32    | Caballero de la Muerte |
| 7  | 64    | Chamán                 |
| 8  | 128   | Mago                   |
| 9  | 256   | Brujo                  |
| 11 | 1024  | Druida                 |

### 'Flags' o Marcadores

| Marcador | Descripción                                       |
|----------|---------------------------------------------------|
| 1        | Usa taparrabos (No sé si se refiera a la tela XD) |
| 2        | Clase de jugador                                  |
| 4        | Muestra la mascota                                |
| 8        | Sin uso aparente                                  |
| 16       | Puede equipar malla                               |
| 32       | Puede equipar placas                              |
| 64       | Vincula la zona de inicio                         |

### spellClassSet

| ID | Familia                | Notas                              |
|----|------------------------|------------------------------------|
| 0  | Genérico               |                                    |
| 1  | Unk1                   | Eventos, días festivos             |
| 2  | SinUso                 |                                    |
| 3  | Mago                   |                                    |
| 4  | Guerrero               |                                    |
| 5  | Brujo                  |                                    |
| 6  | Sacerdote              |                                    |
| 7  | Druida                 |                                    |
| 8  | Pícaro                 |                                    |
| 9  | Cazador                |                                    |
| 10 | Paladín                |                                    |
| 11 | Chamán                 |                                    |
| 12 | Unk2                   | Hechizos (Resistencia al Silencio) |
| 13 | Poción                 |                                    |
| 14 | SinUso                 |                                    |
| 15 | Caballero de la Muerte |                                    |
| 16 | SinUso                 |                                    |
| 17 | Mascota                |                                    |

### Descripción de los Campos

> Valor

El valor designa la 'Máscara de Bits' usada en varios lugares del núcleo del emulador y la Base de Datos (quest_template.RequiresClasses etc).

La fórmula para ello es: **Valor = 1 << (ID - 1);**