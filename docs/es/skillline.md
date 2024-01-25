# SkillLine

[`Volver a:DBC`](dbc-index.md)

**SkillLine.dbc**

Éste archivo DBC alberga todas las habilidades existentes dentro del juego.

**Versión 3.3.5a**

## Estructura

| Columna | Campo                    | Tipo         | Notas              |
|---------|--------------------------|--------------|--------------------|
| 1       | ID                       | Integer      |                    |
| 2       | iRefID_SkillLineCategory | Integer      |                    |
| 3       | skillCostID              | Integer      |                    |
| 4       | sRefName                 | String + Loc |                    |
| 5       | description              | String + Loc |                    |
| 6       | iRefID_SpellIcon         | Integer      |                    |
| 7       | verb                     | String + Loc |                    |
| 8       | canLink                  | Integer      | Prof. con recetas  |

## **Contenido**

| ID  | CategoryId* | SkillCostId (ID del coste de aprendizaje de Habilidad) | Nombre                            | SpellIcon (Ícono de hechizo) | AltVerb     | CanLink |
|-----|-------------|--------------------------------------------------------|-----------------------------------|------------------------------|-------------|---------|
| 6   | 7           | 0                                                      | Escarcha                          | 188                          |             | 0       |
| 8   | 7           | 0                                                      | Fuego                             | 183                          |             | 0       |
| 26  | 7           | 0                                                      | Armas                             | 514                          |             | 0       |
| 38  | 7           | 0                                                      | Combate                           | 243                          |             | 0       |
| 39  | 7           | 0                                                      | Sutileza                          | 250                          |             | 0       |
| 43  | 6           | 0                                                      | Espadas                           | 1                            |             | 0       |
| 44  | 6           | 0                                                      | Hachas                            | 1                            |             | 0       |
| 45  | 6           | 0                                                      | Arcos                             | 1                            |             | 0       |
| 46  | 6           | 0                                                      | Armas de fuego                    | 1                            |             | 0       |
| 50  | 7           | 0                                                      | Dominio de bestias                | 255                          |             | 0       |
| 51  | 7           | 0                                                      | Supervivencia                     | 257                          |             | 0       |
| 54  | 6           | 0                                                      | Mazas                             | 1                            |             | 0       |
| 55  | 6           | 0                                                      | Espadas de dos manos              | 1                            |             | 0       |
| 56  | 7           | 0                                                      | Sagrado                           | 70                           |             | 0       |
| 78  | 7           | 0                                                      | Magia sombría                     | 234                          |             | 0       |
| 95  | 6           | 0                                                      | Defensa                           | 1                            |             | 0       |
| 98  | 10          | 0                                                      | Idioma: común                     | 1                            |             | 0       |
| 101 | 9           | 0                                                      | Racial enano                      | 1                            |             | 0       |
| 109 | 10          | 0                                                      | Idioma: orco                      | 1                            |             | 0       |
| 111 | 10          | 0                                                      | Idioma: enánico                   | 1                            |             | 0       |
| 113 | 10          | 0                                                      | Idioma: darnassiano               | 1                            |             | 0       |
| 115 | 10          | 0                                                      | Idioma: taurahe                   | 1                            |             | 0       |
| 118 | 6           | 0                                                      | Doble empuñadura                  | 1                            |             | 0       |
| 124 | 9           | 0                                                      | Racial tauren                     | 1                            |             | 0       |
| 125 | 9           | 0                                                      | Racial orco                       | 1                            |             | 0       |
| 126 | 9           | 0                                                      | Racial elfo de la noche           | 1                            |             | 0       |
| 129 | 9           | 0                                                      | Primeros auxilios                 | 504                          |             | 1       |
| 134 | 7           | 0                                                      | Combate feral                     | 107                          |             | 0       |
| 136 | 6           | 0                                                      | Bastones                          | 1                            |             | 0       |
| 137 | 10          | 0                                                      | Idioma: thalassiano               | 1                            |             | 0       |
| 138 | 10          | 0                                                      | Idioma: dracónico                 | 1                            |             | 0       |
| 139 | 10          | 0                                                      | Idioma: demoníaco                 | 1                            |             | 0       |
| 140 | 10          | 0                                                      | Idioma: titánico                  | 1                            |             | 0       |
| 141 | 10          | 0                                                      | Idioma: lengua antigua            | 1                            |             | 0       |
| 142 | 9           | 0                                                      | Supervivencia                     | 1                            |             | 0       |
| 148 | 9           | 0                                                      | Montar caballos                   | 1                            |             | 0       |
| 149 | 9           | 0                                                      | Montar lobos                      | 1                            |             | 0       |
| 150 | 9           | 0                                                      | Montar tigres                     | 1                            |             | 0       |
| 152 | 9           | 0                                                      | Montar carneros                   | 1                            |             | 0       |
| 155 | 9           | 0                                                      | Nadar                             | 1                            |             | 0       |
| 160 | 6           | 0                                                      | Mazas de dos manos                | 1                            |             | 0       |
| 162 | 6           | 0                                                      | Sin armas                         | 1                            |             | 0       |
| 163 | 7           | 0                                                      | Puntería                          | 126                          |             | 0       |
| 164 | 11          | 0                                                      | Herrería                          | 335                          | Transformar | 1       |
| 165 | 11          | 0                                                      | Peletería                         | 346                          | Remachar    | 1       |
| 171 | 11          | 0                                                      | Alquimia                          | 339                          | Rellenar    | 1       |
| 172 | 6           | 0                                                      | Hachas de dos manos               | 1                            |             | 0       |
| 173 | 6           | 0                                                      | Dagas                             | 1                            |             | 0       |
| 176 | 6           | 0                                                      | Armas arrojadizas                 | 1                            |             | 0       |
| 182 | 11          | 0                                                      | Herboristería                     | 345                          |             | 0       |
| 183 | 12          | 0                                                      | COMÚN (DND)                       | 1                            |             | 0       |
| 184 | 7           | 0                                                      | Reprensión                        | 555                          |             | 0       |
| 185 | 9           | 0                                                      | Cocina                            | 1467                         |             | 1       |
| 186 | 11          | 0                                                      | Minería                           | 2418                         |             | 0       |
| 188 | 7           | 0                                                      | Mascota: diablillo                | 1                            |             | 0       |
| 189 | 7           | 0                                                      | Mascota: manáfago                 | 1                            |             | 0       |
| 197 | 11          | 0                                                      | Sastrería                         | 341                          | Bordar      | 1       |
| 202 | 11          | 0                                                      | Ingeniería                        | 333                          | Componer    | 1       |
| 203 | 7           | 0                                                      | Mascota: araña                    | 1                            |             | 0       |
| 204 | 7           | 0                                                      | Mascota: abisario                 | 1                            |             | 0       |
| 205 | 7           | 0                                                      | Mascota: súcubo                   | 1                            |             | 0       |
| 206 | 7           | 0                                                      | Mascota: infernal                 | 1                            |             | 0       |
| 207 | 7           | 0                                                      | Mascota: guardia apocalíptico     | 1                            |             | 0       |
| 208 | 7           | 0                                                      | Mascota: lobo                     | 1                            |             | 0       |
| 209 | 7           | 0                                                      | Mascota: felino                   | 1                            |             | 0       |
| 210 | 7           | 0                                                      | Mascota: oso                      | 1                            |             | 0       |
| 211 | 7           | 0                                                      | Mascota: jabalí                   | 1                            |             | 0       |
| 212 | 7           | 0                                                      | Mascota: crocolisco               | 1                            |             | 0       |
| 213 | 7           | 0                                                      | Mascota: carroñero                | 1                            |             | 0       |
| 214 | 7           | 0                                                      | Mascota: cangrejo                 | 1                            |             | 0       |
| 215 | 7           | 0                                                      | Mascota: gorila                   | 1                            |             | 0       |
| 217 | 7           | 0                                                      | Mascota: raptor                   | 1                            |             | 0       |
| 218 | 7           | 0                                                      | Mascota: zancudo                  | 1                            |             | 0       |
| 220 | 9           | 0                                                      | Racial: no-muerto                 | 1                            |             | 0       |
| 226 | 6           | 0                                                      | Ballestas                         | 1                            |             | 0       |
| 228 | 6           | 0                                                      | Varitas                           | 1                            |             | 0       |
| 229 | 6           | 0                                                      | Armas de asta                     | 1                            |             | 0       |
| 236 | 7           | 0                                                      | Mascota: escórpido                | 1                            |             | 0       |
| 237 | 7           | 0                                                      | Arcano                            | 125                          |             | 0       |
| 251 | 7           | 0                                                      | Mascota: tortuga                  | 1                            |             | 0       |
| 253 | 7           | 0                                                      | Asesinato                         | 514                          |             | 0       |
| 256 | 7           | 0                                                      | Furia                             | 561                          |             | 0       |
| 257 | 7           | 0                                                      | Protección                        | 276                          |             | 0       |
| 267 | 7           | 0                                                      | Protección                        | 291                          |             | 0       |
| 270 | 7           | 0                                                      | Mascota: cazador genérico         | 1                            |             | 0       |
| 293 | 8           | 0                                                      | Malla de placas                   | 1                            |             | 0       |
| 313 | 10          | 0                                                      | Idioma: gnomótico                 | 1                            |             | 0       |
| 315 | 10          | 0                                                      | Idioma: trol                      | 1                            |             | 0       |
| 333 | 11          | 0                                                      | Encantamiento                     | 578                          | Encantar    | 1       |
| 354 | 7           | 0                                                      | Demonología                       | 90                           |             | 0       |
| 355 | 7           | 0                                                      | Aflicción                         | 88                           |             | 0       |
| 356 | 9           | 0                                                      | Pesca                             | 580                          |             | 0       |
| 373 | 7           | 0                                                      | Mejora                            | 19                           |             | 0       |
| 374 | 7           | 0                                                      | Restauración                      | 13                           |             | 0       |
| 375 | 7           | 0                                                      | Combate elemental                 | 62                           |             | 0       |
| 393 | 11          | 0                                                      | Desollar                          | 1                            |             | 0       |
| 413 | 8           | 0                                                      | Malla                             | 1                            |             | 0       |
| 414 | 8           | 0                                                      | Cuero                             | 1                            |             | 0       |
| 415 | 8           | 0                                                      | Tela                              | 1                            |             | 0       |
| 433 | 8           | 0                                                      | Escudo                            | 1                            |             | 0       |
| 473 | 6           | 0                                                      | Armas de puño                     | 1                            |             | 0       |
| 533 | 9           | 0                                                      | Montar raptor                     | 1                            |             | 0       |
| 553 | 9           | 0                                                      | Montar mecazancudos               | 1                            |             | 0       |
| 554 | 9           | 0                                                      | Equitación para no-muertos        | 1                            |             | 0       |
| 573 | 7           | 0                                                      | Restauración                      | 962                          |             | 0       |
| 574 | 7           | 0                                                      | Equilibrio                        | 225                          |             | 0       |
| 593 | 7           | 0                                                      | Destrucción                       | 547                          |             | 0       |
| 594 | 7           | 0                                                      | Sagrado                           | 70                           |             | 0       |
| 613 | 7           | 0                                                      | Disciplina                        | 685                          |             | 0       |
| 633 | 7           | 0                                                      | Ganzúa                            | 1                            |             | 0       |
| 653 | 7           | 0                                                      | Mascota: murciélago               | 1                            |             | 0       |
| 654 | 7           | 0                                                      | Mascota: hiena                    | 1                            |             | 0       |
| 655 | 7           | 0                                                      | Mascota: ave rapaz                | 1                            |             | 0       |
| 656 | 7           | 0                                                      | Mascota: serpiente alada          | 1                            |             | 0       |
| 673 | 10          | 0                                                      | Idioma: viscerálico               | 1                            |             | 0       |
| 713 | 9           | 0                                                      | Montar kodos                      | 317                          |             | 0       |
| 733 | 9           | 0                                                      | Racial: trol                      | 0                            |             | 0       |
| 753 | 9           | 0                                                      | Racial: gnomo                     | 0                            |             | 0       |
| 754 | 9           | 0                                                      | Racial: humano                    | 0                            |             | 0       |
| 755 | 11          | 0                                                      | Joyería                           | 1768                         | Transformar | 1       |
| 756 | 9           | 0                                                      | Racial elfo de sangre             | 0                            |             | 0       |
| 758 | -1          | 0                                                      | Mascota - Evento - Control remoto | 0                            |             | 0       |
| 759 | 10          | 0                                                      | Idioma: draenei                   | 0                            |             | 0       |
| 760 | 9           | 0                                                      | Racial draenei                    | 0                            |             | 0       |
| 761 | 7           | 0                                                      | Mascota: guardia vil              | 0                            |             | 0       |
| 762 | 9           | 0                                                      | Equitación                        | 255                          |             | 0       |
| 763 | 7           | 0                                                      | Mascota: dracohalcón              | 1530                         |             | 0       |
| 764 | 7           | 0                                                      | Mascota: raya abisal              | 1577                         |             | 0       |
| 765 | 7           | 0                                                      | Mascota: esporiélago              | 2033                         |             | 0       |
| 766 | 7           | 0                                                      | Mascota: acechador de distorsión  | 1952                         |             | 0       |
| 767 | 7           | 0                                                      | Mascota: devastador               | 1585                         |             | 0       |
| 768 | 7           | 0                                                      | Mascota: serpiente                | 2167                         |             | 0       |
| 769 | 7           | 22                                                     | Interno                           | 1775                         |             | 0       |
| 770 | 7           | 0                                                      | Sangre                            | 2636                         |             | 0       |
| 771 | 7           | 0                                                      | Escarcha                          | 2632                         |             | 0       |
| 772 | 7           | 0                                                      | Profano                           | 2633                         |             | 0       |
| 773 | 11          | 0                                                      | Inscripción                       | 3267                         | Inscribir   | 1       |
| 775 | 7           | 0                                                      | Mascota: palomilla                | 0                            |             | 0       |
| 776 | 7           | 0                                                      | Forja de runas                    | 2727                         | Grabar      | 0       |
| 777 | 7           | 0                                                      | Monturas                          | 2224                         |             | 0       |
| 778 | 7           | 0                                                      | Compañeros                        | 0                            |             | 0       |
| 780 | 7           | 0                                                      | Mascota: quimera exótica          | 0                            |             | 0       |
| 781 | 7           | 0                                                      | Mascota: demosaurio exótico       | 0                            |             | 0       |
| 782 | 7           | 0                                                      | Mascota: necrófago                | 221                          |             | 0       |
| 783 | 7           | 0                                                      | Mascota: silítido exótico         | 0                            |             | 0       |
| 784 | 7           | 0                                                      | Mascota: gusano exótico           | 0                            |             | 0       |
| 785 | 7           | 0                                                      | Mascota: avispa                   | 0                            |             | 0       |
| 786 | 7           | 0                                                      | Mascota: rinoceronte exótico      | 0                            |             | 0       |
| 787 | 7           | 0                                                      | Mascota: can del Núcleo exótico   | 0                            |             | 0       |
| 788 | 5           | 0                                                      | Mascota: bestia espíritu exótica  | 0                            |             | 0       |

## CategoryId

Este campo es tomado del archivo SkillLineCategory.dbc

El contenido que se encuentra almacenado allí es el siguiente:

| Category Id | Nombre                                                                      |
|-------------|-----------------------------------------------------------------------------|
| 5           | Atributos                                                                   |
| 6           | Habilidades de armas                                                        |
| 7           | Habilidades de Clase                                                        |
| 8           | Habilidades de armadura (Capacidad de equipamiento de material de armadura) |
| 9           | Habilidades secundarias                                                     |
| 10          | Idiomas                                                                     |
| 11          | Profesiones                                                                 |
| 12          | No se visualiza dentro del juego                                            |
