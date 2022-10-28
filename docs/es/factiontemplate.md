# FactionTemplate

[`Volver a:DBC`](dbc-index.md)

Éste archivo DBC alberga información acerca de todas las facciones individuales existentes dentro del juego. Una ID (Identificador Único) de una facción cualquiera dentro del propio archivo contiene todos los datos necesarios para calcular la hostilidad, amistad o neutralidad hacia cualquier otra facción.

**IMPORTANTE: Los valores a continuación sólo tienen un uso particular para las tablas [creature_template](creature_template) y [gameobject_template](gameobject_template).**

**Versión 3.3.5a**

## **Estructura**

| Nº Campo | Nombre                                   | Tipo             |
|----------|------------------------------------------|------------------|
| 1        | ID                                       | Int              |
| 2        | Name (Ref to [Faction.dbc](Faction.dbc)) | Int              |
| 4        | ourMask                                  | Bitmask (4 bits) |
| 5        | friendlyMask                             | Bitmask (4 bits) |
| 6        | hostileMask                              | Bitmask (4 bits) |
| 7-10     | enemyFactions                            | Int              |
| 11-14    | friendFactions                           | Int              |

# **Explicaciones y cálculos**

Cada Identificador (ID) distinto entre sí posee diferentes relaciones hacia cualquier otra facción.

El cálculo más sencillo a la hora de contabilizar la hostilidad o amistad es fijarse directamente en las columnas de 'facciones amistosas' y/o 'facciones enemigas'. Por ejemplo, en caso de que nuestra facción a checar tenga una ID proveniente de otra facción en la lista de 'facciones enemigas', entonces por inducción básica es hostil a la misma (como mínimo). De igual forma aplica al nivel de amistad en la columna 'facciones Amistosas' respectivamente.

En caso de que una facción en particular no tenga una ID de otra facción distinta en cualquiera de las dos columnas mencionadas, entonces nos complicaríamos bastante a la hora de calcular la hostilidad o la amabilidad de la misma.

Primero que todo, definamos los cuatro grupos de facciones:

| ID | Bit | Nombre                                              |
|----|-----|-----------------------------------------------------|
| 0  | 1   | Todos los jugadores (y sus mascotas)                |
| 1  | 2   | Jugadores de la Alianza (y sus mascotas)            |
| 2  | 4   | Jugadores de la Horda (y sus mascotas)              |
| 3  | 8   | Monstruo (al no ser un jugador, no posee mascotas)  |

La primera máscara (ourMask) define con qué tipo de facción estamos tratando. Por ejemplo, la facción 1 (JUGADOR, Humano) tiene el valor número 3 como ourMask; quiere decir que tiene los dos primeros bits configurados, por lo cual se clasifica tanto como para 'Todos los jugadores' al igual que los 'Jugadores de la Alianza'.

La segunda máscara (friendlyMask) define con qué grupos de facciones es amistosa. Esto significa que si este campo contiene el bit de un grupo de facción, entonces es amistoso con esta facción. Por ejemplo, la facción 5 (PLAYER, No-Muerto) tiene el valor número 4 catalogado como friendlyMask; quiere decir que posee el tercer bit establecido, por lo cual es amistoso con los "jugadores de la Horda".

La tercera máscara (hostileMask) define con qué grupos de facciones es hostil. Esta facción será hostil con cualquier tipo de facción cuyo bit esté activado en este campo. Por ejemplo, miremos las dos primeras facciones de Ventormenta. La primera (facción 11) tiene como hostileMask el valor 12. La representación binaria de esto es 1100, con los bits tercero y cuarto ya establecidos. La segunda facción de Ventormenta (facción 12) tiene como hostileMask el valor 4. La representación binaria de esta es 0100, con el tercer bit activado respectivamente. Aplicando las fórmulas en ambos valores, podremos ver que la facción 11 es hostil a los jugadores de la Horda y también a cualquier cosa que no sea un jugador, mientras que la facción 12 sólo es hostil a los jugadores de la Horda. La facción 12 no atacará a ninguna criatura que haga parte de la facción de los monstruos.

Para aquellas personas más familiarizadas con las matemáticas, la fórmula básica para comprobar la amabilidad es la siguiente:

``` cpp
(friendlyMask & other.ourMask) != 0 
```
...en donde la otra es una facción diferente. Lo mismo ocurre con la hostilidad:

``` cpp
(hostileMask & other.ourMask) != 0
```

Para aquellos no tan inclinados por las matemáticas, tendremos que comparar dos números binarios. 
Primero, tendrías que convertir todas las 'máscaras de bits' a la forma binaria con cuatro dígitos; así que el número 1 se convierte en 0001, el 2 en 0010, el 3 en 0011, etc.

Segundo, alinear el valor de 'friendlyMask' u 'hostileMask' con el valor de 'ourMask'. Por ejemplo:

``` cpp
     1100 //hostileMask of faction 11
     1000 //ourMask of faction 14
```

Ahora, realiza un "Y" (AND) lógico en ambos valores, el de abajo junto con el de arriba y luego simplemente sigue estas reglas:

-   1 and 1 is 1
-   1 and 0 is 0
-   0 and 1 is 0
-   0 and 0 is 0

Continuando con nuestro ejemplo:

```
    1100
    1000
    ----
    1000
```

Por último, compruebe el resultado que logre obtener con el valor 0. Sólo '0000' da 0, por tanto cualquier otra cosa no sería igual a 0. Si el resultado **'no**' es igual a 0, entonces la facción correspondiente es hostil/amistosa con la otra facción. Sólo 0000 será igual a 0, cualquier otra cosa no será igual a 0. Si el resultado **'no**' es igual a 0, entonces la facción es hostil/amistosa hacia la otra facción. En nuestro ejemplo, está claro que no tenemos 0 (de hecho tenemos 8, sí es convertida a base 10 de nuevo), por lo que la facción 11 es hostil a la facción 14 y la atacará.

De todos los cálculos anteriores, nos damos cuenta de que en caso que 'ourMask' para una facción cualquiera sea igual a 0 (eso significa 0000), sería neutral a todo (no necesariamente amistoso). Sí friendlyMask para una facción cualquiera es 0, entonces no será amistosa con nada (a menos que poséa otros Identificador (ID) de una facción en la columna de facciones amistosas). Por último, si la tabla hostileMask de una facción cualquiera es igual a 0, nunca será hostil con nada (de nuevo puede haber excepciones en la columna de facciones enemigas de la tabla de abajo).

En resumen, debes seguir los siguientes pasos para calcular si la facción A es hostil a la facción B:

1.  Busca la facción B en la lista de facciones enemigas de la facción A en la siguiente tabla
    - Si la encuentras, entonces la facción A es hostil a la facción B
    - Si no la encuentras, continúa con los siguientes pasos:
