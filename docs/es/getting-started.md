# Primeros pasos con AzerothCore

## Introducci�n

�Le gustar�a aprender sobre AzerothCore (AC), configurar su servidor de WoW por primera vez, entender c�mo modificarlo y poder contribuir? �Usted vino al lugar correcto!

Comenzar con la emulaci�n de WoW puede ser complicado al principio, pero no se preocupe, estaremos all� para ayudarlo en caso de que tenga alg�n problema o tenga alguna pregunta que hacer. Solo lea [esta p�gina](https://www.azerothcore.org/wiki/How-to-ask-for-help) antes de pedir ayuda.

Si mientras lees alguno de los tutoriales enlazados en esta p�gina encuentras algo que no te queda claro: h�znoslo saber. Haremos todo lo posible para reformularlo y hacerlo m�s f�cil de entender para los principiantes. �Mejorar los documentos tambi�n es una forma de contribuir!

![AzerothCore learning code](https://user-images.githubusercontent.com/75517/109369720-b6fa7d00-789d-11eb-86b4-5fe15d6ab834.png)


## Requisitos de conocimientos

Esto **NO** reqiere requisitos t�cnicos. Solo necesitas ser paciente y estar dispuesto a aprender.

Si ya tienes algunos conocimientos de programaci�n seguro que ser�a una ventaja para ti. Sin embargo, cr�ame, no necesita ning�n conocimiento previo para aprender sobre los servidores de WoW.

*Nota personal del autor de este tutorial: cuando instal� por primera vez mi primer servidor de WoW ten�a 15 a�os, no ten�a ning�n conocimiento de programaci�n, usaba Windows XP y apenas entend�a ingl�s. Estoy seguro de que si est� leyendo esto, ya tiene m�s habilidades que las que ten�a cuando intentaba instalar MaNGOS+UDB+ScriptDev2 y obtener un servidor WoW decente para ejecutarlo en mi m�quina local.
Inicialmente, pas� horas tratando de leer y comprender los tutoriales de diferentes personas escritos en diferentes sitios web, pero finalmente lo logr�. AzerothCore es un proyecto todo en uno, por lo que va a ser m�s f�cil que eso, �tenga paciencia conmigo y lo lograr�!*

�Tentado a usar un repack en su lugar? [No lo hagas](https://www.mangosrumors.org/why-you-should-not-use-repacks-to-run-your-wow-server/).

## Instalaci�n de AzerothCore en su computadora

El primer paso siempre es instalar un servidor WoW local en tu propia m�quina. Y hay varias formas de hacerlo, que pueden variar seg�n el sistema operativo.

### Tu sistema operativo

Perm�tanme ser claro sobre una cosa: **TODOS los sistemas operativos son compatibles con AzerothCore**.
Por lo tanto, puede instalar correctamente AzerothCore GNU/Linux, macOS o Windows sin ning�n problema.

Sin embargo, puedo decirle que si usa una distribuci�n de Linux como **Ubuntu 20.04**, el proceso ser� m�s f�cil. Si desea instalar Ubuntu, puede descargarlo desde [aqu�] (https://ubuntu.com/download/desktop) y puede encontrar muchos tutoriales en l�nea sobre c�mo hacerlo. Hay un buen tutorial sobre c�mo ejecutar WoW en Linux [aqu�] (https://www.mangosrumors.org/how-to-run-wow-on-linux/).

�Te gustar�a quedarte con **Windows** o **macOS**? Eso est� absolutamente bien.

![AzerothCore supports GNU/Linux, macOS and Windows](https://user-images.githubusercontent.com/75517/109369213-e5775880-789b-11eb-8356-99a4ab842bfb.png)

### Diferentes formas de instalar AzerothCore

B�sicamente, hay 3 formas principales de instalar AC:

- La "**configuraci�n cl�sica**": esta es la configuraci�n tradicional que normalmente usar�as para instalar un emulador com�n de WoW. **Todos los sistemas operativos son compatibles.** Hacer esta configuraci�n probablemente tambi�n le brinde una mejor visi�n general de los componentes del servidor.
- La "**configuraci�n de Docker**": esta es una configuraci�n simplificada que usa Docker para automatizar muchas cosas para usted. Esta configuraci�n suele ser m�s f�cil. **Puede usar esta configuraci�n en todos los sistemas operativos donde puede instalar [Docker](https://www.docker.com/products/docker-desktop).**
- La "**configuraci�n del tablero**": esta es una forma **EXTREMADAMENTE F�CIL** de instalar AzerothCore en su m�quina, basada en una colecci�n de scripts bash creados por [Yehonal](https://github.com/Yehonal ). Sin embargo, **solo puede usar esta configuraci�n en Ubuntu** o plataformas similares. Windows no es compatible, y probablemente todav�a no estemos all� con macOS tambi�n.

Puede elegir una configuraci�n o incluso probar m�s de una. Puedes encontrar todas las instrucciones aqu�:

- [azerothcore.org/wiki/Installation](https://www.azerothcore.org/wiki/Installation)

Si encuentra alg�n problema o duda al intentar instalar su servidor AC, [p�danos ayuda](https://github.com/azerothcore/wiki/blob/master/docs/how-to-ask-for-help.md).

�Tienes tu servidor WoW instalado? �Felicidades! Ahora veamos qu� puedes hacer a continuaci�n.

![AzerothCore server running on macOS](https://user-images.githubusercontent.com/75517/109369101-80236780-789b-11eb-900c-bcc17a3cf13c.png)

## Accede al juego, aprende los comandos de GM

En primer lugar, `establezca realmlist localhost` y �nase a su propio servidor usando la cuenta `test1` con la contrase�a `a` (s�, contrase�a de una letra). Esta cuenta ya es `GM` por lo que puede usar los comandos de esta lista:

- [azerothcore.org/wiki/GM-Commands](https://www.azerothcore.org/wiki/GM-Commands)

Conf�e en los comandos, los necesitar� para cualquier actividad de administraci�n, prueba o desarrollo.

![AzerothCore GM](https://user-images.githubusercontent.com/75517/109369940-ba423880-789e-11eb-88d6-e6d8f7b8a723.png)

## Considere aprender git

Puede simplemente copiar y pegar a ciegas los comandos `git` que ver� en los tutoriales vinculados aqu�, lo m�s probable es que no tenga problemas con ellos.
Sin embargo, aprender correctamente `git` te har� realmente consciente de lo que est�s haciendo, y este conocimiento puede ayudarte con cualquier otro proyecto de desarrollo de software con el que puedas trabajar.
S�, porque `git` es una de las herramientas m�s importantes utilizadas en muchos proyectos de ingenier�a de software. Aprender sus conceptos b�sicos no solo te ayudar� mucho con AzerothCore, sino que tambi�n es algo muy bueno para poner en tu CV.

Puede encontrar muchos recursos en l�nea sobre c�mo aprender `git`, por ejemplo [try.github.io](https://try.github.io/)

![AzerothCore learning git](https://user-images.githubusercontent.com/75517/109370018-fb3a4d00-789e-11eb-8532-1ab1bf8fba60.png)

## Aprende a actualizar tu servidor de WoW

Publicamos mejoras en AzerothCore a diario. Debe aprender a actualizar su servidor y seguir actualiz�ndolo con frecuencia. Recomendamos evitar trabajar en versiones anteriores de AzerothCore porque pueden tener errores que ya resolvimos y no querr�s quedarte atr�s.

Por lo tanto, es **muy importante** que actualice su servidor AzerothCore peri�dicamente. Te recomendamos hacerlo al menos una vez a la semana. Lea esta gu�a:

- [azerothcore.org/wiki/Update](https://www.azerothcore.org/wiki/Update)

Despu�s de seguir el procedimiento de actualizaci�n, es importante **verificar** que:

- La aplicaci�n de su servidor (n�cleo) se ha actualizado correctamente, utilice el comando `informaci�n del servidor` para asegurarse de ello.
- Su base de datos se actualiz� correctamente y se aline� con su versi�n principal, [lea esta respuesta en stackoverflow] (https://stackoverflow.com/a/55282168/3497671).

![AzerothCore server info](https://user-images.githubusercontent.com/75517/109370296-00e46280-78a0-11eb-9ed0-b9df14f2008b.png)

## Aprende a revisar las relaciones p�blicas

Una excelente manera de comenzar a contribuir es probando las relaciones p�blicas realizadas por otros colaboradores. Esto no solo es bastante f�cil de hacer, sino que es extremadamente �til para el proyecto y puede ayudarlo a ingresar a nuestro proceso de desarrollo.

Este tema es tan importante que hay un tutorial dedicado a �l:

- [azerothcore.org/wiki/How-to-test-a-PR](https://www.azerothcore.org/wiki/How-to-test-a-PR)

![image](https://user-images.githubusercontent.com/75517/109370244-d397b480-789f-11eb-9ac7-64d98ca0d33c.png)

## Aprendiendo a trabajar con la base de datos

La base de datos es el mejor lugar para comenzar a desarrollar un servidor de WoW. Porque es m�s f�cil que los otros componentes y hay herramientas que pueden generar autom�ticamente el c�digo para usted. Por ejemplo, Keira3.

### Descargar Keira3

Keira3 es un editor de base de datos para AzerothCore que te permite editar o agregar contenidos al mundo muy f�cilmente, te recomendamos instalarlo y jugar con �l:

- [azerothcore.org/Keira3](https://www.azerothcore.org/Keira3)

Keira3 genera autom�ticamente el c�digo SQL necesario para crear o cambiar cosas en la base de datos.
�Suena complicado? Pru�balo y ver�s c�mo funciona.

![AzerothCore Keira3](https://user-images.githubusercontent.com/75517/109370160-769bfe80-789f-11eb-9958-dc17ff48f39a.png)

### Descargar un cliente MySQL

Tambi�n necesitar� una herramienta de administraci�n de base de datos gen�rica para administrar tablas y su contenido.

- [Herramienta de administraci�n de base de datos](database-management-tool)

![Base de datos mundial de AzerothCore vista con sequel-ace](https://user-images.githubusercontent.com/75517/109370368-42750d80-78a0-11eb-946c-c0831a02b52b.png)

### La documentaci�n de DB es tu amiga

Lea siempre la documentaci�n de cada tabla con la que trabaje:

- [azerothcore.org/wiki/database-world](https://www.azerothcore.org/wiki/database-world)

### SmartAI

Con SmartAI puedes hacer muchas cosas. Puedes agregar un comportamiento especial a un elemento del juego, como una criatura, sin siquiera tocar una sola l�nea de C++.

En pocas palabras, con SmartAI puedes hacer que una entidad (por ejemplo, una Criatura) realice una determinada **acci�n** cuando ocurre un determinado **evento**, especificando opcionalmente un **objetivo**. En otras palabras, puede hacer que las entidades reaccionen a los eventos con un comportamiento definido por usted.

Por ejemplo, puedes hacer que una criatura lance un hechizo (acci�n), cuando su salud est� por debajo del 50 % de su salud total (evento), contra un miembro aleatorio del grupo del grupo (objetivo).

T�cnicamente, `smart_script` es solo una tabla dentro de la base de datos mundial (y su documentaci�n se puede encontrar [aqu�](https://www.azerothcore.org/wiki/smart_scripts)). Herramientas como Keira3 te ayudan a trabajar con SmartAI mediante una pr�ctica interfaz gr�fica.

Intenta abrir Keira3, busca cualquier criatura que tenga "SmartAI" como "AIName", �brelo y haz clic en "SmartAI" en el men� de la derecha.
Aparecer� un editor visual que lo ayudar� cuando trabaje con SmartAI.

![AzerothCore SmartAI con Keira3](https://user-images.githubusercontent.com/75517/109367698-1bfea480-7897-11eb-9cf0-f047b3dcdb85.png)

Experimente con SmartAI y conf�e en �l. Es una herramienta simple pero muy poderosa.
Despu�s de conocerlo un poco, podr�s hacer muchas cosas. Muchos errores se pueden corregir simplemente usando SmartAI.

La IA de la mayor�a de las criaturas que encontrar�s en el mundo se realiza con SmartAI. Mientras que las criaturas m�s complejas (t�picamente jefes de raid) est�n escritas en C++.

![SmartAI frente a C++](https://user-images.githubusercontent.com/75517/109369529-e78de700-789c-11eb-97d5-02ecc6c85a0a.png)

### Aprenda el lenguaje SQL

Por lo general, solo necesitar� los conceptos b�sicos del lenguaje SQL y, en la mayor�a de los casos, probablemente lo resolver� por s� mismo; sin embargo, no es una mala idea leer sobre el lenguaje SQL. Puede encontrar muchos recursos en l�nea, por ejemplo:

- [https://www.w3schools.com/sql/sql_intro.asp](https://www.w3schools.com/sql/sql_intro.asp)

si comprende c�mo funcionan las declaraciones b�sicas como `SELECT`, `UPDATE`, `INSERT` y `DELETE`, eso suele ser suficiente. No necesita profundizar demasiado en SQL para poder contribuir.

## �Comparte tu c�digo!

Puede enviar su mejora a trav�s de PR. Lea esta gu�a:

- [C�mo crear una Pull Request (PR)](https://www.azerothcore.org/wiki/how-to-create-a-pr)

## �Empieza a contribuir!

Si dominaste algunas de las partes anteriores, ya hay **MUCHO** que puedes hacer para ayudar a nuestro proyecto y convertirte en colaborador.
Por ejemplo:

- Ayude a los desarrolladores probando PRs y dando su opini�n
- Realice una clasificaci�n de errores confirmando problemas y ayud�ndonos a identificar y cerrar los informes no v�lidos
- Tambi�n puede ayudar [clasificando los errores que provienen de los jugadores de ChromieCraft] (https://github.com/chromiecraft/chromiecraft) (nuestro proyecto secundario)
- Informe de cualquier error que pueda encontrar usted mismo
- Intente corregir errores, muchos de ellos pueden corregirse con algo de SQL y puede usar Keira3 para eso (por ejemplo, usando SmartAI u otros editores integrados). Siendo este un proyecto de c�digo abierto, puede encontrar muchos ejemplos en nuestro repositorio principal de GitHub

�Te gustar�a hablar con nosotros? �nase al [servidor AzerothCore Discord](https://discordapp.com/invite/gkt4y2x).

![Contribuyendo a AzerothCore](https://user-images.githubusercontent.com/75517/109370461-b44d5700-78a0-11eb-916c-81c8500fa969.png)

## Conclusi�n y pr�ximos pasos

Nunca dejes de aprender. Vaya a aprender los conceptos b�sicos detr�s de la Programaci�n Orientada a Objetos (POO).
Obtenga un tutorial de C++, comience a experimentar con el c�digo fuente principal. Mira las PRs de otras personas como ejemplos.

Estudie los mecanismos b�sicos del servidor de juegos (lea art�culos como [este](https://stackoverflow.com/questions/62249204/how-does-the-update-diff-work-in-azerothcore)). Intente [crear m�dulos](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore).

O aprenda otro lenguaje de programaci�n, hay muchas herramientas que puede crear para los usuarios o desarrolladores de AzerothCore usando su lenguaje de programaci�n favorito.

Hagas lo que hagas, recuerda siempre: **StackOverflow es tu amigo**.

-------------------------------------------------

En este tutorial, quer�a ayudar a los principiantes y demostrarles cu�nto pueden aprender y contribuir sin siquiera saber C++. Todo lo que necesitas es algo de tiempo y paciencia.

�Feliz codificaci�n!

-- Shin aka Francesco
