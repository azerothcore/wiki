# Ejecutar Worldserver y Authserver en Visual Studio

Ejecutar el Worldserver y el Authserver a través de Visual Studio tiene algunas ventajas.

1. Puedes depurar código fácilmente usando breakpoints o encontrar fácilmente el Call Stack de un crash.

    1. También permitirá que tu servidor se pause en lugar de crashear cuando llegues a un crash, y puedes simplemente continuar tras depurar. 

1. Si estás trabajando en el código, esto puede ahorrarte tiempo cuando necesites entrar al juego a probar, ya que no necesitarías abrir tu carpeta de binarios e iniciarlos individualmente.

## Configurar Visual Studio

1. Elige la configuración de build deseada; en esta guía nos referiremos a Debug.

    <a href="/wiki/images/run-worldserver-and-authserver-in-visual-studio-1.jpg" target="_blank">
    <img src="/wiki/images/run-worldserver-and-authserver-in-visual-studio-1.jpg" height="50%" width="50%">
    </a>

1. Haz click derecho en **Solution 'AzerothCore' (20 of 20 projects)**.

    1. Selecciona **Properties**.

    1. Selecciona **Multiple Startup Projects**.

        1. En el menú desplegable, selecciona **Start** para **authserver** y **worldserver**.

    <a href="/wiki/images/run-worldserver-and-authserver-in-visual-studio-2.jpg" target="_blank">
    <img src="/wiki/images/run-worldserver-and-authserver-in-visual-studio-2.jpg" height="50%" width="50%">
    </a>

1. Haz click derecho en **authserver**.

    1. Selecciona **Properties**.

    1. Selecciona **Debugging**.

        1. En **Command Arguments** elige tu path al archivo .conf para tu build de Debug.

        1. En **Working Directory** elige tu path al directorio de tus binarios.

    <a href="/wiki/images/run-worldserver-and-authserver-in-visual-studio-3.jpg" target="_blank">
    <img src="/wiki/images/run-worldserver-and-authserver-in-visual-studio-3.jpg" height="50%" width="50%">
    </a>

1. Haz el paso 3. para **worldserver** también.

1. Iniciar el Worldserver y el Authserver.

    1. Pulsa el botón **Start** o **F5** para lanzar Worldserver y Authserver dentro de Visual Studio. (Esto es bueno para depurar)

    1. Pulsa **Ctrl + F5** para iniciar Worldserver y Authserver fuera de Visual Studio
