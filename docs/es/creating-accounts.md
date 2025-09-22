---
redirect_from: "/es/Creating-Accounts"
---

# Creación de cuentas

Para poder entrar en su nuevo servidor necesita una cuenta.

Se recomienda utilizar el nivel de seguridad 3 para su propia cuenta.

## Para crear una cuenta

```
account create <user> <pass>
```

**Ejemplo:**

```
account create admin admin
```

## Para establecer el nivel de seguridad de su cuenta

| Nivel | Nivel de seguridad |
|-------|--------------------|
| 0     | SEC_PLAYER         |
| 1     | SEC_MODERATOR      |
| 2     | SEC_GAMEMASTER     |
| 3     | SEC_ADMINISTRATOR  |

```
account set gmlevel <user> <level> <realm>
```

**Ejemplo:**

{% include note.html content="Si el comando se ejecutó mientras la cuenta estaba iniciada sesión, deberá volver a iniciar sesión para que el nivel de seguridad se actualice correctamente." %}

```
account set gmlevel admin 3 -1
```

**Nota:** (-1 para todos los reinos)

{% include note.html content="Utilice -1 para seleccionar todos los reinos o especificar el ID del reino específico." %}

## Cambio de contraseña

```
account set password <user> <password> <password>
```

**Ejemplo:**

```
account set password admin 1234 1234
```

## Mayor nivel de seguridad

El nivel de seguridad más alto es SEC_CONSOLE (4) que su servidor de mundos tiene por defecto.

Tiene acceso a la gestión de la cuenta y no se recomienda para las cuentas en el juego para cualquier persona que no sabe lo que está haciendo.

Para actualizar una cuenta al nivel de seguridad 4 es necesario editar manualmente los campos en la base de datos o ejecutar la siguiente consulta.

```sql
UPDATE `account_access` AS `access`
INNER JOIN `account` AS `account` ON `access`.`id` = `account`.`id`
SET `gmlevel` = 4 WHERE `username` = '<user>';
```
