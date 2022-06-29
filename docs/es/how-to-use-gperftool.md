# Cómo usar GPERFTool

AzerothCore integra la biblioteca de herramientas de rendimiento de Google que le permite analizar la ejecución del código de su aplicación en lo que respecta a la CPU y la memoria.
En resumen: thread-friendly heap-checker, heap-profiler, y cpu-profiler.

* [Repositorio](https://github.com/gperftools/gperftools#readme)
* [Documentación](https://gperftools.github.io/gperftools/)

## Instalar  (Ubuntu):

Ejecutar en una terminal: `sudo apt-get install google-perftools libgoogle-perftools-dev`

Nota: las dependencias anteriores ya están instaladas en nuestro archivo docker

##  Usando (con el tablero AzerothCore):

1. Para habilitar gperftools debe compilar con el indicador del compilador `-DWITH_PERFTOOLS=ON -DNOJEM=ON -DWITH_DYNAMIC_LINKING=0`. Puede usar CUSTOMOPTIONS en `config.sh` para configurarlo para el compilador del tablero. También debe establecer la configuración de `CTYPE` en al menos `RelWithDebInfo` (más rápido pero con menos información) o `Debug` (más lento pero con más información).
2. Configure las variables dentro de  `config.sh`, en la sección ` GOOGLE PERF TOOLS` según sus necesidades
3. Ejecute el  worldserver con `sudo ./acore.sh run-worldserver`
4. Ejecute `sudo killall -12 worldserver` Este comando iniciará el proceso de monitoreo.
5. Ejecute `sudo killall -12 worldserver` nuevamente para detener el proceso cuando lo desee. En este momento tendrás listo el archivo .prof en la carpeta configurada a continuación.
6. Ejecute `google-pprof --callgrind <path/of/worldserver/bin> </path/of/prof/file> > worldserver.callgrind` Esto generará un archivo callgrind que se puede leer con
[QCacheGrind](https://sourceforge.net/projects/qcachegrindwin/), [KCacheGrind](http://kcachegrind.sourceforge.net/html/Home.html) o cualquier otra herramienta compatible.

Esto es lo que verá (captura de pantalla de KCacheGrind):

![kcachegrind](https://user-images.githubusercontent.com/147092/117697104-615a1f00-b1c2-11eb-8599-f5893a04de0c.png)
