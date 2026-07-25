# Cluster Mode

{% include warning.html content="Cluster mode is <b>experimental</b> and still under development." %}

## Overview

Cluster mode lets several worldservers serve a **single realm**, splitting players and maps between them. Each worldserver can be told which maps it is allowed to handle, and players are redirected to the right worldserver when they change map.

AzerothCore only provides the integration points. All of the distributed logic lives in the [ToCloud9](https://github.com/walkline/ToCloud9) project: service discovery, the gateway that players actually connect to, shared GUID pools, and the guild, mail, auction house, chat and group services.

For the architecture and the reasoning behind it, see the [ToCloud9 README](https://github.com/walkline/ToCloud9#readme).

## Building

AzerothCore talks to ToCloud9 through `libsidecar`, a shared library built from the ToCloud9 repository.

By default the core builds against a **stub** of that library, so cluster code compiles but does nothing. Normal builds need no extra dependencies and are unaffected.

To build against the real library:

1. Build it in a ToCloud9 checkout:

```bash
make build-sidecar
```

2. Copy the resulting library into `deps/libsidecar/` of your AzerothCore source tree:

| Platform | Files |
| -------- | ----- |
| Linux    | `libsidecar.so` |
| macOS    | `libsidecar.dylib` |
| Windows  | `libsidecar.dll` and `libsidecar.lib` |

3. Configure the build with the [CMake option](cmake-options) `-DUSE_REAL_LIBSIDECAR=1`.

The CMake summary confirms the choice with `Use stub for libsidecar : No`.

## Configuration

The options live in the `CLUSTER SETTINGS` block at the end of `worldserver.conf`. See [How to work with Conf Files](how-to-work-with-conf-files) before editing.

| Setting | Default | Description |
| ------- | ------- | ----------- |
| `Cluster.Enabled` | `0` | Enables cluster mode. |
| `Cluster.AvailableMaps` | `""` | Comma-separated list of map IDs this worldserver may handle, e.g. `"0,1,573"`. Empty means any map. |
| `Cluster.IsCrossrealm` | `0` | Enables cross-realm functionality. Requires a connection to a MySQL cross-realm reverse proxy. |

{% include important.html content="With <code>Cluster.Enabled = 1</code> the ToCloud9 gateway becomes the trusted authentication boundary. The worldserver then skips session-key digest verification, packet encryption, warden, IP/country locks, ban and minimum security level enforcement, and the character ownership check on login. The worldserver port must only be reachable by the gateway, <b>never directly by players</b>." %}

## Running a cluster

Setup instructions are maintained in the ToCloud9 repository:

* [Docker Compose](https://github.com/walkline/ToCloud9#readme), the quickest way to get a cluster running.
* [Windows + WSL, without Docker](https://github.com/walkline/ToCloud9/blob/master/doc/RunNonDockerWinWSLAzerothCore.md)
* [Windows, without Docker](https://github.com/walkline/ToCloud9/blob/master/doc/RunNonDockerWindowsAzerothCore.md)

## Getting help

Cluster mode issues that are not specific to the AzerothCore side belong in the [ToCloud9 issue tracker](https://github.com/walkline/ToCloud9/issues) or its [Discord channel](https://discord.gg/QxfBD9uGbN).
