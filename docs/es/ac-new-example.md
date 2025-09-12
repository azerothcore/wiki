# Ejemplo de NUEVOS requisitos de Windows

| Guía de instalación                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| Este artículo forma parte de la Guía de instalación. Puede leerlo por separado o hacer clic en el enlace anterior para navegar fácilmente entre los pasos. |                                                           |
| [<< Inicio: Guía de instalación](classic-installation)                                                                                 | [Paso 2: Instalación del núcleo >>](windows-core-installation) |

{% include callout.html content="Windows ≥ 10<br/>
Boost ≥ 1.78<br/>
MySQL ≥ 8.0 (Recommended 8.4)<br/>
OpenSSL ≥ 3.x.x<br/>
CMake ≥ 3.16<br/>
MS Visual Studio (Comunidad) ≥ 17 (2022) (De oficina) (Sin vista previa)" type="info" %}

|                            Header                             |
| :-----------------------------------------------------------: |
|                          [Git](#git)                          |
|               [Github Desktop](#github-desktop)               |
| [Visual Studio Community 2022](#visual-studio-community-2022) |
|                        [MySQL](#mysql)                        |
|                 [MySQL Client](#mysql-client)                 |
|                        [CMake](#cmake)                        |
|                      [OpenSSL](#openssl)                      |
|                        [Boost](#boost)                        |

## [Git](#git)

### Descargar

- https://git-scm.com/download/win

### Instalación

- Ejecute el instalador independiente

{% include note.html content="Durante la instalación, se le solicitará que ajuste su entorno PATH. Seleccione 'Git desde la línea de comandos y también desde software de terceros'." %}

## [Github Desktop](#github-desktop)

### Descargar

- https://desktop.github.com

### Instalación

- Descargue el instalador y siga los pasos para configurarlo.

## [Visual Studio Community 2022](#visual-studio-community-2022)

### Descargar

- https://visualstudio.microsoft.com/downloads

{% include note.html content="Make sure you're getting 'Visual Studio 2022 Community' and not 'Visual Studio Code'." %}

### Instalación

- Instalar el compilador de C++.
  Necesitará instalar el compilador C++.

  Para ello, seleccione **Desarrollo de escritorio para C++** en **Cargas de trabajo -> Escritorio y dispositivos móviles**.

   <a href="/wiki/images/visualstudio.jpg" target="_blank">
    <img src="/wiki/images/visualstudio.jpg" height="50%" width="50%">
   </a>

## [MySQL](#mysql)

### Descargar

- https://dev.mysql.com/downloads/mysql/8.4.html

### Instalación

1. Ejecute el instalador MSI de Windows.
2. Desplácese hasta el final y haga clic en "No, gracias, ¡sólo llévame a las descargas!"
3. Cuando la instalación esté casi terminada, asegúrese de que la opción "Iniciar el Asistente de configuración de instancias MySQL" esté marcada y luego haga clic en "Finalizar".
4. Al iniciarse el Asistente de configuración de instancias de MySQL, la mayoría de las opciones predeterminadas son correctas, pero recuerde el nombre de usuario y la contraseña que usa (root // lo que sea). Los necesitará para iniciar sesión en la herramienta de administración de bases de datos que elija (abajo) y poder importar archivos SQL posteriormente.
5. Para comprobar si MySQL está configurado correctamente, presione Ctrl+Alt+Supr, acceda al Administrador de tareas y seleccione la pestaña "Servicios". En la lista de servicios, debería ver "MySQL" con el estado "En ejecución".

6. Agregar MySQL a las variables de entorno.

   1. Vaya al Panel de control -> Sistema
   2. Vaya a Configuración avanzada del sistema

   3. Ir a Variables de entorno
   4. En "Variables del sistema", seleccione **Path**
   5. Edite y agregue su ruta de instalación de MySQL. Por ejemplo: **C:\Program Files\MySQL\MySQL Server 8.0\bin\\**

{% include note.html content="Archivos de desarrollo de MySQL: Estos archivos se incluyen con MySQL Server. Búsquelos en el directorio de archivos de programa: MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib. Los necesitará más adelante para el servidor." %}

## [MySQL Client](#mysql-client)

### Descargar

- [HeidiSQL](https://www.heidisql.com/download.php) (Ideal para principiantes)

- MySQL CLI (El más rápido, viene con su instalación de MySQL)

- [DBeaver](https://dbeaver.io/) (Herramienta de gestión de bases de datos multiplataforma)

- [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)

{% include note.html content="You only have to pick one of the options on top." %}

### Instalación

1. Intenta conectarte a tu base de datos. Quizás estés buscando "Conectar al host", "Nueva conexión" o "Administrador de sesiones", según el programa que uses.

2. Cree una nueva conexión/sesión. El nombre de host/dirección IP "127.0.0.1" o "localhost" es suficiente si instaló MySQL en el mismo equipo donde instaló HeidiSQL o SQLYog. Simplemente ingrese su contraseña de root o cualquier otra contraseña y podrá conectarse a su base de datos. Esta es la información utilizada en este paso [MySQL](#mysql)

## [CMake](#cmake)

### Descargar

- https://cmake.org/download

{% include note.html content="NUNCA descargue e instale la RC (Release Candidate), SIEMPRE la última versión" %}

### Instalación

- Ejecute el instalador MSI de Windows.

{% include note.html content="Recomendamos compilar en modo de 64 bits." %}

## [OpenSSL](#openssl)

### Descargar

- http://www.slproweb.com/products/Win32OpenSSL.html

{% include note.html content="Encuentre la versión de 64 bits buscando la última versión 3.x.x Win64 OpenSSL que NO es la versión 'light'." %}

### Instalación

- Ejecute el instalador EXE/MSI de Windows.

{{site.data.alerts.note}}
Si recibe el error "Falta Microsoft Visual C++ .... Redistributable" al instalar OpenSSL, descargue el <a href="https://aka.ms/vs/17/release/vc_redist.x64.exe">Paquete redistribuible de Microsoft Visual C++ 2017/2019/2022 (x64) (descarga directa)</a> (instalador de 1,7 MB) e instálelo.
{{site.data.alerts.end}}

{{site.data.alerts.note}}
Al instalar OpenSSL, seleccione el directorio de binarios de OpenSSL (/bin) (NO el directorio de sistema de Windows) cuando se le presente la opción de copiar las DLL de OpenSSL. Estas DLL deberán ser fáciles de encontrar para la <a href="windows-core-installation">instalación principal</a>.
{{site.data.alerts.end}}

## [Boost](#boost)

### Descargar

- https://www.boost.org

- [1.81.0](https://sourceforge.net/projects/boost/files/boost-binaries/1.81.0/boost_1_81_0-msvc-14.3-64.exe/download)

{% include note.html content="Solo tienes que elegir una de las opciones de arriba. La que tenga el número específico se descargará directamente a esa versión." %}

### Instalación

- Agregue una variable de entorno a la variable "Sistema" llamada "BOOST_ROOT" cuyo valor sea el directorio de instalación de Boost, por ejemplo, `C:/local/boost_1_81_0`. Es importante usar '**/**', no '**\\**', al apuntar al directorio. (Asegúrese de que no tenga una barra diagonal al final de la ruta). Si persisten los problemas, agregue la misma variable también en la sección de variables `USER`, como se muestra en la imagen a continuación).

<a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
</a>

{% include note.html content="Tenga en cuenta que esta imagen muestra el número de versión 1.72.0: use su número de versión real en su configuración." %}

{% include note.html content="Asegúrate de que el valor de la variable BOOST_ROOT tenga la dirección correcta. Como/esto/aquello, no como\esto\aquello" %}

<br>

|                            Header                             |
| :-----------------------------------------------------------: |
|                          [Git](#git)                          |
|               [Github Desktop](#github-desktop)               |
| [Visual Studio Community 2022](#visual-studio-community-2022) |
|                        [MySQL](#mysql)                        |
|                 [MySQL Client](#mysql-client)                 |
|                        [CMake](#cmake)                        |
|                      [OpenSSL](#openssl)                      |
|                        [Boost](#boost)                        |

## Ayuda

If you are still having problems, check:

- [FAQ](faq)

- [Errores comunes](common-errors)

- [Cómo pedir ayuda](how-to-ask-for-help)

- [Únete a nuestro servidor de Discord] (https://discord.gg/gkt4y2x), pero no es un canal de soporte disponible las 24 horas. Un miembro del equipo te responderá cuando tenga tiempo.

| Guía de instalación                                                                                                                  |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| Este artículo forma parte de la Guía de instalación. Puede leerlo por separado o hacer clic en el enlace anterior para navegar fácilmente entre los pasos. |                                                           |
| [<< Inicio: Guía de instalación](classic-installation)                                                                                 | [Paso 2: Instalación del núcleo >>](windows-core-installation) |
