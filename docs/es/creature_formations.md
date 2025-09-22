# creature\_formations

[<-Volver a:World](database-world)

**Tabla \`creature\_formations\`**

Esta tabla permite agrupar grupos. Los miembros del grupo seguirán a otros y atacarán a sus objetivos.

**Estructura**

| Campo           | Tipo  | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| --------------- | ----- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [leaderGUID][1] | INT   | UNSIGNED  |       | NO   | NULL        |       |            |
| [memberGUID][2] | INT   | UNSIGNED  | PRI   | NO   | NULL        |       |            |
| [dist][3]       | FLOAT | UNSIGNED  |       | NO   | NULL        |       |            |
| [angle][4]      | FLOAT | UNSIGNED  |       | NO   | NULL        |       |            |
| [groupAI][5]    | INT   | UNSIGNED  |       | NO   | NULL        |       |            |
| [point_1][6]    | INT   | UNSIGNED  |       | NO   | 0           |       |            |
| [point_2][7]    | INT   | UNSIGNED  |       | NO   | 0           |       |            |

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

GUID del miembro del grupo. NOTA: Se requiere una entrada con `leaderGUID` y `memberGUID` con `leaderGUID` para que el grupo funcione.

Ejemplo:

* Líder = 1
* Miembros = 2 and 3

| Líder GUID | Miembros GUID |
| ---------- | ------------- |
| 1          | 1             |
| 1          | 2             |
| 1          | 3             |

## dist

Distancia máxima entre el líder del grupo y el miembro

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `creature_formations_chk_1`.

## angle

Ángulo entre el líder y el miembro
Nota: ¡Solo se utilizan grados! Los valores deben estar entre 0 y 360.

![ángulo](assets/images/angle.png)

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `creature_formations_chk_1`.

## groupAI

Establece los comportamientos de los miembros del grupo, los valores son:

| Valor | Bandera | Nombre                                     | Comentario                                                       	 |
| ----- | ------- | ------------------------------------------ | ------------------------------------------------------------------- |
| 0     |         |                                            | Nadie ayuda a nadie y ningún miembro sigue al líder.     	      	 |
| 1     | 0x001   | GROUP_AI_FLAG_MEMBER_ASSIST_LEADER         | El miembro se enoja si el líder se enoja                         	 |
| 2     | 0x002   | GROUP_AI_FLAG_LEADER_ASSIST_MEMBER         | El líder agro si el miembro agro.                                	 |
| 3     |         |                                            | Todos ayudan a todos y ningún miembro sigue al líder.            	 |
| 4     | 0x004   | GROUP_AI_FLAG_EVADE_TOGETHER               | Todos evaden si algún miembro evade (entra en modo evasión)      	 |
| 8     | 0x008   | GROUP_AI_FLAG_RESPAWN_ON_EVADE             | Todos reaparecen si los miembros evaden (entran en modo evasión) 	 |
| 16    | 0x010   | GROUP_AI_FLAG_DONT_RESPAWN_LEADER_ON_EVADE | Se utiliza con la bandera 0x008 para evitar que el líder reaparezca |
| 24    |         |                                            | Todos excepto el líder reaparecen si los miembros evaden.           |
| 512   | 0x200   | GROUP_AI_FLAG_FOLLOW_LEADER                | Nadie ayuda a nadie y los miembros siguen al líder.               	 |
| 515   |         |                                            | Todos ayudan a todos y los miembros siguen al líder.         		 |

## point\_1  

## point\_2

Estos valores se utilizan para establecer los puntos de ruta de finalización previos del leaderGUID para los memberGUID, donde la ruta es una ruta de retorno directa y los memberGUID no deben cruzarse al otro lado del leaderGUID en el cambio de dirección.

Si tu líder tiene una trayectoria como la de abajo, donde se mueve al punto 5 y luego regresa al 1, establecerías el punto 1 = 4 y el punto 2 = 8 en el memberGUID. Si el memberGUID está en un ángulo de 90° hasta el punto 5, cambiará al ángulo de 270° para el viaje de regreso. Esto solo es necesario para mantener a las criaturas en el lado correcto. Estos valores se pueden dejar en 0 para las criaturas que siguen directamente detrás del leaderGUID o para cualquier criatura en una trayectoria circular.

```
	1     2     3     4    5

	-----<--------->------

       8    7      6
```
