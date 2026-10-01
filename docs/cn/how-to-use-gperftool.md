# 如何使用 GPERFTool

AzerothCore 集成了 google performance tools 库，它允许你在 CPU 和内存方面分析应用程序的代码执行情况。
简而言之：线程友好的堆检查器（heap-checker）、堆分析器（heap-profiler）和 CPU 分析器（cpu-profiler）。

* [仓库](https://github.com/gperftools/gperftools#readme)
* [文档](https://gperftools.github.io/gperftools/)

## 安装（Ubuntu）：

在终端中运行：

- Ubuntu 26.04：`sudo apt-get install libgoogle-perftools-dev`
- Ubuntu 24.04：`sudo apt-get install google-perftools libgoogle-perftools-dev`

注意：上述依赖已安装在我们的 docker 文件中。

Ubuntu 26.04 移除了 `google-perftools` 包，该包提供了本页末尾使用的 `google-pprof` 命令。请在那里单独安装 [pprof](https://github.com/google/pprof) 工具（`go install github.com/google/pprof@latest`），并使用 `pprof` 而不是 `google-pprof`。

## 用法（配合 AzerothCore 仪表盘）：

1. 要启用 gperftools，你需要使用 `-DWITH_PERFTOOLS=ON -DNOJEM=ON -DWITH_DYNAMIC_LINKING=0` 编译器标志进行编译。你可以在 `config.sh` 中使用 CUSTOMOPTIONS 来为仪表盘编译器设置它。你还需要将 `CTYPE` 配置至少设置为 `RelWithDebInfo`（更快但信息较少）或 `Debug`（较慢但信息更多）。
2. 根据你的需要，配置 `config.sh` 中 `GOOGLE PERF TOOLS` 部分内的变量。
3. 使用 `sudo ./acore.sh run-worldserver` 运行 worldserver。
4. 运行 `sudo killall -12 worldserver`。此命令将启动监控进程。
5. 当你想停止时，再次运行 `sudo killall -12 worldserver`。此时你将拥有一个 .prof 文件，就绪于下面配置的文件夹中。
6. 运行 `google-pprof --callgrind <path/of/worldserver/bin> </path/of/prof/file> > worldserver.callgrind`。这将生成一个 callgrind 文件，可以用
[QCacheGrind](https://sourceforge.net/projects/qcachegrindwin/)、[KCacheGrind](http://kcachegrind.sourceforge.net/html/Home.html) 或任何其他兼容工具读取。

这就是你将看到的（KCacheGrind 的截图）：

![kcachegrind](https://user-images.githubusercontent.com/147092/117697104-615a1f00-b1c2-11eb-8599-f5893a04de0c.png)
