---
redirect_from: "/Environment-Variable"
---

# Variable de entorno

### Introducción
Para usar el servidor MySQL desde la línea de comandos, debes tener el path del sistema correcto. Esto normalmente se hace automáticamente.

Cómo comprobar si el servidor MySQL es una variable de entorno:
* Pulsa `Windows + R` y escribe cmd
* En el CMD abierto escribe `mysql`

Si el servidor MySQL no es una variable de entorno obtendrás un error como: `Not recognised command`

### Requisitos
Es imprescindible tener el servidor MySQL ya instalado; si no tienes MySQL server instalado sigue [este tutorial](http://www.azerothcore.org/wiki/Requirements)

### Procedimiento

* Localiza `mysql.exe`. Por ejemplo: `C:\Program Files\MySQL\MySQL Server 5.6\bin`
* Busca `Editar las variables de entorno del sistema`
* Haz click en `Variables de entorno` y localiza `Variables de usuario para $USERNAME`
* Selecciona la variable `Path` y haz click en Editar
* Pulsa el botón `Nuevo` e inserta el path a `mysql.exe` que localizaste antes
* * Ejemplo: `C:\Program Files\MySQL\MySQL Server 5.6\bin`

Ahora todo está configurado y puedes acceder a `mysql` desde la línea de comandos.

Para comprobar si la configuración se hizo correctamente pulsa `Windows + R` y escribe cmd; cuando escribas `mysql` en la consola verás todas las opciones.

[Haz click aquí para volver a la Configuración de la base de datos](http://www.azerothcore.org/wiki/Database-Setup)
