---
redirect_from: "/cn/CMake-options"
---

# CMake 选项

## 性能（PERFORMANCE）

如果你想要禁用性能优化，请添加这个标志 `-DENABLE_EXTRAS=0`

仅在调试时需要。

## 额外日志（EXTRA LOGS）

如果你想要启用额外日志，请添加这个标志：`-DENABLE_EXTRA_LOGS=1`

注意：这会非常消耗 CPU。

## 警告（WARNINGS）

编译时启用所有警告：`-DWITH_WARNINGS=1`

## 预编译头（PCH）

禁用所有 PCH 的使用：

`-DNOPCH=1`

或者逐个禁用：
```
-DUSE_COREPCH=0
-DUSE_SCRIPTPCH=0
```

可能会增加编译时间。

## LIBSIDECAR

针对真正的 `libsidecar` 而非内置桩（stub）进行编译：`-DUSE_REAL_LIBSIDECAR=1`

仅在[集群模式](cluster-mode)下需要。共享库必须首先放置在 `deps/libsidecar` 中。

## 其他选项

其他选项可在此处查看：

* https://github.com/azerothcore/azerothcore-wotlk/blob/master/conf/dist/config.cmake#L58
* https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/cmake/showoptions.cmake
