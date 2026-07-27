---
redirect_from: "/CMake-options"
---

# CMake Options

## PERFORMANCE

If you want to disable performance optimizations, add this flag `-DENABLE_EXTRAS=0`

Only necessary if you're debugging.

## EXTRA LOGS

If you want to enable extra logs, add this flag: `-DENABLE_EXTRA_LOGS=1`

Note: Will be CPU intensive.

## WARNINGS

Enable all warnings when compiling: `-DWITH_WARNINGS=1`

## Precompiled Headers (PCH)

Disable all uses of PCH:

`-DNOPCH=1`

Or one by one:
```
-DUSE_COREPCH=0
-DUSE_SCRIPTPCH=0
```

May increase build times.

## LIBSIDECAR

Build against the real `libsidecar` instead of the built-in stub: `-DUSE_REAL_LIBSIDECAR=1`

Only needed for [Cluster Mode](cluster-mode). The shared library must be placed in `deps/libsidecar` first.

## OTHER OPTIONS

Other options are available here:

* https://github.com/azerothcore/azerothcore-wotlk/blob/master/conf/dist/config.cmake#L58
* https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/cmake/showoptions.cmake
