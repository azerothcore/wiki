# Pasos finales del servidor

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 5: Red](es/networking) | [Paso 7: Mantener el servidor actualizado >>](es/keeping-the-server-up-to-date) |

## Iniciar el servidor

- Ejecuta authserver y worldserver en tu carpeta de build.

Para información detallada sobre cómo configurar un reiniciador y un debugger, ve a la página [how-to-restart-and-debug](es/how-to-restart-and-debug)

{% include warning.html content="¡NUNCA crees una cuenta directamente en tu base de datos a menos que estés ABSOLUTAMENTE SEGURO de que sabes qué hacer y cómo hacerlo!" %}

- Luego, crea tu cuenta de acceso escribiendo directamente en la ventana de **worldserver** el comando GM **account create**. Sintaxis: (ver ejemplos abajo)

- Si quieres asignar la cuenta como GM, escribe en la ventana de worldserver: **account set gmlevel $account #level #realmid**, donde **$account** es el nombre de la cuenta a cambiar, **#level** puede ser 0-4 y **#realmid** es el ID del reino. Establecer un **#level** de "3" es el nivel de cuenta GM (números más altos = mayor acceso), y "-1" es el ID del reino que significa "todos los reinos".

{% include tip.html content="Abre tu base de datos **acore_world** y busca la tabla **command**. Muestra una lista completa de comandos GM, sus descripciones y niveles de seguridad.<br/>Esta será siempre la lista más actualizada que puedas encontrar, asumiendo que mantienes tu base de datos y el Core actualizados." %}

- Minimiza tus servidores y ejecuta **WoW** (nunca ejecutes WoW usando el Launcher a menos que hayas editado la opción patchlist del realmlist.wtf de arriba).

- Inicia sesión con el usuario/contraseña que acabas de crear.

- El reino de AzerothCore debería poder seleccionarse. Inicia sesión, crea un personaje y ¡listo!

## Crear una cuenta

Lee [creación de cuentas](es/creating-accounts).

## Configurar el acceso remoto

Para propósitos de desarrollo, este paso no es necesario. Sin embargo, para mayor seguridad cuando quieras que otras personas creen cuentas, deberías configurar un formulario de registro, así no tienes que pegar sus contraseñas. Consulta [Acceso remoto](es/remote-access) sobre cómo enviar comandos al servidor.

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 5: Red](es/networking) | [Paso 7: Mantener el servidor actualizado >>](es/keeping-the-server-up-to-date) |
