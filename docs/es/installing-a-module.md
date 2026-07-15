# Instalar un módulo

| Guía de instalación |
| :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 8: Configuración del cliente](es/client-setup) |

Añadir un módulo es un paso opcional para alterar la jugabilidad blizzlike que ofrece AzerothCore por defecto.

## Instalar el módulo

1. Encuentra un módulo que se ajuste a tus necesidades en el [Catálogo de AzerothCore](https://www.azerothcore.org/catalogue#/).
2. Clona el repositorio
    - Clona el repositorio usando Git de la misma forma en que se clonó AzerothCore por primera vez en la [Instalación del Core](es/core-installation). El repositorio debe clonarse dentro del directorio \modules\, p. ej. E:\AzerothCore\modules\
    - Descarga el archivo ZIP del catálogo y extráelo en el directorio \modules\, p. ej. E:\AzerothCore\modules\mod-anticheat

{% include note.html content="Si tu módulo tiene un sufijo, p. ej. -master, ¡debe eliminarse para que el módulo funcione!" %}

## Recompilar

Para que tu módulo funcione necesitas recompilar el código fuente. Para una guía detallada sobre cómo recompilar, vuelve a leer la [Instalación del Core](es/core-installation).

1. Reconfigura y regenera CMake.
    - Para asegurarte de que el módulo se instaló correctamente, puedes comprobar si aparece en los logs de CMake bajo **\* Modules configuration (static)**

2. Recompila el core.

Tu Worldserver ejecutará automáticamente cualquier consulta SQL proporcionada por los módulos.

Siempre deberías revisar el archivo README del módulo para ver si se necesitan pasos manuales para que el módulo funcione correctamente.

## Errores comunes

- Durante la compilación obtengo el error "error LINK2019: unresolved external symbol "void __cdcel Addmod_module_masterScripts(void)"
    - Elimina **-master** del nombre del directorio del módulo.

- El módulo, por alguna razón, no funciona dentro del juego.
    - Siempre puedes usar el comando **.server debug** para ver todos los módulos cargados.
    - Recurre siempre al archivo README del módulo para conocer los pasos exactos de instalación de ese módulo.

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación |
| :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 8: Configuración del cliente](es/client-setup) |
