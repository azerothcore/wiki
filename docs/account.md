# account

[<-Back-to:Auth](database-auth.md)

**The \`account\` table**

**Structure**

| Field                 | Type          | Attributes | Key | Null | Default           | Extra          | Comment    |
| --------------------- | ------------- | ---------- | --- | ---- | ----------------- | -------------- | ---------- |
| [id][1]               | INT           | UNSIGNED   | PRI | NO   |                   | AUTO_INCREMENT | Identifier |
| [username][2]         | VARCHAR(32)   | SIGNED     | UNI | NO   | ''                |                |            |
| [salt][3]             | BINARY(32)    | SIGNED     |     | NO   |                   |                |            |
| [verifier][4]         | BINARY(32)    | SIGNED     |     | NO   |                   |                |            |
| [session_key][5]      | BINARY(40)    | SIGNED     |     | YES  |                   |                |            |
| [totp_secret][6]      | VARBINARY(100)| SIGNED     |     | YES  |                   |                |            |
| [email][7]            | VARCHAR(255)  | SIGNED     |     | NO   | ''                |                |            |
| [reg_mail][8]         | VARCHAR(255)  | SIGNED     |     | NO   | ''                |                |            |
| [joindate][9]         | TIMESTAMP     | SIGNED     |     | NO   | CURRENT_TIMESTAMP |                |            |
| [last_ip][10]         | VARCHAR(15)   | SIGNED     |     | NO   | 127.0.0.1         |                |            |
| [last_attempt_ip][11] | VARCHAR(15)   | SIGNED     |     | NO   | 127.0.0.1         |                |            |
| [failed_logins][12]   | INT           | UNSIGNED   |     | NO   | 0                 |                |            |
| [locked][13]          | TINYINT       | UNSIGNED   |     | NO   | 0                 |                |            |
| [lock_country][14]    | VARCHAR(2)    | SIGNED     |     | NO   | 00                |                |            |
| [last_login][15]      | TIMESTAMP     | SIGNED     |     | YES  |                   |                |            |
| [online][16]          | INT           | UNSIGNED   |     | NO   | 0                 |                |            |
| [expansion][17]       | TINYINT       | UNSIGNED   |     | NO   | 2                 |                |            |
| [mutetime][18]        | BIGINT        | SIGNED     |     | NO   | 0                 |                |            |
| [mutereason][19]      | VARCHAR(255)  | SIGNED     |     | NO   | ''                |                |            |
| [muteby][20]          | VARCHAR(50)   | SIGNED     |     | NO   | ''                |                |            |
| [locale][21]          | TINYINT       | UNSIGNED   |     | NO   | 0                 |                |            |
| [os][22]              | VARCHAR(3)    | SIGNED     |     | NO   | ''                |                |            |
| [recruiter][23]       | INT           | UNSIGNED   |     | NO   | 0                 |                |            |
| [totaltime][24]       | INT           | UNSIGNED   |     | NO   | 0                 |                |            |

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
[18]: #mutetime
[19]: #mutereason
[20]: #muteby
[21]: #locale
[22]: #os
[23]: #recruiter
[24]: #totaltime

## Description of the fields

### id

The unique account ID.

### username

The user's account name.

**NOTE:** usernames are limited to 20 characters and have no character restriction.

### salt

salt is a cryptographically random 32-byte value.

### verifier

verifier is derived from salt, as well as the user's username (all uppercase) and their password (all uppercase).

To obtain the verifier you need to calculate:

1. Calculate `h1 = SHA1("USERNAME:PASSWORD")`, substituting the user's username and password converted to uppercase.

2. Calculate `h2 = SHA1(salt || h1)`, where || is concatenation (the . operator in PHP).

**NOTE:** Both `salt` and `h1` are binary, not hexadecimal strings!

3. Treat `h2` as an integer in little-endian order (the first byte is the least significant).

4. Calculate `(g ^ h2) % N`.

**NOTE:** `g` and `N` are parameters, which are fixed in the WoW implementation.

`g = 7`

`N = 0x894B645E89E1535BBDAD5B8B290650530801B18EBFBF5E8FAB3C82872A3E9BB7`

5. Convert the result back to a byte array in little-endian order.

**For PHP implementations**

Make sure the PHP GMP extension is loaded! Uncomment `extension=gmp` in your php.ini.

[CalculateSRP6Verifier.php](https://gist.github.com/Treeston/db44f23503ae9f1542de31cb8d66781e)

[GetSRP6RegistrationData.php](https://gist.github.com/Treeston/40b99dd71f55d55c68857919088b2e41)

[VerifySRP6Login.php](https://gist.github.com/Treeston/34d9249fb467dddc11b2568e74f8cb1e)

### session_key

`field-no-description|5`

### totp_secret

The authenticator key.

Key can be generated through the Google Authenticator API, a 3rd-party TOTP generator, or manually specified (must be a Base32-compliant expression that is 16 characters).

Implementation link on Wikipedia for the Google Authenticator API

<http://en.wikipedia.org/wiki/Google_Authenticator#Implementations>

### email

The e-mail address associated with this account.

### reg_mail

The registration e-mail address associated with this account.

### joindate

The date when the account was created.

### last_ip

The last IP used by the person who logged in the account.

### failed_logins

The number of failed logins attempted on the account.

### locked

Boolean 0 or 1 controlling if the account has been locked or not. This can be controlled with the ".account lock" GM command. If locked (1), the user can only log in with their [last_ip][11]. If unlocked (0), a user can log in from any IP, and their last_ip will be updated if it is different. ".Ban account" does not lock it.

### last_login

The date when the account was last logged into.

### totaltime

Total time played on all the characters of a player. Even the deleted characters that are no longer in the database.
Stored in Unix Time.

### online

Boolean 0 or 1 controlling if the account is currently logged in and online.

### expansion

Integer 0, 1 or 2 controlling if the client logged in on the account has any expansions. (for example if client is TBC, but expansion is set to 0, it will not be able to enter outlands and etc.)

| Value | Expansion                      |
| ----- | ------------------------------ |
| 0     | Classic                        |
| 1     | The Burning Crusade (TBC)      |
| 2     | Wrath of the Lich King (WotLK) |

### mutetime

The time, in Unix time, when the account will be unmuted. To see when mute will be expired you can use this query:

```sql
SELECT FROM_UNIXTIME(`mutetime`);
```

### mutereason

The reason for the mute.

### muteby

The character name with the rights to the .mute command that give the mute.

### locale

The locale used by the client logged into this account. If multiple locale data has been configured and added to the world servers, the world servers will return the proper locale strings to the client. See [localization IDs](Localization_lang)

### os

Stores information about client's OS. Used by Warden system.

- Win
- Mac

### recruiter

The account ID of another account. Used for recuit-a-friend system. See [account.id][1]
