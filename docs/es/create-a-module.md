# Crear un módulo

## **Cómo crear un módulo**

Antes de empezar te sugerimos que leas la [Documentación sobre la estructura modular](The-Modular-Structure) para entender el funcionamiento de AzerothCore.

### Recursos

- Plantilla del módulo: [https://github.com/azerothcore/skeleton-module](https://github.com/azerothcore/skeleton-module)
- Plantilla de scripts: https://github.com/azerothcore/azerothcore-boilerplates
- Todos los hooks del núcleo se enumeran en [ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h). Si necesita hooks personalizados, pueden añadirse al núcleo mediante [enviando un PR](https://www.azerothcore.org/wiki/How-to-create-a-PR).

- Si necesita crear un nuevo hook para su módulo, siga esta guía: [Cómo crear un nuevo hook](hooks-script.md)

### **La base**

1. Crear una carpeta dentro del directorio `modules/`

2. Ahora puedes desarrollar añadir cualquier cosa al proyecto principal, como algunos scripts o incluso una biblioteca entera

**Nota:** sugerimos utilizar la [estructura de directorios](Directory-Structure) estándares de AzerothCore para organizar mejor sus módulos y familiarizarse con el proyecto principal.

### **Añadir el primer script**

1. Antes de continuar, te sugerimos que sigas nuestra guía sobre cómo crear un script para AzerothCore

2. Después de crear tu script tienes que crear un archivo .cpp para manejar la carga del script.

Por ejemplo (suponiendo que haya creado una carpeta `src`):

**my_custom_loader.cpp**

```cpp
// Desde SC
void AddMyCustomScripts();

// Añadir todo
// Véase la convención de nomenclatura https://github.com/azerothcore/azerothcore-wotlk/blob/master/doc/changelog/master.md#how-to-upgrade-4
// además, sustituya aquí todos los "-" del nombre de la carpeta del módulo por "_".
void Addmod_my_customScripts()
{
    AddMyCustomScripts();
}
```

NOTA: AddMyCustomScripts está compuesto por:

- Add (prefijo)

MyCustom (Un identificador de nombre único para su script para evitar colisiones de funciones)

Scripts (Sufijo)

### **Crear un archivo de configuración personalizado**

si necesita añadir un archivo de configuración personalizado a su módulo que se instalará con el servidor, los pasos son muy sencillos.

1. Añadir un archivo con la extensión `.conf.dist` en la carpeta `./conf`.
2. Ya está hecho. Sí, realmente, eso es todo.

### **Añade tus archivos db a db_assembler**

Puedes crear bases, actualizaciones y sql personalizados que se cargarán automáticamente en nuestro db_assembler

**trabajo en curso....**
