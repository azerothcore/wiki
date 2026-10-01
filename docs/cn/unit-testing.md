# AzerothCore 单元测试

## 如何编译并运行 AC 单元测试

1. 你必须在 `cmake` 命令中传入 `-DBUILD_TESTING=1` 来编译核心。

例如：

```
cd azerothcore
mkdir build
cd build
cmake ../ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static -DBUILD_TESTING=1
make install -j 6
```

2. 现在你可以使用以下命令运行单元测试：

```
./build/src/test/unit_tests
```

## 如何为 AzerothCore 编写单元测试

### Googletest 框架

我们在 AzerothCore 中使用 [googletest](https://github.com/google/googletest) 作为测试框架。一些介绍其工作原理的有用参考资料：

- http://google.github.io/googletest/primer.html
- https://github.com/google/googletest/blob/master/googlemock/README
- https://github.com/nordlow/gtest-tutorial
- https://google.github.io/googletest/gmock_for_dummies.html

你可以在网上找到许多其他介绍 googletest 或一般单元测试用法的参考资料。
如果你知道其他有用的资源，欢迎编辑此页面并将它们添加进来。

我们建议在开始编写单元测试**之前**阅读 googletest 文档。

### 文件结构

单元测试位于 `src/test` 目录下。要添加新测试，只需编辑现有文件或创建新文件。

我们尽量遵循与 `src/*` 目录相同的结构，例如，为了测试位于以下路径的文件：

```
src/server/game/Miscellaneous/Formulas.h
```

我们将它的测试放在：

```
src/test/server/game/Miscellaneous/FormulasTest.cpp
```

### 单例问题

AzerothCore 中有一些遗留代码耦合度高，存在一些不经过重构就无法 mock 的单例。

按照 [gmock 指南](https://github.com/google/googletest/blob/master/googlemock/docs/for_dummies)，要 mock 一个类，你应当首先定义它的接口。然后你就可以创建 mock 并在单元测试中使用它们。

以下是重构 AzerothCore 单例使其可 mock（并总体上改善软件架构）的示例：

- [sLog](https://github.com/azerothcore/azerothcore-wotlk/pull/3801)
- [sWorld](https://github.com/azerothcore/azerothcore-wotlk/pull/3862)

### AzerothCore 中现有的单元测试示例

- 全部位于 [src/test](https://github.com/azerothcore/azerothcore-wotlk/tree/master/src/test)

### 在 IDE 中运行测试

你也可以直接在 [CLion](https://github.com/azerothcore/azerothcore-wotlk/discussions/3881) 等 IDE 中运行测试。

CLion 可以让你轻松地以调试模式并带覆盖率运行测试：

![AzerothCore 使用 CLion 运行测试](https://user-images.githubusercontent.com/75517/101983422-520a9000-3c7b-11eb-8442-5c9fd18e13f6.png)

然后它会显示哪些代码行已被测试覆盖（绿色行），哪些仍未覆盖（红色行）：

![AzerothCore 使用 CLion 显示测试覆盖率](https://user-images.githubusercontent.com/75517/101983433-6fd7f500-3c7b-11eb-882d-0aed16f0f03a.png)


祝测试愉快！
