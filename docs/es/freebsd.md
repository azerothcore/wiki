# FreeBSD

## Instalar dependencias
Necesitas instalar las dependencias de compilación y de ejecución:

```
pkg install mysql80-server
pkg install cmake
pkg install boost-all
```
## Instalar AzerothCore

Clona el proyecto

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```

Entra en el directorio del proyecto

```
cd azerothcore
```

Crea el directorio de build

```
mkdir build
```

Entra en el directorio

```
cd build
```

Configura AzerothCore para la compilación

```
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static
```

Compila AzerothCore

```
make -j<número de núcleos>
```

Instala AzerothCore

```
make install
```
