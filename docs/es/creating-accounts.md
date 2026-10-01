---
redirect_from: "/es/Creating-Accounts"
---

# Creación de cuentas

Para poder iniciar sesión en tu nuevo servidor necesitas una cuenta.

Se recomienda usar el nivel de seguridad 3 para tu propia cuenta.

Ejecuta los siguientes comandos en la consola de Worldserver.

## Para crear una cuenta

```
account create <user> <pass>
```

**Ejemplo:**

```
account create admin admin
```

## Para establecer el nivel de seguridad de tu cuenta

| Nivel | Nivel de seguridad |
|-------|-------------------|
| 0     | SEC_PLAYER        |
| 1     | SEC_MODERATOR     |
| 2     | SEC_GAMEMASTER    |
| 3     | SEC_ADMINISTRATOR |

```
account set gmlevel <user> <level> <realm>
```

{% include note.html content="Si el comando se ejecutó mientras la cuenta tenía la sesión iniciada, necesitas volver a iniciar sesión para que el nivel de seguridad se actualice correctamente." %}

**Ejemplo:**

```
account set gmlevel admin 3 -1
```

{% include note.html content="Usa -1 para seleccionar todos los reinos, o especifica el id del reino concreto." %}

## Cambiar la contraseña

```
account set password <user> <password> <password>
```

**Ejemplo:**

```
account set password admin 1234 1234
```

## Nivel de seguridad superior

El nivel de seguridad más alto es SEC_CONSOLE (4), que tu worldserver tiene por defecto.

Tiene acceso a la gestión de cuentas y no se recomienda para cuentas dentro del juego para nadie que no sepa lo que está haciendo.

Para actualizar una cuenta al nivel de seguridad 4 necesitas editar manualmente los campos en la base de datos o ejecutar la consulta de abajo.

```sql
UPDATE `account_access` AS `access`
INNER JOIN `account` AS `account` ON `access`.`id` = `account`.`id`
SET `gmlevel` = 4 WHERE `username` = '<user>';
```