2.  Busca hostileMask para la facción A en la tabla de abajo
3.  Busca ourMáscara para la facción B en la tabla de abajo
4.  Haz la operación 'Y' (AND ó &) sobre ambos valores
    - Si el resultado es 0, entonces la facción A no es hostil a la facción B (pero tampoco es necesariamente amistosa)
    - Si el resultado no es 0, entonces la facción A es hostil a la facción B

Ahora, éstos son los pasos para calcular si la facción A es amistosa con la facción B:

1.  Busca la facción B en la lista de facciones amistosas dentro de la facción A en la tabla siguiente
    - Si la encuentras, entonces la facción A es amistosa con la facción B
    - Si no la encuentras, continúa con los siguientes pasos:
2.  Busca friendlyMask para la facción A en la tabla de abajo
3.  Busca ourMáscara para la facción B en la tabla de abajo
4.  Haz la operación 'Y' (AND ó &) sobre ambos valores
    - Si el resultado es 0, entonces la facción A no es amistosa de la facción B (pero tampoco es necesariamente hostil)
    - Si el resultado no es 0, entonces la facción A es amistosa con la facción B

# **Contenido**

|ID|Nombre|Máscara de bits propia|Máscara de bits amistosos|Máscara de bits hostiles|Facciones enemigas|Facciones amistosas|
|------|-------------------------------------|---------|--------------|-------------|---------------------|-------------------|
1|JUGADOR, Humano|3|2|12||
2|JUGADOR, Orco|5|4|10||
3|JUGADOR, Enano|3|2|12||
4|JUGADOR, Elfo de la Noche|3|2|12||
5|JUGADOR, No-Muerto|5|4|10||
6|JUGADOR, Tauren|5|4|10||
7|Criatura|0|0|0||
10|Escolta|3|2|0||
11|Ventormenta|3|2|12||
12|Ventormenta|2|2|4||72
14|Monstruo|8|0|1||
15|Criatura|0|0|0||7
16|Monstruo|8|0|1||14
17|Hermandad Defias|8|0|1||15
18|Murloc|8|0|1||19
19|Gnoll - Crestagrana|8|0|1||17
20|Gnoll - Zarparrío|8|0|1||16
21|No-Muerto, Aparición|8|0|1||20
22|Bestia - Araña|8|0|1||22
23|Exiliados de Gnomeregan|2|2|4||
24|Ferocanis|8|0|1||24
25|Kobold|8|0|0||25
26|Kobold|8|0|1||25
27|Hermandad Defias|8|0|1|1|15
28|Troll, Sangrapellejo|8|0|1||26
29|Orgrimmar|4|4|2||
30|Troll, Machacacráneos|8|0|1||27
31|Presa|0|0|0|973|148 28
32|Bestia - Lobo|0|0|0|28|
33|Escolta|5|4|0||
34|Hermandad Defias|8|0|0||15
35|Amistoso|0|1|0||31
36|Trogg|0|0|0||32
37|Troll, Peloescarcha|8|0|1||33
38|Bestia - Lobo|8|0|1|28|29
39|Gnoll - Pielsombra|8|0|1||18
40|Orco, Roca Negra|8|0|1||34
41|Villano|8|0|1|36|35
42|Victima|1|1|0||36
43|Villano|8|0|0|36|35
44|Bestia - Oso|8|0|1||37
45|Ogro|8|0|1||38
46|Mercenarios Kurzen|8|0|1||39
47|Ventura y Cia|8|0|1||41
48|Bestia - Raptor|8|0|1||42
49|Basilisco|8|0|1||43
50|Vuelo, Verde|8|0|1||44
51|Perdidos|8|0|1|46 40|45
52|Muñeco de Gizlock|8|0|0|770|
53|Human, Ronda de Noche|2|2|12||49
54|Enanos Hierro Negro|8|0|1||48
55|Forjaz|2|2|4||47
56|Human, Ronda de Noche|2|2|12||49
57|Forjaz|3|2|12||
58|Criatura|8|0|0||
59|Trogg|8|0|1||32
60|Vuelo, Rojo|8|0|1||50
61|Gnoll - Pellejomusgo|8|0|1||51
62|Orco, Faucedraco|8|0|1|1015 932 934|52
63|Gnomo - Leproso|8|0|1||53
64|Exiliados de Gnomeregan|2|2|4||
65|Orgrimmar|0|0|0|45|76
66|Leopardo|8|0|1|28|55
67|Cruzada Escarlata|8|0|1||56
68|Entrañas|4|4|2||
69|Trinquete |0|0|0||470
70|Gnoll - Putrepellejo|8|0|1||57
71|Entrañas|5|4|10||
72|Bestia - Gorilla|8|0|1||58
73|Bestia - Pájaro Carroñero|8|0|1||669
74|Naga|8|0|1|289|60
76|Dalaran|0|2|4||61
77|Espíritu Abandonado|8|0|0||
78|Aullido Oscuro|8|0|1||
79|Darnassus|3|2|12||
80|Darnassus|2|2|4||69
81|Grell|8|0|1||64
82|Furbolg|8|0|1||65
83|Horda Generico|4|4|2||
84|Alianza Generico|2|2|4||
85|Orgrimmar|5|4|10||
86|Gizlock's Charm|0|1|0|769|771
87|La Hermandad|8|0|1||70
88|Milicia de Trabalomas|2|2|4||71
89|Cruzada Escarlata|8|0|1|20|56
90|Demonio|8|0|1||73
91|Elemental|8|0|1||74
92|Espíritu |8|0|1||
93|Monstruo|8|0|1||
94|Tesoro|0|8|0||
95|Gnoll - Morrobarro|8|0|1||78
96|Trabalomas, Alcalde de Costasur |2|2|0||
97|La Hermandad|8|0|0|79|70
98|Entrañas|4|4|10||
99|Victima|8|0|0||
100|Tesoro|0|0|9||
101|Tesoro|0|8|4||
102|Tesoro|0|8|2||
103|Vuelo, Negro|8|0|1|689|80
104|Cima del Trueno|4|4|2||
105|Cima del Trueno|5|4|10||
106|Horda Generico|4|4|10||
107|Troll, Peloescarcha|8|0|1||
108|La Hermandad|0|0|0|79|70
109|Jabalí, Crines de Acero 2|8|0|1||110 111
110|Jabalí, Crines de Acero 2|8|0|1|85|110
111|Jabalí, Erizapúas|8|0|1||85 111
112|Jabalí, Erizapúas|8|0|1|110|85 111
113|Escolta|1|1|0||
114|Tesoro|0|0|1||
115|JUGADOR, Gnomo|3|2|12||
116|JUGADOR, Troll|5|4|10||
118|Forjaz|4|4|2||
119|Bucaneros Velasangre |8|0|1||87
120|Bahía del Botín|0|0|0||21
121|Bahía del Botín|1|0|8||21
122|Forjaz|2|2|4||
123|Ventormenta|2|2|4||
124|Darnassus|2|2|4||
125|Orgrimmar|4|4|2||
126|Trolls Lanza Negra|4|4|2||
127|Villiano|0|0|1||
128|Brazanegra|8|0|1||88
129|Makrura|8|0|1||89
130|Centauro, Kolkar|8|0|1||90
131|Centauro, Galak|8|0|1||91
132|Clan Centauro Gelkis|8|0|1||92
133|Clan Centauro Magram|8|0|1||93
134|Maraudine|8|0|1||94
148|Monstruo|8|0|1||
149|Theramore|2|2|0||
150|Theramore|3|2|12||
151|Theramore|2|0|4||
152|Jabalí, Crines de Acero|8|0|1||109 111
153|Jabalí, Crines de Acero|8|0|0||109 111
154|Jabalí, Caramuerte|8|0|1||109 85 111 110
168|Enemigo|0|0|1||
188|Ambiente|0|0|0||148 28
189|Criatura|0|0|0||
190|Ambiente|0|0|0||
208|Caravana Nethergarde|2|2|0||168
209|Caravana Nethergarde|2|2|0||168
210|Alianza Genérico|2|2|12||189
230|Filibusteros de los Mares del Sur|8|0|1||573
231|Escolta|3|2|8||
232|Escolta|5|4|8||
233|No-Muerto, Plaga|8|0|1|68|20
250|Escolta|1|1|8||
270|Cueva de los Lamentos|8|0|1||229
290|Escolta|1|1|0||
310|Silítido|8|0|1||249
311|Silítido|8|0|0||249
312|Bestia - Araña|8|0|1||22
330|Cueva de los Lamentos|8|0|0||229
350|Brazanegra|8|0|0||88
370|Ejército de C'Thun|8|8|1|912|915
371|Remante de Lunargenta|2|2|4||269
390|Bahía del Botín|0|0|0|60|21
410|Basilisco|8|0|1||43
411|Bestia - Murciélago|8|0|1||310
412|Los Rapiñadores|4|4|2|509|510
413|Escórpido|8|0|1||309
414|Bastión Facues de Madera|8|0|1|65|576
415|Titán|8|0|1||311
416|Titán|8|0|0||
430|Capataz Fizzule|0|0|0||
450|Cueva de los Lamentos|8|0|1|40|229
470|Titán|8|0|1||
471|Ravenholdt|0|0|0||349
472|La Hermandad|8|0|1|349|70
473|Ravenholdt|0|0|0|70|349
474|Gadgetzan|0|0|0||369
475|Gadgetzan|1|0|8||369
494|Error de Gnomeregan|8|0|1|53|389
495|Escolta|1|1|8||40
514|Arpía|8|0|1||409
534|Alianza Generico|2|2|0||
554|Filo Ardiente|8|0|7||429
574|Futivo Sedaumbría|8|0|1|450|449
575|Araña|8|0|1||450
594|Trogg|8|0|0||
614|Victima|0|1|0||36
634|Monstruo|8|0|0||
635|Círculo Cenarion|0|0|0||609
636|Bastión Fauces de Madera|8|0|1|65|576
637|Trinquete|1|0|8||470
654|Troll, Secacorteza|8|0|1||82
655|Centauro, Kolkar|8|0|5||90
674|Enanos Hierro Negro |0|0|0||48
694|Alianza Generico|2|2|4||189
695|Srs. del Agua de Hydraxis|0|0|0||749
714|Horda Generico|4|4|0||
734|Enanos Hierro Negro|1|1|0||48
735|Goblin, Dueño de bar Hierro Negro|1|1|0||489
736|Goblin, Dueño de bar Hierro Negro|8|0|1||489
754|Enanos Hierro Negro|8|0|1|34|48
774|Escolta|3|2|0||
775|Escolta|5|4|0||
776|Linaje de Nozdormu|0|0|0|249 80|910 531
777|Poder de Kalimdor|1|1|0|915|912
778|Gigante|8|0|1||511
794|El Alba Argenta|1|0|0||529
795|Troll, Vilrama|8|0|1||572
814|El Alba Argenta|1|0|0||529
834|Elemental|8|0|1||74
854|Vista Eterna|1|0|8||577
855|Vista Eterna|0|0|0||577
874|Instructores de Sableinvernales|2|2|4||
875|Exiliados de Gnomeregan|2|2|4||
876|Trols Lanza Negra|4|4|2||
877|Trols Lanza Negra|5|4|10||
894|Theramore|2|2|4||108
914|Muñeco de Entrenamiento|0|0|0||
934|Furbolg, Incorrupto|8|0|1||575
954|Demonio|8|0|1||73
974|No-Muerto, Aparición|8|0|1||20
994|Círculo Cenarion|0|0|0||609
995|Cima del Trueno|4|4|2||
996|Círculo Cenarion|1|0|8|249|609
1014|Trols Rompelanzas|0|0|0||629
1015|Trols Rompelanzas|0|0|0||629
1034|Horda Generico|4|0|2||
1054|Alianza Generico|3|2|12||189
1055|Alianza Generico|2|2|4||189
1074|Orgrimmar|4|4|2||
1075|Theramore|2|2|4||108
1076|Darnassus|2|2|4||69
1077|Theramore|2|2|4||108
1078|Ventormenta|2|2|4||72
1080|Amistoso|0|1|0|74|31 649
1081|Elemental|8|0|1|649|74
1094|Bestia - Verraco|0|0|0||
1095|Muñeco de Entrenamiento|0|0|0||
1096|Theramore|3|2|12|679|
1097|Darnassus|2|2|4||
1114|Vuelo, Negro: Cebo|8|0|1|80|689
1134|Entrañas|5|4|10|679|
1154|Entrañas|5|4|10|679|
1174|Orgrimmar|4|4|2||
1194|Campo de Batalla Neutral|0|0|0||
1214|Clan Lobo Gélido|5|4|10|730|729
1215|Clan Lobo Gélido|4|4|2|730|729
1216|Guardia Pico Tormenta|3|2|12|729|730
1217|Guardia Pico Tormenta|2|2|4|729|730
1234|Señores del Fuego Sulfuron|8|0|1|749|750
1235|Señores del Fuego Sulfuron|8|0|1|749|750
1236|Señores del Fuego Sulfuron|8|0|1|749|750
1254|Círculo Cenarion|1|0|8||609
1274|Criatura|0|0|4||
1275|Criatura|0|0|2||
1294|Gizlock|8|0|1|770|
1314|Horda Generico|4|4|2||
1315|Alianza Generico|2|2|4||
1334|Guardia Pico Tormenta|2|2|4|729|730
1335|Clan Lobo Gélido|4|4|2|730|729
1354|Shen'dralar|0|0|0||809
1355|Shen'dralar|0|0|0||809
1374|Ogro (Capitan Kromcrush)|8|0|1||38
1375|Tesoro|0|0|9||
1394|Vuelo, Negro|8|0|1|689 47|80
1395|Atacantes Silítidos|8|0|1||916
1414|Guia Espiritual - Alianza|0|0|4||
1415|Guia Espiritual - Horda|0|0|2||
1434|Jaedenar|8|0|1||869
1454|Victima|0|1|0|35|36
1474|Hermandad del Torio|0|0|0||59
1475|Hermandad del Torio |0|0|0||59
1494|Horda Generico|4|4|2||66
1495|Horda Generico|5|4|10||66
1496|Horda Generico|4|4|2||66
1514|Centinelas Ala de Plata|2|2|4||
1515|Escoltas Grito de Guerra|4|4|2||
1534|Guardia Pico Tormenta|2|2|4|729|730
1554|Clan Lobo Gélido|5|4|8||
1555|Darkmoon Faire|0|0|0||909
1574|Zandalar Tribe|0|0|0||270
1575|Ventormenta|3|2|12||
1576|Remante de Lunargenta|2|2|4||269
1577|La Liga de Arathor|2|2|4|510|509
1594|Darnassus|3|2|12||
1595|Orgrimmar|5|4|10||
1596|Guardia Pico Tormenta|3|2|12|729|730
1597|Clan Lobo Gélido|5|4|10|730|729
1598|Los Rapiñadores|4|4|2|509|510
1599|La Liga de Arathor|2|2|4|510|509
1600|Darnassus|2|2|8||
1601|Linaje de Nozdormu|0|0|0|249 80|910 531
1602|Ciudad de Lunargenta|4|4|2||
1603|Ciudad de Lunargenta|5|4|10||
1604|Ciudad de Lunargenta|4|4|2||
1605|Vuelo, Bronce|0|0|1||531
1606|Criatura|0|4|2|7|
1607|Criatura|0|4|2|7|
1608|Círculo Cenarion|1|0|8|249|609
1610|JUGADOR, Elfo de Sangre|5|4|10||
1611|Forjaz|3|2|4|916|
1612|Orgrimmar|5|4|2|916|
1613|Poder de Kalimdor|1|1|0|915|912
1614|Monstruo|8|0|1||14
1615|Cártel Bonvapor|1|0|8||21 577 369
1616|RC Objetos|0|15|0|918|919
1617|RC Enemigos|0|0|1|919|918
1618|Forjaz|2|2|12||
1619|Orgrimmar|4|4|10||
1620|Enemigo|0|0|15||
1621|Azul|2|0|4|920|
1622|Rojo|2|0|4|921|
1623|Tranquillien|4|4|2||
1624|El Alba Argenta|1|0|8||529
1625|El Alba Argenta|1|0|8||529
1626|No-Muerto, Plaga|8|0|1|679|20
1627|Errantes|4|4|2||
1628|Tranquillien|4|4|2||
1629|JUGADOR, Draenei|3|2|12||
1630|Invasores de la Plaga|8|0|7|14 148|928 20
1634|Invasores de la Plaga|8|0|0|68 72|928 20
1635|Cártel Bonvapor|0|0|0|891|169 892
1636|Errantes|4|4|2||
1637|Errantes|4|4|2||
1638|Exodar|2|2|4||
1639|Exodar|3|2|12||
1640|Exodar|2|2|4||
1641|Escoltas Grito de Guerra|4|4|2||
1642|Centinelas Ala de Plata|2|2|4||
1643|Trol, Bosque|8|0|1||937
1644|Los Hijos de Lothar|2|2|4||
1645|Los Hijos de Lothar|3|2|12||
1646|Exodar|2|2|4||
1647|Exodar|3|2|12||
1648|Los Hijos de Lothar|2|2|4||72
1649|Los Hijos de Lothar|2|2|4||72
1650|Los Mag'har|5|4|10||
1651|Los Mag'har|4|4|2|28|
1652|Los Mag'har|4|4|2||
1653|The Mag'har|4|4|2||
1654|Exodar|2|2|4||69
1655|Exodar|2|2|4||69
1656|Ciudad de Lunargenta|5|4|10||
1657|Ciudad de Lunargenta|4|4|2||
1658|Ciudad de Lunargenta|4|4|2||
1659|Expedición Cenarion|1|0|8|60|942
1660|Expedición Cenarion|1|0|8||942
1661|Expedición Cenarion|1|0|8||942
1662|Orco Vil|8|0|1||943
1663|Espíritu Orco Vil|8|0|1|945|944
1664|Hijos de los Fantasmas Lothar|8|0|1|944|945
1665|Nada|1|7|8||
1666|Bastión de Honor|3|2|12||
1667|Bastión de Honor|2|2|4||72
1668|Thrallmar|5|4|10||
1669|Thrallmar|4|4|2||
1670|Thrallmar|4|4|2||
1671|Bastión de Honor|2|2|4||
1672|Test Facción 1|1|7|0|952|949
1673|ToWoW - Bandera|0|0|0|951|950
1674|Test Facción 4|0|15|0|951|950 953
1675|Test Facción 3|0|15|0|949|952
1676|ToWoW - Trigger Horda Bandera (DND)|0|15|0||954
1677|ToWoW - Trigger Alianza Bandera (DND)|0|15|0||954
1678|El Ethereum|8|0|1||956
1679|Roto|8|0|1|40|955
1680|Elemental|0|1|0|957|74
1681|Elemental Terráneo|8|0|1|74|74
1682|Robots de Combate|0|0|0|958|
1683|Actor Bueno|0|0|0|960|959
1684|Actor Malo|0|0|0|959|960
1685|Furbolg Semprepino|2|0|4||961
1686|Furbolg Semprepino|2|2|4|962|961
1687|Buhíco Enloquecido|8|0|1|961|962
1688|Ajedrez Alianza|0|1|0|964|963
1689|Ajedrez Horda|0|1|0|963|964
1690|Ajedrez Alianza|0|1|0|964|963
1691|Ajedrez Horda|0|1|0|963|964
1692|Monstruo Espanto|8|8|1|966|965
1693|Monstruo Buddy Espanto|8|8|1|965|966
1694|Exodar|2|2|4||
1695|Ciudad de Lunargenta|4|4|2||
1696|El Ojo Violeta|0|0|0||967
1697|Orco Vil|8|0|1|946 947|943
1698|Exodar|2|2|4|968|930
1699|Exodar|2|2|4|968|930
1700|Exodar|2|2|4|968|930
1701|Halcón del Sol|8|0|7|930|968
1702|Halcón del Sol|8|0|7|930|968
1703|Muñeco de Entrenamiento|0|0|0||
1704|Orco Vil|8|0|1|679|943
1705|Orco Vil|8|0|1||943 679
1706|Gigante Hongoso|8|0|1|970|971
1707|Esporaggar|1|0|8||970
1708|Esporaggar|1|0|8||970
1709|Esporaggar|1|0|8|971|970
1710|Expedición Cenarion|1|0|8||942
1711|Monstruo, Depredador|8|0|1|974|973
1712|Monstruo, Presa|8|0|1||974
1713|Monstruo, Presa|8|0|1||974
1714|Halcón del Sol|8|0|7|930 975|968
1715|Vacío Anormal|8|0|1||975
1716|Defensores de Hyjal|0|1|8||976
1717|Defensores de Hyjal|0|1|0||976
1718|Defensores de Hyjal|0|1|0|977|976
1719|Defensores de Hyjal|0|1|8||976
1720|Invasores de Hyjal|8|0|1|976|977
1721|Kurenai|3|2|12||978
1722|Kurenai|2|2|4||978
1723|Kurenai|2|2|4||978
1724|Kurenai|2|2|4||978
1725|Anillo de la Tierra|0|7|8||469 67
1726|Anillo de la Tierra|0|7|0||469 67
1727|Anillo de la Tierra|0|7|8||469 67
1728|Expedición Cenarion|1|0|8|14|942
1729|Thrallmar|4|4|2||
1730|El Consorcio|1|0|8||933
1731|El Consorcio|1|0|8||933
1732|Alianza Generico|2|2|4||
1733|Alianza Generico|2|2|4||
1734|Horda Generico|4|4|2||
1735|Horda Generico|4|4|2||
1736|Monstruo Buddy Espanto|8|8|0|965|966
1737|Bastión de Honor|2|2|4||72
1738|Arakkoa|8|0|1||981
1739|Estandarte de Marisma de Zangar (Alianza)|0|0|1||982
1740|Estandarte de Marisma de Zangar (Horda)|0|0|1||982
1741|Los Sha'tar|1|0|8||935
1742|Estandarte Marisma de Zangar (Neutral)|0|0|1||984
1743|Los Aldor|0|0|0||932
1744|Los Arúspices|0|0|0||934
1745|Ciudad de Lunargenta|4|4|2|679|
1746|Los Arúspices|0|0|0||934
1747|Cavernas del Tiempo - Thrall|1|1|0|986 987|985
1748|Cavernas del Tiempo - Durnholde|8|0|1|985|986
1749|Cavernas del Tiempo - Guardia de Costasur|0|0|0|985|987
1750|Consejo de la Sombra Secreta|8|0|1||14
1751|Monstruo|8|0|1|932 935|
1752|Atacante Portal Oscuro, Legión|8|0|7|991 992 943 529|993
1753|Atacante Portal Oscuro, Legión|8|0|7|991 992 943 529|993
1754|Atacante Portal Oscuro, Legión|8|0|7|991 992 943 529|993
1755|Defensor Portal Oscuro, Alianza|2|2|0|993|991 992
1756|Defensor Portal Oscuro, Alianza|2|2|0|993|991 992
1757|Defensor Portal Oscuro, Alianza|2|2|0|993|991 992
1758|Defensor Portal Oscuro, Horda|4|4|0|993|992 991
1759|Defensor Portal Oscuro, Horda|4|4|0|993|992 991
1760|Defensor Portal Oscuro, Horda|4|4|0|993|992 991
1761|Incitador Trigger|0|0|15|994|
1762|Incitador Trigger 2|0|0|7|996 997 998 994|
1763|Incitador Trigger 3|0|0|7|997 998 994 995|
1764|Incitador Trigger 4|0|0|7|998 994 995 996|
1765|Incitador Trigger 5|0|0|7|994 995 996 997|
1766|El Alba Argenta|0|0|0|993|529
1767|El Alba Argenta|0|0|0|993|529
1768|Demonio|0|0|15|14 529|73
1769|Demonio|0|0|15|14 529|73
1770|Actor Bueno|0|1|0|960|959
1771|Actor Malo|0|0|1|959|960
1772|Mana Criatura|8|0|1|968|999
1773|Siervo de Khadgar|0|1|0||1000
1774|Amistoso|0|1|0|1000|31
1775|The Sha'tar|1|0|8||935
1776|The Aldor|0|0|0|1010|932
1777|The Aldor|0|0|0||932
1778|La Escama de las Arenas|0|0|0||990
1779|Vigilantes del Tiempo|0|0|0||989
1780|Clan Aguja del Filo|8|0|1|929|1001
1781|Clan Aguja del Filo|8|0|1|1001|929
1782|Clan Aguja del Filo|8|0|1|929|1001
1783|Clan Aguja del Filo|8|0|1|1001|929
1784|Clan Aguja del Filo|8|0|1|929|1001
1785|Clan Aguja del Filo|8|0|1|1001|929
1786|Demonio|8|0|1||73
1787|Monstruo|8|0|1|994|14
1788|El Consorcio|1|0|8|968|933
1789|Halcón del Sol|8|0|7|933|968
1790|Clan Aguja del Filo|8|0|1|929|1001
1791|Clan Aguja del Filo|8|0|1|1001|929
1792|Orco Vil|8|0|1||943
1793|Halcón del Sol|8|0|7|930|968
1794|Protectorado|0|1|0||1003
1795|Protectorado|0|1|0|956|1003
1796|El Ethereum|8|0|1|1003|956
1797|Protectorado|0|1|0||1003
1798|Annihilator Arcana (DNR)|8|0|1||968 1004
1799|Compeñero de entrenamiento de El Ethereum|8|0|1|956|1002
1800|El Ethereum|8|0|1|1002|956
1801|Horda|5|4|10||
1802|Alianza|3|2|12||
1803|Ambiente|0|0|4||
1804|Ambiente|0|0|2||
1805|Los Aldor|1|1|0||932
1806|Amistoso|0|1|8||31
1807|Protectorado|1|1|8||1003
1808|Kirin'Var - Belmara|8|0|1||1007
1809|Kirin'Var - Cohlien|8|0|1||1009
1810|Kirin'Var - Dathric|8|0|1||1006
1811|Kirin'Var - Luminrath|8|0|1||1008
1812|Amistoso|0|1|8||31
1813|Siervo de Illdian|8|0|1|1023|1010
1814|Monstruo compañero de entrenamiento|8|8|1|965|966
1815|Bestia - Lobo|8|0|1|28|29
1816|Amistoso|0|1|0||31
1818|Bajo Arrabal|0|0|0||1011
1819|Alianza Generico|2|2|12|73|471
1820|Juramorte Lengua de Ceniza|0|0|0||1012
1821|Espíritus de Sombraluna 1|0|1|0||1013
1822|Espíritus de Sombraluna 2|0|1|0||1013
1823|El Ethereum|8|0|1||956
1824|Abisal|0|0|0||1015
1825|Demonio|0|0|15|14 529|73
1826|Siervo de Illdian|8|0|1|73 1023|1010
1827|Culto Vermis|8|0|1||1016
1828|Ent|0|0|0|1016|1017
1829|Demonio Leotheras I|0|1|0||1018 14
1830|Demonio Leotheras II|0|1|0||1019 14
1831|Demonio Leotheras III|0|1|0||1020 14
1832|Demonio Leotheras IV|0|1|0||1021 14
1833|Demonio Leotheras V|0|1|0||1022 14
1834|Azaloth|0|0|15|14 1010|1023
1835|Horda Generico|4|4|10|73|471
1836|El Consorcio|1|0|8||933
1837|Esporaggar|1|0|8|971|970
1838|Los Arúspices|0|0|0|1010|934
1839|Despellajador de Roca|8|0|1|1025|1024
1840|Despellejador Cazador|1|7|0|1024|1025
1841|Sombra Sombraluna|0|1|0||1026
1842|Comunicador de la Legión|0|0|1||
1843|Siervo de Illdian|8|0|1|932 934 1033 1012|1010
1844|Los Aldor|0|0|0|1010|932
1845|Los Arúspices|0|0|0|1010|934
1846|Ancianos del Bosque del Cuervo|8|0|1||1028
1847|Monstruo de entrenamiento |8|8|1|966|965
1848|Monstruo compañero de entrenamiento|8|8|1|965|966
1849|Siervo de Illdian|8|0|1|1023|1010
1850|Abisal|0|0|0|52|1015
1851|Lower City|1|0|8||1011
1852|Ajedrez, Amistoso Todos Ajedrez|0|1|0||963 964 1029
1853|Siervo de Illdian|8|0|1|932 934|1010
1854|Los Aldor|0|0|0|1030|932 934
1855|Los Arúspices|0|0|0|1030|934 932
1856|Guardianes del Cielo Sha'tari|1|0|0||1031
1857|Amistoso|1|1|8||1032
1858|Juramorte Lengua de Ceniza|0|1|0|1030|932 934 1012 1033
1859|Maiev|0|1|0|1030|932 934 1012 1033
1860|Sombras Skettis Arakkoa|0|1|0||1034
1862|Skettis Arakkoa|8|0|1||1035
1863|Orc, Faucedraco|8|0|1|1015 1036 932 934|52
1864|Enemigo Faucedraco|8|0|1|52|14
1865|Orc, Faucedraco|8|0|1||52
1866|Juramorte Lengua de Ceniza|1|0|0|1010|1012
1867|Maiev|0|1|0|1010|932 934 1012 1033
1868|Monstruo compañero de entrenamiento|0|1|0|965|966
1869|Arakkoa|8|0|0||1035
1870|Guardianes del Cielo Sha'tari|1|0|0||1031
1871|Skettis Arakkoa|8|0|1||1035
1872|Ogri'la|1|0|0||1038
1873|Destripador de Roca|8|0|1||1024
1874|Ogri'la|1|0|0||1038
1875|Los Aldor|0|0|0|52|932
1876|Los Arúspices|0|0|0|52|934
1877|Orc, Faucedraco|8|0|1|1015 932 934|52
1878|Frenzy|8|0|1||1041
1879|Enenmigo Guardianes del Cielo|8|0|1|1031|1042
1880|Orc, Faucedraco|8|0|1||52
1881|Skettis Arakkoa|8|0|1||1035
1882|Siervo de Illidan|8|0|1|1023|1010
1883|Desertor de Theramore|8|0|7||1044
1884|Tuskarr|8|8|1||
1885|Vrykul|8|0|1||1045
1886|Criatura|8|0|1||7
1887|Criatura|8|0|0||7 7
1888|Piratas del Mard del Norte|8|8|1||1046
1889|SINUSO|8|0|1||1048
1890|Troll, Amani|8|0|1||1049
1891|Expedición Denuedo|3|2|4||1050
1892|Expedición Denuedo|2|2|4||1050
1893|Expedición Denuedo|3|2|4|1045|1050
1894|Vrykul|8|0|1||1045
1895|Vrykul|8|0|1|1050|1045
1896|Feria de la Luna Negra|1|1|8||909
1897|La Mano de la Venganza|4|4|2|1045 1050|1052 1067
1898|Expedición Denuedo|2|2|4|1067|1050
1899|Expedición Duenedo|2|2|4|1067|1050
1900|La Mano de la Venganza|4|4|2|1053|1052 1067
1901|Expedición de la Horda|4|4|2||1052
1902|Actor Malo|8|0|1||
1904|Actor Malo|8|0|1||
1905|Can de peste domesticado|0|0|0|1054|1055
1906|Grifo Moteado|8|0|1|1055|1054
1907|Test Facción 1|1|0|8|949|948
1908|Test Facción 1|1|0|0|949|948
1909|Bestia - Raptor|0|0|9|14|42
1910|Vrykul (Espíritu Antiguo 1)|0|1|0||1056
1911|Vrykul (Espíritu Antiguo 2)|0|1|0||1057
1912|Vrykul (Espíritu Antiguo 3)|1|1|0||1058
1913|CTF - Bandera - Alianza|0|7|0||1059
1914|Vrykul|8|0|1|1067 1085|1045
1915|Test|0|0|0||1060
1916|Maiev|0|1|0|1010|932 934 1012 1033
1917|Criatura|0|0|1||7
1918|Expedición de la Horda|4|4|2|679|1052
1919|Gladiador Vrykul|8|0|1|1063|1062
1920|Combatiente Valgarde|3|0|4|1062|1063
1921|Los Taunka|0|4|2||1064
1922|Los Taunka|0|4|2||1064
1923|Los Taunka|0|4|2||1064
1924|Monstruo, Fuerza de Reacción 1|8|0|1||1065
1925|Monstruo|8|0|9|14|
1926|Liga de los Exploradores|2|0|4||1068
1927|Liga de los Exploradores|2|0|4||1068
1928|La Mano de la Venganza|4|0|2||1067 1052
1929|La Mano de la Venganza|4|0|2||1067 1052
1930|Carrera de Carneros PowerUp DND|0|0|0||1069
1931|Trampa de Carrera de Carneros DND|0|0|0||1070
1932|Elemental|0|0|15|14|74
1933|Amistoso|0|4|0||31
1934|Actor Bueno|2|2|4|960|959
1935|Actor Bueno|4|4|2|960|959
1936|Las Ardillas de Craig|0|0|0||
1937|Las Ardillas de Craig|0|0|0||
1938|Las Ardillas de Craig|0|0|0||
1939|Las Ardillas de Craig|0|0|0||
1940|Las Ardillas de Craig
|0|0|0||
1941|Las Ardillas de Craig
|0|0|0||
1942|Las Ardillas de Craig
|0|0|0||960
1943|Las Ardillas de Craig
|0|0|0||
1944|Las Ardillas de Craig
|0|0|0||
1945|Las Ardillas de Craig
|15|15|15||1071 551 189
1947|Las Ardillas de Craig|15|15|15||1071 551 189
1948|Azul|1|2|1|469|921
1949|Los Kalu'ak|0|0|0|1046|1073
1950|Los Kalu'ak|0|0|0||1073
1951|Darnassus|2|2|12|22 29|69
1952|Vacaciones - Barril de Agua|0|1|0||1074
1953|Monstruo, Depredador|8|0|1|974|973
1954|Enanos Hierro Negro|8|0|1||1076
1955|Enanos Hierro Negro|8|0|1||1076
1956|Ofensiva del Sol Devastado|1|0|0||1077
1957|Ofensiva del Sol Devastado|1|0|0||1077
1958|Actor Malo|8|0|1|959|960
1959|Actor Malo|0|1|0|959|960
1960|Ofensiva del Sol Devastado|1|0|0||1077
1961|Combate Mascotas de Compañía|0|15|0|1078|
1962|No-Muerto, Plaga|8|0|1|73|20
1963|Demonio|8|0|1|20|73
1964|No-Muerto, Plaga|8|0|1|73|20
1965|Monstruo de entrenamiento |8|8|1|966|965
1966|Murloc|8|0|0|60|19
1967|Shattered Sun Offensive|1|0|0|1077|
1968|Murloc, Winterfin|0|0|8|19|1079
1969|Murloc|8|0|1|1079|19
1970|Monstruo|8|0|1|1079|14
1971|Amistoso, Fuerza de Reacción|0|1|0||1080
1972|Objeto, Fuerza de Reacción|0|0|0||
1973|Expedición Denuedo|3|2|4||1050
1974|Expedición Denuedo|2|2|4|1084 20|1050
1975|No-Muerto, Plaga|8|0|7|1050|20
1976|Expedición Denuedo|3|2|4|679|1050
1977|Expedición Denuedo|3|2|4|1050|
1978|Ofensiva Grito de Guerra|4|0|2||1085
1979|Ofensiva Grito de Guerra|4|0|2||1085
1980|Ofensiva Grito de Guerra|4|0|2|20|1085
1981|Ofensiva Grito de Guerra|4|0|2||1085
1982|No-Muerto, Plaga|8|0|1|1085|20
1983|Monstruo de entrenamiento |8|8|1|966|965
1984|Monstruo compañero de entrenamiento|8|8|1|965|966
1985|Monstruo|8|0|1|20|14
1986|Escolta|1|1|8|1057 1058 1056|40
1987|Expedición Cenarion|1|0|0|1086|942 148
1988|No-Muerto, Plaga|8|0|7|1050|20
1989|Cazador Furtivo|8|0|1|148 942|1086
1990|Ambiente|8|0|1||148 942
1991|No-Muerto, Plaga|0|0|7|14 148|928 20
1992|Monstruo|0|0|9|14|
1993|Monstruo de entrenamiento |2|2|4|966|965
1994|Monstruo compañero de entrenamiento|2|2|4|965|966
1995|CTF - Bandera - Alianza|0|5|2||1059
1997|CTF - Bandera - Alianza|0|3|4||1059
1998|Monstruo|8|0|1||1087
1999|Monstruo, Presa|8|0|0||974
2000|Monstruo, Presa|8|0|0||974
2001|Furbolg, Colmillorojo|8|8|1|1089|1088
2003|Furbolg, Pataescarcha|8|8|1|1088|1089
2004|Expedición Denuedo|3|2|4|20|1050
2005|No-Muerto, Plaga|8|0|7|1050|20
2006|Kirin Tor|0|0|0||1090
2007|Kirin Tor|0|0|0||1090
2008|Kirin Tor|0|0|0||1090
2009|Kirin Tor|1|0|0||1090
2010|Acuerdo del Reposo del Dragón|0|0|0||1091
2011|Acuerdo del Reposo del Dragón|0|0|0||1091
2012|Acuerdo del Reposo del Dragón|0|0|0||1091
2013|Acuerdo del Reposo del Dragón|0|0|0||1091
2014|Azjol-Nerub|0|0|0||1092
2016|Azjol-Nerub|0|0|0|20|1092
2017|Azjol-Nerub|0|0|0||1092
2018|No-Muerto, Plaga|8|0|7|1092|20
2019|Los Taunka|0|4|2|20|1064
2020|Ofensiva Grito de Guerra|4|4|2||1085
2021|REUSAR|3|2|4||1082
2022|Monstruo|8|0|1||14
2023|Invasores de la Plaga|9|0|6|14 148|928 20
2024|La Mano de la Venganza|5|0|2||1067
2025|The Silver Covenant|3|2|4|67|1094
2026|The Silver Covenant|3|2|4|67|1094
2027|The Silver Covenant|3|2|4|67|1094
2028|Ambient|0|1|0||
2029|Monstruo, Predator|8|0|1|974 28|973
2030|Monstruo, Predator|8|0|1|974 28|973
2031|Horda Generico|4|4|0||148
2032|Grizzly Hills Trapper|0|2|4||1095
2033|Monstruo|8|0|1|56|
2034|Ofensiva Grito de Guerra|4|0|2|1095|1085
2035|No-Muerto, Scourge|8|0|7|31|20
2036|Amistoso|0|1|8|20|31
2037|Expedición Denuedo|2|2|4|148|1050
2038|Ambient|8|0|0|1050|148
2039|Monstruo|8|0|1|1050|14
2040|Expedición Denuedo|3|2|4|14|1050
2041|Acuerdo del Reposo del Dragón|0|0|0|20|1091
2042|No-Muerto, Scourge|8|0|7|1091|20
2043|No-Muerto, Scourge|8|0|7|1050 1085|20
2044|Expedición Denuedo|1|2|4|20|1050
2045|Ofensiva Grito de Guerra|0|4|2|20|1085
2046|Escolta|5|4|8||
2047|Los Kalu'ak|0|0|0|965|
2048|Invasores de la Plaga|8|0|0||928 20
2049|Invasores de la Plaga|0|0|0||928 20
2050|Caballeros de la Espada de Ébano|1|0|0||1098
2051|Caballeros de la Espada de Ébano|1|0|0||1098
2052|Puerta del Cólera Plaga|8|1|0|1050 1085 1101 1100|1099
2053|Puerta del Cólera Alianza|1|6|0|20 1099|1100
2054|Puerta del Cólera Horda|0|6|0|20 1099|1101
2055|Monstruo de entrenamiento |4|4|2|966|965
2056|Monstruo compañero de entrenamiento|4|4|2|965|966
2057|Monstruo, Fuerza de Reacción Zona 2|8|0|1||1066
2058|CTF - Bandera - Horda|0|7|0||1102
2059|CTF - Bandera - Neutral|0|7|0||1103
2060|Tribu Corazón Frenético|0|0|0||1104
2061|Tribu Corazón Frenético|0|0|0|1105|1104
2062|Tribu Corazón Frenético|0|0|0|1105|1104
2063|Los Oráculos|0|0|0||1105
2064|Los Oráculos|0|0|0|1104|1105
2065|Los Oráculos|0|0|0|14|1105
2066|Los Oráculos|0|0|0|1104|1105
2067|Acuerdo del Reposo del Dragón|0|0|8|14|1091
2068|No-Muerto, Plaga|8|0|7|1107 1106 959|20
2069|Troll, Drakkari|8|0|7|1106 20|1107
2070|Cruzada Argenta|0|0|0||1106
2071|Cruzada Argenta|0|0|0||1106
2072|Cruzada Argenta|0|0|0||1106
2073|Cruzada Argenta|0|0|0|1107 20|1106
2074|Cavernas del Tiempo - Durnholde|8|0|0||986 987
2075|CoT Plaga|8|0|1|1108|1110
2076|CoT Arthas|0|1|0|1110 1109|1108
2077|CoT Arthas|0|1|0|1110 1109|1108
2078|CoT Ciudadano de Stratholme|0|0|0||1109
2079|CoT Arthas|0|1|0|1110 1109|1108
2080|No-Muerto, Plaga|8|0|7|1111|20
2081|Freya|0|1|0|20|1111
2082|No-Muerto, Plaga|0|1|0||20
2083|No-Muerto, Plaga|0|1|0||20
2084|No-Muerto, Plaga|0|1|0|529 56|20
2085|No-Muerto, Plaga|0|1|0|529 56|20
2086|Alba Argenta|8|0|1||529
2087|Alba Argenta|8|0|1||529
2088|Actor Malo|0|0|1|20 56|960
2089|Cruzada Escarlata|8|0|1|20 529|56
2090|Montura - Taxi - Alianza|2|0|0||1112
2091|Montura - Taxi - Horda|4|0|0||1113
2092|Montura - Taxi - Neutral|0|1|0||1114
2093|No-Muerto, Plaga|0|1|0|959|20
2094|No-Muerto, Plaga|0|1|0||20
2095|Cruzada Escarlata|8|0|1|20 529|56
2096|Cruzada Escarlata|0|0|0|20 529|56
2097|No-Muerto, Plaga|8|0|1||20
2098|Elemental, Aire|8|0|1|1115|1116
2099|Elemental, Agua|8|0|1|1116|1115
2100|No-Muerto, Plaga|0|1|8|529 56|20
2101|Actor Malo|0|1|0|959|960
2102|Actor Malo|0|0|1|959|960
2103|Cruzada Escarlata|8|0|1|20 529|56
2104|Monstruo de entrenamiento|1|1|0|966|965
2105|Monstruo compañero de entrenamiento|1|1|0|965|966
2106|Ambiente|8|0|1|28|148
2107|Los Hijos de Hodir|8|0|0|1120 1121|1119
2108|Gigantes de Hierro|8|0|1|1119|1120
2109|Vrykul Helado|8|0|1||1121
2110|Amistoso|0|1|8||31
2111|Monstruo|8|0|1|31|14
2112|Los Hijos de Hodir|8|0|0|1121|1119
2113|Vrykul Helado|8|0|1|1119|1121
2114|Vrykul|8|0|1||1045 20
2115|Actor Bueno|0|1|8|1107 20|959
2116|Vrykul|8|0|1||1045
2117|Actor Bueno|0|1|8|1107 20|959
2118|Terráneo|0|1|0|1120|1122
2119|Monstruo Árbitro|8|0|1||965 966 1123
2120|Monstruo Árbitro|8|0|1||965 966 1123
2121|The Sunreavers|4|4|2||1124
2122|Los Atracasol|4|4|2||1124
2123|Los Atracasol|4|4|2||1124
2124|Monstruo|8|0|1|1119|14
2125|Vrykul Helado|8|0|1|148|1121
2126|Vrykul Helado|8|0|1|148|1121
2127|Ambiente|0|0|0|1121|148
2128|Encuentro Hyldnir|0|1|0|1125|1125
2129|Los Atracasol|4|4|10||1124
2130|El Pacto de Plata|3|2|12|67|1094
2131|Cruzada Argenta|0|0|0|1107 20|1106
2132|Ofensiva Grito de Guerra|5|4|2||1085
2133|Vrykul Helado|8|0|1|1119|1121
2134|Cruzada Argenta|0|0|0|20|1106
2135|Amistoso|0|1|0||31
2136|Ambiente|0|0|0||148
2137|Amistoso|0|1|0|148|31
2138|Cruzada Argenta|0|0|0|1107 20|1106
2139|Invasores de la Plaga|8|0|1|68 72|928 20
2140|Amistoso|0|1|0|20|31
2141|Amistoso|0|1|8||31
2142|Alianza|3|2|12||
2143|Expedición Denuedo|2|2|4|1085|1050
2144|Caballeros de la Espada de Ébano|1|0|0|20|1098
2145|Invasores de la Plaga|8|0|7|14 148|928 20
2148|Los Kalu'ak|0|0|0||1073
2150|Monstruo compañero de entrenamiento|8|8|1|965|
2155|Forjaz|2|2|4||47
2156|Monstruo, Depredador|0|0|0||973
2176|Actor Bueno|4|4|2|960|959
2178|Actor Bueno|2|2|4|960|959
2189|Odio a Todo|8|0|15||1145
2190|Odio a Todo|8|0|15||1145
2191|Odio a Todo|8|0|15||1145
2209|No-Muerto, Plaga|8|0|7|1098 1106|20
2210|Ciudad de Lunargenta|4|7|0||
2212|No-Muerto, Plaga|8|0|7|1098 1106|20
2214|Caballeros de la Espada de Ébano|1|6|0|20|1098 529
2216|El Veredicto Cinéreo|0|0|0||1106 1156 1098
2217|El Veredicto Cinéreo|0|0|0||1106 1156 1098
2218|El Veredicto Cinéreo|0|0|0|20|1106 1156 1098
2219|El Veredicto Cinéreo|0|0|0|20|1106 1156 1098
2226|Caballeros de la Espada de Ébano|1|6|0|20|1098 529
2230|Cruzada Argenta|0|0|0|1107 20|1106
2235|CTF - Bandera - Horda 2|0|5|2||
2236|CTF - Bandera - Alianza 2|0|3|4||