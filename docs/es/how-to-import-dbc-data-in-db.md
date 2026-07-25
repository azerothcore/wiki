# Cómo importar datos DBC dentro de la base de datos de AC

Esta guía te mostrará cómo importar datos DBC dentro de la base de datos de AzerothCore y editarlos. Para la guía vamos a usar AreaTable.dbc como ejemplo,
cambiando la zona de Hyjal de "Normal" a "Sanctuary (con duelos permitidos)". 
Si haces esto, convertirás esa zona en crossfaction y, por ejemplo, podrás usarla para eventos.

## Requisitos

- [Nodejs](https://nodejs.org/en/) para el node-dbc-reader

## Primeros pasos

### 1. instala mi dbc-reader

Clona o descarga [este repositorio](https://github.com/wowgaming/node-dbc-reader) y ejecuta `npm install` dentro de la carpeta descargada.

*Lee la documentación de ese repositorio si necesitas ejecutar comandos más complejos.*

### 2. Busca tus datos

Ejecuta este comando para comprobar que la zona es correcta: `npm run start -- --search="[616].includes({*})" --columns=ID AreaTable`

Este comando buscará en la columna **ID** con la siguiente condición: `[616].includes({*})`, lo que significa que el programa buscará todos los IDs que incluyan
los valores dentro del array [ ]. En este caso solo necesitamos el valor 616. 

*Nota: la opción --search está respaldada por un eval, lo que significa que puedes ejecutar cualquier método de javascript para realizar una comparación*

El resultado de ese comando será:
```json
{
    "ID": 616,
    "ContinentID": 1,
    "ParentAreaID": 0,
    "AreaBit": 619,
    "Flags": 64,
    "SoundProviderPref": 0,
    "SoundProviderPrefUnderwater": 11,
    "AmbienceID": 31,
    "ZoneMusic": 0,
    "IntroSound": 0,
    "ExplorationLevel": 0,
    "AreaName_Lang_enUS": "Hyjal",
    "AreaName_Lang_enGB": "",
    "AreaName_Lang_koKR": "",
    "AreaName_Lang_frFR": "",
    "AreaName_Lang_deDE": "",
    "AreaName_Lang_enCN": "",
    "AreaName_Lang_zhCN": "",
    "AreaName_Lang_enTW": "",
    "AreaName_Lang_zhTW": "",
    "AreaName_Lang_esES": "",
    "AreaName_Lang_esMX": "",
    "AreaName_Lang_ruRU": "",
    "AreaName_Lang_ptPT": "",
    "AreaName_Lang_ptBR": "",
    "AreaName_Lang_itIT": "",
    "AreaName_Lang_Unk": "",
    "AreaName_Lang_Mask": 16712190,
    "FactionGroupMask": 0,
    "LiquidTypeID_1": 0,
    "LiquidTypeID_2": 0,
    "LiquidTypeID_3": 0,
    "LiquidTypeID_4": 0,
    "MinElevation": -500,
    "Ambient_Multiplier": 0,
    "Lightid": 0
  }
  ````

El valor: `"Flags": 64` significa "zona normal", tenemos que sobrescribirlo con `19456 - Sanctuary (Duels allowed)`.

Para la documentación de DBC consulta [esta wiki](https://wowdev.wiki/Category:DBC_WotLK)

Puedes consultar la lista de los flags [aquí](areatable)

3. Exporta el SQL

Ahora ejecuta el mismo comando de arriba pero con el tipo de salida : `npm run start -- -s "[616].includes({*})" -t sql  --columns=ID AreaTable` para extraer la consulta INSERT

Salida: 
```sql
INSERT IGNORE INTO areatable_dbc (`ID`,`ContinentID`,`ParentAreaID`,`AreaBit`,`Flags`,`SoundProviderPref`,`SoundProviderPrefUnderwater`,`AmbienceID`,`ZoneMusic`,`IntroSound`,`ExplorationLevel`,`AreaName_Lang_enUS`,`AreaName_Lang_enGB`,`AreaName_Lang_koKR`,`AreaName_Lang_frFR`,`AreaName_Lang_deDE`,`AreaName_Lang_enCN`,`AreaName_Lang_zhCN`,`AreaName_Lang_enTW`,`AreaName_Lang_zhTW`,`AreaName_Lang_esES`,`AreaName_Lang_esMX`,`AreaName_Lang_ruRU`,`AreaName_Lang_ptPT`,`AreaName_Lang_ptBR`,`AreaName_Lang_itIT`,`AreaName_Lang_Unk`,`AreaName_Lang_Mask`,`FactionGroupMask`,`LiquidTypeID_1`,`LiquidTypeID_2`,`LiquidTypeID_3`,`LiquidTypeID_4`,`MinElevation`,`Ambient_Multiplier`,`Lightid`)
 VALUES (616,1,0,619,64,0,11,31,0,0,0,"Hyjal","","","","","","","","","","","","","","","",16712190,0,0,0,0,0,-500,0,0);
````

4. Crea la consulta de actualización

Crea la consulta de actualización para establecer la facción adecuada:

```sql
UPDATE areatable_dbc SET Flags=19456 WHERE ID=616
```

5. Crea tu PR

Si estás usando esta guía para arreglar un bug (no con fines de personalización), 
ahora puedes crear [tu PR](How-to-create-a-PR) con las 2 consultas de arriba
