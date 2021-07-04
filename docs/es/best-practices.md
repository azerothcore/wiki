# Mejores pr�cticas

Una colecci�n de las mejores pr�cticas para usar AzerothCore.


## Cambios personalizados

- **NUNCA** agregue cambios personalizados a las fuentes de AzerothCore. [Crear m�dulos](http://www.azerothcore.org/wiki/Create-a-Module) en su lugar.

Si necesita nuevos enlaces para implementar sus cambios personalizados en los m�dulos, no dude en enviar un PR que los implemente.

Razones:

1. Mantener limpio el c�digo fuente base le facilitar� la actualizaci�n.
2. Mantener sus personalizaciones en m�dulos le permitir� habilitarlas o deshabilitarlas f�cilmente para solucionar cualquier problema potencial.
3. El software modularizado es mucho m�s f�cil de mantener.


## Solicitudes de extracci�n (PR)

- [Sincroniza tu fork](http://www.azerothcore.org/wiki/Syncing-your-fork) antes de abrir un PR.

Razones:

1. Ayuda a prevenir conflictos de fusi�n
2. Implementar� (y probar�) los cambios tal como se aplicaron a la �ltima versi�n maestra.

- **NUNCA** empuje los cambios a la rama `master`. Siempre tu rama "master" limpia.

Cuando creas un nuevo PR, haz `git checkout master` y crea una nueva rama usando` git checkout -b new-branch`.

Razones:

1. Esto le permitir� crear m�ltiples RP que sean independientes entre s�.
2. Esto le permitir� actualizar f�cilmente sus branches con el �ltimo master sincronizando primero su fork y luego fusionando `master` en branches.