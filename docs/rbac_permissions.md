# rbac\_permissions

[<-Back-to:Auth](database-auth)

**The \`rbac\_permissions\` table**

This table defines all available RBAC permissions. Each permission represents a single capability — a gameplay privilege, a command, or a role that bundles other permissions together.

For a system overview, see [RBAC](rbac).

**Table Structure**

| Field    | Type         | Attributes | Key | Null | Default | Extra | Comment       |
| -------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------- |
| [id](#id)     | INT          | UNSIGNED   | PRI | NO   | 0       |       | Permission id   |
| [name](#name) | VARCHAR(100) | SIGNED     |     | NO   |         |       | Permission name |

**Description of the fields**

### id

The unique permission identifier. ID ranges are:

| Range | Purpose |
| ----- | ------- |
| 1–53 | Gameplay permissions (instant logout, skip queue, join BG, etc.) |
| 192–195 | Security-level roles (Administrator, Gamemaster, Moderator, Player) |
| 196–199 | Command roles (Admin Commands, GM Commands, Mod Commands, Player Commands) |
| 200–924 | Individual command permissions (one per `.command`) |
| 100000+ | Module permissions (auto-assigned via [module_rbac_permissions](module_rbac_permissions)) |

### name

A human-readable name describing the permission. Follows conventions:

- Gameplay permissions: descriptive name (e.g. `Instant logout`, `Skip Queue`)
- Roles: prefixed with `Role:` (e.g. `Role: Sec Level Administrator`)
- Commands: prefixed with `Command:` (e.g. `Command: rbac account list`)
