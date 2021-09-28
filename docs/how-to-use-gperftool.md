# How to use GPERFTool

AzerothCore integrates the google performance tools library that allows you to analyse the code execution of your application when it comes to CPU and Memory.
In short: thread-friendly heap-checker, heap-profiler, and cpu-profiler.

* [Repository](https://github.com/gperftools/gperftools#readme)
* [Documentation](https://gperftools.github.io/gperftools/)

## Install (Ubuntu):

Run in a terminal: `sudo apt-get install google-perftools libgoogle-perftools-dev`

Note: dependencies above are already installed in our docker file

## Usage (with the AzerothCore dashboard):

1. To enable the gperftools you need to compile with the `-DWITH_PERFTOOLS=ON -DNOJEM=ON -DWITH_DYNAMIC_LINKING=0` compiler flag. You can use CUSTOMOPTIONS in `config.sh` to set it for the dashboard compiler. You also need to set the `CTYPE` conf to at least `RelWithDebInfo` (faster but less info) or `Debug` (slower but more info).
2. Configure the variables inside the `config.sh`, at the ` GOOGLE PERF TOOLS` section, accordingly to your needs.
3. run the worldserver with the `sudo ./acore.sh run-worldserver`
4. run `sudo killall -12 worldserver` This command will start the monitoring process. 
5. Run `sudo killall -12 worldserver` again to stop the process when you want. At this time you will have the .prof file ready in the folder configured below.
6. Run `google-pprof --callgrind <path/of/worldserver/bin> </path/of/prof/file> > worldserver.callgrind` This will generate a callgrind file that can be read with
[QCacheGrind](https://sourceforge.net/projects/qcachegrindwin/), [KCacheGrind](http://kcachegrind.sourceforge.net/html/Home.html) or any other compatible tools

This is what you will see (screenshot of KCacheGrind):

![kcachegrind](https://user-images.githubusercontent.com/147092/117697104-615a1f00-b1c2-11eb-8599-f5893a04de0c.png)
