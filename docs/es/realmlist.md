# realmlist

[<-Volver a:Auth](database-auth.md)

Leer en: [English :gb:](../realmlist) [Spanish :es:](realmlist)

**Tabla \`realmlist\`**

Esta tabla establece información sobre todos los reinos disponibles. Cada fila controla un reino diferente.

**Estructura**

| Field                      | Type         | Attributes | Key | Null | Default       | Extra          | Comment |
| -------------------------- | ------------ | ---------- | --- | ---- | ------------- | -------------- | ------- |
| [id][1]                    | INT          | UNSIGNED   | PRI | NO   |               | AUTO_INCREMENT |         |
| [name][2]                  | VARCHAR(32)  | SIGNED     | UNI | NO   | ''            |                |         |
| [address][3]               | VARCHAR(255) | SIGNED     |     | NO   | 127.0.0.1     |                |         |
| [localAddress][4]          | VARCHAR(255) | SIGNED     |     | NO   | 127.0.0.1     |                |         |
| [localSubnetMask][5]       | VARCHAR(255) | SIGNED     |     | NO   | 255.255.255.0 |                |         |
| [port][6]                  | SMALLINT     | UNSIGNED   |     | NO   | 8085          |                |         |
| [icon][7]                  | TINYINT      | UNSIGNED   |     | NO   | 0             |                |         |
| [flag][8]                  | TINYINT      | UNSIGNED   |     | NO   | 2             |                |         |
| [timezone][9]              | TINYINT      | UNSIGNED   |     | NO   | 0             |                |         |
| [allowedSecurityLevel][10] | TINYINT      | UNSIGNED   |     | NO   | 0             |                |         |
| [population][11]           | FLOAT        | SIGNED     |     | NO   | 0             |                |         |
| [gamebuild][12]            | INT          | UNSIGNED   |     | NO   | 12340         |                |         |

[1]: #id
[2]: #name
[3]: #address
[4]: #localaddress
[5]: #port
[6]: #icon
[7]: #flag
[8]: #timezone
[9]: #allowedsecuritylevel
[10]: #population
[11]: #gamebuild

**Descripción de los campos**

### id

El ID del reino. Este número es único para cada reino y DEBE correlacionarse con el valor de configuración RealmID en worldserver.conf.

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `realmlist_chk_1`.

### name

El nombre del reino. Aparecerá en la lista de selección de reinos y en la pantalla de selección de personajes.

### address

La dirección IP pública (WAN) o LAN del servidor mundial. Utilice 127.0.0.1 en este campo si sólo usted se conecta al servidor (y se ejecuta en la misma máquina que su cliente).

También puede utilizar un nombre de dominio como *ejemplo.com.*

### localAddress

Principalmente 127.0.0.1

### port

El puerto en el que se ejecuta el WorldServer. Si todos los WorldServers están en la misma máquina, todos tendrán que usar un puerto diferente.

### icon

El icono del reino.

| Icon | Type    |
| ---- | ------- |
| 0    | Normal  |
| 1    | JcJ     |
| 4    | Normal  |
| 6    | JdR     |
| 8    | JdR JcJ |

### flag

Realmflag o marcador de este reino.

| Flag | Hex value | Description      |
| ---- | --------- | ---------------- |
| 0    | 0x0       | Ninguno          |
| 1    | 0x1       | Inválido         |
| 2    | 0x2       | Fuera de Línea   |
| 4    | 0x4       | SpecifyBuild     |
| 8    | 0x8       | Medio            |
| 16   | 0xF       | Medio            |
| 32   | 0x10      | Nuevos Jugadores |
| 64   | 0x20      | Recomendado      |
| 128  | 0x40      | Lleno            |

### timezone

La zona horaria del reino, se mostrará en las pestañas del realmlist

| Zona Horaria | Nombre en Pantalla |
| ------------ | ------------------ |
| 1            | Development        |
| 2            | United States      |
| 3            | Oceanic            |
| 4            | Latin America      |
| 5            | Tournament         |
| 6            | Korea              |
| 7            | Tournament         |
| 8            | English            |
| 9            | German             |
| 10           | French             |
| 11           | Spanish            |
| 12           | Russian            |
| 13           | Tournament         |
| 14           | Taiwan             |
| 15           | Tournament         |
| 16           | China              |
| 17           | CN1                |
| 18           | CN2                |
| 19           | CN3                |
| 20           | CN4                |
| 21           | CN5                |
| 22           | CN6                |
| 23           | CN7                |
| 24           | CN8                |
| 25           | Tournament         |
| 26           | Test Server        |
| 27           | Tournament         |
| 29           | CN9                |
| 30           | Test Server 2      |
| 31           | CN10               |
| 32           | CTC                |
| 33           | CNC                |
| 34           | CN1/4              |
| 35           | CN/2/6/9           |
| 36           | CN3/7              |
| 37           | Russian Tournament |
| 38           | CN5/8              |
| 39           | CN11               |
| 40           | CN12               |
| 41           | CN13               |
| 42           | CN14               |
| 43           | CN15               |
| 44           | CN16               |
| 45           | CN17               |
| 46           | CN18               |
| 47           | CN19               |
| 48           | CN20               |
| 49           | Brazil             |
| 50           | Italian            |
| 51           | Hyrule             |
| 52           | QA2 Test           |
| 53           |                    |
| 54           |                    |
| 55           | Recommended Realm  |
| 56           | Test               |
| 57           | Recommended Realm  |
| 58           |                    |
| 59           | Future Test        |

### allowedSecurityLevel

El nivel de GM mínimo requerido para que las cuentas puedan entrar en este reino. El cambio de este valor actualizará automáticamente la lista de reinos visibles en el juego, pero el WorldServer debe reiniciarse para que surta efecto.

### population

Este campo se actualiza automáticamente a intervalos regulares y tendrá la población actual. La fórmula para calcular el valor de este campo es: CantidadDeJugadores / MaxCantidadDeJugadores \*2. En la lista de reinos del juego, los umbrales de población baja, media y alta son 0,5, 1,0 y 2,0 respectivamente.

### gamebuild

Versión del cliente aceptada para el reino.

| Versión de Build | Parche del Cliente |
| ---------------- | ------------------ |
| 5875             | 1.12.1             |
| 6005             | 1.12.2             |
| 8606             | 2.4.3              |
| 9947             | 3.1.3              |
| 10146            | 3.2.0              |
| 10505            | 3.2.2a             |
| 10571            | 3.3.0              |
| 11159            | 3.3.0a             |
| 11403            | 3.3.2              |
| 11623            | 3.3.3              |
| 11723            | 3.3.3a             |
| 12340            | 3.3.5a             |
