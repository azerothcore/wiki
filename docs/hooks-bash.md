---
redirect_from: "/Hooks-Bash"
---

# Hooks Bash

## HOOKS FOR COMPILER

### ON_AFTER_OPTIONS (Unimplemented)

Custom scripts or actions that need to be executed after all build options are determined, but before configuration or compilation starts.


### ON_AFTER_CONFIG

Run custom scripts or actions after CMake configuration is complete, but before the actual build starts. For example, you might want to patch files, generate additional configs, or log configuration details.


### ON_AFTER_BUILD

Run custom scripts or actions after the build is finished, such as copying files, cleaning up, or post-processing build artifacts.


## How to create and register a hook

In [includes.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/compiler/includes/includes.sh)  under the compiler folder, is where you have register your hook.

### Example (Function)

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

Always the function first, before registering th hook, otherwise there's nothing to register.

### Example (Registering the Hook)

```bash
registerHooks "ON_AFTER_BUILD" my_custom_hook
```

```bash
registerHooks "ON_AFTER_CONFIG" my_config_hook
```

When registering the hooks, you've to choose what compiler hooks to use (`ON_AFTER_OPTIONS`, `ON_AFTER_CONFIG` or `ON_AFTER_BUILD`) than you tell what function to be associated to each compiler hook.

### Multiple Hooks at once

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

## How do I run the hook

You don't, it's ran automatically in [functions.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/compiler/includes/functions.sh) under the compiler folder.

You will the `runHooks "ON_AFTER_CONFIG"` and  `runHooks "ON_AFTER_BUILD"`. But `runHooks "ON_AFTER_OPTIONS"` is currently unimplemented.

## Troubleshooting

- Make sure your hook function is defined before you register it.
- Ensure the hook is actually called in the build scripts (example: `runHooks "ON_AFTER_BUILD"`.
- If your hook doesn't run, check for typos in the hook registered name or function name.

## Pratical Example

```bash
function copy_custom_config() {
    cp /path/to/myconfig.conf "$BINPATH/"
    echo "Custom config copied to $BINPATH"
}
registerHooks "ON_AFTER_BUILD" copy_custom_config
```

This will grab your build output directory (example: `/home/user/build`) under the variable name: `$BINPATH`, and copy the `myconfig.conf` file into the build output directory, so you will see `myconfig.conf` in the build folder.

