# module\_rbac\_permissions

[<-Back-to:Auth](database-auth)

**The \`module\_rbac\_permissions\` table**

This table allows modules to register their own RBAC permissions without risk of ID collisions with core permissions or other modules. Each module uses local IDs (1, 2, 3, ...) and the table auto-assigns global IDs starting at 100000.

For a system overview, see [RBAC](rbac).

**Table Structure**

| Field          | Type         | Attributes | Key    | Null | Default | Extra          | Comment                              |
| -------------- | ------------ | ---------- | ------ | ---- | ------- | -------------- | ------------------------------------ |
| [module][1]    | VARCHAR(255) | SIGNED     | PRI    | NO   |         |                | Module dir name, e.g. mod-cfbg       |
| [id][2]        | INT          | UNSIGNED   | PRI    | NO   |         |                | Module-local permission id           |
| [global_id][3] | INT          | UNSIGNED   | UNIQUE | NO   |         | AUTO_INCREMENT | Auto-assigned global permission ID   |
| [name][4]      | VARCHAR(100) | SIGNED     |        | NO   |         |                | Permission name                      |

[1]: #module
[2]: #id
[3]: #global_id
[4]: #name

The primary key is the composite `(module, id)`, which prevents cross-module ID collisions. The `global_id` column has a separate `UNIQUE` index and auto-increments starting at 100000.

**Description of the fields**

### module

The module directory name (e.g. `mod-cfbg`, `mod-eluna`). This must match the module's directory name under `modules/`.

### id

A module-local permission ID. Each module manages its own ID sequence starting at 1. The same local ID can be used by different modules without conflict because the primary key includes the module name.

### global\_id

An auto-assigned globally unique permission ID used by the core RBAC system. The `AUTO_INCREMENT` starts at 100000 to avoid collisions with core permission IDs (1–924). Modules should never set this value manually — it is assigned by the database on insert.

### name

A human-readable name for the permission. By convention, command permissions use the format `Command: .commandname subcommand`.

## Module Integration Guide

### Step 1: Register permissions in SQL

Create a SQL file in your module's `data/sql/db-auth/` directory:

```sql
INSERT IGNORE INTO `module_rbac_permissions` (`module`, `id`, `name`) VALUES
('mod-example', 1, 'Command: .example hello'),
('mod-example', 2, 'Command: .example info');
```

Use `INSERT IGNORE` so the SQL is safe to re-run.

### Step 2: Look up global IDs in C++

In your module's C++ code, use `AccountMgr` to translate local IDs to global IDs:

```cpp
#include "AccountMgr.h"

uint32 globalId = sAccountMgr->GetModulePermission("mod-example", 1);
```

Returns 0 if the permission is not found in the database.

### Step 3: Use in CommandScript

When defining commands, use the global ID as the permission for each command:

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

### Step 4: Assign to roles

To make your module commands available to specific roles, insert into [rbac_linked_permissions](rbac_linked_permissions) using a subquery to resolve the global ID:

```sql
-- Grant mod-example commands to GM role (197)
INSERT IGNORE INTO `rbac_linked_permissions` (`id`, `linkedId`)
SELECT 197, `global_id`
FROM `module_rbac_permissions`
WHERE `module` = 'mod-example';
```
