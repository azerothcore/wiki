---
redirect_from: "/Environment-Variable"
---

# Variable de entorno

### Introducción
Para usar el servidor MySQL desde la línea de comandos, debe tener la ruta de acceso correcta del sistema. Esto suele hacerse automáticamente.

Cómo comprobar si el servidor MySQL es una variable de entorno:
* Presione `Windows + R` y escriba cmd
* En el CMD abierto escriba `mysql`

Si el servidor MySQL no es una variable de entorno, recibirá un error como: `Comando no reconocido`

### Requisitos
Es imprescindible tener ya instalado el servidor MySQL, si no tienes instalado el servidor MySQL sigue [este tutorial](http://www.azerothcore.org/wiki/Requirements)

### Procedimiento

* Busque `mysql.exe`. Por ejemplo: `C:\Program Files\MySQL\MySQL Server 5.6\bin`
* Buscar `Editar las variables de entorno del sistema`
* Click `Environment Variables` and locate `User variables for $USERNAME`
* Seleccione la variable `Path` y haga clic en Editar
* Presione el botón «Nuevo» e inserte la ruta a «mysql.exe» que encontró anteriormente
* * Ejemplo: `C:\Program Files\MySQL\MySQL Server 5.6\bin`

Ahora todo está configurado y puedes acceder a `mysql` desde la línea de comando.

Para comprobar si la configuración se realizó correctamente presione `Windows + R` y escriba cmd, cuando escriba `mysql` en la consola verá todas las opciones.

[Haga clic aquí para volver a la configuración de la base de datos](http://www.azerothcore.org/wiki/Database-Setup)
