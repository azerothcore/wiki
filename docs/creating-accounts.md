---
redirect_from: "/Creating-Accounts"
---

# Creating Accounts

To be able to log in to your new server you need an account. 

It is recommended to use security level 3 for your own account.

## To create an account

```
account create <user> <pass>
```

## To set your account security level

| Level | Security Level |
| :---: | :------------- 
| 0 | SEC_PLAYER |
| 1 | SEC_MODERATOR |
| 2 | SEC_GAMEMASTER |
| 3 | SEC_ADMINISTRATOR |

```
account set gmlevel <user> <level> <realm> (-1 all realms)
```

## Changing password

```
account set password <user> <password> <password>
```

## Higher security level

The highest security level is SEC_CONSOLE (4) which your worlserver has by default.

It has access to account management and is not recommended for in-game accounts for anyone that does not know what they are doing.

To update an account to security level 4 you need to manually edit the fields in the database or run the query below.

```sql
UPDATE account_access AS access
INNER JOIN account AS account ON access.id = account.id
SET gmlevel = 4 WHERE name = '<user>';
```

