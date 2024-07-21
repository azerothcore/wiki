# Keira3 Internals

Esta es una colección de notas que pretenden explicar el funcionamiento interno de Keira3 con fines de desarrollo.

Si sólo quieres usar Keira3, no necesitas nada de lo siguiente. Si quieres modificar Keira3, por ejemplo para mejorarlo o añadirle nuevas funciones, puede que esta página te resulte útil.

## Principales tecnologías

Keira3 se basa en las siguientes tecnologías web de código abierto:

- [**TypeScript**](http://www.typescriptlang.org/) es el lenguaje principal de Keira3. Es un superconjunto de JavaScript. Si conoces JavaScript y tienes algunos conocimientos básicos de lenguajes POO como Java y C#, ya te sentirás bastante familiarizado con TypeScript. Si no es así, puede que te resulte útil [este curso](https://www.udemy.com/course/understanding-typescript/). Si no sabes nada de JavaScript, será mejor que adquieras primero unos conocimientos básicos.

- [**Angular**](https://angular.io/). Este es el framework principal de Keira3. Recomendamos encarecidamente familiarizarse con él antes de meter las manos en el código de Keira3. Si buscas un curso completo de Angular, te recomendamos [este](https://www.udemy.com/course/the-complete-guide-to-angular-2/).

- Utilizamos [**SCSS**](https://sass-lang.com/) para dar estilo a nuestra interfaz de usuario. Es una extensión de CSS. Es necesario conocer los fundamentos de CSS para poder cambiar la interfaz de Keira3. SCSS debería ser bastante intuitivo para cualquiera que entienda de CSS.

- [**Bootstrap**](https://getbootstrap.com/) es el framework CSS utilizado como base para el estilo de Keira3. No es necesario que seas un experto en Bootstrap, sin embargo te recomendamos que al menos estés familiarizado con su [Grid system](https://getbootstrap.com/docs/4.5/layout/grid/) y utilidades como el [spacing](https://getbootstrap.com/docs/4.5/utilities/spacing/).

- [**Electron**](https://electronjs.org/) es el framework que permite construir aplicaciones de escritorio utilizando tecnologías web. No utilizamos muchas funciones nativas de Electron, por lo que normalmente no hay que preocuparse por ello cuando se desarrolla Keira3.

## Pruebas

Utilizamos [automatización de pruebas](https://en.wikipedia.org/wiki/Test_automation) en Keira3 en nuestro ciclo de desarrollo. Para cada pull request / commit, nuestro CI ejecuta automáticamente un montón de pruebas automatizadas.

Concretamente, tenemos:

- **Unit tests**. Todos los archivos `*.spec.ts` se ejecutan con `ng test`. Mantenemos el **100% de cobertura**. Esto significa que si intentas enviar código no probado, la construcción CI de tu PR fallará. Utilizamos el [Angular testing framework](https://angular.io/guide/testing) para ello.

- **Integration tests**. Es todo el archivo `*.integration.spec.ts`, también se ejecutan con `ng test`, junto con las pruebas unitarias. Puedes ver las pruebas de integración de Keira3 casi como un conjunto de pruebas e2e, la principal diferencia es que todas las interacciones de la DB son burladas. La diferencia entre las pruebas unitarias y las de integración es: en las pruebas unitarias probamos las unidades simulando todas sus dependencias, mientras que en las pruebas de integración probamos las "grandes piezas" de Keira3 juntas (simulando sólo la BD). Principalmente se utiliza para probar los editores.

- **E2E tests**. Tenemos un pequeño conjunto de pruebas e2e basadas en [Playwright](https://playwright.dev/). Por ejemplo, para comprobar la integración de sqlite. El comando `npm run e2e` servirá automáticamente la aplicación y ejecutará las pruebas e2e.

### ¿Por qué la automatización de pruebas?

Porque cada vez que modificas tu aplicación, nunca sabes si estás rompiendo alguna funcionalidad existente a menos que pruebes manualmente todo una y otra vez. Cuando tienes pruebas automatizadas, todavía no estás 100% seguro de no romper cosas existentes, pero al menos pueden darte alguna garantía.

## Estructura de los archivos

Directorios relevantes:

- **e2e**: todos los casos de prueba e2e, aislados de todo lo demás.

- **src/assets**: imágenes y archivos de estilo **global** (los archivos de estilo de los componentes se encuentran en `src/app`).

- **src/app**: código fuente de la aplicación, así como las pruebas unitarias y de integración.

- **src/app/config**: archivos de configuración de la aplicación, como las configuraciones de enrutamiento y las específicas de la biblioteca.

- **src/app/features**: código fuente de las principales características de Keira3 (cada una aislada de las demás). **REGLA**: una función NO puede importar nada de otra función. Si algo está destinado a ser compartido a través de las características, entonces debe ser colocado en `src/app/shared`.

- **src/app/main**: componentes que no pertenecen a una función específica, pero que están aislados. Por ejemplo, el componente raíz `AppComponent`, la barra lateral, la ventana de inicio de sesión, etc.

- **src/app/shared**: todo tipo de utilidades, módulos, componentes, servicios, clases abstractas, utilidades de prueba, etc... que **están destinados a ser utilizados por más de una función**.

## Diseño y fundamentos de la arquitectura

El código de Keira3 está estructurado utilizando [POO](https://en.wikipedia.org/wiki/Object-oriented_programming) con técnicas como [herencia](https://www.typescriptlang.org/docs/handbook/classes.html#inheritance) y [tipos genéricos](https://www.typescriptlang.org/docs/handbook/generics.html) para maximizar la reutilización del código.

Dentro del directorio `src/app/shared/abstract` hay una colección de clases abstractas que están destinadas a ser extendidas por los [Componentes](https://angular.io/guide/architecture-components) y [Servicios](https://angular.io/guide/architecture-services) concretos de Angular que implementarán las características de Keira3.

*Si no está familiarizado con la terminología utilizada hasta ahora, consulte los hipervínculos anteriores antes de continuar.*

Keira3 es [**modular**](https://en.wikipedia.org/wiki/Modular_programming), puedes verlo como una colección de características y utilidades compartidas que se organizan en [Arquitectura modular](https://angular.io/guide/architecture-modules).

## Terminología y convenciones de Keira3

Normalmente, las características de Keira3 se caracterizan por los siguientes elementos.

### Tipos de tablas

Todas las definiciones de las tablas de AzerothCore DB están definidas en Keira3 dentro de `src/app/shared/types`.

Si quieres crear un nuevo editor, primero tienes que crear su definición allí.

### La entidad principal

Por ejemplo, ***Creature*** es una entidad principal. Si quieres modificar un vendedor (`npc_vendor`) o un botín de una criatura (`creature_loot_template`), todavía tienes que seleccionar (o crear) una Criatura.

Siempre hay una tabla (y por tanto también un Editor) para la Entidad Principal. Para las criaturas es `creature_template`.

No puedes tener un vendedor, botín, etc... sin tener una criatura primero. En otras palabras, no puedes tener una fila `npc_vendor` sin vincularla a una entrada existente de `creature_template`.

Otro ejemplo podría ser: no se puede tener una fila en `quest_template_addon` sin vincularla a una fila existente de `quest_template`. Porque `quest_template` es la entidad principal de los editores de Quest.

### Editor

Un editor suele estar vinculado a una tabla. Por ejemplo, el editor ***Creature*** -> ***Trainer*** permite editar la tabla `npc_trainer`.

Hay dos tipos principales de editores en Keira3:

#### Editores de una fila

Son los editores de tablas que contienen **una fila por cada entidad**.

Por ejemplo, la tabla `creature_template_addon` sólo puede tener UNA fila para cada criatura. Nunca puedes tener 2 filas que apunten a la misma criatura en esta tabla.

Cada fila está identificada de forma única por una clave primaria, que es el ID de la entidad seleccionada. Típicamente en la BD se llaman `id`, `ID`, `entry`, `Entry`, etc... sí, son completamente inconsistentes, pero es lo que heredamos de MaNGOS/TrinityCore. En Keira3 lo llamamos simplemente `entityIdField`.

#### Editores de varias filas

Son los editores que contienen **múltiples filas para cada entidad**.

Por ejemplo, la tabla `npc_vendor` puede tener varias filas que pertenecen a la misma criatura. Cada fila de `npc_vendor` representa un artículo específico que es vendido por una criatura específica. Y una criatura puede vender 0, 1 o muchos artículos. Entonces cada criatura puede tener 0, 1 o muchas filas en la tabla `npc_vendor`. ¿Tiene sentido, verdad?

Cada fila tiene 2 claves primarias, típicamente (pero no siempre) llamadas `id` y `guid`. En Keira3 las llamamos siempre `entityIdField` y `entitySecondIdField`. El `entityIdField` es el ID de la entidad seleccionada.

Volvamos al ejemplo de `npc_vendor`:

- `entityIdField` sería el ID de la criatura.
- `entitySecondIdField` sería el ID del item.

#### Componente y servicio del editor

Cada editor en Keira3 tiene su propio [Component](https://angular.io/guide/architecture-components) y [Service](https://angular.io/guide/architecture-services), donde:

- Puede ver un **Componente del Editor** como la "parte de la interfaz de usuario". Refleja el estado de la tabla que se está editando y contiene un formulario que permite al usuario cambiar sus propiedades. Los componentes son típicamente "tontos" (sin mucho código lógico) y se refieren principalmente al código HTML. Por supuesto, está vinculado al Servicio del Editor.

- El **Servicio del Editor** contiene toda la lógica que alimenta a un Editor, así como el **estado** de la tabla actual que se está editando. Es responsable de llamar al `QueryService` cada vez que el usuario edita alguna propiedad para volver a generar las consultas SQL.

Para maximizar la reutilización del código, se han creado las siguientes clases abstractas:

- `EditorService`: base de todos los Servicios de Redacción.
- `SingleRowEditorService`: extiende `EditorService`, base de todos los servicios de edición de una fila (por ejemplo, `CreatureTemplateService` extiende esta clase).
- `MultiRowEditorService`: extiende `EditorService`, base de todos los servicios de edición de varias filas (por ejemplo, `CreatureLootTemplateService` extiende esta clase).

- `EditorComponent`: base de todos los componentes del editor
- `SingleRowEditorComponent`: extiende `EditorComponent`, base de todos los componentes de edición de una fila (por ejemplo, `CreatureTemplateComponent` extiende esta clase).
- `MultiRowEditorComponent`: extiende `EditorComponent`, base de todos los componentes del editor de varias filas (por ejemplo, `CreatureLootTemplateComponent` extiende esta clase).

### Handler

Los Handlers son servicios responsables de mantener estados como:

- Qué entidad se ha seleccionado (por ejemplo, cuando se selecciona una criatura, el ID de la misma se guarda dentro del `CreatureHandlerService`).
- Qué editores se quedan con los cambios sin guardar

Los grupos de editores que se refieren a la misma entidad principal deben compartir **un Handler**. Por ejemplo, todos los editores de criaturas se refieren al `CreatureHandlerService`, todos los editores de Quest se refieren al `QuestHandlerService`, y así sucesivamente...

Todas las clases de Handlers extienden la clase abstracta `HandlerService`.

## Seleccionadores

Existen varios tipos de selectores que permiten al usuario seleccionar fácilmente un valor para un campo determinado.

Los selectores suelen estar a disposición del usuario haciendo clic en el botón con tres puntos:

![image](https://user-images.githubusercontent.com/75517/118693269-351a5000-b80b-11eb-81b5-15065634a5b4.png)

Existen tres tipos principales de selectores, que se enumeran a continuación.

### SingleValueSelectorBtnComponent

El `SingleValueSelectorBtnComponent` es un componente reutilizable que permite al usuario seleccionar un **valor único** de una lista de valores, para un campo determinado.

Comprobemos por ejemplo el campo `exp` de `creature_template`, que permite especificar UN valor:

```
0 - Classic
1 - TBC
2 - WOTLK
```

Todo lo que tienes que hacer para implementar dicho selector es definir los valores de la lista creando un array de `Opción`:

![image](https://user-images.githubusercontent.com/75517/118694016-e7eaae00-b80b-11eb-8701-bc59c80ec3bd.png)

Todas las opciones se encuentran en `src/app/shared/constants/options`, por lo que sólo tienes que crear un nuevo archivo como el anterior.

A continuación, debe importar la matriz de opciones, en este caso `EXPANSIONS`, en el archivo `.ts` de su componente y declararla como `PUBLIC READONLY` para que esté disponible para la plantilla del componente:

![image](https://user-images.githubusercontent.com/75517/118694375-4dd73580-b80c-11eb-8f22-4f2ec76bfe68.png)

Ahora puedes usarlo en la plantilla `.html` del componente añadiendo el elemento html `keira-single-value-selector-btn` y pasando las siguientes propiedades:

- `[control]` el control del formulario, por ejemplo `editorService.form.controls.exp` (nota: `exp` es el nombre del campo).
- `[config]` un objeto que especifica la propiedad `options` y `name`.
- `[modalClass]` la clase del modal, para poder cambiar el tamaño del mismo, por ejemplo `modal-md` o `modal-lg` (opcional).

![image](https://user-images.githubusercontent.com/75517/118693601-7c084580-b80b-11eb-9a6d-8833d6581920.png)

Este es el resultado:

<img src="https://user-images.githubusercontent.com/75517/118694803-c1794280-b80c-11eb-9099-00758983ca2e.png" width=300>

<img src="https://user-images.githubusercontent.com/75517/118694841-cf2ec800-b80c-11eb-8719-b770a7fd0c98.png" width=500>

### FlagsSelectorBtnComponent

El `FlagsSelectorBtnComponent` es otro componente reutilizable muy útil que permite al usuario componer un valor a partir de un conjunto de **flags** (máscara de bits), para un campo determinado. Si términos como bits, máscara de bits, flags, etc. te suenan raros, te recomendamos que leas [esta página](Bit-and_bytes-tutorial) para entender completamente cómo funcionan los valores de las flags.

Veamos, por ejemplo, cómo se implementa el campo `dynamicflags` de `creature_template`.

Primero hay que definir la lista de valores (de bits) creando un array de `Flag`:

![image](https://user-images.githubusercontent.com/75517/118695616-aeb33d80-b80d-11eb-97cd-a6b7933b632d.png)

Todos los valores de las banderas se encuentran en `src/app/shared/constants/flags` por lo que puedes crear un nuevo archivo allí, por ejemplo `dynamic-flags.ts` en nuestro caso.

Básicamente tienes que definir cuál es el significado de cada bit. No hay que olvidar que los bits suelen empezar por cero.

A continuación, es necesario importar la matriz `DYNAMIC_FLAGS` en el archivo `.ts` del componente y hacerla disponible para su plantilla `.html` declarándola `PUBLIC READONLY`:

![image](https://user-images.githubusercontent.com/75517/118696084-339e5700-b80e-11eb-951d-0b8f7acf1052.png)

Ahora sólo tienes que usarlo en el html añadiendo el componente `keira-flags-selector-btn` allí:

![image](https://user-images.githubusercontent.com/75517/118695922-02258b80-b80e-11eb-9c29-ec6ae693d13c.png)

Los atributos de este componente son:

- `[control]` el control del formulario, por ejemplo `editorService.form.controls.dynamicflags` (nota: `dynamicflags` es el nombre del campo).
- `[config]` un objeto que especifica la propiedad `options` y `name`).
- `[modalClass]` la clase del modal, para poder cambiar el tamaño del mismo, por ejemplo `modal-md` o `modal-lg` (opcional).

Este es el resultado:

<img src="https://user-images.githubusercontent.com/75517/118697264-685ede00-b80f-11eb-9609-6b4af903bcdc.png" width=300>

![image](https://user-images.githubusercontent.com/75517/118697333-790f5400-b80f-11eb-8795-cdeae8ebfd64.png)

### Otros selectores

Existen otros selectores que permiten al usuario seleccionar valores haciendo una búsqueda en la BD o en el contenido DBC del sqlite integrado en Keira3.

Puedes encontrar sus implementaciones en `src/app/shared/modules/selectors` así como ejemplos de uso en la aplicación.

![image](https://user-images.githubusercontent.com/75517/118693136-10be7380-b80b-11eb-9721-081bf1f4128d.png)

Ejemplo: el **selector de items**.

![image](https://user-images.githubusercontent.com/75517/118697495-a2c87b00-b80f-11eb-9db4-69357704d5f5.png)

Se puede utilizar siempre que se necesite un ID de item:

![image](https://user-images.githubusercontent.com/75517/118697570-bbd12c00-b80f-11eb-9959-feb7186dab45.png)
