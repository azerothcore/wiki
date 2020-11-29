# account

[<-Back-to:Auth](database-auth.md)

**The \`account\` table**

This table holds information on all available accounts.

## Structure

| Field               | Type         | Attributes | Key | Null | Default             | Extra          | Comment    |
|---------------------|--------------|------------|-----|------|---------------------|----------------|------------|
| [id][1]             | int(10)      | unsigned   | PRI | NO   |                     | Auto increment | Identifier |
| [username][2]       | varchar(32)  |            | UNI | NO   | ''                  |                |            |
| [sha_pass_hash][3]  | varchar(40)  |            |     | NO   | ''                  |                |            |
| [sessionkey][4]     | varchar(80)  |            |     | NO   | ''                  |                |            |
| [v][5]              | varchar(64)  |            |     | NO   | ''                  |                |            |
| [s][6]              | varchar(64)  |            |     | NO   | ''                  |                |            |
| [token_key][7]      | varchar(100) |            |     | NO   | ''                  |                |            |
| [email][8]          | varchar(255) |            |     | NO   | ''                  |                |            |
| [reg_mail][9]       | varchar(255) |            |     | NO   | ''                  |                |            |
| [joindate][10]      | timestamp    | signed     |     | NO   | CURRENT_TIMESTAMP   |                |            |
| [last_ip][11]       | varchar(15)  |            |     | NO   | 127.0.0.1           |                |            |
| [failed_logins][12] | int(10)      | unsigned   |     | NO   | 0                   |                |            |
| [locked][13]        | tinyint(3)   | unsigned   |     | NO   | 0                   |                |            |
| [last_login][14]    | timestamp    | signed     |     | NO   | 0000-00-00 00:00:00 |                |            |
| [totaltime][15]     | int(10)      | unsigned   |     | NO   | 0                   |                |            |
| [online][16]        | tinyint(3)   | signed     |     | NO   | 0                   |                |            |
| [expansion][17]     | tinyint(3)   | unsigned   |     | NO   | 2                   |                |            |
| [mutetime][18]      | bigint(20)   | signed     |     | NO   | 0                   |                |            |
| [mutereason][19]    | varchar(255) | signed     |     | NO   | ''                  |                |            |
| [muteby][20]        | varchar(50)  | signed     |     | NO   | ''                  |                |            |
| [locale][21]        | tinyint(3)   | unsigned   |     | NO   | 0                   |                |            |
| [os][22]            | varchar(3)   | signed     |     | NO   | ''                  |                |            |
| [recruiter][23]     | int(10)      | unsigned   |     | NO   | 0                   |                |            |


[1]: #id
[2]: #username
[3]: #sha_pass_hash
[4]: #sessionkey
[5]: #v
[6]: #s
[7]: #token_key
[8]: #email
[9]: #reg_mail
[10]: #joindate
[11]: #last_ip
[12]: #failed_logins
[13]: #locked
[14]: #last_login
[15]: #totaltime
[16]: #online
[17]: #expansion
[18]: #mutetime
[19]: #mutereason
[20]: #muteby
[21]: #locale
[22]: #os
[23]: #recruiter


## Description of the fields

### id

The unique account ID.

### username

The user's account name.

**NOTE**: usernames are limited to 20 characters and have no character restriction.

### sha\_pass\_hash

This field contains the encrypted password. The encryption is SHA1 and is in the following format: username:password. The SQL to create the password (or to compare with the current hash) is:

| Language | Code                                                                |
|----------|---------------------------------------------------------------------|
| SQL      | UPPER(SHA1(CONCAT(UPPER('myusername'), ':', UPPER('mypass'))));     |
| PHP      | strtoupper(sha1(strtoupper($username).':'.strtoupper($password)));  |

**NOTE**: Passwords are limited to 16 characters and have no character restriction.

### sessionkey

`field-no-description|5`

### v
### s

`v` and `s` fields are used by server authentication system since the client uses a SRP6 protocol to handle authentication

If you change the password these fields must be set to 0 allowing the server to regenerate them at login. 
The .account password command already does it, but you must take care about it on external registration systems (web client)

### **token\_key**

The authenticator key.

Key can be generated through the Google Authenticator API, a 3rd-party TOTP generator, or manually specified (must be a Base32-compliant expression that is 16 characters).

Implementation link on Wikipedia for the Google Authenticator API

<http://en.wikipedia.org/wiki/Google_Authenticator#Implementations>

### email

The e-mail address associated with this account.

### reg\_mail

The registration e-mail address associated with this account.

### joindate

The date when the account was created.

### last\_ip

The last IP used by the person who logged in the account.

### failed\_logins

The number of failed logins attempted on the account.

### locked

Boolean 0 or 1 controlling if the account has been locked or not. This can be controlled with the ".account lock" GM command. If locked (1), the user can only log in with their [last\_ip](#account-last_ip). If unlocked (0), a user can log in from any IP, and their last\_ip will be updated if it is different. ".Ban account" does not lock it.

### last\_login

The date when the account was last logged into.

### totaltime

Total time played on all the characters of a player. Even the deleted characters that are no longer in the database.
Stored in Unix Time.

### online

Boolean 0 or 1 controlling if the account is currently logged in and online.

### expansion

Integer 0, 1 or 2 controlling if the client logged in on the account has any expansions. (for example if client is TBC, but expansion is set to 0, it will not be able to enter outlands and etc.)

-   0 = Classic
-   1 = The Burning Crusade (TBC)
-   2 = Wrath of the Lich King (WotLK)
-   3 = Cataclysm
-   4 = Mist of Pandaria (MOP)
-   5 = Warlords of Draenor (WOD)
-   6 = Legion

### mutetime

The time, in Unix time, when the account will be unmuted. To see when mute will be expired you can use this query:

``` cpp
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

-   Win
-   Mac

### recruiter

The account ID of another account. Used for recuit-a-friend system. See [account.id](account#id)
