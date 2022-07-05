# Cómo probar un PR (pull request)

## Introducción

En AzerothCore nos preocupamos por la calidad y la estabilidad del juego. Por ello, **no enviamos los cambios directamente a la rama maestra**. En su lugar, cada vez que introducimos un nuevo cambio, creamos un nuevo [Pull Request](https://help.github.com/articles/about-pull-requests/) (a menudo acortado en PR).

Esto nos permite **revisar y probar** adecuadamente cualquier cambio antes de que llegue a los entornos de producción. Todos los que puedan instalar AzerothCore también pueden contribuir probando los PRs. Esta guía explicará cómo hacerlo.

Cuantos más usuarios nos ayuden a probar los PR, mejor será nuestra actividad de desarrollo en términos de velocidad y calidad.

## ¿Qué PRs hay que probar?

Etiquetamos como [**A la espera de ser probado**](https://github.com/azerothcore/azerothcore-wotlk/pulls?q=is%3Apr+is%3Aopen+label%3A%22Waiting+to+be+tested%22) todos los PRs que ya han sido completados por el autor y han tenido su código revisado.

Al hacer clic en la etiqueta de arriba se mostrará la lista de todos los PRs que deben ser probados para llegar a la rama `master`.

## ¿Qué necesito antes de probar un PR?

Es necesario:

- Tener AzerothCore instalado en tu sistema (ver [Instalación](es/installation)).
- Tener una cuenta en GitHub, puede [registrar una aquí](https://github.com/join) de forma gratuita.

### ¿Y si el PR sólo tiene cambios en la BD (base de datos)?

Algunos PRs sólo tienen cambios en la base de datos (sin cambios en C++). Si ese es el caso, hay un [procedimiento simplificado para probar esos cambios](es/How-to-test-DB-only-changes).

Si no estás seguro, sigue leyendo aquí y haz la prueba tradicional de PR que servirá para todo tipo de PR.

### Notas que clonaron un fork de AzerothCore en lugar del repo principal:

Es típico crear y clonar tu propio fork de AzerothCore si también eres desarrollador.

Si ese es tu caso, entonces tienes que

- añadir el principal AzerothCore remoto utilizando:

```
git remote add upstream https://github.com/azerothcore/azerothcore-wotlk.git
```

- sustituya `origin` por `upstream` en todos los comandos indicados a continuación

## Obtenga el código PR para ser probado

- Abre un terminal y ve al directorio de tus fuentes de AzerothCore, por ejemplo usando `cd azerothcore-wotlk`.

![image](https://user-images.githubusercontent.com/75517/52176403-b6708480-27b2-11e9-93b0-9f3d3232e817.png)

- Aquí asumimos que estás comenzando desde una rama "master" limpia y actualizada. Puedes verificar en qué rama estás escribiendo "git checkout". Si no estás en master, vuelve a master usando `git checkout master`. Ya que estás aquí, también puedes hacer `git pull` para asegurarte de que tienes la última rama maestra. Y recuerda, **nunca añadas cambios personalizados a la rama maestra** (crea siempre una rama nueva y separada si es necesario).

- Comprueba el ID del PR que quieres probar, aparecerá en la URL y el título del PR. Por ejemplo, el ID de este PR es **1383**: [PR 1383](https://github.com/azerothcore/azerothcore-wotlk/pull/1383)

![image](https://user-images.githubusercontent.com/75517/52176395-9ccf3d00-27b2-11e9-9600-64206e7b33bc.png)

- Ahora debe ejecutar los siguientes comandos sustituyendo "XXXX" por el ID del PR que desea probar:

```bash
git checkout -b pr-XXXX
```

```bash
git pull origin pull/XXXX/head
```

Ejemplo:

```bash
git checkout -b pr-1383
```

```bash
git pull origin pull/1383/head
```

Los comandos anteriores crearán una nueva rama local llamada `pr-XXXX` que contendrá todos los cambios que deben ser probados.

La terminal mostrará un editor (normalmente `nano` o `vim`) que le pedirá que guarde el mensaje de confirmación de la fusión. Simplemente guarde los cambios y salga del editor.

- Si el editor es `nano`, puedes hacerlo simplemente usando `ctrl + o` y `ENTER` para guardar y luego `ctrl + x` para salir.
- Si el editor es `vim` puedes mantener la tecla `SHIFT` y pulsar dos veces `Z` para guardar y existir.

Puedes leer más sobre la configuración de `git` y su editor por defecto [aquí](http://web.mit.edu/6.005/www/fa14/tutorial/git/config.html).

- Nota: Compruebe el mensaje en su consola. Si dice "La fusión automática ha fallado; arregle los conflictos y luego confirme el resultado", debe informar al PR, pidiendo al desarrollador que por favor arregle los conflictos de fusión, y elimine la etiqueta "esperando a ser probado" y adjunte una etiqueta "conflicto de fusión".

## Actualice su servidor local para aplicar los cambios

Ahora sólo tiene que actualizar su servidor local con los nuevos cambios. El procedimiento es análogo al de una actualización normal del servidor.

Básicamente necesitas **recompilar tus fuentes** y **actualizar la BD**.

**Nota:** Si se agregaron archivos nuevos o se eliminaron algunos / renombraron, recuerdo ejecutar el cmake para que los reconozca durante la compilación.

### Utilizando la configuración tradicional

Si está utilizando la instalación tradicional, tiene que volver a compilar siguiendo los pasos de la [3) Compilación](es/instalación#3-compilación) de la guía de instalación principal.

También necesita actualizar su DB. Puede utilizar el ensamblador de BD para hacerlo, pero normalmente es más rápido importar manualmente los archivos sql pendientes que incluye el PR. Estos archivos se encuentran en `data/sql/updates/pending_db_*`.

**Consejo**: Normalmente, un PR consiste en un archivo de actualización del mundo nuevo ubicado en `data/sql/updates/pending_db_world`. Puede comprobar qué archivos se han añadido para detectar cualquier archivo sql añadido yendo a la pestaña "Archivos cambiados" de la página de PR:

![File Changes](https://user-images.githubusercontent.com/75517/52176720-ea4da900-27b6-11e9-8459-d58adf7fd50c.png)

A continuación, inicie el servidor como lo hace siempre.

### Uso de la configuración de Docker

Si está utilizando la configuración de Docker, puede simplemente activar la recompilación ejecutando:

- Linux:

```bash
./bin/acore-docker-build
```

- Windows:

```bash
./acore.sh docker build
```

Entonces para lanzar el servidor tienes que destruir y recrear los contenedores usando `docker-compose down` y `docker-compose up`.

**Nota**: esto también actualizará automáticamente su DB.

## Verifique su versión actual

Para asegurarse de que está ejecutando correctamente su servidor con el PR, compruebe la fecha y el nombre de la rama en la salida del comando `server info`. Deben coincidir con el PR.

Ahora entra en el juego y haz tus pruebas.

## ¿Qué hay que probar?

Las instrucciones sobre lo que hay que probar en el ámbito de un PR deben ser proporcionadas por el autor del PR en la descripción del mismo. Si no es el caso, no dudes en dejar un comentario en la descripción del PR pidiendo instrucciones de prueba.

Para los usuarios avanzados: también puedes echar un vistazo a lo que realmente se ha cambiado en el PR y decidir tú mismo qué probar. A veces es bueno tener un punto de vista diferente. Sólo asegúrese de describir lo que ha probado en su informe.

## Informar de los resultados de las pruebas

Es importante informar de los resultados de las pruebas dejando un comentario **en la página de PR**.

Deberías escribir:

- Lo que ha probado
- ¿Las cosas que ha probado funcionan como se pretendía?
- A veces también puede especificar cómo funcionaban las cosas **antes** y **después** del PR
- Por favor, inserte tantos detalles como sea posible
- También puede insertar capturas de pantalla o vídeos

## Ejemplos de buenos informes de pruebas

![image](https://user-images.githubusercontent.com/75517/52176856-1702c000-27b9-11e9-9030-48fe01669247.png)

![image](https://user-images.githubusercontent.com/75517/52176862-3bf73300-27b9-11e9-8852-51624d882ccd.png)

![image](https://user-images.githubusercontent.com/75517/52176828-980d8780-27b8-11e9-9fcc-071d64176022.png)

![image](https://user-images.githubusercontent.com/75517/52176837-becbbe00-27b8-11e9-9b42-94a9521b6647.png)

![image](https://user-images.githubusercontent.com/75517/52176842-cee39d80-27b8-11e9-97e6-25f272a346bd.png)

![image](https://user-images.githubusercontent.com/75517/52176846-ea4ea880-27b8-11e9-9497-919cec1e22ff.png)

![image](https://user-images.githubusercontent.com/75517/52176849-02262c80-27b9-11e9-927f-687dcc43cb26.png)

![image](https://user-images.githubusercontent.com/75517/52176867-44e80480-27b9-11e9-9f43-070e4edcb77d.png)

## Pruebas de finalización

Una vez que haya dejado un informe de prueba, querrá revertir su instalación de AC al estado base para realizar más pruebas. Para ello, utiliza `git reset --hard` para eliminar todos los cambios no realizados, seguido de `git checkout master` para volver a la rama maestra. Para poner orden, también puedes usar `git clean -fd` para deshacerte de cualquier archivo sin seguimiento. Finalmente, puedes escribir `git status` para asegurarte de que todo vuelve a la normalidad.
