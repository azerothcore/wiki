# RBAC

[<-Back-to:Documentation Index](documentation-index)

## Overview

Role-Based Access Control (RBAC) is AzerothCore's permission system. It provides fine-grained control over what each account can do — from individual commands to gameplay privileges like skipping the login queue or joining battlegrounds.

With RBAC you can:

- Control access to every command individually
- Create roles that bundle related permissions together
- Override specific permissions per account without changing their overall rank
- Let modules register their own permissions without conflicting with core IDs

## Architecture

The RBAC system is built on four concepts:

1. **Permissions** — Individual capabilities (e.g. "can use `.tele`", "skip queue", "join battlegrounds")
2. **Roles** — Permissions that link to other permissions, forming a group. Granting a role grants everything it contains
3. **Defaults** — Mappings from `account_access.gmlevel` to an initial RBAC role, so security levels map to permission sets automatically
4. **Account Overrides** — Per-account grants or denies that fine-tune access beyond the defaults

### Database Tables

| Table | Purpose |
| ----- | ------- |
| [rbac_permissions](rbac_permissions) | Defines all available permissions |
| [rbac_linked_permissions](rbac_linked_permissions) | Links roles to their child permissions |
| [rbac_default_permissions](rbac_default_permissions) | Maps security levels to default roles |
| [rbac_account_permissions](rbac_account_permissions) | Per-account overrides (grant/deny) |
| [module_rbac_permissions](module_rbac_permissions) | Module-registered permissions |

A convenience view `vw_rbac` joins the linked and default tables for easier querying.

## Permission ID Ranges

| Range | Purpose | Examples |
| ----- | ------- | ------- |
| 1–53 | Gameplay permissions | Instant logout, skip queue, join BG/arena/dungeon finder |
| 192–195 | Security-level roles | Administrator (192), Gamemaster (193), Moderator (194), Player (195) |
| 196–199 | Command roles | Admin Commands (196), GM Commands (197), Mod Commands (198), Player Commands (199) |
| 200–924 | Individual command permissions | One per `.command` |
| 100000+ | Module permissions | Auto-assigned via [module_rbac_permissions](module_rbac_permissions) |

## Role Hierarchy

Roles inherit from each other through linked permissions. Each higher role links to the one below it, so an Administrator automatically receives every permission a Player has.

```
Administrator (192)
├── Core admin perms (7, 21, 42, 43)
├── Admin Commands (196)
└── Gamemaster (193)
    ├── Core GM perms (45, 48, 52, 53)
    ├── GM Commands (197)
    └── Moderator (194)
        ├── Core mod perms (1, 2, 9, 11, 13–47, 51, ...)
        ├── Mod Commands (198)
        └── Player (195)
            ├── Core player perms (3, 4, 5, 6, 24, 49, 50)
            └── Player Commands (199)
```

### Default Security Level Mapping

When a player logs in, their `account_access.gmlevel` determines which role they receive:

| gmlevel | Role | Permission ID |
| ------- | ---- | ------------- |
| 3 | Administrator | 192 |
| 2 | Gamemaster | 193 |
| 1 | Moderator | 194 |
| 0 | Player | 195 |

These defaults are stored in [rbac_default_permissions](rbac_default_permissions).

## Permission Resolution

When an account's permissions are calculated, the following steps occur:

1. **Collect grants** — Account-specific grants from [rbac_account_permissions](rbac_account_permissions) plus defaults from [rbac_default_permissions](rbac_default_permissions)
2. **Expand grants** — Each granted permission is expanded recursively through [rbac_linked_permissions](rbac_linked_permissions). If permission 192 links to 193, and 193 links to 194, all are included
3. **Collect denies** — Account-specific denies from [rbac_account_permissions](rbac_account_permissions)
4. **Expand denies** — Denied permissions are also expanded through linked permissions
5. **Subtract** — Final permissions = Expanded Grants − Expanded Denies

This means denying a role denies everything that role contains.

## Commands

The `.rbac` commands allow live management of account permissions without restarting the server.

| Command | Permission | Description |
| ------- | ---------- | ----------- |
| `.rbac account list <account>` | 202 | List granted, denied, and default permissions for an account |
| `.rbac account grant <account> <permId> [realmId]` | 203 | Grant a permission to an account |
| `.rbac account deny <account> <permId> [realmId]` | 204 | Deny a permission for an account |
| `.rbac account revoke <account> <permId> [realmId]` | 205 | Revoke a previously granted or denied permission |
| `.rbac list [permId]` | 206 | List all permissions, or show details for a specific permission |

Changes take effect immediately for online players.

## Module Integration

Modules can register their own RBAC permissions using the [module_rbac_permissions](module_rbac_permissions) table. Each module uses local IDs (1, 2, 3, ...) that are automatically mapped to global IDs starting at 100000, avoiding conflicts with core permission IDs and between modules.

See [module_rbac_permissions](module_rbac_permissions) for the full integration guide.
