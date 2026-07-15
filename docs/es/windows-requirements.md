# Windows: Requisitos

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](es/classic-installation) | [Paso 2: Instalación del Core >>](es/windows-core-installation) |

{% include callout.html content="Windows ≥ 10<br/>
Boost ≥ 1.78<br/>
MySQL ≥ 8.0 (Recomendado 8.4)<br/>
OpenSSL ≥ 3.x.x<br/>
CMake ≥ 3.27<br/>
MS Visual Studio (Community) ≥ 17 (2022) (Desktop) (Sin preview)" type="info" %}

1. [Git](https://git-scm.com/download/win)

    1. Descarga el instalador independiente

        - Durante la instalación de Git — Ajusta tu variable de entorno PATH. Elige "Git from the command line and also from 3rd-party software".

2. [Github Desktop](https://desktop.github.com/)

    1. Descarga el instalador y sigue los pasos para configurarlo.

3. Instala el compilador / IDE [Visual Studio Community](https://visualstudio.microsoft.com/downloads/)

   Necesitarás instalar el compilador de C++.

   Para ello, selecciona **Desktop development for C++** en **Workloads -> Desktop & Mobile**.

   <a href="/wiki/images/visualstudio.jpg" target="_blank">
   <img src="/wiki/images/visualstudio.jpg" height="50%" width="50%">
   </a>

4. [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/8.4.html)

    1. Descarga el instalador MSI de Windows.

    2. Baja hasta el fondo y haz clic en "No thanks, just take me to the downloads!"

    3. Cuando la instalación esté casi terminada, asegúrate de que "Launch the MySQL Instance Configuration Wizard" esté marcado, luego haz clic en "Finish".

    4. Cuando se abra el MySQL Instance Configuration Wizard, la mayoría de las opciones por defecto están bien, pero recuerda el usuario y la contraseña que uses (root // lo que sea). Los necesitarás para iniciar sesión en tu herramienta de gestión de base de datos elegida (abajo) para importar archivos SQL más adelante.

    5. Para comprobar si MySQL está configurado correctamente, presiona CTRL+ALT+SUPR en tu teclado, entra al Administrador de tareas y selecciona la pestaña "Servicios". En la lista de servicios deberías ver "MySQL" con estado "En ejecución".

    6. Añade MySQL a las Variables de entorno.

        1. Ve al Panel de control -> Sistema

        2. Ve a Configuración avanzada del sistema

        3. Ve a Variables de entorno

        4. En "Variables del sistema" selecciona **Path**

        5. Edita y añade tu ruta de instalación de MySQL, p. ej. **C:\Program Files\MySQL\MySQL Server 8.4\bin\\**

       Asegúrate de localizar los archivos de desarrollo de MySQL; los necesitarás más adelante. Estos archivos vienen incluidos con MySQL Server, búscalos en el directorio de archivos de programa, p. ej. MySQL\MySQL Server 8.4\lib.

5. Elige una herramienta de gestión de base de datos

    - MySQL cli (La más rápida)

    - [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)

    - [HeidiSQL](https://www.heidisql.com/download.php) (La mejor para principiantes)

    - [DBeaver](https://dbeaver.io/) (Herramienta de gestión de base de datos multiplataforma)

    1. Intenta conectarte a tu base de datos. Puede que busques "Connect to Host", "New Connection" o "Session Manager" según el programa que uses.

    2. Crea una nueva conexión/sesión. El nombre de host / dirección IP "127.0.0.1" o "localhost" está bien si instalaste MySQL en el mismo equipo en el que instalaste HeidiSQL o SQLYog. Simplemente rellena tu contraseña root // lo que sea y ya deberías poder conectarte a tu base de datos.

6. [CMake](https://cmake.org/download/)

    1. Descarga e instala el archivo **Latest Release** windows-x86_64.msi, **NUNCA las versiones RC (Release Candidate).**

    2. Recomendamos compilar en modo de 64 bits.

7. [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) Descarga la versión de 64 bits.

    1. Encuentra la versión de 64 bits buscando el último 3.x.x Win64 OpenSSL que NO sea la versión "light". (Ejemplo: Win64 OpenSSL v3.0.7)

    {% include note.html content="Si obtienes el error 'Missing Microsoft Visual C++ .... Redistributable' al instalar OpenSSL, descarga el [Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x64) (Descarga directa)](https://aka.ms/vs/17/release/vc_redist.x64.exe) (instalador de 1.7MB) e instálalo." %}

    {% include note.html content="Al instalar OpenSSL, elige el directorio de binarios de OpenSSL (/bin), NO el directorio del sistema de Windows, cuando te den a elegir dónde copiar las DLL de OpenSSL. Estas DLL deberán poder localizarse fácilmente para la [Instalación del Core](es/windows-core-installation)." %}

8. [Boost](https://www.boost.org/).

    1. Descarga el binario precompilado de Windows para Visual Studio 2022. [64bit](https://sourceforge.net/projects/boost/files/boost-binaries/1.81.0/boost_1_81_0-msvc-14.3-64.exe/download)

    2. Añade una variable de entorno a las variables "System" llamada "BOOST_ROOT" con el valor de tu directorio de instalación de Boost, p. ej. `C:/local/boost_1_81_0`. Es importante usar '**/**', no '**\\**', al apuntar al directorio. (Asegúrate de que no tenga una barra al final (fin de la ruta). Si aún tienes problemas, añade la misma variable también en la sección de variables `USER`, como se muestra en la imagen de abajo.)

    <a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
    </a>

{% include note.html content="Ten en cuenta que esta imagen muestra el número de versión 1.72.0 - usa tu número de versión real en tu configuración." %}

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](es/classic-installation) | [Paso 2: Instalación del Core >>](es/windows-core-installation) |
