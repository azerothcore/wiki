# Primeros pasos con AzerothCore

## Introducción

¿Te gustaría aprender sobre AzerothCore (AC), configurar tu servidor de WoW por primera vez, entender cómo modificarlo y ser capaz de contribuir? ¡Has llegado al lugar correcto!

Empezar con la emulación de WoW puede resultar complicado al principio, pero no te preocupes, estaremos ahí para ayudarte en caso de que encuentres algún problema o tengas alguna pregunta. Solo lee [esta página](How-to-ask-for-help) antes de pedir ayuda.

Si mientras lees cualquiera de los tutoriales enlazados en esta página encuentras algo que no está claro: háznoslo saber. Haremos lo posible por reformularlo y hacerlo más fácil de entender para los principiantes. ¡Mejorar la documentación también es una forma de contribuir!

![AzerothCore learning code](https://user-images.githubusercontent.com/75517/109369720-b6fa7d00-789d-11eb-86b4-5fe15d6ab834.png)


## Requisitos de conocimientos

**NO** hay requisitos técnicos. Solo necesitas ser paciente y tener ganas de aprender.

Si ya tienes algunos conocimientos de programación, seguramente será una ventaja para ti. Sin embargo, créeme, no necesitas ningún conocimiento previo para aprender sobre servidores de WoW.

*Nota personal del autor de este tutorial: cuando instalé mi primer servidor de WoW tenía 15 años, no tenía ningún conocimiento de programación, usaba Windows XP y apenas entendía inglés. Estoy seguro de que si estás leyendo esto, ya tienes más habilidades de las que yo tenía cuando intentaba instalar MaNGOS+UDB+ScriptDev2 y conseguir que un servidor de WoW decente funcionara en mi máquina local.
Al principio, pasé horas intentando leer y entender tutoriales de diferentes personas escritos en diferentes sitios web, pero al final lo conseguí. AzerothCore es un proyecto todo-en-uno, así que va a ser más fácil que eso; ¡ten paciencia y lo lograrás!*

¿Tentado a usar un repack en su lugar? [No lo hagas](https://www.mangosrumors.org/why-you-should-not-use-repacks-to-run-your-wow-server/).

## Instalar AzerothCore en tu ordenador

El primer paso es siempre instalar un servidor de WoW local en tu propia máquina. Y hay varias formas de hacerlo, que pueden variar según el sistema operativo.

### Tu sistema operativo

Déjame dejar clara una cosa: **TODOS los sistemas operativos son compatibles con AzerothCore**.
Así que puedes instalar AzerothCore con éxito en GNU/Linux, macOS o Windows sin ningún problema.

Sin embargo, puedo decirte que si usas una distribución de Linux como **Ubuntu 26.04**, el proceso va a ser más fácil. Si quieres instalar Ubuntu, puedes descargarlo [aquí](https://ubuntu.com/download/desktop) y puedes encontrar muchos tutoriales online sobre cómo hacerlo. Hay un buen tutorial sobre cómo ejecutar WoW en Linux [aquí](https://www.mangosrumors.org/how-to-run-wow-on-linux/).

¿Te gustaría quedarte con **Windows** o **macOS**? Está absolutamente bien.

![AzerothCore supports GNU/Linux, macOS and Windows](https://user-images.githubusercontent.com/75517/109369213-e5775880-789b-11eb-8356-99a4ab842bfb.png)

### Diferentes formas de instalar AzerothCore

Básicamente, hay 3 formas principales de instalar AC:

- La "**instalación clásica**": esta es la configuración tradicional que normalmente usarías para instalar un emulador de WoW común. **Todos los sistemas operativos son compatibles.** Hacer esta configuración probablemente también te da una mejor visión general de los componentes del servidor.
- La "**instalación con docker**": esta es una configuración simplificada que usa Docker para automatizar muchas cosas por ti. Esta configuración suele ser más fácil. **Puedes usar esta configuración en todos los sistemas operativos donde puedas instalar [Docker](https://www.docker.com/products/docker-desktop).**
- La "**instalación con dashboard**": esta es una forma **EXTREMADAMENTE FÁCIL** de instalar AzerothCore en tu máquina, basada en una colección de scripts bash creados por [Yehonal](https://github.com/Yehonal). Sin embargo, **solo puedes usar esta configuración en Ubuntu** o plataformas similares. Windows no es compatible, y probablemente aún no estamos ahí con macOS tampoco.

Puedes elegir una configuración, o incluso probar más de una. Puedes encontrar todas las instrucciones aquí:

- [azerothcore.org/wiki/Installation](installation)

Si encuentras algún problema o duda al intentar instalar tu servidor de AC, [pídenos ayuda](https://github.com/azerothcore/wiki/blob/master/docs/how-to-ask-for-help).

¿Ya tienes tu servidor de WoW instalado? ¡Enhorabuena! Ahora veamos qué puedes hacer a continuación.

![AzerothCore server running on macOS](https://user-images.githubusercontent.com/75517/109369101-80236780-789b-11eb-900c-bcc17a3cf13c.png)

## Accede al juego, aprende los comandos GM

Antes que nada, asegúrate de que tu cliente tenga su realmlist.wtf configurado con lo siguiente: `set realmlist localhost`. Después de esto (asumiendo que ya has configurado AzerothCore) asegúrate de tener creada una cuenta `GM` (con seguridad de 2 o superior). Si no has creado una cuenta o no estás seguro, sigue esto: [Crear cuentas](creating-accounts).
Después de esto tu cuenta `GM` podrá usar los siguientes comandos, con un enlace a una lista de todos los comandos abajo:

- [azerothcore.org/wiki/GM-Commands](GM-Commands)

Toma confianza con los comandos, los necesitarás para cualquier actividad de administración, testing o desarrollo.

![AzerothCore GM](https://user-images.githubusercontent.com/75517/109369940-ba423880-789e-11eb-88d6-e6d8f7b8a723.png)

## Considera aprender git

Puedes simplemente copiar y pegar a ciegas los comandos de `git` que verás en los tutoriales enlazados aquí; lo más probable es que no tengas problemas con ellos.
Sin embargo, aprender `git` correctamente te hará realmente consciente de lo que estás haciendo, y este conocimiento puede ayudarte con cualquier otro proyecto de desarrollo de software en el que trabajes.
Sí, porque `git` es una de las herramientas más importantes usadas en muchos proyectos de ingeniería de software. Aprender sus fundamentos no solo te ayudará mucho con AzerothCore, sino que también es algo muy bueno para poner en tu CV.

Puedes encontrar muchos recursos online sobre cómo aprender `git`, por ejemplo [try.github.io](https://try.github.io/)

![AzerothCore learning git](https://user-images.githubusercontent.com/75517/109370018-fb3a4d00-789e-11eb-8532-1ab1bf8fba60.png)

## Aprende cómo actualizar tu servidor de WoW

Lanzamos mejoras a AzerothCore a diario. Deberías aprender cómo actualizar tu servidor y mantenerlo actualizado a menudo. Recomendamos evitar trabajar en versiones antiguas de AzerothCore porque pueden tener bugs que ya hemos resuelto y no querrás quedarte atrás.

Por eso es **muy importante** que actualices tu servidor de AzerothCore regularmente. Te recomendamos hacerlo al menos una vez por semana. Lee esta guía:

- [azerothcore.org/wiki/Update](update)

Después de seguir el procedimiento de actualización, es importante **verificar** que:

- Tu aplicación de servidor (core) se ha actualizado correctamente; usa el comando `server info` para asegurarte de ello.
- Tu BD se ha actualizado correctamente y alineado con tu versión del core, [lee esta respuesta en stackoverflow](https://stackoverflow.com/a/55282168/3497671).

![AzerothCore server info](https://user-images.githubusercontent.com/75517/109370296-00e46280-78a0-11eb-9ed0-b9df14f2008b.png)

## Aprende a probar PRs

Una gran forma de empezar a contribuir es probando los PRs hechos por otros colaboradores. Esto no solo es bastante fácil de hacer, sino que es extremadamente útil para el proyecto y puede ayudarte a introducirte en nuestro proceso de desarrollo.

Este tema es tan importante que hay un tutorial dedicado a él:

- [azerothcore.org/wiki/How-to-test-a-PR](How-to-test-a-PR)

![image](https://user-images.githubusercontent.com/75517/109370244-d397b480-789f-11eb-9ac7-64d98ca0d33c.png)

## Aprender a trabajar con la base de datos

La base de datos es el mejor lugar para empezar a desarrollar un servidor de WoW. Porque es más fácil que los otros componentes, y hay herramientas que son capaces de generar el código por ti automáticamente. Por ejemplo, Keira3.

### Descarga Keira3

Keira3 es un editor de BD para AzerothCore que te permite editar o añadir contenidos al mundo muy fácilmente; recomendamos instalarlo y jugar con él:

- [azerothcore.org/Keira3](https://www.azerothcore.org/Keira3)

Keira3 genera automáticamente el código SQL necesario para crear o cambiar cosas en la base de datos.
¿Suena complicado? Pruébalo y verás cómo funciona.

![AzerothCore Keira3](https://user-images.githubusercontent.com/75517/109370160-769bfe80-789f-11eb-9958-dc17ff48f39a.png)

### Descarga un cliente MySQL

Necesitarás también una herramienta genérica de gestión de bases de datos para gestionar las tablas y sus contenidos.

- [Herramienta de gestión de bases de datos](database-management-tool)

![AzerothCore world database viewed with sequel-ace](https://user-images.githubusercontent.com/75517/109370368-42750d80-78a0-11eb-946c-c0831a02b52b.png)

### La documentación de la BD es tu amiga

Lee siempre la documentación sobre cada tabla con la que trabajes:

- [azerothcore.org/wiki/database-world](database-world)

### SmartAI

Con SmartAI puedes hacer muchas cosas. Puedes añadir un comportamiento especial a un elemento del juego como una creature, sin tocar nunca una sola línea de C++.

En pocas palabras, con SmartAI puedes hacer que una entidad (por ejemplo una Creature) realice una determinada **acción** cuando ocurre un determinado **evento**, especificando opcionalmente un **objetivo**. En otras palabras, puedes hacer que las entidades reaccionen a los eventos con un comportamiento definido por ti.

Por ejemplo, puedes hacer que una creature lance un hechizo (acción), cuando su salud baje por debajo del 50% de su salud total (evento), contra un miembro aleatorio del grupo (objetivo).

Técnicamente, el `smart_script` es solo una tabla dentro de la base de datos world (y su documentación se puede encontrar [aquí](smart_scripts)). Herramientas como Keira3 te ayudan a trabajar con SmartAI usando una interfaz gráfica práctica.

Intenta abrir Keira3, busca cualquier creature que tenga "SmartAI" como "AIName", ábrela y haz click en "SmartAI" en el menú de la derecha.
Se te presentará un editor visual que te asistirá al trabajar con SmartAI.

![AzerothCore SmartAI with Keira3](https://user-images.githubusercontent.com/75517/109367698-1bfea480-7897-11eb-9cf0-f047b3dcdb85.png)

Experimenta con SmartAI y toma confianza con él. Es una herramienta sencilla pero muy potente.
Después de adquirir algo de conocimiento de ella, podrás hacer muchas cosas. Muchos bugs se pueden arreglar simplemente usando SmartAI.

La IA de la mayoría de las creatures que encontrarás en el mundo está hecha con SmartAI. Mientras que las creatures más complejas (típicamente los bosses de raid) se scriptean en C++.

![SmartAI vs C++](https://user-images.githubusercontent.com/75517/109369529-e78de700-789c-11eb-97d5-02ecc6c85a0a.png)

### Aprende el lenguaje SQL

Normalmente solo necesitarás lo básico del lenguaje SQL, y en la mayoría de los casos probablemente lo descubrirás por ti mismo; sin embargo, no es mala idea leer sobre el lenguaje SQL. Puedes encontrar muchos recursos online, por ejemplo:

- [https://www.w3schools.com/sql/sql_intro.asp](https://www.w3schools.com/sql/sql_intro.asp)

si entiendes cómo funcionan sentencias básicas como `SELECT`, `UPDATE`, `INSERT` y `DELETE`, eso suele ser suficiente. No necesitas profundizar demasiado en SQL para poder contribuir.

## ¡Comparte tu código!

Puedes enviar tu mejora mediante un PR. Lee esta guía:

- [Cómo crear un Pull Request (PR)](how-to-create-a-pr)

## ¡Empieza a contribuir!

Si has dominado algunas de las partes anteriores, ya hay **MUCHO** que puedes hacer para ayudar a nuestro proyecto y convertirte en un colaborador.
Por ejemplo:

- Ayuda a los desarrolladores probando PRs y dando tu feedback
- Haz algo de triaje de bugs confirmando issues y ayudándonos a identificar y cerrar los reportes inválidos
- También puedes ayudar [haciendo triaje de los bugs que vienen de los jugadores de ChromieCraft](https://github.com/chromiecraft/chromiecraft) (nuestro proyecto hijo)
- Reporta cualquier bug que puedas encontrar tú mismo
- Intenta arreglar bugs; muchos de ellos se pueden arreglar simplemente con algo de SQL y puedes usar Keira3 para eso (p. ej. usando SmartAI u otros editores integrados). Al ser este un proyecto de código abierto, puedes encontrar muchos ejemplos en nuestro repositorio principal de GitHub

¿Te gustaría hablar con nosotros? Únete [al servidor de Discord de AzerothCore](https://discordapp.com/invite/gkt4y2x).

![Contributing to AzerothCore](https://user-images.githubusercontent.com/75517/109370461-b44d5700-78a0-11eb-916c-81c8500fa969.png)

## Conclusión y próximos pasos

Nunca dejes de aprender. Ve a aprender los fundamentos detrás de la Programación Orientada a Objetos (OOP).
Consigue algún tutorial de C++, empieza a experimentar con el código fuente del core. Mira los PRs de otras personas como ejemplos.

Estudia los mecanismos básicos del servidor de juego (lee artículos como [este](https://stackoverflow.com/questions/62249204/how-does-the-update-diff-work-in-azerothcore)). Intenta [crear módulos](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore).

O aprende otro lenguaje de programación; hay muchas herramientas que podrías construir para los usuarios o desarrolladores de AzerothCore usando tu lenguaje de programación favorito.

Hagas lo que hagas, recuerda siempre: **StackOverflow es tu amigo**.

-------------------------------------------------

En este tutorial, quería ayudar a los principiantes y demostrar cuánto puedes aprender y contribuir sin siquiera saber C++. Todo lo que necesitas es algo de tiempo y paciencia.

¡Feliz coding!

-- Shin, alias Francesco
