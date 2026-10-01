---
redirect_from: "/cn/Hooks-Cmake"
---

# Hooks CMake

### AFTER_LOAD_CONF（未实现）

在配置文件加载完成之后、源码或构建步骤开始之前需要执行的自定义脚本或操作。

### BEFORE_SRC_LOAD（未实现）

在源码加载之前运行自定义脚本或操作。可用于准备环境或在源码被处理之前修改源文件。

### AFTER_SRC_LOAD（未实现）

在源码加载之后运行自定义脚本或操作。这是进行后处理、校验或生成额外文件的好地方。

### AFTER_AUTHSERVER_CMAKE（未实现）

在 authserver 的 CMake 处理完成之后运行自定义脚本或操作。可用于特定于 authserver 的构建后步骤或集成任务。

### AFTER_WORLDSERVER_CMAKE（未实现）

在 worldserver 的 CMake 处理完成之后运行自定义脚本或操作。可用于特定于 worldserver 的构建后步骤或集成任务。

### BEFORE_GAME_LIBRARY（未实现）

在游戏库构建之前运行自定义脚本或操作。可用于设置、修补或准备依赖。

### AFTER_GAME_LIBRARY（未实现）

在游戏库构建之后运行自定义脚本或操作。可用于主构建完成后的清理、打包或进一步的自动化操作。

## 如何创建和注册一个钩子

在 compiler 文件夹下的 [includes.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/compiler/includes/includes.sh) 中，是你注册钩子的地方。

此部分及以下内容可以使用 bash 或 CMake 语法。

```bash
function my_hook_function() {
    echo "Custom action!"
}
```

始终要先定义函数，然后再注册钩子，否则就没有什么可注册的了。

### 示例（注册钩子）

```bash
registerHooks "AFTER_SRC_LOAD" my_after_src_load_function
```

注册钩子时，你必须选择要使用的编译器钩子（`AFTER_LOAD_CONF`、`BEFORE_SRC_LOAD`、`AFTER_SRC_LOAD`、`AFTER_AUTHSERVER_CMAKE`、`AFTER_WORLDSERVER_CMAKE` 或 `BEFORE_GAME_LIBRARY`），然后告诉它每个编译器钩子关联哪个函数。

### 同时注册多个钩子

```bash
function after_src_load_hook() {
    echo "Source code loaded!"
}
function after_game_library_hook() {
    echo "Game library build complete!"
}
registerHooks "AFTER_SRC_LOAD" after_src_load_hook
registerHooks "AFTER_GAME_LIBRARY" after_game_library_hook
```

## 如何运行钩子

你不需要手动运行，它会自动在 compiler 文件夹下的 [functions.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/compiler/includes/functions.sh) 中被调用。

你将使用：`AFTER_LOAD_CONF`、`BEFORE_SRC_LOAD`、`AFTER_SRC_LOAD`、`AFTER_AUTHSERVER_CMAKE`、`AFTER_WORLDSERVER_CMAKE` 或 `BEFORE_GAME_LIBRARY`，目前这些均尚未实现。

## 故障排除

- 确保你的钩子函数在注册之前已经定义。
- 确保钩子确实在构建脚本中被调用（例如：`runHooks "AFTER_SRC_LOAD"`）。
- 如果你的钩子没有运行，请检查注册的钩子名称或函数名是否有拼写错误。

## 实用示例

```bash
function after_game_library_hook() {
    echo "Game library build complete. Running post-build steps!"
    tar -czf "$BINPATH/game_library.tar.gz" "$BINPATH/game_library.so"
}
registerHooks "AFTER_GAME_LIBRARY" after_game_library_hook
```

这会将你的构建输出目录（例如：`/home/user/build`）赋值给变量 `$BINPATH`，在 `game library` 构建完成后，钩子会将库文件打包成 `.tar.gz` 放在你的构建文件夹中。
