# account

[<-Volver a:Auth](database-auth.md)

**Tabla \`account\`**

**Estructura**

| Field                 | Type         | Attributes | Key | Null | Default           | Extra          | Comment    |
| --------------------- | ------------ | ---------- | --- | ---- | ----------------- | -------------- | ---------- |
| [id][1]               | INT          | UNSIGNED   | PRI | NO   |                   | AUTO_INCREMENT | Identifier |
| [username][2]         | VARCHAR(32)  |            | UNI | NO   |                   |                |            |
| [salt][3]             | BINARY(32)   |            |     | NO   |                   |                |            |
| [verifier][4]         | BINARY(32)   |            |     | NO   |                   |                |            |
| [session_key][5]      | BINARY(40)   |            |     | YES  |                   |                |            |
| [token_key][6]        | VARCHAR(100) |            |     | NO   |                   |                |            |
| [email][7]            | VARCHAR(255) |            |     | NO   |                   |                |            |
| [reg_mail][8]         | VARCHAR(255) |            |     | NO   |                   |                |            |
| [joindate][9]         | TIMESTAMP    |            |     | NO   | CURRENT_TIMESTAMP |                |            |
| [last_ip][10]         | VARCHAR(15)  |            |     | NO   | 127.0.0.1         |                |            |
| [last_attempt_ip][11] | VARCHAR(15)  |            |     | NO   | 127.0.0.1         |                |            |
| [failed_logins][12]   | INT          | UNSIGNED   |     | NO   | 0                 |                |            |
| [locked][13]          | TINYINT      | UNSIGNED   |     | NO   | 0                 |                |            |
| [lock_country][14]    | VARCHAR(2)   |            |     | NO   | 0                 |                |            |
| [last_login][15]      | TIMESTAMP    |            |     | YES  | NULL              |                |            |
| [online][16]          | INT          | UNSIGNED   |     | NO   | 0                 |                |            |
| [expansion][17]       | TINYINT      | UNSIGNED   |     | NO   | 2                 |                |            |
| [mutetime][18]        | BIGINT       | SIGNED     |     | NO   | 0                 |                |            |
| [mutereason][19]      | VARCHAR(255) |            |     | NO   |                   |                |            |
| [muteby][20]          | VARCHAR(50)  |            |     | NO   |                   |                |            |
| [locale][21]          | TINYINT      | UNSIGNED   |     | NO   | 0                 |                |            |
| [os][22]              | VARCHAR(3)   |            |     | NO   |                   |                |            |
| [recruiter][23]       | INT          | UNSIGNED   |     | NO   | 0                 |                |            |
| [totaltime][24]       | INT          | UNSIGNED   |     | NO   | 0                 |                |            |

[1]: #id
[2]: #username
[3]: #salt
[4]: #verifier
[5]: #session_key
[6]: #token_key
[7]: #email
[8]: #reg_mail
[9]: #joindate
[10]: #last_ip
[11]: #last_attempt_ip
[12]: #failed_logins
[13]: #locked
[14]: #lock_country
[15]: #last_login
[16]: #online
[17]: #expansion
[18]: #mutetime
[19]: #mutereason
[20]: #muteby
[21]: #locale
[22]: #os
[23]: #recruiter
[24]: #totaltime

## Descripción de los campos

### id

El ID único de la cuenta.

### username

El nombre de la cuenta de usuario.

**NOTA:** los nombres de usuario están limitados a 20 caracteres y estos mismos no tienen restricción por caracter.

### salt

Salt es un valor criptográfico aleatorio de 32 bytes.

### verifier

El verificador se deriva de salt, así como el nombre de usuario (todo en mayúsculas) y su contraseña (todo en mayúsculas).

Para obtener el verificador hay que calcular:

1. Calcule `h1 = SHA1("USUARIO:CONTRASEÑA")`, sustituyendo el nombre de usuario y la contraseña convertidos en mayúsculas.

2. Calcule `h2 = SHA1(salt || h1)`, dónde || es la concatenación (el operador . en PHP).

**NOTA:** ¡Tanto `salt` como `h1` son cadenas binarias, no hexadecimales!

3. Tratar `h2` como un entero en orden little-endian (el primer byte es el menos significativo).

4. Calcule `(g ^ h2) % N`.

**NOTA:** `g` y `N` son parámetros, que están fijados en la implementación de WoW.

`g = 7`

`N = 0x894B645E89E1535BBDAD5B8B290650530801B18EBFBF5E8FAB3C82872A3E9BB7`

5. Convierte el resultado en una matriz de bytes en orden little-endian.

**Para implementaciones de PHP**

¡Asegúrese de que la extensión PHP GMP esté cargada! Descomente `extension=gmp` en su php.ini.

[CalculateSRP6Verifier.php](https://gist.github.com/Treeston/db44f23503ae9f1542de31cb8d66781e)

[GetSRP6RegistrationData.php](https://gist.github.com/Treeston/40b99dd71f55d55c68857919088b2e41)

[VerifySRP6Login.php](https://gist.github.com/Treeston/34d9249fb467dddc11b2568e74f8cb1e)

### session_key

`campo-sin-descripción|5`

### token_key

La clave del autentificador.

La clave puede generarse a través de la API de Google Authenticator, un generador TOTP de terceros, o especificarse manualmente (debe ser una expresión compatible con Base32 de 16 caracteres).

Enlace de implementación en Wikipedia para la API de Google Authenticator

<https://es.wikipedia.org/wiki/Google_Authenticator#Implementaciones>

### email

La dirección de correo electrónico asociada a esta cuenta.

### reg_mail

La dirección de correo electrónico de registro asociada a esta cuenta.

### joindate

La fecha de creación de la cuenta.

### last_ip

La última IP utilizada por la persona que se conectó a la cuenta.

### failed_logins

El número de inicios de sesión fallidos en la cuenta.

### locked

Booleano 0 o 1 que controla si la cuenta ha sido bloqueada o no. Esto se puede controlar con el comando GM ".account lock". Si está bloqueada (1), el usuario sólo puede iniciar sesión con su [last_ip][11]. Si está desbloqueado (0), el usuario puede conectarse desde cualquier IP, y su last_ip se actualizará si es diferente. ".Ban account" no la bloquea.

### last_login

La fecha en la que se inició sesión por última vez.

### totaltime

Tiempo total jugado en todos los personajes de un jugador. Incluso en personajes borrados que ya no se encuentran en la base de datos.
Almacenado en tiempo Unix.

### online

Booleano 0 o 1 que controla si la cuenta está actualmente conectada y en línea.

### expansion

Entero 0, 1 o 2 que controla si el cliente conectado a la cuenta tiene alguna otra expansión. (por ejemplo, si el cliente es TBC ( 1 ), pero la expansión está configurada como 0 ( vanilla ), no podrá entrar en Terrallende, etc.)

| Valor | Expansión                      |
| ----- | ------------------------------ |
| 0     | Classic                        |
| 1     | The Burning Crusade (TBC)      |
| 2     | Wrath of the Lich King (WotLK) |

### mutetime

La hora, en tiempo Unix, en la que la cuenta será desmuteada. Para ver cuándo expirará el silenciamiento puedes usar esta consulta:

```sql
SELECT FROM_UNIXTIME(`mutetime`);
```

### mutereason

La razón del muteo.

### muteby

El nombre del personaje con los derechos o el poder sobre el comando .mute que da el silenciamiento.

### locale

La configuración regional utilizada por el cliente conectado a esta cuenta. Si se han configurado y añadido múltiples datos de localización a los servidores mundiales, éstos devolverán al cliente las cadenas de localización adecuadas. Ver [IDs de localización](es/Localization_lang)

### os

Almacena información sobre el sistema operativo del cliente. Utilizado por el sistema Warden.

- Win
- Mac

### recruiter

El ID de otra cuenta asociada a esta cuenta. Se utiliza para el sistema de "recuit-a-friend" (reclutar un amigo). Ver [account.id][1]