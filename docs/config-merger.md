# Config Merger Tool

A command-line tool to update your AzerothCore configuration files with new options from distribution files.

## Overview

When AzerothCore is updated, new configuration options may be added to the `.conf.dist` distribution files. The config merger tool compares your existing `.conf` files against the latest `.conf.dist` files and helps you add any missing options while preserving your custom settings.

Two versions are available: a **Python version** (recommended) and a legacy **PHP version**.

| | Python | PHP |
| - | - | - |
| Requirement | Python 3.6+ | PHP 5.6+ and a web server |
| Interface | CLI / interactive menu | Web-based |
| Platform | Windows, Linux, macOS | Any with web server |

## Setup

There are two ways to get the script into your configs directory:

1. **Manually** — copy `config_merger.py` from `apps/config-merger/python/` in the AzerothCore source directly into your `/configs` folder.
2. **Via CMake** — enable `TOOL_CONFIG_MERGER` when compiling. The script will be placed alongside your configs automatically.

### Expected file structure

```
configs/
├── config_merger.py
├── authserver.conf.dist
├── authserver.conf
├── worldserver.conf.dist
├── worldserver.conf
└── modules/
    ├── mod_example.conf.dist
    ├── mod_example.conf
    └── ...
```

## Usage

### Interactive mode

Run the script from your configs directory:

```bash
python config_merger.py
```

You can also double-click `config_merger.py` on Windows to launch it directly.

You will be prompted for the configs path (press Enter to use the current directory), then presented with a menu:

```
AzerothCore Config Updater/Merger (v. 1)
--------------------------
1 - Update Auth Config
2 - Update World Config
3 - Update Auth and World Configs
4 - Update All Modules Configs
5 - Update Modules (Selection) Configs
0 - Quit
```

For each missing option found, the tool shows the option name, its comments and default value, then asks:

```
Add [option_name] to config? (y/n):
```

A timestamped backup (e.g. `worldserver.conf(d11_m12_y2025_14h_30m_45s).bak`) is created before any changes are written.

### CLI mode

```bash
python config_merger.py [config_dir] [target] [options]
```

**target** values:

| Value | Description |
| - | - |
| `auth` | Update authserver.conf only |
| `world` | Update worldserver.conf only |
| `both` | Update both server configs |
| `modules` | Update all module configs |
| `modules-select` | Interactive module selection |

**Options:**

| Flag | Description |
| - | - |
| `-y`, `--yes` | Auto-add all new options without prompting |
| `--version` | Show version information |

**Examples:**

```bash
# Update both configs automatically
python config_merger.py /path/to/configs both -y

# Update all modules with confirmation prompts
python config_merger.py . modules
```
