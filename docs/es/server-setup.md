# Configuración del Servidor

| Guía de Instalación                                                                                                                                      |                                                                     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| Este artículo es parte de la Guía de Instalación. Puedes leerlo por separado o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 2: Instalación del Core](core-installation)                                                                                                     | [Paso 4: Instalación de la Base de Datos >>](database-installation) |

**Tabla de contenido**
- [Archivos de datos](#archivos-de-datos) - Requerido/Opcional (No es necesario si extraes los archivos).
- [Extractores](#extractores) - Requerido/Opcional (No es necesario si descargas los archivos).
- [Archivos de Configuración: Worldserver y Authserver](#archivos-de-configuración-worldserver-y-authserver) - Requerido

Ahora que tienes el código fuente compilado, necesitas agregar algunos archivos necesarios, ya sea descargándolos o extrayéndolos.

Algunos archivos son opcionales, pero altamente recomendados:

| Directorio |                       |
| :--------- | :-------------------- |
| dbc        | Obligatorio           |
| maps       | Obligatorio           |
| vmaps      | ALTAMENTE RECOMENDADO |
| mmaps      | ALTAMENTE RECOMENDADO |
| cameras    | Recomendado           |

## Archivos de datos

Si tienes la intención de usar un cliente enUS, puedes descargar los archivos de datos a continuación. Si deseas usar un cliente en otro idioma, necesitarás [extraer](#extractores) los datos tú mismo.

<a class="no-icon" href="https://github.com/wowgaming/client-data/releases/" target="_blank"><i class="fa-solid fa-download"></i> Archivos de datos enUS (AC Data v16)</a>

1. Descarga los archivos de arriba.

2. Crea una nueva carpeta dentro de la carpeta de compilación llamada **Data**. Es decir, en Windows: **C:\Build\bin\RelWithDebInfo\Data** o en Linux: **$HOME/azerothcore/data/**

3. Extrae los archivos del archivo zip y colócalos dentro de la carpeta **Data**.

4. Edita la opción de configuración [DataDir](#updating-datadir) para que apunte a la ubicación de tu carpeta.

## Extractores

**(No es necesario si descargaste los archivos anteriores)**

Si descargaste los archivos anteriores, puedes saltarte este paso y continuar con [worldserver.conf y authserver.conf](#archivos-de-configuración-worldserver-y-authserver).

Esta parte es solo un resumen general del proceso. Por favor, léelo con más detalle según el sistema operativo con el que estés trabajando.

[Configuración de servidor en Linux](linux-server-setup)

[Configuración de servidor en macOS](macos-server-setup)

[Configuración de servidor en Windows](windows-server-setup)

AzerothCore necesita ciertos archivos extraídos del cliente de World of Warcraft. Debes extraerlos de un cliente 3.3.5a.

Por defecto, compilarás tu núcleo con herramientas y obtendrás los siguientes archivos ejecutables: **mapextractor**, **vmap4extractor**, **vmap4assembler**, **mmaps_generator** (.exe en Windows).

Coloca los archivos junto a tu archivo binario de World of Warcraft (wow.exe en Windows) y ejecútalos.

Después de extraer todos los archivos necesarios, crea una carpeta llamada **Data** dentro del directorio **RelWithDebInfo** o **Debug** y coloca los archivos allí. Alternativamente, puedes especificar un directorio diferente donde deseas mantenerlos cambiando el valor de DataDir en el archivo worldserver.conf.

Si usas extractores de otros proyectos o ramas, ¡es casi seguro que tu AzerothCore no reconocerá los datos extraídos o ni siquiera funcionará!

Cuando esto esté completo, puedes recibir el siguiente mensaje, que se puede ignorar con seguridad:

```
Processing Map 724
[################################################################]
Extracting GameObject models...Extracting World\Wmo\Band\Final_Stage.wmo
No such file.
Couldn't open RootWmo!!!
Done!
  
Extract V4.00 2012_02. Work complete. No errors.
```

### Solución de problemas

"**Unable to open wmo_list.txt! Nothing extracted.**"

Debes ejecutar Mapextractor.exe antes de makevmaps_simple.bat.

## Archivos de Configuración: Worldserver y Authserver

Cada vez que se recompila el núcleo, se crea un archivo de configuración .dist, donde se almacenan todas las opciones predeterminadas. Este archivo no tiene un propósito real, excepto para distribuir todas las opciones del núcleo.

### Creación de los archivos de configuración

1. Ve a tu carpeta de configuraciones, por ejemplo, D:\build\bin\RelWithDebInfo\configs

2. Elimina la parte **.dist** de **worldserver.conf.dist** y **authserver.conf.dist**.

    - Deberías quedarte con **worldserver.conf** y **authserver.conf**.

Abre los archivos .conf y desplázate hasta **LoginDatabaseInfo**, **WorldDatabaseInfo** y **CharacterDatabaseInfo** e ingresa la información de inicio de sesión de MySQL para que el servidor pueda acceder a tu base de datos.

En una configuración recién compilada, tendrás los siguientes valores por defecto:

```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth"         -> worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world"        -> worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters"   -> worldserver.conf
```

Esa parte de la configuración sigue este formato o estructura específica:

```
Variablename = "MySQLIP;Port;Username;Password;database"  
```

Los siguientes pasos deben ser verificados:

- El nombre de host (127.0.0.1) puede mantenerse igual si AzerothCore se está instalando en la misma computadora donde ejecutas WoW.
  Si no es así, sigue las instrucciones en [Tabla Realmlist](realmlist).

- El puerto (3306) es el valor estándar configurado. Si cambiaste el puerto predeterminado en la configuración de MySQL, debes cambiarlo en consecuencia.
  El nombre de usuario y la contraseña pueden ser variables. Puedes optar por:

    - usar el par de nombre de usuario y contraseña predeterminados acore / acore.

    - crear un inicio de sesión único dentro de un Gestor de Usuarios en tu herramienta de gestión de bases de datos preferida (comúnmente identificado por un ícono que parece una persona o varias personas) y darle los permisos necesarios (los permisos SELECT, INSERT, UPDATE, DELETE son suficientes, y es mucho más seguro).

### Actualización de DataDir

1. En tu archivo worldserver.conf, localiza la opción **DataDir**.

2. Edítala con la ruta de tu carpeta. Por ejemplo, **C:\Build\bin\RelWithDebInfo\Data**

{% include tip.html content="Para la mayoría de los cambios en la configuración de worldserver.conf, simplemente puedes escribir .reload config en el juego para ver los cambios al instante sin reiniciar el servidor." %}

{% include warning.html content="El equipo de AzerothCore y los propietarios NO patrocinan ni apoyan en ningún caso servidores públicos ilegales. Si utilizas estos proyectos para ejecutar un servidor público ilegal y no para pruebas o aprendizaje, es tu propia elección personal." %}

### (Opcional) Opciones de configuración mediante variables de entorno

Es posible cargar opciones de configuración mediante variables de entorno, de las cuales puedes leer más [aquí](config-overrides-with-env-var).

## Ayuda

Si aún tienes problemas, consulta:

* [Preguntas frecuentes (FAQ)](faq)

* [Errores comunes](common-errors)

* [Cómo pedir ayuda](how-to-ask-for-help)

* [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del personal te responderá cuando tenga tiempo.

| Guía de Instalación                                                                                                                                      |                                                                     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| Este artículo es parte de la Guía de Instalación. Puedes leerlo por separado o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 2: Instalación del Core](core-installation)                                                                                                     | [Paso 4: Instalación de la Base de Datos >>](database-installation) |
