# 在 Visual Studio 中运行 Worldserver 和 Authserver

通过 Visual Studio 运行 Worldserver 和 Authserver 有一些好处。

1. 你可以使用断点轻松调试代码，或者轻松找到崩溃的调用堆栈（Call Stack）。

    1. 它还能让你的服务器在遇到崩溃时暂停而不是崩溃，并且你可以在调试完成后轻松继续。

1. 如果你在修改代码，当你需要进入游戏测试时，这可以节省时间，因为你无需打开二进制文件夹并逐个启动它们。

## 配置 Visual Studio

1. 选择所需的构建配置，在本指南中我们将使用 Debug（调试）。

    <a href="/wiki/images/run-worldserver-and-authserver-in-visual-studio-1.jpg" target="_blank">
    <img src="/wiki/images/run-worldserver-and-authserver-in-visual-studio-1.jpg" height="50%" width="50%">
    </a>

1. 右键单击 **Solution 'AzerothCore' (20 of 20 projects)**。

    1. 选择 **Properties**（属性）。

    1. 选择 **Multiple Startup Projects**（多个启动项目）。

        1. 在下拉菜单中，为 **authserver** 和 **worldserver** 选择 **Start**（启动）。

    <a href="/wiki/images/run-worldserver-and-authserver-in-visual-studio-2.jpg" target="_blank">
    <img src="/wiki/images/run-worldserver-and-authserver-in-visual-studio-2.jpg" height="50%" width="50%">
    </a>

1. 右键单击 **authserver**。

    1. 选择 **Properties**（属性）。

    1. 选择 **Debugging**（调试）。

        1. 在 **Command Arguments**（命令参数）中选择你的 Debug 构建对应的 .conf 文件的路径。

        1. 在 **Working Directory**（工作目录）中选择你的二进制文件目录的路径。

    <a href="/wiki/images/run-worldserver-and-authserver-in-visual-studio-3.jpg" target="_blank">
    <img src="/wiki/images/run-worldserver-and-authserver-in-visual-studio-3.jpg" height="50%" width="50%">
    </a>

1. 对 **worldserver** 也执行第 3 步。

1. 启动 Worldserver 和 Authserver。

    1. 按 **Start**（启动）按钮或 **F5** 在 Visual Studio 中启动 Worldserver 和 Authserver。（这适合调试）

    1. 按 **Ctrl + F5** 在 Visual Studio 之外启动 Worldserver 和 Authserver
