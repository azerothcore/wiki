# rbac\_permissions

[<-Volver a:Auth](database-auth)

**Tabla \`rbac\_permissions\`**

Esta tabla define todos los permisos RBAC disponibles. Cada permiso representa una única capacidad — un privilegio de juego, un comando, o un rol que agrupa otros permisos.

Para una visión general del sistema, consulta [RBAC](rbac).

**Estructura**

| Field    | Type         | Attributes | Key | Null | Default | Extra | Comment       |
| -------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------- |
| [id](#id)     | INT          | UNSIGNED   | PRI | NO   | 0       |       | Permission id   |
| [name](#name) | VARCHAR(100) | SIGNED     |     | NO   |         |       | Permission name |

**Descripción de los campos**

### id

El identificador único del permiso. Los rangos de ID son:

| Range | Propósito |
| ----- | ------- |
| 1–53 | Permisos de juego (cierre de sesión instantáneo, saltar cola, unirse a BG, etc.) |
| 192–195 | Roles de nivel de seguridad (Administrator, Gamemaster, Moderator, Player) |
| 196–199 | Roles de comandos (Admin Commands, GM Commands, Mod Commands, Player Commands) |
| 200–925 | Permisos de comandos individuales (uno por `.command`) |
| 100000+ | Permisos de módulos (asignados automáticamente vía [module_rbac_permissions](module_rbac_permissions)) |

### name

Un nombre legible que describe el permiso. Sigue estas convenciones:

- Permisos de juego: nombre descriptivo (p. ej. `Instant logout`, `Skip Queue`)
- Roles: con el prefijo `Role:` (p. ej. `Role: Sec Level Administrator`)
- Comandos: con el prefijo `Command:` (p. ej. `Command: rbac account list`)
