# Códigos de salida

AzerothCore tiene 3 códigos de salida por defecto que se invocan si se apaga, reinicia o bloquea el servidor.

```cpp
enum ShutdownExitCode
{
    SHUTDOWN_EXIT_CODE = 0,
    ERROR_EXIT_CODE    = 1,
    RESTART_EXIT_CODE  = 2,
};
```

`SHUTDOWN_EXIT_CODE` es llamado cuando se utilizan los comandos **.server shutdown**, **.server idleshutdown**, **.server exit** o si el [m_serviceStatus == 0](https://github.com/azerothcore/azerothcore-wotlk/blob/a594bf5b290e5476c61bab29809a079e93c5daa2/src/server/worldserver/Main.cpp#L575-L581) para Windows.

`ERROR_EXIT_CODE` es llamado cuando el servidor falla. Esto puede deberse a un desbordamiento de guid/id/entry, a que [Network.Threads](https://github.com/azerothcore/azerothcore-wotlk/blob/a594bf5b290e5476c61bab29809a079e93c5daa2/src/server/worldserver/worldserver.conf.dist#L2909-L2913) sea <= 0 o a que el servidor no pueda inicializar la red.

`RESTART_EXIT_CODE` se llama cuando se utilizan los comandos **.server restart** y **.server idlerestart**.

La mejor manera de saber dónde se llaman todos los códigos de salida es encontrarlos en el código fuente.

## Commands

```
.server idleshutdown #delay [#exit_code]
.server idlerestart #delay [#exit_code]
.server shutdown #delay [#exit_code]
.server restart #delay [#exit_code]
```

Los comandos **.server shutdown/restart**, **.server idleshutdown/restart** tienen un argumento para **[#exit_code]**.

El código de salida por defecto para el apagado es siempre 0 y el código de salida por defecto para el reinicio es siempre 2 si el argumento se deja en blanco.

El argumento puede tomar un valor entre 0 - 125 que le permite emitir un código de salida personalizado distinto de los predeterminados.

## Scripts que incluyen códigos de salida

El hecho de que el Worldserver envíe códigos de salida le permite crear un script externo que puede actuar cuando lee un código de salida específico que se muestra.

Por ejemplo, es posible escribir un script para reiniciar automáticamente si el Worldserver envía `RESTART_EXIT_CODE`.

Puede ver [esta](https://github.com/azerothcore/azerothcore-exitcode-script) secuencia de comandos por lotes para Windows.
