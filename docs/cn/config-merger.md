# 配置合并工具（Config Merger）

一个命令行工具，用于用发行文件中的新选项更新你的 AzerothCore 配置文件。

## 概述

当 AzerothCore 更新时，新的配置选项可能会被添加到 `.conf.dist` 发行文件中。配置合并工具会将你现有的 `.conf` 文件与最新的 `.conf.dist` 文件进行比较，帮助你在保留自定义设置的同时添加任何缺失的选项。

有两个版本可用：一个 **Python 版本**（推荐）和一个旧的 **PHP 版本**。

| | Python | PHP |
| - | - | - |
| 要求 | Python 3.6+ | PHP 5.6+ 和 Web 服务器 |
| 界面 | CLI / 交互式菜单 | 基于 Web |
| 平台 | Windows、Linux、macOS | 任意带 Web 服务器的平台 |

## 安装

有两种方法可以将脚本放到你的配置目录中：

1. **手动** — 将 `config_merger.py` 从 AzerothCore 源码中的 `apps/config-merger/python/` 直接复制到你的 `/configs` 文件夹。
2. **通过 CMake** — 编译时启用 `TOOL_CONFIG_MERGER`。脚本会自动放置在你的配置旁边。

### 预期的文件结构

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

## 使用方法

### 交互模式

在配置目录中运行脚本：

```bash
python config_merger.py
```

在 Windows 上你也可以直接双击 `config_merger.py` 来启动。

系统会提示你输入配置路径（按 Enter 使用当前目录），然后显示一个菜单：

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

对于找到的每个缺失选项，工具会显示选项名称、注释和默认值，然后询问：

```
Add [option_name] to config? (y/n):
```

在写入任何更改之前，会创建一个带时间戳的备份（例如 `worldserver.conf(d11_m12_y2025_14h_30m_45s).bak`）。

### CLI 模式

```bash
python config_merger.py [config_dir] [target] [options]
```

**target（目标）值：**

| 值 | 描述 |
| - | - |
| `auth` | 仅更新 authserver.conf |
| `world` | 仅更新 worldserver.conf |
| `both` | 更新两个服务器配置 |
| `modules` | 更新所有模块配置 |
| `modules-select` | 交互式模块选择 |

**选项：**

| 标志 | 描述 |
| - | - |
| `-y`、`--yes` | 自动添加所有新选项，无需提示 |
| `--version` | 显示版本信息 |

**示例：**

```bash
# 自动更新两个配置
python config_merger.py /path/to/configs both -y

# 更新所有模块并带确认提示
python config_merger.py . modules
```
