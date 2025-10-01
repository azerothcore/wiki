# FreeBSD

## Instalar dependencias
Necesita instalar las dependencias de compilación y tiempo de ejecución:

```
pkg install mysql80-server
pkg install cmake
pkg install boost-all
```
## Instalar Azerothcore

Clonar el proyecto

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```

Ingresar al directorio del proyecto

```
cd azerothcore
```

Crear el directorio de compilación

```
mkdir build
```

Entrar al directorio

```
cd build
```

Entrar al directorio

```
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static
```

Compilar Azerothcore

```
make -j<number of cores>
```

Instalar Azerothcore

```
make install
```

