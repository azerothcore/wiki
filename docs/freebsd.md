# FreeBSD

## Install Dependencies
You need to install the build and runtime dependancies:

```
pkg install mysql80-server
pkg install cmake
pkg install boost-all
```
## Install Azerothcore

Clone the project

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```

Enter the project's directory

```
cd azerothcore
```

Create the build directory

```
mkdir build
```

Enter the directory

```
cd build
```

Configure azerothcore for building

```
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static
```

Compile Azerothcore

```
make -j<number of cores>
```

Install Azerothcore

```
make install
```

