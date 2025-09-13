# account

[<-Volver a: Auth](database-auth)

**Tabla \`account\`**

`table-no-description`

**Estructura**

| Campo                             | Tipo           | Atributos | Llave | Null | por defecto       | Extra          | Comentario           |
| --------------------------------- | -------------- | --------- | ----  | ---- | ----------------- | -------------- | -------------------- |
| [id](#id)                         | INT            | UNSIGNED  | PRI   | NO   |                   | AUTO_INCREMENT | Identifier           |
| [username](#username)             | VARCHAR(32)    |           | UNI   | NO   | ''                |                |                      |
| [salt](#salt)                     | BINARY(32)     |           |       | NO   |                   |                |                      |
| [verifier](#verifier)             | BINARY(32)     |           |       | NO   |                   |                |                      |
| [session_key](#sessionkey)        | BINARY(40)     |           |       | YES  |                   |                |                      |
| [totp_secret](#totpsecret)        | VARBINARY(100) |           |       | YES  |                   |                |                      |
| [email](#email)                   | VARCHAR(255)   |           |       | NO   | ''                |                |                      |
| [reg_mail](#regmail)              | VARCHAR(255)   |           |       | NO   | ''                |                |                      |
| [joindate](#joindate)             | TIMESTAMP      |           |       | NO   | CURRENT_TIMESTAMP |                |                      |
| [last_ip](#lastip)                | VARCHAR(15)    |           |       | NO   | 127.0.0.1         |                |                      |
| [last_attempt_ip](#lastattemptip) | VARCHAR(15)    |           |       | NO   | 127.0.0.1         |                |                      |
| [failed_logins](#failedlogins)    | INT            | UNSIGNED  |       | NO   | 0                 |                |                      |
| [locked](#locked)                 | TINYINT        | UNSIGNED  |       | NO   | 0                 |                |                      |
| [lock_country](#lockcountry)      | VARCHAR(2)     |           |       | NO   | 00                |                |                      |
| [last_login](#lastlogin)          | TIMESTAMP      |           |       | YES  |                   |                |                      |
| [online](#online)                 | INT            | UNSIGNED  |       | NO   | 0                 |                |                      |
| [expansion](#expansion)           | TINYINT        | UNSIGNED  |       | NO   | 2                 |                |                      |
| [Flags](#flags)                   | INT            | UNSIGNED  |       | NO   | 0                 |                | Banderas de cuenta   |
| [mutetime](#mutetime)             | BIGINT         |           |       | NO   | 0                 |                |                      |
| [mutereason](#mutereason)         | VARCHAR(255)   |           |       | NO   | ''                |                |                      |
| [muteby](#muteby)                 | VARCHAR(50)    |           |       | NO   | ''                |                |                      |
| [locale](#locale)                 | TINYINT        | UNSIGNED  |       | NO   | 0                 |                |                      |
| [os](#os)                         | VARCHAR(3)     |           |       | NO   | ''                |                |                      |
| [recruiter](#recruiter)           | INT            | UNSIGNED  |       | NO   | 0                 |                |                      |
| [totaltime](#totaltime)           | INT            | UNSIGNED  |       | NO   | 0                 |                |                      |

[1]: #id
[2]: #username
[3]: #salt
[4]: #verifier
[5]: #session_key
[6]: #totp_secret
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
[18]: #flags
[19]: #mutetime
[19]: #mutereason
[20]: #muteby
[21]: #locale
[22]: #os
[23]: #recruiter
[24]: #totaltime

**Descripción de los campos**

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

1. Calcular `h1 = SHA1("USUARIO:CONTRASEÑA")`, sustituyendo el nombre de usuario y la contraseña convertidos en mayúsculas.

2. Calcular `h2 = SHA1(salt || h1)`, dónde || es la concatenación (el operador . en PHP).

**NOTA:** ¡Tanto `salt` como `h1` son cadenas binarias, no hexadecimales!

3. Tratar `h2` como un entero en orden little-endian (el primer byte es el menos significativo).

4. Calcular `(g ^ h2) % N`.

**NOTA:** `g` y `N` son parámetros, que están fijados en la implementación de WoW.

`g = 7`

`N = 0x894B645E89E1535BBDAD5B8B290650530801B18EBFBF5E8FAB3C82872A3E9BB7`

5. Convierte el resultado en una matriz de bytes en orden little-endian.

**Para implementaciones de PHP**

¡Asegúrese de que la extensión PHP GMP esté cargada! Descomente `extension=gmp` en su php.ini.

[CalculateSRP6Verifier.php](https://gist.github.com/Treeston/db44f23503ae9f1542de31cb8d66781e)

[GetSRP6RegistrationData.php](https://gist.github.com/Treeston/40b99dd71f55d55c68857919088b2e41)

[VerifySRP6Login.php](https://gist.github.com/Treeston/34d9249fb467dddc11b2568e74f8cb1e)

### session\_key

`campo-sin-descripción|5`

### totp\_secret

La clave del autentificador.

La clave puede generarse a través de la API de Google Authenticator, un generador TOTP de terceros, o especificarse manualmente (debe ser una expresión compatible con Base32 de 16 caracteres).

Enlace de implementación en Wikipedia para la API de Google Authenticator

<https://es.wikipedia.org/wiki/Google_Authenticator#Implementaciones>

### email

La dirección de correo electrónico asociada a esta cuenta.

### reg\_mail

La dirección de correo electrónico de registro asociada a esta cuenta.

### joindate

La fecha de creación de la cuenta.

### last\_ip

La última IP utilizada por la persona que se conectó a la cuenta.

### last\_attempt\_ip
** PARA RELLENAR **

### failed\_logins

El número de inicios de sesión fallidos en la cuenta.

### locked

Booleano 0 o 1 que controla si la cuenta ha sido bloqueada o no. Esto se puede controlar con el comando GM ".account lock". Si está bloqueada (1), el usuario sólo puede iniciar sesión con su [last_ip][11]. Si está desbloqueado (0), el usuario puede conectarse desde cualquier IP, y su last_ip se actualizará si es diferente. ".Ban account" no la bloquea.

### locked\_country

** PARA RELLENAR **

### last\_login

La fecha en la que se inició sesión por última vez.

### online

Booleano 0 o 1 que controla si la cuenta está actualmente conectada y en línea.

### expansion

Entero 0, 1 o 2 que controla si el cliente conectado a la cuenta tiene alguna otra expansión. (por ejemplo, si el cliente es TBC ( 1 ), pero la expansión está configurada como 0 ( vanilla ), no podrá entrar en Terrallende, etc.)

| Valor | Expansión                      |
| ----- | ------------------------------ |
| 0     | Classic                        |
| 1     | The Burning Crusade (TBC)      |
| 2     | Wrath of the Lich King (WotLK) |

### Flags

| Nombre                            | Descripción                                       | Valor de bit  |
| --------------------------------- | ------------------------------------------------- | ------------- |
| ACCOUNT_FLAG_GM                   | La cuenta es GM                                   | 1             |
| ACCOUNT_FLAG_NOKICK               | DESCONOCIDO                                       | 2             |
| ACCOUNT_FLAG_COLLECTOR            | Edición de coleccionista                          | 4             |
| ACCOUNT_FLAG_TRIAL                | Cuenta de prueba                                  | 8             |
| ACCOUNT_FLAG_CANCELLED            | DESCONOCIDO                                       | 16            |
| ACCOUNT_FLAG_IGR                  | Sala de juegos de Internet (¿cibercafé?)          | 32            |
| ACCOUNT_FLAG_WHOLESALER           | DESCONOCIDO                                       | 64            |
| ACCOUNT_FLAG_PRIVILEGED           | DESCONOCIDO                                       | 128           |
| ACCOUNT_FLAG_EU_FORBID_ELV        | DESCONOCIDO                                       | 256           |
| ACCOUNT_FLAG_EU_FORBID_BILLING    | DESCONOCIDO                                       | 512           |
| ACCOUNT_FLAG_RESTRICTED           | DESCONOCIDO                                       | 1024          |
| ACCOUNT_FLAG_REFERRAL             | Recluta-un-amigo (referente o árbitro)            | 2048          |
| ACCOUNT_FLAG_BLIZZARD             | DESCONOCIDO                                       | 4096          |
| ACCOUNT_FLAG_RECURRING_BILLING    | DESCONOCIDO                                       | 8192          |
| ACCOUNT_FLAG_NOELECTUP            | DESCONOCIDO                                       | 16384         |
| ACCOUNT_FLAG_KR_CERTIFICATE       | ¿Certificado coreano?                             | 32768         |
| ACCOUNT_FLAG_EXPANSION_COLLECTOR  | TBC Edición de coleccionista                      | 65536         |
| ACCOUNT_FLAG_DISABLE_VOICE        | No puedo unirme al chat de voz                    | 131072        |
| ACCOUNT_FLAG_DISABLE_VOICE_SPEAK  | No puedo hablar en el chat de voz                 | 262144        |  
| ACCOUNT_FLAG_REFERRAL_RESURRECT   | Pergamino de la Resurrección                      | 524288        |
| ACCOUNT_FLAG_EU_FORBID_CC         | DESCONOCIDO                                       | 1048576       |
| ACCOUNT_FLAG_OPENBETA_DELL        | Promoción de la edición Dell XPS WoW              | 2097152       |
| ACCOUNT_FLAG_PROPASS              | DESCONOCIDO                                       | 4194304       |
| ACCOUNT_FLAG_PROPASS_LOCK         | Pase Pro (Torneo Arena)                           | 8388608       |
| ACCOUNT_FLAG_PENDING_UPGRADE      | DESCONOCIDO                                       | 16777216      |
| ACCOUNT_FLAG_RETAIL_FROM_TRIAL    | DESCONOCIDO                                       | 33554432      |
| ACCOUNT_FLAG_EXPANSION2_COLLECTOR | WotLK Edición de coleccionista                    | 67108864      |
| ACCOUNT_FLAG_OVERMIND_LINKED      | Vinculado con la cuenta de Battle.net             | 134217728     |
| ACCOUNT_FLAG_DEMOS                | DESCONOCIDO                                       | 268435456     |
| ACCOUNT_FLAG_DEATH_KNIGHT_OK      | Permitido crear Caballero de la Muerte            | 536870912     |
| ACCOUNT_FLAG_S2_REQUIRE_IGR       | DESCONOCIDO (¿Está relacionado con StarCraft II?) | 1073741824    |
| ACCOUNT_FLAG_S2_TRIAL             | DESCONOCIDO (¿Está relacionado con StarCraft II?) | 2147483648    |

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

### totaltime

Tiempo total jugado en todos los personajes de un jugador. Incluso en personajes borrados que ya no se encuentran en la base de datos.
Almacenado en tiempo Unix.