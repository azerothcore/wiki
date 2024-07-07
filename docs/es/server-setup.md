# Configuración del Servidor

| Guía de instalación                                                                                                                                 |                                                                        |
| :-                                                                                                                                                  | :-                                                                     |
| Este artículo es una parte de la Guía de Instalación. Puede leerlo solo o hacer clic en el enlace anterior para moverse fácilmente entre los pasos. |
| [<< Paso 2: Instalación del Core](core-installation)                                                                                             | [Paso 4: Instalación de la Base de Datos >>](database-installation) |

Ahora que tiene el código fuente compilado, necesita añadir algunos archivos que son requeridos. Puede añadirlos ya sea descargándolos o extrayéndolos.

Algunos archivos son opcionales pero ALTAMENTE recomendados:

| Directorio |                       |
| :-         | :-                    |
| dbc        | Obligatorio           |
| maps       | Obligatorio           |
| vmaps      | ALTAMENTE RECOMENDADO |
| mmaps      | ALTAMENTE RECOMENDADO |
| cameras    | Recomendado           |

## Descarga

Si no desea usar herramientas para extraer estos archivos, puede descargarlos:

Github link:

<a href="https://github.com/wowgaming/client-data/releases/" target="_blank">Archivos completos (v13) - Dede 06/01/2022 a la fecha</a> (RECOMENDADO - Usado en el script de descarga automática en `/apps/`)

<!-- this link contains v10 -->
<!-- Mega link:

<a href="https://mega.nz/#F!pyYlkK6b!pNz-zhThXQIg0_rO5L_RsQ" target="_blank">DBC & maps for all versions</a> (ALTERNATIVE)
-->

1. Descargue los archivos de arriba.

1. Cree una nueva carpeta llamada **Data** dentro de la build. Por ejemplo: **E:\AzerothCore\RelWithDebInfo\Data**

1. Extraiga los archivos comprimidos, dentro de la carpeta **Data** que acabó de crearr.

1. Edite la ruta en el valor de [DataDir](#config-files-worldserver-conf-.--authserver-conf) para que corresponda con la de su carpeta.

## Extractores (No son necesarios si descargó los archivos anteriores)

Si descargó los archivos anteriores, puede saltarse este paso e ir directamente a [worldserver.conf / authserver.conf](#worldserverconf--authserverconf).

Esta parte es simplemente un resúmen general del proceso total. Por favor, lea el que corresponda con su sistema operativo.

[Linux](linux-server-setup)

[macOS](macos-server-setup)

[Windows](windows-server-setup)

AzerothCore requiere ciertos archivos extraidos del cliente de World of Warcraft. Se deben extraer de un cliente en versión 3.3.5a.

Por defecto, usted compilará su código con herramientas y obtendrá los siguientes archivos ejecutables: **mapextractor**, **vmap4extractor**, **vmap4assembler**, **mmaps_generator** (.exe en windows).

Ubique estos archivos en la carpeta en donde se encuentre el archivo binario de World of Warcraft (wow.exe en windows) y ejecútelos.

Después de extraer los archivos necesarios cree una carpeta llamada **Data** dentro del directorio **RelWithDebInfo** o **Debug** y ubique los archivos ahí dentro. De forma alternativa, puede especificar un directorio diferente en el que quiera guardar estos archvivos, cambiando el valor de DataDir en el archivo worldserver.conf.

Si usted usa extractores de otros proyectos o ramas, es casi seguro que su instalación de AzerothCore no va a reconocer los archivos extraidos o no van a, siquiera, funcionar.!

Cuando complete el proceso, recibirá el siguiente mensaje, el cual puede ignorar.

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

Necesita ejecutar Mapextractor.exe antes que makevmaps_simple.bat.

## Archivos de configuración: worldserver.conf / authserver.conf

### Creación de los archivos de configuración

1. Haga copias de ambos archivos .dist .

1. Para cada copia remueva la extensión .dist .

Abra los archivos .dist y busque LoginDatabaseInfo, WorlDatabaseInfo y CharacterDatabaseInfo y registre su información de acceso a MySQL para que el servidor pueda accedera su base de datos.

En un archivo recién compilado, tendrá los siguientes valores por defecto:

```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth" worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world" worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters" worldserver.conf
```

Estos siguen la siguiente estructura:

```
Variablename = "MySQLIP;Port;Username;Password;database"  
``` 

Los siguientes pasos deben ser verificados: 

- El nombre del Host (127.0.0.1) puede quedarse igual si usted instaló AzerothCore en el mismo computador en el que lo va a correr.
  De lo contrario, siga las instrucciones en [Realmlist Table](realmlist). 

- El puerto (3306) el el valor estándar configurado. Si usted lo cambia en la configuración de mysql, recuerde cambiarlo en donde corresponda.
  El nombre de usuario y la contraseña pueden variar. Usted puede escoger entre: 

    - Usar los valores por defecto

    - Crear un usuario y una contraseña unicos mediante la herramienta de gestión de bases de datos de su preferencia y asignar los permisos necesarios (los permisos para acceder a SELECT, INSERT, UPDATE, DELETE  son suficientes y es lo más seguro).

### Actualizando DataDir

1. En su archivo worldserver.conf ubique la opción **DataDir**.

1. Editela para que corresponda con la ruta de su carpeta. Ejemplo: **E:\AzerothCore\RelWithDebInfo\Data**

*Consejo: Para la mayoría de los cambios en el archivo worldserver.conf, usted puede simplemente usar el comando .reload config dentro del juego, para ver los cambios instantaneamente sin reiniciar el servidor.*

*Nota: El equipo de  AzerothCore y los dueños EN NINGUN CASO patrocinan ni apoyan servidores ilegales públicos. Si usted decide usar este proyecto para lanzar un servidor ilegal público es estrictamente su decision personal.*

<br>

## Ayuda

Si sigue teniendo problemas, compruebe:

* [Preguntas frecuentes](faq)

* [Errores Comunes](common-errors)

* [Cómo pedir ayuda](how-to-ask-for-help)

* [Únase a nuestro servidor de Discord](https://discord.gg/gkt4y2x), tenga en cuenta que no es un canal de soporte 24/7. Un miembro del staff member le responderá siempre que tenga tiempo.

| Guía de instalación                                                                                                                                 |                                                                        |
| :-                                                                                                                                                  | :-                                                                     |
| Este artículo es una parte de la Guía de Instalación. Puede leerlo solo o hacer clic en el enlace anterior para moverse fácilmente entre los pasos. |
| [<< Paso 2: Instalación del Core](core-installation)                                                                                             | [Paso 4: Instalación de la Base de Datos >>](database-installation) |
