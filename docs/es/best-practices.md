# Mejores prácticas

Una colección de las mejores prácticas para usar AzerothCore.


## Cambios personalizados

- **NUNCA** agregue cambios personalizados a las fuentes de AzerothCore. [Crear módulos](http://www.azerothcore.org/wiki/Create-a-Module) en su lugar.

Si necesita nuevos enlaces para implementar sus cambios personalizados en los módulos, no dude en enviar un PR que los implemente.

Razones:

1. Mantener limpio el código fuente base le facilitará la actualización.
2. Mantener sus personalizaciones en módulos le permitirá habilitarlas o deshabilitarlas fácilmente para solucionar cualquier problema potencial.
3. El software modularizado es mucho más fácil de mantener.


## Solicitudes de extracción (PR)

- [Sincroniza tu fork](http://www.azerothcore.org/wiki/Syncing-your-fork) antes de abrir un PR.

Razones:

1. Ayuda a prevenir conflictos de fusión
2. Implementará (y probará) los cambios tal como se aplicaron a la última versión maestra.

- **NUNCA** empuje los cambios a la rama `master`. Siempre tu rama "master" limpia.

Cuando creas un nuevo PR, haz `git checkout master` y crea una nueva rama usando` git checkout -b new-branch`.

Razones:

1. Esto le permitirá crear múltiples RP que sean independientes entre sí.
2. Esto le permitirá actualizar fácilmente sus branches con el último master sincronizando primero su fork y luego fusionando `master` en branches.