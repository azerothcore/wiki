# C�digos de salida

AzerothCore tiene 3 c�digos de salida predeterminados que se activan si apaga, reinicia o bloquea el servidor.

```cpp
enum ShutdownExitCode
{
    SHUTDOWN_EXIT_CODE = 0,
    ERROR_EXIT_CODE    = 1,
    RESTART_EXIT_CODE  = 2,
};
```

SHUTDOWN_EXIT_CODE se llama cuando usa los comandos **.server shutdown**, **.server idleshutdown**, **.server exit** o si [m_serviceStatus == 0](https://github.com/azerothcore /azerothcore-wotlk/blob/a594bf5b290e5476c61bab29809a079e93c5daa2/src/server/worldserver/Main.cpp#L575-L581) para Windows.

RESTART_EXIT_CODE se llama cuando usa los comandos **.server restart** y **.server idlerestart**.

ERROR_EXIT_CODE se llama a  cuando el servidor falla. Esto puede deberse a un desbordamiento de guid/id/entry, [Network.Threads](https://github.com/azerothcore/azerothcore-wotlk/blob/a594bf5b290e5476c61bab29809a079e93c5daa2/src/server/worldserver/worldserver.conf.dist# L2909-L2913) siendo <= 0 o si el servidor no puede inicializar la red.

La mejor manera de saber d�nde se llaman todos los c�digos de salida es busc�ndolos en el c�digo fuente.

## Comandos

```
.server idleshutdown #delay [#exit_code]
.server idlerestart #delay [#exit_code]
.server shutdown #delay [#exit_code]
.server restart #delay [#exit_code]
```

Los comandos **.server shutdown/restart**, **.server idleshutdown/restart** tienen un argumento para **[#exit_code]**.

El c�digo de salida predeterminado para apagar siempre es 0 y el c�digo de salida predeterminado para reiniciar siempre es 2 si el argumento se deja en blanco.

El argumento puede tomar un valor entre 0 y 125, lo que le permite generar un c�digo de salida personalizado que no sea el predeterminado.

## Scripts que incluyen c�digos de salida

Hacer que Worldserver env�e c�digos de salida le permite crear un script externo que puede actuar cuando lee un c�digo de salida espec�fico que se muestra.

Por ejemplo, es posible escribir un script para que se reinicie autom�ticamente si Worldserver env�a RESTART_EXIT_CODE.

Puede ver [este](https://github.com/azerothcore/azerothcore-exitcode-script) script por lotes para Windows sobre c�mo se pueden usar los c�digos de salida.
