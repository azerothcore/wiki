# Cluster Mode

| Installation Guide                                                                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 9: Optional Additions](optional-additions)                                                                                  |

{% include warning.html content="Cluster mode is <b>experimental</b> and still under development." %}

## Overview

Cluster mode lets several worldservers serve a **single realm**, splitting players and maps between them. Each worldserver can declare which maps it is willing to handle; [ToCloud9](https://github.com/walkline/ToCloud9) then assigns maps across the fleet and redirects players to the right worldserver when they change map.

AzerothCore only provides the integration points (config, map assignment hooks, login/redirect path, and the sidecar C API). The distributed logic lives in ToCloud9: service discovery, the **gateway** clients connect to, shared GUID pools, and the auth, characters, guild, mail, auction house, chat, group and matchmaking services.

For the architecture and the reasoning behind it, see the [ToCloud9 README](https://github.com/walkline/ToCloud9#readme) and the [AzerothCore discussion](https://github.com/azerothcore/azerothcore-wotlk/discussions/16748).

## Building

AzerothCore talks to ToCloud9 through **libsidecar**, a shared library from the ToCloud9 repository.

By default the core builds against an in-tree **stub** of that library, so cluster code compiles but does nothing. Normal (non-cluster) builds need no extra dependencies and are unaffected.

To run cluster mode you must link against the **real** library. The supported implementation is **libsidecar-cpp** (native C++, same C ABI).

### 1. Build libsidecar-cpp

In a ToCloud9 checkout:

```bash
cd game-server/libsidecar-cpp
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF
cmake --build . --config Release
```

On Windows, use an **x64** Native Tools / VS generator, for example:

```cmd
cmake .. -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF
cmake --build . --config Release
```

Pre-built Windows binaries are also published on the [ToCloud9 releases](https://github.com/walkline/ToCloud9/releases) page (`libsidecar-cpp-windows-x64-v143` for VS 2022, `v142` for VS 2019).

### 2. Install the library into AzerothCore

Place the artifacts under `deps/libsidecar/` of your AzerothCore source tree. CMake expects the shared library **next to** that directory’s `CMakeLists.txt` (not only under a nested `lib/`), and the C headers under `include/`.

On **macOS** and **Linux**, libsidecar-cpp is built with `VERSION` / `SOVERSION`, so the build directory contains **three** related names — one real binary and two symlinks. Copy **all** of them and **preserve the symlinks** (do not flatten them into three full copies).

| Platform | Typical files in the build directory |
| -------- | ------------------------------------ |
| macOS | `libsidecar.0.0.1.dylib` (real file)<br>`libsidecar.0.dylib` → `libsidecar.0.0.1.dylib`<br>`libsidecar.dylib` → `libsidecar.0.dylib` |
| Linux | `libsidecar.so.0.0.1` (real file)<br>`libsidecar.so.0` → `libsidecar.so.0.0.1`<br>`libsidecar.so` → `libsidecar.so.0` |
| Windows | `libsidecar.dll` **and** `libsidecar.lib` (no versioned symlinks) |

AzerothCore’s CMake looks up the unversioned name (`libsidecar.dylib` / `libsidecar.so` / `libsidecar.dll`). The loader still follows the symlink chain to the real binary, so omitting the versioned file or breaking the links will fail at link or run time.

Also keep the headers in sync with the library you built:

```text
deps/libsidecar/include/   ← copy from ToCloud9 game-server/libsidecar-cpp/include/
```

The cluster-mode tree already ships matching headers; replace them when you upgrade libsidecar.

Example (macOS / Linux, after a Release build of libsidecar-cpp). Use `cp -a` so the two symlinks stay symlinks:

```bash
# macOS
cp -a game-server/libsidecar-cpp/build/libsidecar*.dylib /path/to/azerothcore/deps/libsidecar/
# Linux
# cp -a game-server/libsidecar-cpp/build/libsidecar.so* /path/to/azerothcore/deps/libsidecar/

cp game-server/libsidecar-cpp/include/*.h /path/to/azerothcore/deps/libsidecar/include/

# runtime loader also needs the same trio (real file + two symlinks):
sudo cp -a game-server/libsidecar-cpp/build/libsidecar*.dylib /usr/lib/   # macOS
# sudo cp -a game-server/libsidecar-cpp/build/libsidecar.so* /usr/lib/  # Linux
```

On Windows, copy `libsidecar.dll` next to `worldserver.exe` (or onto `PATH`) in addition to `deps/libsidecar/` for linking.

### 3. Configure AzerothCore with the real library

Pass the [CMake option](cmake-options) **`-DUSE_REAL_LIBSIDECAR=ON`** when configuring the core.

The CMake summary confirms the choice with:

```text
* Use stub for libsidecar         : No
```

If that line still says `Yes`, the real library was not selected or was not found where CMake expects it.

## Configuration

The options live in the `CLUSTER SETTINGS` block at the end of `worldserver.conf`. See [How to work with Conf Files](how-to-work-with-conf-files) before editing.

| Setting | Default | Description |
| ------- | ------- | ----------- |
| `Cluster.Enabled` | `0` | Enables cluster mode and initializes libsidecar. |
| `Cluster.AvailableMaps` | `""` | Comma-separated list of map IDs this worldserver may handle, e.g. `"0,1,573"`. Empty means any map; ToCloud9’s servers-registry then assigns a subset across the fleet. |
| `Cluster.IsCrossrealm` | `0` | Enables cross-realm behaviour. Requires a connection to a MySQL cross-realm reverse proxy (ToCloud9 `mysqlreverseproxy`). |

Like other AzerothCore settings, these can be overridden with environment variables (`AC_CLUSTER_ENABLED`, `AC_CLUSTER_AVAILABLE_MAPS`, `AC_CLUSTER_IS_CROSSREALM`, and related ports such as `AC_WORLD_SERVER_PORT`). Sidecar service endpoints are configured separately via `TC9_*` / service env vars documented in ToCloud9.

{% include important.html content="With <code>Cluster.Enabled = 1</code> the ToCloud9 gateway becomes the trusted authentication boundary. The worldserver then skips session-key digest verification, packet encryption, warden, IP/country locks, ban and minimum security level enforcement, and the character ownership check on login. The worldserver port must only be reachable by the gateway, <b>never directly by players</b>." %}

You must also run the ToCloud9 microservices (at least servers-registry, guidserver, gateway, authserver, and the services you rely on for guild/mail/chat/group/auction/matchmaking) and point libsidecar at them. Do **not** run AzerothCore’s own `authserver` for that realm when using the ToCloud9 auth path.

## Running a cluster

Setup instructions are maintained in the ToCloud9 repository:

* [Docker Compose](https://github.com/walkline/ToCloud9#readme) — quickest way to get a full cluster
* [Helm chart](https://github.com/walkline/ToCloud9/tree/master/chart) — Kubernetes
* [Windows + WSL, without Docker](https://github.com/walkline/ToCloud9/blob/master/doc/RunNonDockerWinWSLAzerothCore.md)
* [Windows native, without Docker](https://github.com/walkline/ToCloud9/blob/master/doc/RunNonDockerWindowsAzerothCore.md) (libsidecar-cpp)
* **Linux / macOS without Docker**: build libsidecar-cpp as above, configure the core with `-DUSE_REAL_LIBSIDECAR=ON`, apply ToCloud9 SQL migrations for the characters DB, start the ToCloud9 services, then run one or more worldservers with `Cluster.Enabled = 1` (and distinct ports / `TC9_GRPC_PORT` / `TC9_HEALTH_CHECK_PORT` per process)

Minimal multi-worldserver example (after services are up):

```bash
# worldserver A
AC_CLUSTER_ENABLED=1 AC_WORLD_SERVER_PORT=9601 ./worldserver

# worldserver B (override sidecar ports so they do not clash)
AC_CLUSTER_ENABLED=1 AC_WORLD_SERVER_PORT=9602 \
  TC9_GRPC_PORT=9603 TC9_HEALTH_CHECK_PORT=9604 ./worldserver

# optional: pin a process to a single map (e.g. Icecrown Citadel)
AC_CLUSTER_ENABLED=1 AC_CLUSTER_AVAILABLE_MAPS=631 AC_WORLD_SERVER_PORT=9605 \
  TC9_GRPC_PORT=9606 TC9_HEALTH_CHECK_PORT=9607 ./worldserver
```

## Getting help

Cluster mode issues that are not specific to the AzerothCore side belong in the [ToCloud9 issue tracker](https://github.com/walkline/ToCloud9/issues) or its [Discord channel](https://discord.gg/QxfBD9uGbN).
