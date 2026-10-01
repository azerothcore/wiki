# 使用环境变量覆盖配置

环境变量可以覆盖配置值。

默认情况下，核心会按以下顺序读取配置值：

```
1. 环境变量
2. .conf 文件
3. 核心中定义的基础值
```

环境变量的键是根据 .conf 文件中定义的键自动生成的。

```cpp
    // 转换示例：
    //   SomeConfig => SOME_CONFIG
    //   myNestedConfig.opt1 => MY_NESTED_CONFIG_OPT_1
    //   LogDB.Opt.ClearTime => LOG_DB_OPT_CLEAR_TIME
    //   GM.InGMList.Level   => AC_GM_IN_GMLIST_LEVEL
```

## 使用示例

**Unix:**
```sh
$ export AC_DATA_DIR=/usr
$ AC_WORLD_SERVER_PORT=8080 ./worldserver
```

**Windows:**
```ps
> $env:AC_REALM_ID = '2'; .\worldserver
```
