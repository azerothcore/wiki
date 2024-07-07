# Pasos finales

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 5: Red](networking) | [Paso 7: Mantener actualizado el Servidor >>](keeping-the-server-up-to-date) |

## Iniciando el Servidor

- Ejecute authserver y worldserver en la carpeta de su build.

Para información detallada sobre cómo configurar un reiniciador y un debugger, vaya a la página [cómo-reiniciar-y-depurar](how-to-restart-and-debug).

**NUNCA cree una cuenta directamente en su base de datos a menos que esté TOTALMENTE SEGURO de que sabe lo que está haciendo y cómo hacerlo.**

- Luego cree su cuenta de inicio de sesión escribiendo directamente en la ventana **worldserver** usando el comando GM **account create**. Sintáxis: (ver ejemplos posteriores)

- Si desea asignar la cuenta como GM, escriba en la ventana worldserver: **account set gmlevel $cuenta #nivel #id del reino** en donde **$cuenta** es la el nombre de la cuenta a cambiar, **#nivel** puede ser 0-4 y **#id del reino** el el ID del reino. Establecer un **#nivel** de "3" equivale a una cuenta de nivel GM (numeros más altos = mayor acceso), y "-1" como id del reino significa "para todos los reinos".

*Consejo: Abra su base de datos **acore_world** y busque la tabla **command**. Esto muestra una lista completa de comandos, sus descripciones y el nivel de seguridad.*
*Esta será siempre la lista más actualizada que podrá encontrar, asumiendo que mantiene la base de datos y el Core actualizados.*

- Minimize las ventanas del servidor y ejecute **WoW** (nunca ejecute WoW usando el launcher a menos que haya editado la opción patchlist del realmlist.wtf).

- Ingrese usando el usuario y contraseña que acabó de crear.

- El reino AzerothCore debería poderse seleccionar. Ingrese, cree un nuevo personaje y ¡eso es todo!

## Creación de cuentas

Lea [creación de cuentas](creating-accounts).

## Configurando el acceso remoto
Para propósitos de desarrollo, este paso no es necesario. Sin embaro, para incrementar la seguridad cuando usted quiera que otras personas creen cuentas, debería configurar un formulario de registro, de manera que no tenga que copiar y pegar sus contraseñas. Revise: [Acceso remoto](remote-access) sobre cómo enviar comandos al servidor.

<br>

## Ayuda

Si sigue teniendo inconvenientes, revise:

* [Preguntas frecuentes](faq)

* [Errores Comunes](common-errors)

* [Cómo solicitar ayuda](how-to-ask-for-help)

* [Unase a nuestro discord](https://discord.gg/gkt4y2x). Aunque no es un canal de soporte 24/7, un miembro del staff le responderá siempre que tenga tiempo.


| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 5: Red](networking) | [Paso 7: Mantener actualizado el Servidor >>](keeping-the-server-up-to-date) |
