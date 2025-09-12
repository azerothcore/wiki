# account

[<-Back-to:Auth](database-auth)

**The \`account\` table**

`table-no-description`

**Table Structure**

| Field                             | Type           | Attributes | Key | Null | Default           | Extra          | Comment       |
| --------------------------------- | -------------- | ---------- | --- | ---- | ----------------- | -------------- | ------------- |
| [id](#id)                         | INT            | UNSIGNED   | PRI | NO   |                   | AUTO_INCREMENT | Identifier    |
| [username](#username)             | VARCHAR(32)    |            | UNI | NO   | ''                |                |               |
| [salt](#salt)                     | BINARY(32)     |            |     | NO   |                   |                |               |
| [verifier](#verifier)             | BINARY(32)     |            |     | NO   |                   |                |               |
| [session_key](#sessionkey)        | BINARY(40)     |            |     | YES  |                   |                |               |
| [totp_secret](#totpsecret)        | VARBINARY(100) |            |     | YES  |                   |                |               |
| [email](#email)                   | VARCHAR(255)   |            |     | NO   | ''                |                |               |
| [reg_mail](#regmail)              | VARCHAR(255)   |            |     | NO   | ''                |                |               |
| [joindate](#joindate)             | TIMESTAMP      |            |     | NO   | CURRENT_TIMESTAMP |                |               |
| [last_ip](#lastip)                | VARCHAR(15)    |            |     | NO   | 127.0.0.1         |                |               |
| [last_attempt_ip](#lastattemptip) | VARCHAR(15)    |            |     | NO   | 127.0.0.1         |                |               |
| [failed_logins](#failedlogins)    | INT            | UNSIGNED   |     | NO   | 0                 |                |               |
| [locked](#locked)                 | TINYINT        | UNSIGNED   |     | NO   | 0                 |                |               |
| [lock_country](#lockcountry)      | VARCHAR(2)     |            |     | NO   | 00                |                |               |
| [last_login](#lastlogin)          | TIMESTAMP      |            |     | YES  |                   |                |               |
| [online](#online)                 | INT            | UNSIGNED   |     | NO   | 0                 |                |               |
| [expansion](#expansion)           | TINYINT        | UNSIGNED   |     | NO   | 2                 |                |               |
| [flags](#flags)                   | INT            | UNSIGNED   |     | NO   | 0                 |                | Account Flags |
| [mutetime](#mutetime)             | BIGINT         |            |     | NO   | 0                 |                |               |
| [mutereason](#mutereason)         | VARCHAR(255)   |            |     | NO   | ''                |                |               |
| [muteby](#muteby)                 | VARCHAR(50)    |            |     | NO   | ''                |                |               |
| [locale](#locale)                 | TINYINT        | UNSIGNED   |     | NO   | 0                 |                |               |
| [os](#os)                         | VARCHAR(3)     |            |     | NO   | ''                |                |               |
| [recruiter](#recruiter)           | INT            | UNSIGNED   |     | NO   | 0                 |                |               |
| [totaltime](#totaltime)           | INT            | UNSIGNED   |     | NO   | 0                 |                |               |

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

#### For PHP implementations

Make sure the PHP GMP extension is loaded! Uncomment `extension=gmp` in your php.ini.

[CalculateSRP6Verifier.php](https://gist.github.com/Treeston/db44f23503ae9f1542de31cb8d66781e)

[GetSRP6RegistrationData.php](https://gist.github.com/Treeston/40b99dd71f55d55c68857919088b2e41)

[VerifySRP6Login.php](https://gist.github.com/Treeston/34d9249fb467dddc11b2568e74f8cb1e)

### session\_key

`field-no-description|5`

### totp\_secret

The authenticator key.

Key can be generated through the Google Authenticator API, a 3rd-party TOTP generator, or manually specified (must be a Base32-compliant expression that is 16 characters).

Implementation link on Wikipedia for the Google Authenticator API.

<http://en.wikipedia.org/wiki/Google_Authenticator#Implementations>

### email

The e-mail address associated with this account.

### reg\_mail

The registration e-mail address associated with this account.

### joindate

The date when the account was created.

### last\_ip

The last IP used by the person who logged in the account.

### last\_attempt\_ip
** TO BE FILLED IN **

### failed\_logins

The number of failed logins attempted on the account.

### locked

Boolean 0 or 1 controlling if the account has been locked or not. This can be controlled with the ".account lock" GM command. If locked (1), the user can only log in with their [last_ip][11]. If unlocked (0), a user can log in from any IP, and their last_ip will be updated if it is different. ".Ban account" does not lock it.

### locked\_country

** TO BE FILLED IN **

### last\_login

The date when the account was last logged into.

### online

Boolean 0 or 1 controlling if the account is currently logged in and online.

### expansion

Integer 0, 1 or 2 controlling if the client logged in on the account has any expansions. (for example if client is TBC, but expansion is set to 0, it will not be able to enter outlands and etc.)

| Value | Expansion                      |
| ----- | ------------------------------ |
| 0     | Classic                        |
| 1     | The Burning Crusade (TBC)      |
| 2     | Wrath of the Lich King (WotLK) |

### Flags

| Name                              | Description                           | Bit Value  |
| --------------------------------- | ------------------------------------- | ---------- |
| ACCOUNT_FLAG_GM                   | Account is GM                         | 1          |
| ACCOUNT_FLAG_NOKICK               | UNKNOWN                               | 2          |
| ACCOUNT_FLAG_COLLECTOR            | Collector's Edition                   | 4          |
| ACCOUNT_FLAG_TRIAL                | Trial account                         | 8          |
| ACCOUNT_FLAG_CANCELLED            | UNKNOWN                               | 16         |
| ACCOUNT_FLAG_IGR                  | Internet Game Room (Internet café?)   | 32         |
| ACCOUNT_FLAG_WHOLESALER           | UNKNOWN                               | 64         |
| ACCOUNT_FLAG_PRIVILEGED           | UNKNOWN                               | 128        |
| ACCOUNT_FLAG_EU_FORBID_ELV        | UNKNOWN                               | 256        |
| ACCOUNT_FLAG_EU_FORBID_BILLING    | UNKNOWN                               | 512        |
| ACCOUNT_FLAG_RESTRICTED           | UNKNOWN                               | 1024       |
| ACCOUNT_FLAG_REFERRAL             | Recruit-A-Friend (referer or referee) | 2048       |
| ACCOUNT_FLAG_BLIZZARD             | UNKNOWN                               | 4096       |
| ACCOUNT_FLAG_RECURRING_BILLING    | UNKNOWN                               | 8192       |
| ACCOUNT_FLAG_NOELECTUP            | UNKNOWN                               | 16384      |
| ACCOUNT_FLAG_KR_CERTIFICATE       | Korean certificate?                   | 32768      |
| ACCOUNT_FLAG_EXPANSION_COLLECTOR  | TBC Collector's Edition               | 65536      |
| ACCOUNT_FLAG_DISABLE_VOICE        | Can't join voice chat                 | 131072     |
| ACCOUNT_FLAG_DISABLE_VOICE_SPEAK  | Can't speak in voice chat             | 262144     |
| ACCOUNT_FLAG_REFERRAL_RESURRECT   | Scroll of Resurrection                | 524288     |
| ACCOUNT_FLAG_EU_FORBID_CC         | UNKNOWN                               | 1048576    |
| ACCOUNT_FLAG_OPENBETA_DELL        | Dell XPS WoW Edition Promotion        | 2097152    |
| ACCOUNT_FLAG_PROPASS              | UNKNOWN                               | 4194304    |
| ACCOUNT_FLAG_PROPASS_LOCK         | Pro Pass (Arena Tournament)           | 8388608    |
| ACCOUNT_FLAG_PENDING_UPGRADE      | UNKNOWN                               | 16777216   |
| ACCOUNT_FLAG_RETAIL_FROM_TRIAL    | UNKNOWN                               | 33554432   |
| ACCOUNT_FLAG_EXPANSION2_COLLECTOR | WotLK Collector's Edition             | 67108864   |
| ACCOUNT_FLAG_OVERMIND_LINKED      | Linked with Battle.net account        | 134217728  |
| ACCOUNT_FLAG_DEMOS                | UNKNOWN                               | 268435456  |
| ACCOUNT_FLAG_DEATH_KNIGHT_OK      | Allowed to create Death Knight        | 536870912  |
| ACCOUNT_FLAG_S2_REQUIRE_IGR       | UNKNOWN (StarCraft II related?)       | 1073741824 |
| ACCOUNT_FLAG_S2_TRIAL             | UNKNOWN (StarCraft II related?)       | 2147483648 |

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

### totaltime

Total time played on all the characters of a player. Even the deleted characters that are no longer in the database.
Stored in Unix Time.
