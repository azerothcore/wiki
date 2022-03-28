---
redirect_from: "/How-to-create-a-DB-PR"
---

# Como crear una Pull Request SQL en GitHub

Esta es una guía simplificada para crear fácilmente Pull Request que contengan correcciones de la base de datos (código SQL) sin molestarse con la terminal, 
una alternativa más fácil a la [manera tradicional de crear Pull Request](https://www.azerothcore.org/wiki/how-to-create-a-pr).
Si quiere enviar correcciones en C++ o de otro tipo que no sea SQL, siga la otra guía.

## Hazlo sólo una vez: crea tu fork de AzerothCore

Necesitas estar logueado en tu cuenta de [github.com](https://github.com/). Si aún no tienes una cuenta, crea una.

Abre el [repositorio de AzerothCore](https://github.com/azerothcore/azerothcore-wotlk)
y crea un fork del mismo haciendo clic en el botón "Fork" de la parte superior derecha.

![Create a fork of AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/1.png)

## Creando una nueva Pull Request

### 1. Actualiza tu fork en GitHub
Abre tu navegador y navega hasta tu fork en GitHub (cambia `YourUsername` por tu nombre de usuario actual en GitHub):

**https://github.com/YourUsername/azerothcore-wotlk**

Si tu rama `master` no está actualizada con el último AzerothCore, verás algo como esto:

`This branch is XX commits behind azerothcore:master`

![AzerothCore update fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-1.png)

para actualizarlo, haga clic en **Fetch upstream** y luego en **Fetch and merge**.

Como resultado, la rama `master` de tu fork debería decir:

`This branch is even with azerothcore:master`

![AzerothCore fork updated](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-2.png)

### 2. Crear una nueva rama

Asegúrese de que tiene seleccionada la rama `master`, haga clic en el desplegable de ramas y cree una nueva rama.

![AzerothCore fork updated](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-branch.png)

Puedes nombrar tu nueva rama como quieras (normalmente algo relacionado con tu arreglo), 
sólo asegúrate de que no has usado ese nombre antes y que estás creando la nueva rama copiando la rama master.

Deberías ver un mensaje como este **Create branch my-new-branch-123 from master**.

Después de crear la nueva rama, asegúrate de **mantenerla seleccionada**.


### 3. Navegue hasta la carpeta pending_db_world folder

Ahora debes navegar dentro de la carpeta `data/sql/updates/pending_db_world` de tu fork.

Puedes hacerlo manualmente haciendo clic en la carpeta `data`, luego `sql`, `updates`, `pending_db_world`;

...o puedes simplemente abrir este link (cambia `YourUsername` por tu nombre actual en GitHub):

**https://github.com/YourUsername/azerothcore-wotlk/tree/my-new-branch-123/data/sql/updates/pending_db_world**

### 4. Generar un nuevo archivo de actualización rev

En una nueva pestaña de tu navegador, abre [azerothcore.org/pages/rev-generator](https://www.azerothcore.org/pages/rev-generator/).

![AzerothCore SQL update rev generator](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-rev-generator.png)

Esto le dará:

- El nombre del archivo que necesita crear y que contendrá su código SQL.
- El *código de la versión SQL* (una consulta `INSERT INTO`) que deberá añadir al principio del nuevo archivo SQL que subirás.

**Nota**: siempre deben ir juntas y siempre debes tener una nueva rev para cada PR (Pull Request) que envíes.
Si necesita obtener una nueva rev, simplemente actualice la página o haga clic en "Generar nueva".

Cópialos en algún sitio o mantén la pestaña del navegador abierta.

### 5. Crea y commitea un nuevo archivo

De vuelta en GitHub, desde la carpeta `pending_db_world`, haz clic en **Add file** y luego en **Create new file**:

![AzerothCore create new SQL file](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-file-1.png)

Ahora necesitas:

- Establecer el nombre del archivo como el que generó en el paso 4.
- Añadir el código de la versión SQL que generó en el paso 4.
- Agregar una nueva línea, luego agregar su propio código SQL debajo y luego agregar una nueva línea vacía al final del archivo.

![AzerothCore new SQL file example](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-file-2.png)

Ahora desplázate hacia abajo en la página, necesitarás:

1. Rellenar el mensaje del commit, utilizamos [el formato convencional de los commits](https://www.conventionalcommits.org/),
  por ejemplo `fix(DB/Creature): some commit description here`.
2. Incluya alguna descripción adicional (opcional).
3. Asegúrese de que la opción "Commit directly to the `your-new-branch-name`" está seleccionada.
4. Haz clic en **Commit new file**.

![AzerothCore create new commit](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-commit.png)

### 6. Abriendo la Pull Request

Vuelve [al repositorio principal de AzerothCore](https://github.com/azerothcore/azerothcore-wotlk),
notarás que GitHub es lo suficientemente inteligente como para darse cuenta de que estás a punto de abrir un PR
y muestra este bonito cuadro amarillo claro:

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/11.png)

clic en el botón verde (localizado a la derecha) "Compare & pull request" 

Ahora rellene la plantilla del PR siguiendo las instrucciones que aparecerán en la pantalla,
no olvides añadir las **instrucciones de prueba** para que la gente pueda probar tu PR y pueda ser mergeado:

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/12.png)

También es una buena práctica comprobar la pestaña "File changes" para ver que todo está en su sitio como esperas:

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/13.png)

**NOTA:** ¡No respondemos bien a las personas que pierden el tiempo! Si su solución proviene de otra organización o persona 
SIEMPRE debe dar crédito al autor original y comprometerse.

Eso es todo.
