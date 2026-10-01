---
tableofcontents: 1
---

# Preguntas frecuentes

Si tienes problemas para instalar o compilar AzerothCore, lee [Errores comunes](common-errors).

| ¿Estas preguntas frecuentes no respondieron a tus dudas? Lee [Cómo pedir ayuda](how-to-ask-for-help) sobre cómo proceder con tu pregunta de la mejor manera. |
| --- |

## Preguntas frecuentes generales

- ¿Qué sistemas operativos/plataformas son compatibles?
  - Actualmente son compatibles Windows, macOS, Linux y Docker.

- ¿Cuándo debo actualizar mi código fuente?
  - Recomendamos actualizar tu core con frecuencia, al menos una vez a la semana, para beneficiarte de las últimas correcciones del core y parches de seguridad.

- ¿Qué es "Blizzlike"?
  - AzerothCore intenta replicar el estado de Blizzard para World of Warcraft. El término "Blizzlike" significa que está lo suficientemente cerca de ser una réplica de lo que había en los servidores de Blizzard.

- ¿Por qué AzerothCore no imita bugs o exploits "blizzlike"?
  - Aunque nos esforzamos por ofrecer contenido blizzlike, también valoramos la experiencia del usuario. Esto significa que a veces corregimos bugs o exploits que existían en el juego original en su momento para ofrecer una mejor experiencia general a los jugadores.

