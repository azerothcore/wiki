# Sobrescritura de Configuración con Variables de Entorno

Las variables de entorno pueden sobrescribir los valores de configuración.

Por defecto, el núcleo escuchará los valores de configuración en este orden:

```
1. Variables de entorno
2. Archivo .conf
3. Valores base definidos en el núcleo
```

Las claves de las variables de entorno se generan automáticamente en base a las claves definidas en el archivo .conf.

```cpp
    // Ejemplo de conversiones:
    //   SomeConfig => SOME_CONFIG
    //   myNestedConfig.opt1 => MY_NESTED_CONFIG_OPT_1
    //   LogDB.Opt.ClearTime => LOG_DB_OPT_CLEAR_TIME
    //   GM.InGMList.Level   => AC_GM_IN_GMLIST_LEVEL
```

## Ejemplo de uso

**Unix:**
```sh
$ export AC_DATA_DIR=/usr
$ AC_WORLD_SERVER_PORT=8080 ./worldserver
```

**Windows:**
```ps
> $env:AC_REALM_ID = '2'; .\worldserver
```
