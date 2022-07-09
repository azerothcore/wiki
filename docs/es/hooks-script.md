# El sistema ScriptAI

El sistema ScriptAI implementado por AC utiliza una estrategia especial: [Patrón del observador](https://en.wikipedia.org/wiki/Observer_pattern) para implementar una programación dirigida por eventos que es también el **CORE** de nuestro sistema modular.

Esta guía, junto con nuestro [sistema de módulos] (create-a-module.md) te permite ampliar el AzerothCore sin parchearlo directamente. ¡Esto le permite actualizar su repositorio manteniendo sus adiciones y personalizaciones libres de conflictos!

## Recursos

### Lista de hooks

La lista de los hooks se encuentra dentro del archivo [ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h)

### Glosario

- **Hook**: Una función que se declara dentro de un **_ScriptObject_** y que es definida por el **_Listeners_**
- **ScriptObject**: Clase abstracta que debe ser extendida para crear el **_Observer_**.
- **Script type**: La clase que extiende el `ScriptObject` y contiene hooks (por ejemplo, `PLayerScript`, `CreatureScript`, etc.), cuando extiendes la clase de tipo script estás inicializando un **_Concrete Observer_**
- **ScriptRegistry**: Esta clase contiene el registro de todos los Observadores registrados.
- **ScriptMgr**: La clase singleton que contiene la lista de todos los hooks disponibles y actúa como un **_Observer_** notificando a los **_Listeners_** cuando se despacha un evento.

## Cómo crear un hook

¡No se preocupe, no es tan aterrador como puede pensar!.

![hook](https://media4.giphy.com/media/B4ZgcoPTHYXL2/giphy.gif?cid=ecf05e47mvpbtn5sbmgkcg2gurnrjk35hsdt3m7faillyp26&rid=giphy.gif&ct=g)

Antes de pasar al siguiente paso deberías preguntarte: ¿tengo que crear un nuevo tipo de script basado en la clase `ScriptObject` o puedo reutilizar uno de los ya existentes?

Un tipo de script suele estar estrictamente relacionado con una determinada clase del core. Por ejemplo:

- `PlayerScript` -> `Player` class
- `WorldScript` -> `World` class
- `CreatureScript` -> `Creature` class

Y así sucesivamente.

Hay algunas excepciones como el `GlobalScript` que es un Observador utilizado en diferentes clases a lo largo del núcleo. Pero en general, un tipo de script debe referirse a una clase específica.

Por lo tanto, si ha creado una nueva clase que tiene que ser extendida con hooks, entonces puede proceder con el primer punto.

Sin embargo, la mayoría de las veces sólo tienes que añadir nuevos hooks a los scripts existentes, en este caso sólo salta al punto 2 de este capítulo.

### 1) Procedimiento estándar al añadir nuevas clases de scripts

En primer lugar, define la clase actual, y haz que herede de ScriptObject, así:

```cpp
class MyScriptType : public ScriptObject
{
    uint32 _someId;
    private:
        void RegisterSelf();
    protected:
        MyScriptType(const char* name, uint32 someId)
            : ScriptObject(name), _someId(someId)
        {
            ScriptRegistry<MyScriptType>::AddScript(this);
        }
    public:
        // Si una función virtual en tu clase de tipo script
        // no tiene que ser necesariamente anulada, simplemente declárala virtual
        // con un cuerpo vacío. Si, por el contrario, es lógico anularla
        // (es decir, si es el único método de la clase), hazla virtual pura, añadiéndole = 0.
        virtual void OnBeforeSomeEvent(uint32 /*someArg1*/, std::string& /*someArg2/*) { }
        // Esta es una función virtual pura:
        virtual void OnAnotherEvent(uint32 /*someArg*/) = 0;
}
```

A continuación, tienes que añadir una especialización para ScriptRegistry. Pon esto al principio de `ScriptMgr.cpp`:

```cpp
template class ScriptRegistry<MyScriptType>;
```

Ahora añade el registro en la parte inferior del `ScriptMgr.cpp`:

```cpp
MyScriptType::MyScriptType(const char* name)
    : ScriptObject(name)
{
    ScriptRegistry<MyScriptType>::AddScript(this);
}
```

Entonces añade una rutina de limpieza en `ScriptMgr::unload()`.

```
SCR_CLEAR(MyScriptType);
```

¡Y finalmente tu clase está lista para funcionar con el sistema de scripts!

### 2) Implementar las funciones de los hooks

Si no has seguido el punto 1 y quieres reutilizar un `ScriptObject` existente, entonces tienes que declarar primero las funciones dentro de una de las clases de `ScriptObject` preexistentes (como `PlayerScript`, `ServerScript`, etc.)

#### Declarar los hooks

Lo que tienes que hacer ahora es añadir funciones a `ScriptMgr` que puedan ser llamadas desde el núcleo para desencadenar realmente ciertos eventos.

En `ScriptMgr.h`, dentro de `class ScriptMgr`

```cpp
void OnBeforeSomeEvent(uint32 someArg1, std::string& someArg2);
void OnAnotherEvent(uint32 someArg);
```

**NOTA:** para ciertos scripts el método declarado dentro de la clase ScriptMgr y el declarado en el ScriptObject relacionado, no siempre coinciden. Por ejemplo: `OnLogin` es un hook del PlayerScript que se declara como `OnPlayerLogin` cuando se utiliza dentro de la clase ScriptMgr, evitando así colisiones con otros métodos ya que la clase ScriptMgr recoge los hooks de todos los ScriptObjects dentro de la misma lista.

#### Defina sus hooks

Este paso define la forma en que su hook debe llamar a los listeners registrados.

La forma más habitual de hacerlo es la siguiente

En `ScriptMgr.cpp`:

```cpp
void ScriptMgr::OnBeforeSomeEvent(uint32 someArg1, std::string& someArg2)
{
    FOREACH_SCRIPT(MyScriptType)->OnBeforeSomeEvent(someArg1, someArg2);
}
void ScriptMgr::OnAnotherEvent(uint32 someArg)
{
    FOREACH_SCRIPT(MyScriptType)->OnAnotherEvent(someArg);
}
```

Ahora basta con llamar a estas dos funciones desde cualquier lugar del core para activar el evento en todos los scripts registrados de ese tipo.

### Cómo llamar a tus hooks

La clase ScriptMgr se inicializa dentro del AC como un singleton que contendrá todos los observers (ScriptObjects) y sus listeners registrados relacionados (hooks). AC proporciona una propiedad global llamada "sScriptMgr" que puede utilizar para llamar a su script dentro de las funciones de AC.

Por ejemplo:

```cpp
void CoreClass::SomeEvent() 
{
    uint32 arg1=10;
    std::string arg2="something";

    sScriptMgr->OnBeforeSomeEvent(arg1, arg2);

    //[...]
}
```

## Documentar su hook

Recuerda documentar tu nuevo hook siguiendo la guía [Cómo documentar tu código](how-to-document-code.md).

Cuando creas un nuevo hook para publicarlo en el repo de AC, uno de los criterios de aceptación es escribir una documentación adecuada para él, para que otras personas sepan cómo usarlo correctamente. Así que, por favor, lee esa guía con atención.

### Escribir un registro de cambios

Cuando creas o modificas cualquier hook, tienes que crear un nuevo changelog para explicar a la gente cómo adaptar su código y mantenerlos informados sobre estos cambios. Por favor, siga [esta guía](how-to-use-changelog.md) para aprender a hacerlo.

## Convenciones de nomenclatura

Cada hook debe tener la siguiente convención de nombres:

`On[When]<Action>`

Por ejemplo:

- `OnBeforeConfigLoad`
- `OnAfterArenaRatingCalculation`

La acción normalmente coincide con el nombre de la función dentro de la cual se llama al hook.

Si la función madre es lo suficientemente compleja como para contener diferentes hooks, entonces la acción debe reflejar para qué se utiliza el hook.

La parte "Cuando" es opcional, pero se recomienda encarecidamente.

Ayuda a entender en qué parte de la función padre se llama al hook.

Por ejemplo, puedes tener tanto `OnBeforeConfigLoad` como `OnAfterConfigLoad`, para cambiar el comportamiento antes y después de cargar la configuración.

## Hooks avanzados

### Cómo cambiar el comportamiento de una función (filtrado)

Con los hooks no sólo puedes ejecutar acciones específicas en un momento determinado, incluso puedes cambiar el comportamiento de la función donde se llama al hook para hacerlo, tienes 2 soluciones:

#### 1) Utilización de los parámetros de referencia

Este es el más común. Básicamente utilizando el concepto de pasar un parámetro por referencia se puede cambiar todo lo que se pasa al propio hook.

Por ejemplo:

```cpp
OnMotdChange(std::string& newMotd)
```

Pasando el `newMotd` con el carácter '&' se permite a los listeners cambiar el valor del Motd cuando se llama a esa acción.

#### 2) Utilizar un valor de retorno `bool`

Este enfoque no es muy común, la mayoría de los hooks devuelven un tipo "void", y trabajar con referencias es más fácil la mayoría de las veces, pero si realmente lo necesitas puedes implementar un hook declarado de esta manera:

```cpp
bool ScriptMgr::OnBeforePlayerTeleport(Player* player, uint32 mapid, float x, float y, float z, float orientation, uint32 options, Unit* target)
{
    bool ret = true;
    FOR_SCRIPTS_RET(PlayerScript, itr, end, ret) // Devuelve true por defecto si no son scripts
    if (!itr->second->OnBeforeTeleport(player, mapid, x, y, z, orientation, options, target))
        ret = false; // Cambiamos el valor de ret sólo cuando los scripts devuelven false

    return ret;
}
```

Este hook notifica a todos los listeners pero también captura cuando al menos uno de los listeners registrados devuelve "false", en ese caso el valor de retorno final también será false.

En este caso particular, este hook se utiliza dentro de una condición if para no permitir que un jugador sea teletransportado si uno de los listeners devuelve **false** por alguna razón.

Puedes implementar tu lógica diferente (por ejemplo, falso por defecto, verdadero si lo hay) sólo recuerda documentarlo adecuadamente.

### Cree su sistema de hooks dentro de su módulo

Usando la guía anterior puedes incluso crear tu ScriptObject dentro de tu módulo para permitir que la gente lo extienda.

Algunos módulos, como el de balance automático, permiten personalizar cierta parte de su función mediante el uso de hooks internos.

Puede ver este archivo como ejemplo: https://github.com/azerothcore/mod-autobalance/blob/master/src/AutoBalance.h

**NOTA:** También necesitas crear tu propia implementación de ScriptMgr y ofrecer un singleton que permita llamar a tus hooks.

### Consideraciones finales

Existen otras características del sistema ScriptAI que no han sido incluidas en esta documentación, como la creación de scripts vinculados a entidades específicas dentro de nuestra base de datos (Ej. CreatureScript). Este uso avanzado puede ser implementado replicando el código relacionado que tenemos dentro de los archivos ScriptMgr. Si necesitas ayuda o quieres mejorar esta documentación, no dudes en pedir apoyo y editar esta página.

## Recursos externos

- [Stack overflow topic: Is it possible to turn a core patch into a module for AzerothCore?](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore/66340683#66340683)