- ¿Cómo puedo contribuir?
  - Puedes ayudar a corregir issues enviando Pull Requests, lee más [aquí](contribute).
  - Puedes ayudarnos probando nuestros [Pull Requests](contribute#how-to-test-a-pull-request) y participando en las [discusiones de los issues de github](https://github.com/azerothcore/azerothcore-wotlk/issues).
  - Puedes ayudar a mejorar la wiki enviando un [Pull Request](https://github.com/azerothcore/wiki).

- ¿Por qué no fusionáis mi corrección?
  - Todas las correcciones deben ser revisadas por un desarrollador. Los desarrolladores no lo saben todo, así que necesitas esperar hasta que alguien la revise.
  - Algunas correcciones requieren pruebas y no todos los desarrolladores pueden probar, así que necesitas esperar a que alguien más la pruebe.
  - Se fusionan eventualmente tras obtener la etiqueta To Be Merged.
  - Quizás no estés siguiendo los [estándares SQL/C++](standard-operating-procedure).
  - Lee más en [Merge Process](merge-process).

- ¿Cómo reporto un crash?
  - Pegando tu crashlog en un PasteBin o Gist.
  - El crashlog **debe provenir de una compilación RelWithDebInfo o Debug**. Si es de Release, es inútil.
  - [Cómo reiniciar y depurar](how-to-restart-and-debug).

- ¿Soportáis Repacks basados en AzerothCore?
  - No. Los Repacks NO están soportados y recomendamos encarecidamente no usarlos por [varias razones](https://www.mangosrumors.org/why-you-should-not-use-repacks-to-run-your-wow-server/). Puedes consultar [este tutorial](https://www.chromiecraft.com/how-to-install-a-wow-server-on-your-own-computer/) para una forma sencilla de instalar AC sin usar ningún repack.

## Preguntas frecuentes sobre la base de datos

- ¿Con qué frecuencia actualizáis la base de datos?
  - La base de datos se actualiza casi todos los días.

- ¿Cómo actualizo la base de datos?
  - Puedes encontrar todo lo que necesitas para mantener la base de datos actualizada en esta guía sobre [Base de datos: mantener el servidor actualizado](database-keeping-the-server-up-to-date).

## Preguntas frecuentes sobre el core

- ¿Cuándo será estable el código fuente?
  - Pronto...™
  - Hacemos nuestro mejor esfuerzo para mantener la rama master estable y jugable. Nunca subimos código directamente a la rama master, sino que primero requerimos que todos (incluidos los administradores y el staff de AC) abran un PR para que todos puedan revisarlo antes de que se fusione en master.
  - Por favor, ayúdanos [probando PRs](how-to-test-a-pr) y reportando cualquier bug que encuentres.

- No puedo ejecutar los extractores en plataformas Windows, ¿simplemente desaparece cuando hago click en él?
  - Ten en cuenta que es una herramienta de **línea de comandos**, no una herramienta con GUI. Esto significa que necesitas usar la línea de comandos en Windows (por ejemplo, "Símbolo del sistema") en lugar de hacer doble click en ella.

- ¿Por qué no puedo ejecutar mis extractores MAP/DBC más antiguos?
  - Se actualizan por una razón, y te darán errores cuando inicies el Worldserver si no extraes con la última versión.
  - Siempre obtendrás la última versión si compilas con "TOOLS".

- ¿Qué son los Maps, VMaps, MMaps y DBCs?
  {% include note.html content="¡AzerothCore no da soporte ni aprueba ninguna forma de modificación de los archivos del cliente ni de servidores privados/públicos! AzerothCore en sí mismo está pensado para el theory-crafting y el aprendizaje." %}
  - Además del core como binarios que dan las funciones, definiciones y comandos fundamentales e individuales de interpretación del cliente, el core puede describirse como 'un cuerpo' con los siguientes datos que forman su 'anatomía':
    - **Maps**: Los Maps son **necesarios para ejecutar AzerothCore**. Los Maps proporcionan los valores físicos y los datos para que el core los interprete. En base a ellos, el core tiene un diseño que puede compararse con cada cliente. Esto incluye las definiciones de área.
    - **VMaps**: Los VMaps son **opcionales, pero muy recomendados**. Los VMaps ("Virtual Maps") calculan la posibilidad de línea de visión, por ejemplo. Según su contenido, el servidor puede (por ejemplo) calcular si es posible lanzar hechizos (p. ej. si hay una pared entre el objetivo y el lanzador o no).
    - **MMaps**: Los MMaps son **opcionales, pero muy recomendados**. Para reforzar los límites físicos, los MMaps ("Movement Maps") imponen límites físicos a los personajes no jugadores, p. ej. NPCs, ya que su colisión no la maneja el cliente. También mejoran la generación de rutas.
    - **DBC**: Los DBCs son **necesarios para ejecutar AzerothCore**. Los DBCs ("Data Base Client [Files]") dan valores esenciales que el cliente de World of Warcraft interpreta. Definen razas, texturas, modelos locales y más. AzerothCore los interpreta y los carga.
  - Compilar AzerothCore con "TOOLS" siempre creará las herramientas necesarias para extraer y crear estos archivos.

- Tengo problemas al extraer los Maps, VMaps, MMaps, DBCs (y he intentado usar versiones anteriores de los extractores). ¿Qué ocurre?
  - Las herramientas más antiguas están obsoletas y no funcionarán.
  - Necesitas usar una línea de comandos para poder ejecutar las herramientas.

- Me faltan las librerías de MySQL y no parece que pueda encontrarlas en el repositorio, ¿qué ocurre?
  - La librería se llama "mysql.lib" y no la proporciona AzerothCore.
  - Asegúrate de haber instalado tu MySQL-Server con los DEVELOPMENT HEADERS.
  - Puedes seguir la guía de [Instalación del Core](core-installation) para encontrar las librerías.

- Me faltan las librerías de OpenSSL y no parece que pueda encontrarlas en el repositorio, ¿qué ocurre?
  - Necesitas las siguientes dll:
    - legacy.dll
    - libcrypto-3-x64.dll
    - libssl-3-x64.dll
  - Puedes seguir la guía de [Instalación del Core](core-installation) para encontrar las librerías.

## Preguntas frecuentes sobre depuración

- ¿Cómo puedo obtener un buen crashlog en Windows?
  - Compila tu core en RelWithDebInfo o Debug. Un crashlog de Release será inútil.
  - Puedes depurarlo tú mismo si [ejecutas worldserver y authserver en Visual Studio](run-worldserver-and-authserver-in-visual-studio).

## Preguntas frecuentes sobre módulos

- Necesito un nuevo hook para mi módulo personalizado, ¿qué puedo hacer?
  - Puedes añadir el hook a tu propio fork (cf: [crear un nuevo hook](hooks-script)) y crear un nuevo Pull Request al repositorio oficial para que podamos validarlo y fusionarlo.

- ¿Es posible convertir un parche del core en un módulo?
  - Sí. [Is it possible to turn a core patch into a module for AzerothCore? - StackOverflow](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore/66340683#66340683).

## Preguntas frecuentes sobre funcionalidades

- ¿Qué instancias/arenas/campos de batalla funcionan?
  - La mayoría funcionan perfectamente, algunos funcionan peor.
  - Siempre se está trabajando en el Core; los datos más precisos vendrán de que los pruebes tú mismo.

- ¿Funciona Warden?
  - Sí funciona, pero no con un 100% de tasa de éxito. Warden no detecta todos los hacks, ni siquiera en Retail.

- ¿Cómo cierro una instancia o campo de batalla? ¿Cómo puedo desactivar un hechizo?
  - Todas las desactivaciones se manejan en la [tabla disables](disables).

| ¿Estas preguntas frecuentes no respondieron a tus dudas? Lee [Cómo pedir ayuda](how-to-ask-for-help) sobre cómo proceder con tu pregunta de la mejor manera. |
| --- |
