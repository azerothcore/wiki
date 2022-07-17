# IP2LOCATION

Con IP2LOCATION podemos ver aproximadamente de qué país puede venir un jugador utilizando el comando `.pinfo <player>`.

Para poder utilizar este sistema tiene que proporcionar la base de datos **ip2location lite** a su `authserver`.

Descargar **IP2LOCATION-LITE-DB1.csv** de https://download.ip2location.com/lite/

Descomprima el archivo y colóquelo en el directorio de su elección.

En `authserver.conf` y `worldserver.conf` hay que poner la ruta completa del directorio incluyendo el `.csv` en IPLocationFile.

En el inicio de `Auth` y `Worldserver` podrá ver el archivo `.csv` cargado en el registro.
