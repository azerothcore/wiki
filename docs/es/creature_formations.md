# creature\_formations

[<-Volver a: World](database-world)

**Tabla \`creature\_formations\`**

Esta tabla permite agrupar mobs. Los miembros del grupo seguirán a los demás y atacarán a sus objetivos.

**Estructura**

| Field           | Type  | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------- |
| [leaderGUID][1] | INT   | UNSIGNED   |     | NO   | NULL    |       |         |
| [memberGUID][2] | INT   | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [dist][3]       | FLOAT | UNSIGNED   |     | NO   | NULL    |       |         |
| [angle][4]      | FLOAT | UNSIGNED   |     | NO   | NULL    |       |         |
| [groupAI][5]    | INT   | UNSIGNED   |     | NO   | NULL    |       |         |
| [point_1][6]    | INT   | UNSIGNED   |     | NO   | 0       |       |         |
| [point_2][7]    | INT   | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #leaderguid
[2]: #memberguid
[3]: #dist
[4]: #angle
[5]: #groupai
[6]: #point_1
[7]: #point_2

## leaderGUID

GUID del líder del grupo

## memberGUID

GUID del miembro del grupo. NOTA: Es necesario tener una entrada con `leaderGUID` y `memberGUID` con el mismo `leaderGUID` para que el grupo funcione.
Ejemplo:

* Líder = 1
* Miembros = 2 y 3

| leaderGUID | memberGUID |
| ---------- | ---------- |
| 1          | 1          |
| 1          | 2          |
| 1          | 3          |

## dist

Distancia máxima entre el líder del grupo y el miembro

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `creature_formations_chk_1`.

## angle

Ángulo entre el líder y el miembro
Nota: ¡Solo se usan grados! Los valores deberían estar entre 0 y 360

![angle](assets/images/angle.png)

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `creature_formations_chk_1`.

## groupAI

Establece los comportamientos de los miembros del grupo; los valores son:

| Flag  | Bit | Name                                       | Comment                                                        |
| ----- | --- | ------------------------------------------ | -------------------------------------------------------------- |
|       | 0   |                                            | Nadie ayuda a nadie y el miembro no sigue al líder             |
| 0x001 | 1   | GROUP_AI_FLAG_MEMBER_ASSIST_LEADER         | El miembro entra en combate si el líder entra en combate       |
| 0x002 | 2   | GROUP_AI_FLAG_LEADER_ASSIST_MEMBER         | El líder entra en combate si el miembro entra en combate       |
|       | 3   |                                            | Todos ayudan a todos y el miembro no sigue al líder            |
| 0x004 | 4   | GROUP_AI_FLAG_EVADE_TOGETHER               | Todos evaden si algún miembro evade (entra en modo evasión)    |
| 0x008 | 8   | GROUP_AI_FLAG_RESPAWN_ON_EVADE             | Todos reaparecen si los miembros evaden (entra en modo evasión) |
| 0x010 | 16  | GROUP_AI_FLAG_DONT_RESPAWN_LEADER_ON_EVADE | Se usa con la flag 0x008 para evitar que el líder reaparezca   |
|       | 24  |                                            | Todos menos el líder reaparecen si los miembros evaden         |
| 0x200 | 512 | GROUP_AI_FLAG_FOLLOW_LEADER                | Nadie ayuda a nadie y el miembro sigue al líder                |
|       | 515 |                                            | Todos ayudan a todos y el miembro sigue al líder               |

## point\_1

## point\_2

Estos valores se usan para establecer los puntos de ruta previos al final del `leaderGUID` para los `memberGUID` cuando la ruta es un recorrido de ida y vuelta en línea recta y los `memberGUID` no deben cruzar al otro lado del `leaderGUID` al cambiar de dirección.

Si tu líder tiene una ruta como la de abajo, en la que se mueve al punto 5 y luego vuelve al 1, establecerías point\_1 = 4 y point\_2 = 8 en el memberGUID. Si el memberGUID está en el ángulo 90 hasta el punto 5, cambiará al ángulo 270 para el viaje de vuelta. Esto solo es necesario para mantener a las criaturas en el lado correcto. Estos valores se pueden dejar en 0 para las criaturas que siguen directamente detrás del leaderGUID o para cualquier criatura en una ruta circular.

```
	1     2     3     4    5

	-----<--------->------

       8    7      6
```
