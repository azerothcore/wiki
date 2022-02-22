# Primeros pasos con AzerothCore

## Introducción

¿Le gustaría aprender sobre AzerothCore (AC), configurar su servidor de WoW por primera vez, entender cómo modificarlo y poder contribuir? ¡Usted vino al lugar correcto!

Comenzar con la emulación de WoW puede ser complicado al principio, pero no se preocupe, estaremos allí para ayudarlo en caso de que tenga algún problema o tenga alguna pregunta que hacer. Solo lea [esta página](https://www.azerothcore.org/wiki/How-to-ask-for-help) antes de pedir ayuda.

Si mientras lees alguno de los tutoriales enlazados en esta página encuentras algo que no te queda claro: háznoslo saber. Haremos todo lo posible para reformularlo y hacerlo más fácil de entender para los principiantes. ¡Mejorar los documentos también es una forma de contribuir!

![AzerothCore learning code](https://user-images.githubusercontent.com/75517/109369720-b6fa7d00-789d-11eb-86b4-5fe15d6ab834.png)


## Requisitos de conocimientos

Esto **NO** reqiere requisitos técnicos. Solo necesitas ser paciente y estar dispuesto a aprender.

Si ya tienes algunos conocimientos de programación seguro que sería una ventaja para ti. Sin embargo, créame, no necesita ningún conocimiento previo para aprender sobre los servidores de WoW.

*Nota personal del autor de este tutorial: cuando instalé por primera vez mi primer servidor de WoW tenía 15 años, no tenía ningún conocimiento de programación, usaba Windows XP y apenas entendía inglés. Estoy seguro de que si está leyendo esto, ya tiene más habilidades que las que tenía cuando intentaba instalar MaNGOS+UDB+ScriptDev2 y obtener un servidor WoW decente para ejecutarlo en mi máquina local.
Inicialmente, pasé horas tratando de leer y comprender los tutoriales de diferentes personas escritos en diferentes sitios web, pero finalmente lo logré. AzerothCore es un proyecto todo en uno, por lo que va a ser más fácil que eso, ¡tenga paciencia conmigo y lo logrará!*

¿Tentado a usar un repack en su lugar? [No lo hagas](https://www.mangosrumors.org/why-you-should-not-use-repacks-to-run-your-wow-server/).

## Instalación de AzerothCore en su computadora

El primer paso siempre es instalar un servidor WoW local en tu propia máquina. Y hay varias formas de hacerlo, que pueden variar según el sistema operativo.

### Tu sistema operativo

Permítanme ser claro sobre una cosa: **TODOS los sistemas operativos son compatibles con AzerothCore**.
Por lo tanto, puede instalar correctamente AzerothCore GNU/Linux, macOS o Windows sin ningún problema.

Sin embargo, puedo decirle que si usa una distribución de Linux como **Ubuntu 20.04**, el proceso será más fácil. Si desea instalar Ubuntu, puede descargarlo desde [aquí] (https://ubuntu.com/download/desktop) y puede encontrar muchos tutoriales en línea sobre cómo hacerlo. Hay un buen tutorial sobre cómo ejecutar WoW en Linux [aquí] (https://www.mangosrumors.org/how-to-run-wow-on-linux/).

¿Te gustaría quedarte con **Windows** o **macOS**? Eso está absolutamente bien.

![AzerothCore supports GNU/Linux, macOS and Windows](https://user-images.githubusercontent.com/75517/109369213-e5775880-789b-11eb-8356-99a4ab842bfb.png)

### Diferentes formas de instalar AzerothCore

Básicamente, hay 3 formas principales de instalar AC:

- La "**configuración clásica**": esta es la configuración tradicional que normalmente usarías para instalar un emulador común de WoW. **Todos los sistemas operativos son compatibles.** Hacer esta configuración probablemente también le brinde una mejor visión general de los componentes del servidor.
- La "**configuración de Docker**": esta es una configuración simplificada que usa Docker para automatizar muchas cosas para usted. Esta configuración suele ser más fácil. **Puede usar esta configuración en todos los sistemas operativos donde puede instalar [Docker](https://www.docker.com/products/docker-desktop).**
- La "**configuración del tablero**": esta es una forma **EXTREMADAMENTE FÁCIL** de instalar AzerothCore en su máquina, basada en una colección de scripts bash creados por [Yehonal](https://github.com/Yehonal ). Sin embargo, **solo puede usar esta configuración en Ubuntu** o plataformas similares. Windows no es compatible, y probablemente todavía no estemos allí con macOS también.

Puede elegir una configuración o incluso probar más de una. Puedes encontrar todas las instrucciones aquí:

- [azerothcore.org/wiki/Installation](https://www.azerothcore.org/wiki/Installation)

Si encuentra algún problema o duda al intentar instalar su servidor AC, [pídanos ayuda](https://github.com/azerothcore/wiki/blob/master/docs/how-to-ask-for-help.md).

¿Tienes tu servidor WoW instalado? ¡Felicidades! Ahora veamos qué puedes hacer a continuación.

![AzerothCore server running on macOS](https://user-images.githubusercontent.com/75517/109369101-80236780-789b-11eb-900c-bcc17a3cf13c.png)

## Accede al juego, aprende los comandos de GM

En primer lugar, `establezca realmlist localhost` y únase a su propio servidor usando la cuenta `test1` con la contraseña `a` (sí, contraseña de una letra). Esta cuenta ya es `GM` por lo que puede usar los comandos de esta lista:

- [azerothcore.org/wiki/GM-Commands](https://www.azerothcore.org/wiki/GM-Commands)

Confíe en los comandos, los necesitará para cualquier actividad de administración, prueba o desarrollo.

![AzerothCore GM](https://user-images.githubusercontent.com/75517/109369940-ba423880-789e-11eb-88d6-e6d8f7b8a723.png)

## Considere aprender git

Puede simplemente copiar y pegar a ciegas los comandos `git` que verá en los tutoriales vinculados aquí, lo más probable es que no tenga problemas con ellos.
Sin embargo, aprender correctamente `git` te hará realmente consciente de lo que estás haciendo, y este conocimiento puede ayudarte con cualquier otro proyecto de desarrollo de software con el que puedas trabajar.
Sí, porque `git` es una de las herramientas más importantes utilizadas en muchos proyectos de ingeniería de software. Aprender sus conceptos básicos no solo te ayudará mucho con AzerothCore, sino que también es algo muy bueno para poner en tu CV.

Puede encontrar muchos recursos en línea sobre cómo aprender `git`, por ejemplo [try.github.io](https://try.github.io/)

![AzerothCore learning git](https://user-images.githubusercontent.com/75517/109370018-fb3a4d00-789e-11eb-8532-1ab1bf8fba60.png)

## Aprende a actualizar tu servidor de WoW

Publicamos mejoras en AzerothCore a diario. Debe aprender a actualizar su servidor y seguir actualizándolo con frecuencia. Recomendamos evitar trabajar en versiones anteriores de AzerothCore porque pueden tener errores que ya resolvimos y no querrás quedarte atrás.

Por lo tanto, es **muy importante** que actualice su servidor AzerothCore periódicamente. Te recomendamos hacerlo al menos una vez a la semana. Lea esta guía:

- [azerothcore.org/wiki/Update](https://www.azerothcore.org/wiki/Update)

Después de seguir el procedimiento de actualización, es importante **verificar** que:

- La aplicación de su servidor (núcleo) se ha actualizado correctamente, utilice el comando `información del servidor` para asegurarse de ello.
- Su base de datos se actualizó correctamente y se alineó con su versión principal, [lea esta respuesta en stackoverflow] (https://stackoverflow.com/a/55282168/3497671).

![AzerothCore server info](https://user-images.githubusercontent.com/75517/109370296-00e46280-78a0-11eb-9ed0-b9df14f2008b.png)

## Aprende a revisar las relaciones públicas

Una excelente manera de comenzar a contribuir es probando las relaciones públicas realizadas por otros colaboradores. Esto no solo es bastante fácil de hacer, sino que es extremadamente útil para el proyecto y puede ayudarlo a ingresar a nuestro proceso de desarrollo.

Este tema es tan importante que hay un tutorial dedicado a él:

- [azerothcore.org/wiki/How-to-test-a-PR](https://www.azerothcore.org/wiki/How-to-test-a-PR)

![image](https://user-images.githubusercontent.com/75517/109370244-d397b480-789f-11eb-9ac7-64d98ca0d33c.png)

## Aprendiendo a trabajar con la base de datos

La base de datos es el mejor lugar para comenzar a desarrollar un servidor de WoW. Porque es más fácil que los otros componentes y hay herramientas que pueden generar automáticamente el código para usted. Por ejemplo, Keira3.

### Descargar Keira3

Keira3 es un editor de base de datos para AzerothCore que te permite editar o agregar contenidos al mundo muy fácilmente, te recomendamos instalarlo y jugar con él:

- [azerothcore.org/Keira3](https://www.azerothcore.org/Keira3)

Keira3 genera automáticamente el código SQL necesario para crear o cambiar cosas en la base de datos.
¿Suena complicado? Pruébalo y verás cómo funciona.

![AzerothCore Keira3](https://user-images.githubusercontent.com/75517/109370160-769bfe80-789f-11eb-9958-dc17ff48f39a.png)

### Descargar un cliente MySQL

También necesitará una herramienta de administración de base de datos genérica para administrar tablas y su contenido.

- [Herramienta de administración de base de datos](database-management-tool)

![Base de datos mundial de AzerothCore vista con sequel-ace](https://user-images.githubusercontent.com/75517/109370368-42750d80-78a0-11eb-946c-c0831a02b52b.png)

### La documentación de DB es tu amiga

Lea siempre la documentación de cada tabla con la que trabaje:

- [azerothcore.org/wiki/database-world](https://www.azerothcore.org/wiki/database-world)

### SmartAI

Con SmartAI puedes hacer muchas cosas. Puedes agregar un comportamiento especial a un elemento del juego, como una criatura, sin siquiera tocar una sola línea de C++.

En pocas palabras, con SmartAI puedes hacer que una entidad (por ejemplo, una Criatura) realice una determinada **acción** cuando ocurre un determinado **evento**, especificando opcionalmente un **objetivo**. En otras palabras, puede hacer que las entidades reaccionen a los eventos con un comportamiento definido por usted.

Por ejemplo, puedes hacer que una criatura lance un hechizo (acción), cuando su salud esté por debajo del 50 % de su salud total (evento), contra un miembro aleatorio del grupo del grupo (objetivo).

Técnicamente, `smart_script` es solo una tabla dentro de la base de datos mundial (y su documentación se puede encontrar [aquí](https://www.azerothcore.org/wiki/smart_scripts)). Herramientas como Keira3 te ayudan a trabajar con SmartAI mediante una práctica interfaz gráfica.

Intenta abrir Keira3, busca cualquier criatura que tenga "SmartAI" como "AIName", ábrelo y haz clic en "SmartAI" en el menú de la derecha.
Aparecerá un editor visual que lo ayudará cuando trabaje con SmartAI.

![AzerothCore SmartAI con Keira3](https://user-images.githubusercontent.com/75517/109367698-1bfea480-7897-11eb-9cf0-f047b3dcdb85.png)

Experimente con SmartAI y confíe en él. Es una herramienta simple pero muy poderosa.
Después de conocerlo un poco, podrás hacer muchas cosas. Muchos errores se pueden corregir simplemente usando SmartAI.

La IA de la mayoría de las criaturas que encontrarás en el mundo se realiza con SmartAI. Mientras que las criaturas más complejas (típicamente jefes de raid) están escritas en C++.

![SmartAI frente a C++](https://user-images.githubusercontent.com/75517/109369529-e78de700-789c-11eb-97d5-02ecc6c85a0a.png)

### Aprenda el lenguaje SQL

Por lo general, solo necesitará los conceptos básicos del lenguaje SQL y, en la mayoría de los casos, probablemente lo resolverá por sí mismo; sin embargo, no es una mala idea leer sobre el lenguaje SQL. Puede encontrar muchos recursos en línea, por ejemplo:

- [https://www.w3schools.com/sql/sql_intro.asp](https://www.w3schools.com/sql/sql_intro.asp)

si comprende cómo funcionan las declaraciones básicas como `SELECT`, `UPDATE`, `INSERT` y `DELETE`, eso suele ser suficiente. No necesita profundizar demasiado en SQL para poder contribuir.

## ¡Comparte tu código!

Puede enviar su mejora a través de PR. Lea esta guía:

- [Cómo crear una Pull Request (PR)](https://www.azerothcore.org/wiki/how-to-create-a-pr)

## ¡Empieza a contribuir!

Si dominaste algunas de las partes anteriores, ya hay **MUCHO** que puedes hacer para ayudar a nuestro proyecto y convertirte en colaborador.
Por ejemplo:

- Ayude a los desarrolladores probando PRs y dando su opinión
- Realice una clasificación de errores confirmando problemas y ayudándonos a identificar y cerrar los informes no válidos
- También puede ayudar [clasificando los errores que provienen de los jugadores de ChromieCraft] (https://github.com/chromiecraft/chromiecraft) (nuestro proyecto secundario)
- Informe de cualquier error que pueda encontrar usted mismo
- Intente corregir errores, muchos de ellos pueden corregirse con algo de SQL y puede usar Keira3 para eso (por ejemplo, usando SmartAI u otros editores integrados). Siendo este un proyecto de código abierto, puede encontrar muchos ejemplos en nuestro repositorio principal de GitHub

¿Te gustaría hablar con nosotros? Únase al [servidor AzerothCore Discord](https://discordapp.com/invite/gkt4y2x).

![Contribuyendo a AzerothCore](https://user-images.githubusercontent.com/75517/109370461-b44d5700-78a0-11eb-916c-81c8500fa969.png)

## Conclusión y próximos pasos

Nunca dejes de aprender. Vaya a aprender los conceptos básicos detrás de la Programación Orientada a Objetos (POO).
Obtenga un tutorial de C++, comience a experimentar con el código fuente principal. Mira las PRs de otras personas como ejemplos.

Estudie los mecanismos básicos del servidor de juegos (lea artículos como [este](https://stackoverflow.com/questions/62249204/how-does-the-update-diff-work-in-azerothcore)). Intente [crear módulos](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore).

O aprenda otro lenguaje de programación, hay muchas herramientas que puede crear para los usuarios o desarrolladores de AzerothCore usando su lenguaje de programación favorito.

Hagas lo que hagas, recuerda siempre: **StackOverflow es tu amigo**.

-------------------------------------------------

En este tutorial, quería ayudar a los principiantes y demostrarles cuánto pueden aprender y contribuir sin siquiera saber C++. Todo lo que necesitas es algo de tiempo y paciencia.

¡Feliz codificación!

-- Shin aka Francesco
