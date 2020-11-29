# Unit testing at AzerothCore

## How to compile and run the AC unit tests

1. You have to compile your core by passing `-DUNIT_TESTS=1` in your `cmake` command. 

For example:

```
cd azerothcore
mkdir build
cd build
cmake ../ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=1 -DUNIT_TESTS=1
make install -j 6
```

2. You can now run the unit tests using:

```
./build/src/test/unit_tests
```

## How to write unit tests for AzerothCore

### Googletest Framework

We use [googletest](https://github.com/google/googletest) at AzerothCore as our testing framework. Some useful references that explain how it works are available at:

- https://github.com/google/googletest/blob/master/googletest/docs/primer.md
- https://github.com/google/googletest/blob/master/googlemock/README.md
- https://github.com/nordlow/gtest-tutorial

You can find plenty of other references online that explain how to deal with googletest or unit testing in general. 
If you know some other useful resources, feel free to edit this page and add them.

We recommend to read the googletest docs **before** starting to write unit tests.

### File structure

Unit tests are located under `src/test`. To add new tests, just edit the existing files or create new ones.

We try to follow the same structure of the `src/*` directory, for example in order to test the file located at:

```
src/server/game/Miscellaneous/Formulas.h
```

We keep its test at:

```
src/test/server/game/Miscellaneous/FormulasTest.cpp
```

That's it, happy testing!
