# Instalación del Core en Windows

| Guía de Instalación | |
| :- | :- |
| Este artículo forma parte de la Guía de Instalación. Puedes leerlo por separado o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](windows-requirements.md) | [Paso 3: Configuración del Servidor >>](server-setup.md) |

## Software necesario

Consulta [Requisitos](windows-requirements.md) antes de continuar.

## Descarga y compilación del código fuente

### Descarga del código

1. Crea el directorio donde se ubicarán los archivos fuente. En esta guía, utilizaremos **C:\Azerothcore**.

2. Abre Github Desktop.

3. Haz clic en **Archivo** -> **Clonar repositorio...** en la esquina superior izquierda.

4. Haz clic en **URL**.

5. Completa los datos de la siguiente manera:

```text
Repository URL or GitHub username and repository: https://github.com/azerothcore/azerothcore-wotlk
Local path: C:\Azerothcore
```

Click **Clone**. En pocos minutos, los archivos fuente de Azerothcore se clonarán en **C:\Azerothcore**.

### Configuración y generación de la solución Visual C++ con CMake

Antes de comenzar, crea un nuevo directorio llamado **Build**. En esta guía, utilizaremos **C:\Build**.

1. Abre CMake.

2. Haz clic en **Examinar fuente...** → Selecciona el directorio fuente (**C:\Azerothcore**).

3. Haz clic en **Examinar construcción...** → Selecciona el directorio de construcción (**C:\Build**).

4. Haz clic en **Configurar**.

5. En el menú desplegable, elige la versión del compilador que descargaste en la sección de [Requisitos](windows-requirements.md). Asegúrate de elegir la versión **Win64** si trabajas en una compilación de 64 bits.

6. Asegúrate de que **Usar compiladores nativos predeterminados** esté marcado.

7. Haz clic en **Finalizar**.

8. Asegúrate de que **TOOLS_BUILD** esté configurado en `all`. Esto compilará los extractores necesarios más adelante en la configuración.

9. Haz clic en **Configurar** nuevamente. Mientras haya error(es) en rojo en la ventana de registro, deberás verificar tus parámetros y volver a ejecutarlo.

10. Haz clic en **Generar**. Esto instalará los archivos de construcción seleccionados en tu carpeta **C:\Build**.

#### Solución de algunos errores

Si llegaras a encontrar errores en CMake, consulta [Errores comunes](common-errors#core-installation-errors).

### Compilación del código fuente

1. En CMake, presiona **Abrir proyecto** para abrir el archivo **AzerothCore.sln** directamente con Visual Studio.

1. En el menú superior, haz clic en **Compilar** y selecciona **Administrador de configuraciones**.

    1. Establece la **Configuración de solución activa** en **RelWithDebInfo**.

    1. Establece la **Plataforma de solución activa** en **x64** y luego haz clic en Cerrar (la configuración se guarda automáticamente).

1. Haz clic con el botón derecho en **ALL_BUILD** en el Explorador de soluciones en la barra lateral derecha y selecciona **Limpiar**.

1. Haz clic con el botón derecho en **ALL_BUILD** y selecciona **Compilar** (Ctrl + Shift + B).

    1. Si tu GUI no muestra el Explorador de soluciones, haz clic en el menú Compilar y selecciona **Limpiar solución**, y luego **Compilar**.

El tiempo de compilación varía de una máquina a otra, pero puedes esperar que tome entre 5 y 30 minutos.

Si se te pide "Recargar archivos de construcción" durante o después de la compilación, hazlo.

Cuando la compilación esté completa, encontrarás un mensaje en la salida que se parece a esto:

```text
========== Build: 22 succeeded, 0 failed, 0 up-to-date, 1 skipped ==========
```

Encontrarás tus binarios recién compilados en la carpeta **C:\Build\bin\RelWithDebInfo** o **C:\Build\bin\Debug**. Estos se utilizan para ejecutar tu servidor al final de estas instrucciones.

Necesitarás los siguientes archivos para que el núcleo funcione correctamente:

```text
\configs\
authserver.exe
authserver.pbd
worldserver.exe
worldserver.pdb
libmysql.dll

---------
Para OpenSSL 1.1.x

libeay32.dll / libcrypto-1_1.dll / libcrypto-1_1-x64.dll
ssleay32.dll / libssl-1_1.dll / libssl-1_1-x64.dll

---------
Para OpenSSL 3.0 y versiones posteriores

legacy.dll
libcrypto-3.dll / libcrypto-3-x64.dll
libssl-3.dll / libssl-3-x64.dll
```

En la carpeta **configs** deberías encontrar:

```text
authserver.conf.dist
worldserver.conf.dist
```

Hay dos/tres archivos DLL que deben agregarse manualmente a esta carpeta, y debes copiarlos desde los siguientes directorios de instalación/bin:

**libmysql.dll** → C:\Program Files\MySQL\MySQL Server 8.x\lib\

*Nota: Necesitas la versión exacta de libmysql que corresponda al MySQL que has descargado. Debido a esto, no puedes descargar el DLL de la web y necesitas extraerlo de la carpeta.*

#### OpenSSL _antes_ de la versión 1.1.0:

**libeay32.dll** y **ssleay32.dll** → C:\OpenSSL-Win64\ o C:\OpenSSL-Win32\ *(depende de si tu núcleo es de 64 bits o 32 bits)*.

#### Nombres de OpenSSL 1.1.x han cambiado:

**libssl-1_1-x64.dll** y **libcrypto-1_1-x64.dll** → C:\OpenSSL-Win64\bin

#### OpenSSL 3.0 y más reciente instalado, debes copiar:

**legacy.dll** → C:\OpenSSL-Win(32/64)\bin

**libcrypto-3-x64.dll** y **libssl-3-x64.dll** → C:\OpenSSL-Win64\bin

#### Acerca del registro de compilación e informe

Los archivos pdb solo existen si compilar con la configuración Debug o RelWithDebInfo. No es obligatorio, pero se recomienda compilar el núcleo con al menos la configuración RelWithDebInfo para obtener registros de errores adecuados.

Para informar sobre registros de errores, es OBLIGATORIO compilar con la configuración Debug o RelWithDebInfo.

<br>

## Ayuda

fgdfgSi aún tienes problemas, verifica:

* [FAQ](faq.md)

* [Errores comunes](common-errors.md)

* [Cómo solicitar ayuda](how-to-ask-for-help.md)

* [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte las 24 horas. Un miembro del personal te responderá cuando tenga tiempo.

| Guía de Instalación | |
| :- | :- |
| Este artículo forma parte de la Guía de Instalación. Puedes leerlo por separado o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](windows-requirements.md) | [Paso 3: Configuración del Servidor >>](server-setup.md) |
