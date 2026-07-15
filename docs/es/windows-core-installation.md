# Instalación del Core en Windows

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](es/windows-requirements) | [Paso 3: Configuración del servidor >>](es/windows-server-setup) |

## Software necesario

Consulta [Requisitos](es/windows-requirements) antes de continuar.

## Descarga y compilación del código fuente

### Descarga del código

1. Crea el directorio donde se ubicarán los archivos fuente. En esta guía, usaremos **C:\Azerothcore**.

1. Abre Github Desktop

1. Haz clic en **File** -> **Clone repository...** en la esquina superior izquierda

1. Haz clic en **URL**

1. Rellena los datos de la siguiente manera:

```
Repository URL or GitHub username and repository: https://github.com/azerothcore/azerothcore-wotlk
Local path: C:\Azerothcore
```

Haz clic en **Clone**. En pocos minutos, los archivos fuente de Azerothcore se clonarán en **C:\Azerothcore**.

#### Solución de problemas

Si te encuentras con un error como **fatal: early EOF** o **fatal: fetch-pack: invalid index-pack output**, puedes encontrar una solución alternativa aquí: [Errores comunes ACE00105](es/common-errors#ace00105).

### Configuración y generación de la solución Visual C++ con CMake

Antes de comenzar, crea un nuevo directorio llamado **Build**. En esta guía, usaremos **C:\Build**.

1. Abre CMake

1. Haz clic en **Browse Source...** → Selecciona el directorio fuente (**C:\Azerothcore**)

1. Haz clic en **Browse Build...** → Selecciona el directorio de build (**C:\Build**)

1. Haz clic en **Configure**.

1. En el menú desplegable, elige la versión del compilador que descargaste en la sección de [Requisitos](es/windows-requirements). Asegúrate de elegir la versión **Win64** si trabajas en una compilación de 64 bits.

1. Asegúrate de que **Use default native compilers** esté marcado.

1. Haz clic en **Finish**.

1. Asegúrate de que **TOOLS_BUILD** esté configurado en `all`. Esto compilará los extractores necesarios más adelante en la configuración.

1. Haz clic en **Configure** de nuevo. Mientras haya error(es) en rojo en la ventana de registro, deberás revisar tus parámetros y volver a ejecutarlo.

1. Haz clic en **Generate**. Esto instalará los archivos de build seleccionados en tu carpeta **C:\Build**.

{% include note.html content="Si te encuentras con errores en CMake, consulta [Errores comunes](es/common-errors#core-installation-errors)." %}

### Compilación del código fuente {#compiling-the-source}

1. En CMake, presiona **Open Project** para abrir el archivo **AzerothCore.sln** directamente con Visual Studio.

1. En el menú superior, haz clic en **Build** y selecciona **Configuration Manager**.

    1. Establece **Active Solution Configuration** en **RelWithDebInfo**.

    1. Establece **Active Solution Platform** en **x64** y luego haz clic en Close (la configuración se guarda automáticamente).

1. Haz clic derecho en **ALL_BUILD** en el Solution Explorer de la barra lateral derecha y selecciona **Clean**.

1. Haz clic derecho en **ALL_BUILD** y selecciona **Build**. (Ctrl + Shift + B)

    1. Si tu GUI no muestra el Solution Explorer, haz clic en el menú Build y selecciona **Clean Solution**, y luego **Build**.

El tiempo de build varía de una máquina a otra, pero puedes esperar que tome entre 5 y 30 minutos.

Si se te pide "Reload build files" durante o después de la compilación, hazlo.

Cuando el build esté completo, encontrarás en la salida un mensaje similar a este:

```
========== Build: 22 succeeded, 0 failed, 0 up-to-date, 1 skipped ==========
```

Encontrarás tus binarios recién compilados en la carpeta **C:\Build\bin\RelWithDebInfo** o **C:\Build\bin\Debug**. Todos se usan para ejecutar tu servidor al final de estas instrucciones.

Necesitarás los siguientes archivos para que el core funcione correctamente:

```
\configs\
authserver.exe
authserver.pdb
worldserver.exe
worldserver.pdb
libmysql.dll
legacy.dll
libcrypto-3-x64.dll
libssl-3-x64.dll
```

Hay cuatro archivos DLL que deben añadirse manualmente a esta carpeta, y debes copiarlos desde los siguientes directorios:

{% include callout.html content="**libmysql.dll** → C:\Program Files\MySQL\MySQL Server 8.4\lib" type="primary" %}

{% include note.html content="La versión de tu libmysql.dll debe coincidir con la versión de MySQL Server que ejecutas. Si actualizas tu servidor MySQL, necesitas recompilar el core y copiar el nuevo archivo dll." %}

{% include callout.html content="**legacy.dll**, **libcrypto-3-x64.dll** y **libssl-3-x64.dll** → C:\OpenSSL-Win64\bin" type="primary" %}

En la carpeta **configs** deberías encontrar:

```
authserver.conf.dist
worldserver.conf.dist
```

#### Acerca del registro de compilación e informe

Los archivos pdb solo existen si compilas con la configuración Debug o RelWithDebInfo. No es obligatorio, pero se recomienda compilar el core con al menos la configuración RelWithDebInfo para obtener crash logs adecuados.

{% include important.html content="Para reportar crash logs es OBLIGATORIO compilar con la configuración Debug o RelWithDebInfo." %}

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](es/windows-requirements) | [Paso 3: Configuración del servidor >>](es/windows-server-setup) |
