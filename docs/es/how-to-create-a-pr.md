---
redirect_from: "/How-to-create-a-PR"
---

# Como crear una PR

Esta guía explica cómo abrir PRs para enviar cualquier tipo de correciones (C++, SQL, etc...).

Si sólo envías correcciones de DB, deberías probar nuestra nueva [simplificada manera de abrir una PR que contenga código SQL](how-to-create-a-db-pr).

## Hacer sólo UNA VEZ: crear y clonar tu fork de AzerothCore

### 1. Crear un fork de AzerothCore

Necesitas estar registrado en [github.com](https://github.com/). Si aun no tienes una cuenta, crea una.

Abre el [repositorio de AzerothCore](https://github.com/azerothcore/azerothcore-wotlk) 
Y crea un fork de este haciendo click en el botón "Fork" de arriba a la derecha:

![Create a fork of AzerothCore](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/1.png)


### 2. Clona tu fork a tu dispositivo local

Una vez que tu fork esté listo, verás un nuevo repositorio mostrando **YourUsername/azerothcore-wotlk**.

Haz click en el botón "Clone or download" (a la derecha) y copia la dirección https de tu fork:

![Copy your AzerothCore fork address](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/2.png)

Ahora abre la **terminal** (si estas en Windows, usa [terminal git bash](https://git-scm.com/downloads)) 
y escribe `git clone ` seguido de la dirección de tu fork que acabas de copiar:

![Clone your AzerothCore fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/3.png)

```
git clone https://github.com/YourUsername/azerothcore-wotlk.git
```

Espera a que la descarga termine y luego accede al directorio de `azerothcore-wotlk`:

```
cd azerothcore-wotlk
```

![Access the AzerothCore directory](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/4.png)

## Creando una nueva PR

### 1. Actualiza tu fork en GitHub

Abre tu navegador y navega hasta tu fork en GitHub (cambia `YourUsername` con tu usuario actual de GitHub):

**https://github.com/YourUsername/azerothcore-wotlk**

Si tu `master` branch no está actualizado a la última versión de AzerothCore, verás algo como:

`This branch is XX commits behind azerothcore:master`

![AzerothCore update fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-1.png)

para actualizarlo, haz click en **Fetch upstream** y luego **Fetch and merge**.

Como resultado, el `master` branch de tu fork debería directorio:

`This branch is even with azerothcore:master`

![AzerothCore update fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-2.png)

### 2. Actualiza tu clone local

En el anterior paso acabas de actualizar tu fork *remoto*, pero también tienes que sincronizarlo con tu clon local.

Abre tu terminal dentro del directorio `azerothcore-wotlk` y ejecuta:

```
git checkout master; git pull
```

### 3. Crear un nuevo branch

**IMPORTANTE:** nunca cometas cambios en tu branch `master` , esto hará ver tu fork muy desordenado.

Cuando estés creando un nuevo branch, git creará una copia de tu branch **actual**. 
Siempre asegurate de que estas en `master` branch **antes** de crear un nuevo branch escribiendo:
 
```
 git checkout master
```

Crea un nuevo branch dandole un nombre que sea diferente que ningun branch ya existente.

Puedes darle cualquier nombre que quieras (substituye "xxx" con lo que sea que estas corrigiendo):

```
git checkout -b fix-issue-xxxx
```

![Access the AzerothCore directory](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/5.png)


### 4. Añadir tus cambios de C++ (si hay alguno)

Si no has hecho ningún cambio al C++, puedes saltar este paso. De lo contrario ¡Abre tu editor y hazlos ahora! Te esperaré...

En esta guía vamos a asumir que has modificado el archivo `instance_deadmines.cpp`

Ahora añade tu archivo(s) para que sean cometidos:

```
git add src/server/scripts/EasternKingdoms/Deadmines/instance_deadmines.cpp
```

![AzerothCore - add files with git add](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/6.png)

Si has modificado mas archivos, solo añadelos usando `git add path/to/file`

Puedes usar el comando `git status` para comprobar que archivos han sido seleccionados para ser cometidos:

![AzerothCore - git status](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/7.png)


### 5. Añade tus cambios SQL (si hay alguno)

Si no has hecho ningún cambio SQL, puedes saltar este paso. De lo contrario, ejecuta lo siguiente:

```
./data/sql/updates/pending_db_world/create_sql.sh
```

Esto generará un nuevo archivo ubicado en `data/sql/updates/pending_db_world` 
teniendo un nombre único como `rev_XXXXXXXXXXXX.sql`

![AzerothCore - create pending sql file](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/8.png)

Abrelo con un editor de texto. Te darás cuenta de que contiene código SQL como:

```
INSERT INTO `version_db_world` (`sql_rev`) VALUES ('XXXXXXXXXXXX');
```

NO elimines esta linea. Añade tu código SQL debajo y guardalo.

Ahora añade este archivo para que sea cometido usando el comando `git add path/to/file`:

```
git add data/sql/updates/pending_db_world/rev_XXXXXXXXXXXX.sql
``` 

(obviamente remplaza `rev_XXXXXXXXXXXX.sql` con el verdadero nombre del archivo)

![AzerothCore - git add pending sql file](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/9.png)

### 6. Commit & Push tus cambios

#### Hacer solo UNA vez: git config

Primero antes que todo asegurate de usar la plantilla de commit AC (esto debería ser necesario solo una vez):
```
git config --local commit.template ".git_commit_template.txt"
```

Cuando escribas tu mensage de commit, este usará el editor de texto por defecto `Vim` que es bastante complicado de manipular. Sin embargo puedes mantenerlo mas simple usando el editor `Nano` . Aquí está como proceder, escribe:
```
git config --global core.editor "nano"
```

#### Git commit

Luego comete tus cambios escribiendo:
```
git commit
```
Se te pedirá que especifique un mensaje de confirmación apropiado. Por favor, siga las pautas de formato aquí (= cada línea que empieza por un # que será ignorado en el mensaje de confirmación), y puede referirse a una confirmación como [esto](https://github.com/azerothcore/mod-npc-beastmaster/commit/53cf90233091db2191b522f0fa7c4b6009dca22e) como un ejemplo.
Si estas usando `Nano`, pressiona [ctrl]+[x] y escribe yes para guardar y salir (los otros comandos estan escritos abajo de la interfaz en `Nano`, y pueden ser encontrados facilmente en la net o escribiendo `man nano` en la terminal).

Verifica que estás satisfecho usando `git show`. Y sal usando [q]. Si no estas satisfecho, puedes hacer un recommit al **último commit local** escribiendo `git commit --amend`.

Ahora es el momento de hacer un push remotamente. 
Si usas el comando `git push` por primera vez en este branch, 
git te pedirá que especifiques a que branch remoto quieres hacer el push.

Así que deberías ejecutar:

```
git push --set-upstream origin fix-issue-xxxx
```

(Por supuesto remplaza `fix-issue-xxxx` con el nombre de tu branch)

![AzerothCore - git push](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/10.png)


### 7. Abrir la PR

Vuelve al [repositorio principal AzerothCore](https://github.com/azerothcore/azerothcore-wotlk), 
te darás cuenta de que GitHub es lo suficientemente listo para darse cuenta de que est´´as a punto de abrir una PR 
y muestra este recuadro amarillo claro:
 
![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/11.png)

Haz click en el botón verde de "Compare & pull request" (ubicado a la derecha).

Ahora llena la plantilla de la PR siguiendo las instrucciones que aparecerán en tu pantalla, 
no te olvides de añadir **las instrucciones de testing** para que la gente pueda probar tu PR y pueda ser unida:

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/12.png)

Tambien es una buena practica de comprobar la ventana de "File changes" para ver que todo está a tu gusto:

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/13.png)

**NOTA:** No respondemos bien con los leechers! Si tu fix viene de otra organizacion o persona deberías SIEMPRE dar credito al autor original y el commit.

Eso es todo!

## FAQ

### Hay algo mal o faltan archivos en los cambios, Quiero subir más cambios

Solo edita/añade los archivos que quieras, `git add` , luego haz el commit y el push otra vez. 
Si refrescas la pagna de tu PR verás los cambios.

### Ya he creado una PR, debería crear otra?

Solo repite el procedimiento empezando desde el paso 3.

Se cuidadoso creando un nuevo branch: **debes** estar en el `master` branch primero (escribe `git checkout master`).

### Como puedo actualizar el master branch de mi fork?

Si nunca has actualizado tu fork antes, escribe:

```
git remote add upstream https://github.com/azerothcore/azerothcore-wotlk.git
```

Luego sigue estos pasos:

1) `git checkout master`
2) `git fetch upstream`
3) `git merge upstream/master`
4) `git push origin master`

Y ya has actualizado tu fork :)

### Cómo puedo actualizar mi branch con el ultimo master?

Tienes que actualizar el master branch de tu fork primero (mirar arriba).

Luego solo `git checkout your-branch` y `git merge master`.

### Cuánto tiempo tardará que mi PR sea revisada, testeada y unida?

Esto es un proyecto de codigo abierto y la gente trabaja en su tiempo libre, así que no podemos estimarlo.

Lo que si podemos recomendar es: escribe instrucciones **claras** para testear tu PR, asi sera más fácil para todos de testearlo.

Si tus instrucciones no son claras o inexistentes, 
solo los usuarios avanzados seran capaces de testear tu PR y tardara mucho más tiempo.

### Qué terminal fue usada en este tutorial?

https://github.com/robbyrussell/oh-my-zsh

Pero cualquier terminal de linux/mac esta bien también 
Si tienes tan mala suerte de estar en Windows, usa [git bash](https://git-scm.com/downloads).

### Do I have to re-autenticar cada vez que uso git push?

Puedes clonar tu propio fork usando SSH en vez de HTTPS y luego sigue [esta guía](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) to set the SSH keys.

De esta manera puedes usar `git push` sin tener que repetir tu contraseña.
