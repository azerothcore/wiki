# Trabajar con archivos de configuración (.conf & .conf.dist)

## ¿Por qué worldserver y authserver necesitan que los archivos .conf.dist estén presentes en la ruta de instalación?

Es porque AzerothCore los utiliza como "fallback" para las configuraciones que no tienes en el archivo .conf copiado (por ejemplo si hemos actualizado la dist o has eliminado una conf)

## Cómo se componen los archivos de configuración

Todos los archivos de configuración cargan sus propiedades bajo 2 grupos de macros (debe tener uno de ellos en la cabecera de su archivo de configuración):

[authserver] -> para las configuraciones del servidor de autenticación

[worldserver] -> para las configuraciones de los servidores de mundo

Una propiedad está compuesta por un nombre y un valor que se cargará dentro de un objeto al iniciar el servidor / recargar la configuración.

## ¿Cómo funciona la carga de múltiples archivos .conf?

Al iniciar el servidor leemos primero los archivos .dist y cargamos todas las propiedades bajo el objeto sConfig. El archivo .conf será cargado justo después: todas las nuevas propiedades serán añadidas al objeto sConfig, en cambio las propiedades con el mismo nombre sobreescriben las antiguas del .dist

Esto le permite crear un pequeño archivo .conf que NO REQUIERE tener todas las propiedades de .conf.dist dentro ya que han sido cargadas anteriormente.

Por ejemplo, si quieres mantener toda la conf por defecto pero tienes que cambiar sólo las propiedades de la base de datos, puedes crear un archivo worldserver.conf con sólo:

```
[worldserver]
LoginDatabaseInfo     = "127.0.0.1;3306;root;root;azerothcore_test_auth"
WorldDatabaseInfo     = "127.0.0.1;3306;root;root;azerothcore_test_world"
CharacterDatabaseInfo = "127.0.0.1;3306;root;root;azerothcore_test_chars"
```

## Configuración de los módulos

Después de cargar los archivos normales `.conf` y `.conf.dist`, puede cargar un número infinito de archivos de configuración utilizando la API de scripts/módulos. Tendrán el mismo comportamiento que el descrito anteriormente.

**Nota:** No recomendamos sobrescribir las propiedades de configuración del servidor ya que puede tener problemas de concurrencia con otros módulos que también las utilizan. En su lugar, **crea nuevas propiedades con nombres espaciados**.

Por ejemplo, si quieres modificar la funcionalidad de "desactivar la respiración de agua" en tu módulo. En lugar de utilizar la propiedad existente de `worldserver.conf.dist`:

```cpp
DisableWaterBreath = x
```

Utiliza un espacio de nombres como:

```cpp
MyModuleName.DisableWaterBreath = x
```

Y trabajar con eso.


## ¿Puedo utilizar rutas relativas en los archivos de configuración?

Sí, pero no es recomendable. Cada ruta es relativa al directorio desde el que lanzaste el authserver/worldserver, tanto si lo lanzaste manualmente como a través de un script. Así que si haces esto (ejemplo de linux):

```bash
cd /tmp/test
./path/to/worldserver
```

Y tienes rutas relativas en el worldserver.conf como `LogsDir = "../logs/worldserver/"`. Esto creará los registros dentro de `/logs/worldserver`.

## Conclusión

Los archivos de configuración se cargarán siguiendo este flujo:

```
authserver.conf.dist
authserver.conf (overwrite properties from authserver.conf.dist)
worldserver.conf.dist
worldserver.conf (overwrite properties from worldserver.conf.dist)
modules *.conf.dist
modules *.conf (overwrite properties from each module's .conf.dist)
```
