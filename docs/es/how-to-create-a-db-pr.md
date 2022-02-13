---
redirect_from: "/How-to-create-a-DB-PR"
---

# Cómo crear una DB PR a través de GitHub

Esta es una guía simplificada para crear fácilmente PR que contengan correcciones de base de datos (código SQL) sin molestarse con la terminal.
una alternativa más fácil a la [forma tradicional de crear PR] (https://www.azerothcore.org/wiki/how-to-create-a-pr).
Si desea enviar correcciones de C++ u otro tipo que no sea SQL, siga la otra guía.

## Haz solo UNA VEZ: crea tu fork de AzerothCore

Debe iniciar sesión en [github.com](https://github.com/). Si aún no tienes una cuenta, crea una.

Abra el [repositorio de AzerothCore](https://github.com/azerothcore/azerothcore-wotlk)
y cree una fork haciendo clic en el botón "Fork" de la parte superior derecha:

![Crear una Fork de AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/1.png)

## Creando un nuevo PR

### 1. Actualiza tu kork en GitHub

Abra su navegador y navegue hasta su fork en GitHub (cambie `Su nombre de usuario` con su nombre de usuario actual de GitHub):

**https://github.com/Tunombredeusuario/azerothcore-wotlk**

Si su rama `master` no está actualizada con el último AzerothCore, verá algo como:

`Esta rama tiene XX confirmaciones detrás de azerothcore:master`

![Fork de actualización de AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-1.png)

para actualizarlo, haga clic en **Fetch upstream** y luego en **Fetch and merge**.

Como resultado, la rama `master` de tu Fork debería decir:

`Esta rama está a la par con azerothcore:master`

![AzerothCore fork updated](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-2.png)

### 2. Crear una nueva branch

Asegúrese de tener la rama `master` actualmente seleccionada, haga clic en el menú desplegable de ramas y cree una nueva rama.

![Fork de AzerothCore actualizada](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-branch.png)

Puede nombrar su nueva rama de la forma que desee (generalmente algo relacionado con su arreglo),
solo asegúrese de no haber usado ese nombre antes y de que está creando la nueva rama copiando la rama principal.

Debería ver un mensaje como **Crear rama my-new-branch-123 desde master**.

Después de crear la nueva rama, asegúrese de **mantenerla seleccionada**.

### 3. Navegue a la carpetaending_db_world

Ahora necesita navegar dentro de la carpeta `data/sql/updates/pending_db_world` de su fork.

Puede hacerlo manualmente haciendo clic en la carpeta `data`, luego `sql`, `updates`, `pending_db_world`;

... o simplemente puede abrir esta URL (cambie `Su nombre de usuario` con su nombre de usuario real de GitHub):

**https://github.com/YourUsername/azerothcore-wotlk/tree/my-new-branch-123/data/sql/updates/pending_db_world**

### 4. Generar un nuevo archivo de actualización de la versión 

En una nueva pestaña del navegador, abra [azerothcore.org/pages/rev-generator](https://www.azerothcore.org/pages/rev-generator/).

![Generador de actualización de SQL de AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-rev-generator.png)

Esto te dará:

- El nombre del archivo que necesita crear que contendrá su código SQL
- El *código de versión SQL* (una consulta `INSERT INTO`) que deberá agregar en la parte superior del nuevo archivo SQL que enviará

**Nota**: siempre deben ir juntos y siempre debes tener una nueva rev para cada PR que envíes.
Si necesita obtener una nueva versión, simplemente actualice la página o haga clic en "Generar nuevo".

Cópielos en algún lugar o mantenga abierta la pestaña del navegador.

### 5. Crear y confirmar un nuevo archivo

De vuelta en GitHub, desde la carpeta `pending_db_world`, haga clic en **Agregar archivo** y luego en **Crear nuevo archivo**:

![AzerothCore crea un nuevo archivo SQL](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-file-1.png)

Ahora necesitas:

- Establezca el nombre del archivo como el que generó en el paso 4.
- Agregue el código de versión de SQL que generó en el paso 4.
- Agregue una nueva línea, luego agregue su propio código SQL a continuación y luego agregue una nueva línea vacía al final del archivo.

![Ejemplo de nuevo archivo SQL de AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-file-2.png)

Ahora desplácese hacia abajo en la página, deberá:

1. Complete el mensaje de compromiso, usamos el [formato de compromisos convencionales] (https://www.conventionalcommits.org/),
  por ejemplo `fix(DB/Creature): alguna descripción de confirmación aquí`.
2. Incluye alguna descripción extra opcional) .
3. Asegúrese de que esté seleccionado "Comentar directamente con `your-new-branch-name`".
4. Haga clic en **Confirmar archivo nuevo**

![AzerothCore crea nueva confirmación](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-commit.png)

### 6. Abre el PR

Vuelva al [repositorio principal de AzerothCore](https://github.com/azerothcore/azerothcore-wotlk),
notarás que GitHub es lo suficientemente inteligente como para darse cuenta de que estás a punto de abrir un PR
y muestra este bonito cuadro amarillo claro:

![AzerothCore - Comparar y solicitar extracción](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/11.png)

haga clic en el botón verde "Comparar y extraer solicitud" (ubicado a la derecha).

Ahora complete la plantilla de PR siguiendo las instrucciones que aparecerán en la pantalla,
no olvide agregar las **instrucciones de prueba** para que las personas puedan probar su PR y se pueda fusionar:

![AzerothCore - Comparar y solicitar extracción](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/12.png)

También es una buena práctica verificar la pestaña "Cambios de archivo" para ver que todo esté en su lugar como espera:

![AzerothCore - Comparar y solicitar extracción](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/13.png)

**NOTA:** ¡No respondemos bien a las sanguijuelas! Si su solución proviene de otra organización o persona
SIEMPRE debes dar crédito al autor original y comprometerte.

¡Eso es!
