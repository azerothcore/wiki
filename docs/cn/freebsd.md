# FreeBSD

{% include note.html content="本指南由社区制作。可能不是最新版本，也未经官方支持。" %}

## 安装依赖项
您需要安装构建和运行时依赖项：

```
pkg install mysql80-server
pkg install cmake
pkg install boost-all
```
## 安装 AzerothCore

克隆项目

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```

进入项目目录

```
cd azerothcore
```

创建构建目录

```
mkdir build
```

进入目录

```
cd build
```

配置 azerothcore 以进行构建

```
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static
```

编译 AzerothCore

```
make -j<核心数>
```

安装 AzerothCore

```
make install
```
