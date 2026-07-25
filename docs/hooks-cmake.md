---
redirect_from: "/Hooks-Cmake"
---

# Hooks CMake

### AFTER_LOAD_CONF (Unimplemented)

Custom scripts or actions that need to be executed after the configuration files are loaded, but before source code or build steps begin.


### BEFORE_SRC_LOAD (Unimplemented)

Run custom scripts or actions before the source code is loaded. Useful for preparing the environment or modifying source files before they are processed.


### AFTER_SRC_LOAD (Unimplemented)

Run custom scripts or actions after the source code is loaded. This is a good place for post-processing, validation, or generating additional files.


### AFTER_AUTHSERVER_CMAKE (Unimplemented)

Run custom scripts or actions after the CMake process for the authserver is complete. Useful for post-build steps or integration tasks specific to the authserver.


### AFTER_WORLDSERVER_CMAKE (Unimplemented)

Run custom scripts or actions after the CMake process for the worldserver is complete. Useful for post-build steps or integration tasks specific to the worldserver.


### BEFORE_GAME_LIBRARY (Unimplemented)

Run custom scripts or actions before the game library is built. Useful for setup, patching, or preparing dependencies.


### AFTER_GAME_LIBRARY (Unimplemented)

Run custom scripts or actions after the game library is built. Useful for cleanup, packaging, or further automation after the main build is done.


## How to create and register a hook

In [includes.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/compiler/includes/includes.sh)  under the compiler folder, is where you have register your hook.


This and below can be in bash or in CMake syntax.


```bash
function my_hook_function() {
    echo "Custom action!"
}
```

Always the function first, before registering th hook, otherwise there's nothing to register.

### Example (Registering the Hook)

```bash
registerHooks "AFTER_SRC_LOAD" my_after_src_load_function
```

When registering the hooks, you've to choose what compiler hooks to use (`AFTER_LOAD_CONF`, `BEFORE_SRC_LOAD`, `AFTER_SRC_LOAD`, `AFTER_AUTHSERVER_CMAKE`, `AFTER_WORLDSERVER_CMAKE` or `BEFORE_GAME_LIBRARY`) than you tell what function to be associated to each compiler hook.

### Multiple Hooks at once

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

## How do I run the hook

You don't, it's ran automatically in [functions.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/compiler/includes/functions.sh) under the compiler folder.

You will use the: `AFTER_LOAD_CONF`, `BEFORE_SRC_LOAD`, `AFTER_SRC_LOAD`, `AFTER_AUTHSERVER_CMAKE`, `AFTER_WORLDSERVER_CMAKE` or `BEFORE_GAME_LIBRARY` is currently unimplemented.

## Troubleshooting

- Make sure your hook function is defined before you register it.
- Ensure the hook is actually called in the build scripts (example: `runHooks "AFTER_SRC_LOAD"`).
- If your hook doesn't run, check for typos in the hook registered name or function name.

## Pratical Example

```bash
function after_game_library_hook() {
    echo "Game library build complete. Running post-build steps!"
    tar -czf "$BINPATH/game_library.tar.gz" "$BINPATH/game_library.so"
}
registerHooks "AFTER_GAME_LIBRARY" after_game_library_hook
```

This will grab your build output directory (example: `/home/user/build`) under the variable name: `$BINPATH`, after the `game library` is finished building the hook will zip/package library file into a `.tar.gz` in your build folder.