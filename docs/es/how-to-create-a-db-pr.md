---
redirect_from: "/How-to-create-a-DB-PR"
---

# C�mo crear una DB PR a trav�s de GitHub

Esta es una gu�a simplificada para crear f�cilmente PR que contengan correcciones de base de datos (c�digo SQL) sin molestarse con la terminal.
una alternativa m�s f�cil a la [forma tradicional de crear PR] (https://www.azerothcore.org/wiki/how-to-create-a-pr).
Si desea enviar correcciones de C++ u otro tipo que no sea SQL, siga la otra gu�a.

## Haz solo UNA VEZ: crea tu fork de AzerothCore

Debe iniciar sesi�n en [github.com](https://github.com/). Si a�n no tienes una cuenta, crea una.

Abra el [repositorio de AzerothCore](https://github.com/azerothcore/azerothcore-wotlk)
y cree una fork haciendo clic en el bot�n "Fork" de la parte superior derecha:

![Crear una Fork de AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/1.png)

## Creando un nuevo PR

### 1. Actualiza tu kork en GitHub

Abra su navegador y navegue hasta su fork en GitHub (cambie `Su nombre de usuario` con su nombre de usuario actual de GitHub):

**https://github.com/Tunombredeusuario/azerothcore-wotlk**

Si su rama `master` no est� actualizada con el �ltimo AzerothCore, ver� algo como:

`Esta rama tiene XX confirmaciones detr�s de azerothcore:master`

![Fork de actualizaci�n de AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-1.png)

para actualizarlo, haga clic en **Fetch upstream** y luego en **Fetch and merge**.

Como resultado, la rama `master` de tu Fork deber�a decir:

`Esta rama est� a la par con azerothcore:master`

![AzerothCore fork updated](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-2.png)

### 2. Crear una nueva branch

Aseg�rese de tener la rama `master` actualmente seleccionada, haga clic en el men� desplegable de ramas y cree una nueva rama.

![Fork de AzerothCore actualizada](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-branch.png)

Puede nombrar su nueva rama de la forma que desee (generalmente algo relacionado con su arreglo),
solo aseg�rese de no haber usado ese nombre antes y de que est� creando la nueva rama copiando la rama principal.

Deber�a ver un mensaje como **Crear rama my-new-branch-123 desde master**.

Despu�s de crear la nueva rama, aseg�rese de **mantenerla seleccionada**.

### 3. Navegue a la carpetaending_db_world

Ahora necesita navegar dentro de la carpeta `data/sql/updates/pending_db_world` de su fork.

Puede hacerlo manualmente haciendo clic en la carpeta `data`, luego `sql`, `updates`, `pending_db_world`;

... o simplemente puede abrir esta URL (cambie `Su nombre de usuario` con su nombre de usuario real de GitHub):

**https://github.com/YourUsername/azerothcore-wotlk/tree/my-new-branch-123/data/sql/updates/pending_db_world**

### 4. Generar un nuevo archivo de actualizaci�n de la versi�n 

En una nueva pesta�a del navegador, abra [azerothcore.org/pages/rev-generator](https://www.azerothcore.org/pages/rev-generator/).

![Generador de actualizaci�n de SQL de AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-rev-generator.png)

Esto te dar�:

- El nombre del archivo que necesita crear que contendr� su c�digo SQL
- El *c�digo de versi�n SQL* (una consulta `INSERT INTO`) que deber� agregar en la parte superior del nuevo archivo SQL que enviar�

**Nota**: siempre deben ir juntos y siempre debes tener una nueva rev para cada PR que env�es.
Si necesita obtener una nueva versi�n, simplemente actualice la p�gina o haga clic en "Generar nuevo".

C�pielos en alg�n lugar o mantenga abierta la pesta�a del navegador.

### 5. Crear y confirmar un nuevo archivo

De vuelta en GitHub, desde la carpeta `pending_db_world`, haga clic en **Agregar archivo** y luego en **Crear nuevo archivo**:

![AzerothCore crea un nuevo archivo SQL](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-file-1.png)

Ahora necesitas:

- Establezca el nombre del archivo como el que gener� en el paso 4.
- Agregue el c�digo de versi�n de SQL que gener� en el paso 4.
- Agregue una nueva l�nea, luego agregue su propio c�digo SQL a continuaci�n y luego agregue una nueva l�nea vac�a al final del archivo.

![Ejemplo de nuevo archivo SQL de AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-file-2.png)

Ahora despl�cese hacia abajo en la p�gina, deber�:

1. Complete el mensaje de compromiso, usamos el [formato de compromisos convencionales] (https://www.conventionalcommits.org/),
  por ejemplo `fix(DB/Creature): alguna descripci�n de confirmaci�n aqu�`.
2. Incluye alguna descripci�n extra opcional) .
3. Aseg�rese de que est� seleccionado "Comentar directamente con `your-new-branch-name`".
4. Haga clic en **Confirmar archivo nuevo**

![AzerothCore crea nueva confirmaci�n](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-commit.png)

### 6. Abre el PR

Vuelva al [repositorio principal de AzerothCore](https://github.com/azerothcore/azerothcore-wotlk),
notar�s que GitHub es lo suficientemente inteligente como para darse cuenta de que est�s a punto de abrir un PR
y muestra este bonito cuadro amarillo claro:

![AzerothCore - Comparar y solicitar extracci�n](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/11.png)

haga clic en el bot�n verde "Comparar y extraer solicitud" (ubicado a la derecha).

Ahora complete la plantilla de PR siguiendo las instrucciones que aparecer�n en la pantalla,
no olvide agregar las **instrucciones de prueba** para que las personas puedan probar su PR y se pueda fusionar:

![AzerothCore - Comparar y solicitar extracci�n](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/12.png)

Tambi�n es una buena pr�ctica verificar la pesta�a "Cambios de archivo" para ver que todo est� en su lugar como espera:

![AzerothCore - Comparar y solicitar extracci�n](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/13.png)

**NOTA:** �No respondemos bien a las sanguijuelas! Si su soluci�n proviene de otra organizaci�n o persona
SIEMPRE debes dar cr�dito al autor original y comprometerte.

�Eso es!
