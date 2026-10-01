# module\_rbac\_permissions

[<-Volver a:Auth](database-auth)

**Tabla \`module\_rbac\_permissions\`**

Esta tabla permite que los módulos registren sus propios permisos RBAC sin riesgo de colisiones de ID con los permisos del core o de otros módulos. Cada módulo usa IDs locales (1, 2, 3, ...) y la tabla asigna automáticamente IDs globales que empiezan en 100000.

Para una visión general del sistema, consulta [RBAC](rbac).

**Estructura**

| Field          | Type         | Attributes | Key    | Null | Default | Extra          | Comment                              |
| -------------- | ------------ | ---------- | ------ | ---- | ------- | -------------- | ------------------------------------ |
| [module](#module)       | VARCHAR(255) | SIGNED     | PRI    | NO   |         |                | Module dir name, e.g. mod-cfbg       |
| [id](#id)               | INT          | UNSIGNED   | PRI    | NO   |         |                | Module-local permission id           |
| [global_id](#globalid)  | INT          | UNSIGNED   | UNIQUE | NO   |         | AUTO_INCREMENT | Auto-assigned global permission ID   |
| [name](#name)           | VARCHAR(100) | SIGNED     |        | NO   |         |                | Permission name                      |

La clave primaria es la compuesta `(module, id)`, que evita las colisiones de ID entre módulos. La columna `global_id` tiene un índice `UNIQUE` separado y se autoincrementa empezando en 100000.

**Descripción de los campos**

### module

El nombre del directorio del módulo (p. ej. `mod-cfbg`, `mod-eluna`). Debe coincidir con el nombre del directorio del módulo bajo `modules/`.

### id

Un ID de permiso local del módulo. Cada módulo gestiona su propia secuencia de IDs empezando en 1. El mismo ID local puede ser usado por distintos módulos sin conflicto porque la clave primaria incluye el nombre del módulo.

### global\_id

Un ID de permiso globalmente único asignado automáticamente que usa el sistema RBAC del core. El `AUTO_INCREMENT` empieza en 100000 para evitar colisiones con los IDs de permisos del core (1–924). Los módulos nunca deberían fijar este valor manualmente — lo asigna la base de datos al insertar.

### name

Un nombre legible para el permiso. Por convención, los permisos de comando usan el formato `Command: .commandname subcommand`.

## Guía de integración de módulos

### Paso 1: Registrar los permisos en SQL

Crea un archivo SQL en el directorio `data/sql/db-auth/` de tu módulo:

```sql
INSERT IGNORE INTO `module_rbac_permissions` (`module`, `id`, `name`) VALUES
('mod-example', 1, 'Command: .example hello'),
('mod-example', 2, 'Command: .example info');
```

Usa `INSERT IGNORE` para que el SQL sea seguro de reejecutar.

### Paso 2: Consultar los IDs globales en C++

En el código C++ de tu módulo, usa `AccountMgr` para traducir los IDs locales a IDs globales:

```cpp
#include "AccountMgr.h"

uint32 globalId = sAccountMgr->GetModulePermission("mod-example", 1);
```

Devuelve 0 si el permiso no se encuentra en la base de datos.

### Paso 3: Usar en CommandScript

Al definir los comandos, usa el ID global como permiso para cada comando:

```cpp
static uint32 GetPermission(uint32 localId)
{
    return sAccountMgr->GetModulePermission("mod-example", localId);
}

std::vector<ChatCommand> GetCommands() const override
{
    static std::vector<ChatCommand> exampleCommandTable =
    {
        { "hello", GetPermission(1), false, &HandleHelloCommand, "" },
        { "info",  GetPermission(2), false, &HandleInfoCommand,  "" },
    };

    static std::vector<ChatCommand> commandTable =
    {
        { "example", SEC_PLAYER, false, nullptr, "", exampleCommandTable },
    };

    return commandTable;
}
```

### Paso 4: Asignar los permisos

Los permisos de módulo deben asignarse a roles o cuentas antes de que nadie pueda usarlos.

**Asignar a un rol** — enlaza los permisos del módulo a un rol de comandos vía [rbac_linked_permissions](rbac_linked_permissions). Todo el que herede ese rol obtendrá acceso:

```sql
-- Concede todos los comandos de mod-example al rol GM Commands (197)
INSERT IGNORE INTO `rbac_linked_permissions` (`id`, `linkedId`)
SELECT 197, `global_id`
FROM `module_rbac_permissions`
WHERE `module` = 'mod-example';
```

**Asignar a una cuenta concreta** — inserta en [rbac_account_permissions](rbac_account_permissions) o usa el comando `.rbac` dentro del juego:

```sql
-- Concede el primer comando de mod-example a la cuenta 5 en todos los realms
INSERT INTO `rbac_account_permissions` (`accountId`, `permissionId`, `granted`, `realmId`)
SELECT 5, `global_id`, 1, -1
FROM `module_rbac_permissions`
WHERE `module` = 'mod-example' AND `id` = 1;
```

O dentro del juego, una vez que conozcas el ID global (p. ej. 100001):

```
.rbac account grant 5 100001
```
