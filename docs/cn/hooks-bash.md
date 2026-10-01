---
redirect_from: "/cn/Hooks-Bash"
---

# Hooks Bash

## 编译器钩子（HOOKS FOR COMPILER）

### ON_AFTER_OPTIONS（未实现）

在所有构建选项确定之后、配置或编译开始之前需要执行的自定义脚本或操作。

### ON_AFTER_CONFIG

在 CMake 配置完成之后、实际构建开始之前运行自定义脚本或操作。例如，你可能想修补文件、生成额外的配置，或记录配置细节。

### ON_AFTER_BUILD

在构建完成后运行自定义脚本或操作，例如复制文件、清理或对构建产物进行后处理。

## 如何创建和注册一个钩子

在 compiler 文件夹下的 [includes.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/compiler/includes/includes.sh) 中，是你注册钩子的地方。

### 示例（函数）

```bash
function my_custom_hook() {
    echo "This is my custom hook!"
    # Add your custom commands here
}
```

```bash
function my_config_hook() {
    echo "Configuration is complete!"
}
```

始终要先定义函数，然后再注册钩子，否则就没有什么可注册的了。

### 示例（注册钩子）

```bash
registerHooks "ON_AFTER_BUILD" my_custom_hook
```

```bash
registerHooks "ON_AFTER_CONFIG" my_config_hook
```

注册钩子时，你必须选择要使用的编译器钩子（`ON_AFTER_OPTIONS`、`ON_AFTER_CONFIG` 或 `ON_AFTER_BUILD`），然后告诉它每个编译器钩子关联哪个函数。

### 同时注册多个钩子

```bash
function my_build_hook() {
    echo "Build finished!"
}
function my_config_hook() {
    echo "Config finished!"
}
registerHooks "ON_AFTER_BUILD" my_build_hook
registerHooks "ON_AFTER_CONFIG" my_config_hook
```

## 如何运行钩子

你不需要手动运行，它会自动在 compiler 文件夹下的 [functions.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/compiler/includes/functions.sh) 中被调用。

你将使用 `runHooks "ON_AFTER_CONFIG"` 或 `runHooks "ON_AFTER_BUILD"`。但 `runHooks "ON_AFTER_OPTIONS"` 目前尚未实现。

## 故障排除

- 确保你的钩子函数在注册之前已经定义。
- 确保钩子确实在构建脚本中被调用（例如：`runHooks "ON_AFTER_BUILD"`）。
- 如果你的钩子没有运行，请检查注册的钩子名称或函数名是否有拼写错误。

## 实用示例

```bash
function copy_custom_config() {
    cp /path/to/myconfig.conf "$BINPATH/"
    echo "Custom config copied to $BINPATH"
}
registerHooks "ON_AFTER_BUILD" copy_custom_config
```

这会将你的构建输出目录（例如：`/home/user/build`）赋值给变量 `$BINPATH`，并将 `myconfig.conf` 文件复制到构建输出目录中，因此你会在构建文件夹中看到 `myconfig.conf`。
