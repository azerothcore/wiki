---
redirect_from: "/TrinityCore-to-AzerothCore-characters-migration"
---

# Herramienta de migración de Character & Auth de TrinityCore hacia AzerothCore 

### 1) Instalar AzerothCore 

Siga las instrucciones de instalación e instale una nueva configuración de AzerothCore (la necesitaremos después de la conversión).

Las instrucciones para configurar AzerothCore se pueden encontrar [aquí](http://www.azerothcore.org/wiki/Installation).

Asegúrese de tener una instalación nueva completa y de trabajar sin módulos adicionales antes de continuar. 

### 2) Haga una copia de seguridad de sus bases de datos TrinityCore

Haga una copia de seguridad de sus bases de datos TrinityCore antes de continuar (siempre haga una copia de seguridad antes de realizar cambios)
- auth
- characters
- world

### 3) Migración de Character & Auth

Descargue la [Herramienta de migración de Character & Auth de TC hacia AC ](https://github.com/azerothcore/tool-tc-migration).

Los siguientes archivos deben ejecutarse en orden del 1 al 5 en su base de datos de caracteres TrinityCore:

- 1_CREATE_CLEANUP_TABLES
- 2_CREATE_MISSING_TABLES
- 3_ALTER_TABLES
- 4_CLEANUP_AND_CONVERT_SPELLS
- 5_FINAL_CLEANUP

Ejecute el siguiente archivo n.6 en su base de datos de autenticación de Trinitycore

- 6_AUTH_CONVERTER

Cambie el `worldserver.conf` de su servidor AzerothCore para que apunte a su base de datos de personajes convertidos (ex TrinityCore) e inicie el `./worldserver`


