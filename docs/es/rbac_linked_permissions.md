# rbac\_linked\_permissions

[<-Volver a:Auth](database-auth)

**Tabla \`rbac\_linked\_permissions\`**

Esta tabla define las relaciones padre-hijo entre permisos. Cuando se concede un permiso (normalmente un rol), también se conceden todos sus permisos enlazados. Así es como funciona la herencia de roles en el sistema [RBAC](rbac).

**Estructura**

| Field         | Type | Attributes | Key | Null | Default | Extra | Comment              |
| ------------- | ---- | ---------- | --- | ---- | ------- | ----- | -------------------- |
| [id](#id)             | INT  | UNSIGNED   | PRI | NO   |         |       | Permission id        |
| [linkedId](#linkedid) | INT  | UNSIGNED   | PRI | NO   |         |       | Linked Permission id |

Ambos campos tienen una clave foránea a [rbac_permissions.id](rbac_permissions#id) con `ON DELETE CASCADE`.

**Descripción de los campos**

### id

El permiso padre (rol) que contiene otros permisos. Normalmente uno de los IDs de rol:

| ID | Role |
| -- | ---- |
| 192 | Administrator |
| 193 | Gamemaster |
| 194 | Moderator |
| 195 | Player |
| 196 | Admin Commands |
| 197 | GM Commands |
| 198 | Mod Commands |
| 199 | Player Commands |

### linkedId

El permiso hijo que se concede cuando se concede el padre (`id`). Puede ser cualquier permiso de [rbac_permissions](rbac_permissions), incluido otro rol — así es como se encadena la jerarquía (p. ej. Administrator 192 enlaza con Gamemaster 193, que enlaza con Moderator 194, y así sucesivamente).

Los permisos enlazados se expanden recursivamente durante la [resolución de permisos](rbac#permission-resolution).
