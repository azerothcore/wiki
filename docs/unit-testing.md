# Unit testing at AzerothCore

## How to compile and run the AC unit tests

1. You have to compile your core by passing `-DBUILD_TESTING=1` in your `cmake` command. 

For example:

```
cd azerothcore
mkdir build
cd build
cmake ../ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static -DBUILD_TESTING=1
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
- https://github.com/google/googletest/blob/master/googlemock/docs/for_dummies.md

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

### Singleton issues

We have some legacy code in AzerothCore that is tightly coupled and there are singletons that are impossible to mock without some refactoring.

Following the [gmock guidelines](https://github.com/google/googletest/blob/master/googlemock/docs/for_dummies.md), to mock a class you should first define its interface. Then you can create mocks and use them when unit testing.

Examples of refactoring AzerothCore singletons to make them mockable (and improve the software architecture in general) are available:

- [sLog](https://github.com/azerothcore/azerothcore-wotlk/pull/3801)
- [sWorld](https://github.com/azerothcore/azerothcore-wotlk/pull/3862)

### Existing unit tests examples in AzerothCore

- All available in [src/test](https://github.com/azerothcore/azerothcore-wotlk/tree/master/src/test)

### Run tests in IDEs

You can also run the tests directly in IDEs such as [CLion](https://github.com/azerothcore/azerothcore-wotlk/discussions/3881) 

CLion lets you easily run the tests with debug and with coverage:

![AzerothCore running tests with CLion](https://user-images.githubusercontent.com/75517/101983422-520a9000-3c7b-11eb-8442-5c9fd18e13f6.png)

then it shows which lines of the code are covered by the tests (green lines) and which ones are still uncovered (red lines):

![AzerothCore test coverage CLion](https://user-images.githubusercontent.com/75517/101983433-6fd7f500-3c7b-11eb-882d-0aed16f0f03a.png)


Happy testing!
