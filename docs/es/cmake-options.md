---
redirect_from: "/CMake-options"
---

# Opciones de CMake

## RENDIMIENTO

Si quieres desactivar las optimizaciones de rendimiento, añade esta flag `-DENABLE_EXTRAS=0`.

Sólo es necesario si estás depurando.

## EXTRA LOGS

Si desea activar los registros adicionales, añada esta flag: `-DENABLE_EXTRA_LOGS=1`.

Nota: Será un uso intensivo de la CPU.

## ADVERTENCIAS

Habilitar todas las advertencias al compilar: `-DWITH_WARNINGS=1`

## Cabeceras precompiladas (PCH)

Desactivar todos los usos de PCH: `-DNOPCH=1`

O uno por uno:

```
-DUSE_COREPCH=0
-DUSE_SCRIPTPCH=0
```

Puede aumentar los tiempos de construcción.

## OTRAS OPCIONES

Hay otras opciones disponibles aquí:

- https://github.com/azerothcore/azerothcore-wotlk/blob/master/conf/dist/config.cmake#L58
- https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/cmake/showoptions.cmake
