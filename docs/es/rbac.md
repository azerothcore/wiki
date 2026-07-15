# RBAC

[<-Volver a:Índice de documentación](documentation-index)

## Resumen

El Control de Acceso Basado en Roles (RBAC, Role-Based Access Control) es el sistema de permisos de AzerothCore. Proporciona un control detallado sobre lo que puede hacer cada cuenta — desde comandos individuales hasta privilegios de juego como saltarse la cola de inicio de sesión o unirse a campos de batalla.

Con RBAC puedes:

- Controlar el acceso a cada comando de forma individual
- Crear roles que agrupan permisos relacionados
- Sobrescribir permisos concretos por cuenta sin cambiar su rango general
- Permitir que los módulos registren sus propios permisos sin entrar en conflicto con los IDs del core

## Arquitectura

El sistema RBAC se construye sobre cuatro conceptos:

1. **Permisos** — Capacidades individuales (p. ej. "puede usar `.tele`", "saltar cola", "unirse a campos de batalla")
2. **Roles** — Permisos que enlazan con otros permisos, formando un grupo. Conceder un rol concede todo lo que contiene
3. **Predeterminados** — Correspondencias desde `account_access.gmlevel` a un rol RBAC inicial, de modo que los niveles de seguridad se mapean a conjuntos de permisos automáticamente
4. **Sobrescrituras de cuenta** — Concesiones o denegaciones por cuenta que afinan el acceso más allá de los predeterminados

### Tablas de la base de datos

| Table | Propósito |
| ----- | ------- |
| [rbac_permissions](rbac_permissions) | Define todos los permisos disponibles |
| [rbac_linked_permissions](rbac_linked_permissions) | Enlaza los roles con sus permisos hijo |
| [rbac_default_permissions](rbac_default_permissions) | Mapea los niveles de seguridad a roles predeterminados |
| [rbac_account_permissions](rbac_account_permissions) | Sobrescrituras por cuenta (conceder/denegar) |
| [module_rbac_permissions](module_rbac_permissions) | Permisos registrados por módulos |

Una vista de conveniencia `vw_rbac` une las tablas linked y default para consultarlas más fácilmente.

## Rangos de ID de permisos

| Range | Propósito | Ejemplos |
| ----- | ------- | ------- |
| 1–53 | Permisos de juego | Cierre de sesión instantáneo, saltar cola, unirse a BG/arena/buscador de mazmorras |
| 192–195 | Roles de nivel de seguridad | Administrator (192), Gamemaster (193), Moderator (194), Player (195) |
| 196–199 | Roles de comandos | Admin Commands (196), GM Commands (197), Mod Commands (198), Player Commands (199) |
| 200–925 | Permisos de comandos individuales | Uno por `.command` |
| 100000+ | Permisos de módulos | Asignados automáticamente vía [module_rbac_permissions](module_rbac_permissions) |

## Jerarquía de roles

Los roles heredan unos de otros a través de los permisos enlazados. Cada rol superior enlaza con el que tiene debajo, de modo que un Administrator recibe automáticamente todos los permisos que tiene un Player.

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

### Correspondencia predeterminada de nivel de seguridad

Cuando un jugador inicia sesión, su `account_access.gmlevel` determina qué rol recibe:

| gmlevel | Role | Permission ID |
| ------- | ---- | ------------- |
| 3 | Administrator | 192 |
| 2 | Gamemaster | 193 |
| 1 | Moderator | 194 |
| 0 | Player | 195 |

Estos predeterminados se almacenan en [rbac_default_permissions](rbac_default_permissions).

## Resolución de permisos {#permission-resolution}

Cuando se calculan los permisos de una cuenta, ocurren los siguientes pasos:

1. **Recopilar concesiones** — Concesiones específicas de la cuenta de [rbac_account_permissions](rbac_account_permissions) más los predeterminados de [rbac_default_permissions](rbac_default_permissions)
2. **Expandir concesiones** — Cada permiso concedido se expande recursivamente a través de [rbac_linked_permissions](rbac_linked_permissions). Si el permiso 192 enlaza con 193, y 193 enlaza con 194, todos se incluyen
3. **Recopilar denegaciones** — Denegaciones específicas de la cuenta de [rbac_account_permissions](rbac_account_permissions)
4. **Expandir denegaciones** — Los permisos denegados también se expanden a través de los permisos enlazados
5. **Restar** — Permisos finales = Concesiones expandidas − Denegaciones expandidas

Esto significa que denegar un rol deniega todo lo que ese rol contiene.

## Comandos {#commands}

Los comandos `.rbac` permiten gestionar en vivo los permisos de las cuentas sin reiniciar el servidor.

| Command | Permission | Descripción |
| ------- | ---------- | ----------- |
| `.rbac account list <account>` | 202 | Lista los permisos concedidos, denegados y predeterminados de una cuenta |
| `.rbac account grant <account> <permId> [realmId]` | 203 | Concede un permiso a una cuenta |
| `.rbac account deny <account> <permId> [realmId]` | 204 | Deniega un permiso a una cuenta |
| `.rbac account revoke <account> <permId> [realmId]` | 205 | Revoca un permiso concedido o denegado previamente |
| `.rbac list [permId]` | 206 | Lista todos los permisos, o muestra los detalles de un permiso concreto |

Los cambios surten efecto inmediatamente para los jugadores conectados.

## Integración con módulos

Los módulos pueden registrar sus propios permisos RBAC usando la tabla [module_rbac_permissions](module_rbac_permissions). Cada módulo usa IDs locales (1, 2, 3, ...) que se mapean automáticamente a IDs globales que empiezan en 100000, evitando conflictos con los IDs de permisos del core y entre módulos.

Consulta [module_rbac_permissions](module_rbac_permissions) para la guía de integración completa.
