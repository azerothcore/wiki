# Herramienta Config Merger

Una herramienta de línea de comandos para actualizar tus archivos de configuración de AzerothCore con nuevas opciones de los archivos de distribución.

## Visión general

Cuando se actualiza AzerothCore, se pueden añadir nuevas opciones de configuración a los archivos de distribución `.conf.dist`. La herramienta config merger compara tus archivos `.conf` existentes con los últimos archivos `.conf.dist` y te ayuda a añadir cualquier opción que falte, preservando tu configuración personalizada.

Hay dos versiones disponibles: una **versión Python** (recomendada) y una **versión PHP** heredada.

| | Python | PHP |
| - | - | - |
| Requisito | Python 3.6+ | PHP 5.6+ y un servidor web |
| Interfaz | CLI / menú interactivo | Basada en web |
| Plataforma | Windows, Linux, macOS | Cualquiera con servidor web |

## Configuración

Hay dos formas de meter el script en tu directorio de configs:

1. **Manualmente** — copia `config_merger.py` desde `apps/config-merger/python/` en la fuente de AzerothCore directamente a tu carpeta `/configs`.
2. **Vía CMake** — activa `TOOL_CONFIG_MERGER` al compilar. El script se colocará junto a tus configs automáticamente.

### Estructura de archivos esperada

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

## Uso

### Modo interactivo

Ejecuta el script desde tu directorio de configs:

```bash
python config_merger.py
```

También puedes hacer doble click en `config_merger.py` en Windows para lanzarlo directamente.

Se te pedirá el path de los configs (pulsa Enter para usar el directorio actual), y luego se te presentará un menú:

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

Para cada opción faltante encontrada, la herramienta muestra el nombre de la opción, sus comentarios y su valor por defecto, y luego pregunta:

```
Add [option_name] to config? (y/n):
```

Se crea un backup con marca de tiempo (p. ej. `worldserver.conf(d11_m12_y2025_14h_30m_45s).bak`) antes de escribir cualquier cambio.

### Modo CLI

```bash
python config_merger.py [config_dir] [target] [options]
```

Valores de **target**:

| Value | Description |
| - | - |
| `auth` | Actualiza solo authserver.conf |
| `world` | Actualiza solo worldserver.conf |
| `both` | Actualiza ambas configs de servidor |
| `modules` | Actualiza todas las configs de módulos |
| `modules-select` | Selección interactiva de módulos |

**Opciones:**

| Flag | Description |
| - | - |
| `-y`, `--yes` | Añade automáticamente todas las opciones nuevas sin preguntar |
| `--version` | Muestra información de la versión |

**Ejemplos:**

```bash
# Update both configs automatically
python config_merger.py /path/to/configs both -y

# Update all modules with confirmation prompts
python config_merger.py . modules
```
