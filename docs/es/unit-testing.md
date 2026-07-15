# Unit testing en AzerothCore

## Cómo compilar y ejecutar los unit tests de AC

1. Tienes que compilar tu core pasando `-DBUILD_TESTING=1` en tu comando `cmake`. 

Por ejemplo:

```
cd azerothcore
mkdir build
cd build
cmake ../ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static -DBUILD_TESTING=1
make install -j 6
```

2. Ahora puedes ejecutar los unit tests usando:

```
./build/src/test/unit_tests
```

## Cómo escribir unit tests para AzerothCore

### Framework Googletest

En AzerothCore usamos [googletest](https://github.com/google/googletest) como nuestro framework de testing. Algunas referencias útiles que explican cómo funciona están disponibles en:

- http://google.github.io/googletest/primer.html
- https://github.com/google/googletest/blob/master/googlemock/README
- https://github.com/nordlow/gtest-tutorial
- https://google.github.io/googletest/gmock_for_dummies.html

Puedes encontrar muchas otras referencias online que explican cómo trabajar con googletest o el unit testing en general. 
Si conoces algún otro recurso útil, siéntete libre de editar esta página y añadirlo.

Recomendamos leer la documentación de googletest **antes** de empezar a escribir unit tests.

### Estructura de archivos

Los unit tests están ubicados en `src/test`. Para añadir nuevos tests, simplemente edita los archivos existentes o crea nuevos.

Intentamos seguir la misma estructura del directorio `src/*`; por ejemplo, para testear el archivo ubicado en:

```
src/server/game/Miscellaneous/Formulas.h
```

Mantenemos su test en:

```
src/test/server/game/Miscellaneous/FormulasTest.cpp
```

### Problemas con los singletons

Tenemos algo de código heredado en AzerothCore que está fuertemente acoplado y hay singletons que son imposibles de mockear sin cierta refactorización.

Siguiendo las [directrices de gmock](https://github.com/google/googletest/blob/master/googlemock/docs/for_dummies), para mockear una clase primero deberías definir su interfaz. Luego puedes crear mocks y usarlos al hacer unit testing.

Hay ejemplos disponibles de refactorización de singletons de AzerothCore para hacerlos mockeables (y mejorar la arquitectura del software en general):

- [sLog](https://github.com/azerothcore/azerothcore-wotlk/pull/3801)
- [sWorld](https://github.com/azerothcore/azerothcore-wotlk/pull/3862)

### Ejemplos de unit tests existentes en AzerothCore

- Todos disponibles en [src/test](https://github.com/azerothcore/azerothcore-wotlk/tree/master/src/test)

### Ejecutar tests en IDEs

También puedes ejecutar los tests directamente en IDEs como [CLion](https://github.com/azerothcore/azerothcore-wotlk/discussions/3881) 

CLion te permite ejecutar fácilmente los tests con debug y con cobertura:

![AzerothCore running tests with CLion](https://user-images.githubusercontent.com/75517/101983422-520a9000-3c7b-11eb-8442-5c9fd18e13f6.png)

luego muestra qué líneas del código están cubiertas por los tests (líneas verdes) y cuáles siguen sin cubrir (líneas rojas):

![AzerothCore test coverage CLion](https://user-images.githubusercontent.com/75517/101983433-6fd7f500-3c7b-11eb-882d-0aed16f0f03a.png)


¡Feliz testing!
