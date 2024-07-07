# Preguntas frecuentes

Si tiene problemas para instalar o compilar AzerothCore, lea [Errores comunes](common-errors).

| ¿Estas preguntas frecuentes no respondieron a sus preguntas? Lea [Cómo pedir ayuda](how-to-ask-for-help) sobre cómo proceder con su pregunta de la mejor manera. |
| --- |

## Preguntas frecuentes generales

- ¿Qué sistemas operativos o plataformas son compatibles?
  - Actualmente, se admiten Windows, macOS, Linux y Docker.

- ¿Cuándo debo actualizar mi fuente?
  - Recomendamos actualizar su núcleo con frecuencia, al menos una vez a la semana, para beneficiarse de las últimas correcciones de núcleo y parches de seguridad.

- ¿Cuánta RAM necesito para AzerothCore?
  - Puede encontrar toda la información de RAM [aquí](memory-usage).

- ¿Qué es "Blizzlike"?
  - AzerothCore está intentando replicar el estado de Blizzard para World of Warcraft. El término "Blizzlike" significa que está lo suficientemente cerca de ser una réplica de lo que había en los servidores de Blizzard.

- ¿Por qué AzerothCore no imita errores o exploits parecidos a una "Blizzlike"?
  - Aunque nos esforzamos por ofrecer contenido similar a una Blizzlike, también valoramos la experiencia del usuario. Esto significa que a veces corregimos errores o vulnerabilidades que existían durante la venta minorista en ese momento para brindar una mejor experiencia general a los jugadores.

- ¿Cómo puedo contribuir?
  - Puede ayudar a solucionar problemas enviando solicitudes de extracción, lea más [aquí](contribute).
  - Puede ayudarnos probando nuestras [Solicitudes de extracción](contribute#how-to-test-a-pull-request) y participando en las [discusiones sobre problemas de github](https://github.com/azerothcore/azerothcore-wotlk/issues).
  - Puede ayudar a mejorar la wiki enviando una [Solicitud de extracción](https://github.com/azerothcore/wiki).

- ¿Por qué no fusionas mi solución?
  - Todas las correcciones deben ser revisadas por un desarrollador. Todos los desarrolladores no lo saben todo, por lo que debe esperar hasta que alguien lo revise.
  - Algunas correcciones requieren pruebas y no todos los desarrolladores pueden probarlas, por lo que debe esperar a que alguien más las pruebe.
  - Se fusionan eventualmente después de obtener la etiqueta To Be Merged.
  - Quizás no esté siguiendo los [estándares SQL/C++](standard-operating-procedure).
  - Leer más en [Merge Process](merge-process).

- ¿Cómo informo de un accidente?
  - Pegando su registro de fallos en un PasteBin o Gist.
  - El registro de fallos **debe provenir de una compilación RelWithDebInfo o Debug**. Si es de Release, es inútil.
  - [Cómo reiniciar y depurar](how-to-restart-and-debug).

- ¿Soportan Repacks basados ​​en AzerothCore?
  - No. NO se admiten reempaquetamientos y recomendamos encarecidamente no utilizarlos por [varias razones](https://www.mangosrumors.org/why-you-should-not-use-repacks-to-run-your-wow-server/). Puede consultar [este tutorial](https://www.chromiecraft.com/how-to-install-a-wow-server-on-your-own-computer/) para obtener una forma sencilla de instalar AC sin necesidad de volver a empaquetar.


## Preguntas frecuentes relacionadas con la base de datos

- ¿Con qué frecuencia actualiza la base de datos?
  - La base de datos se actualiza casi todos los días.

- ¿Cómo actualizo la base de datos?
  - Puede encontrar todo lo que necesita para mantener la base de datos actualizada en esta guía sobre [Base de datos que mantiene el servidor actualizado](database-keeping-the-server-up-to-date).

## Preguntas frecuentes relacionadas con el núcleo

- ¿Cuándo se estabilizará la fuente?
  - Pronto...™
  - Hacemos nuestro mejor esfuerzo para mantener la rama maestra estable y jugable. Nunca enviamos el código directamente a la rama maestra, sino que primero requerimos que todos (incluidos los administradores de CA y el personal) primero abran un PR para que todos puedan verificarlos antes de que se fusionen con el maestro.
  - Por favor ayúdenos [probando PRs](how-to-test-a-pr) e informando cualquier error que pueda encontrar.

- ¿No puedo ejecutar los extractores en plataformas Windows, simplemente desaparece cuando hago clic en él?
  - Comprenda que es una herramienta de **línea de comandos**, no una herramienta GUI. Esto significa que debe utilizar la línea de comandos en Windows (por ejemplo, "Símbolo del sistema") en lugar de hacer doble clic en ella.


- ¿Por qué no puedo ejecutar mis extractores MAP / DBC más antiguos?
  - Se actualizan por una razón y le darán errores cuando inicie Worldserver si no extrae con la última versión.
  - Siempre obtendrá la última versión si compila con "TOOLS"

- ¿Qué son Maps, VMaps, MMaps y DBCs?
  - Tenga en cuenta que AzerothCore no admite ni aprueba ninguna forma de modificación en los archivos del cliente o en los servidores públicos o privados. AzerothCore en sí mismo está diseñado para la elaboración de teorías y el aprendizaje.**
  - Además del núcleo como binarios que dan una interpretación fundamental e individual al cliente, funciones, definiciones y comandos, el núcleo se puede describir como 'un cuerpo' con los siguientes datos que forman su 'anatomía':
    - **Maps**: Los Maps son **necesarios para ejecutar AzerothCore**. Los mapas proporcionan los valores físicos y los datos para que el núcleo los interprete. En base a estos, el núcleo tiene un diseño que se puede comparar con cada cliente. Esto incluye definiciones de área.
    - **VMaps**: Los VMaps son **opcionales, pero muy recomendables**. VMaps ("Mapas virtuales") calcula la posibilidad de línea de visión, como ejemplo. Según su contenido, el servidor puede (por ejemplo) calcular si es posible lanzar hechizos (por ejemplo, si hay una pared entre el objetivo y el lanzador o no).
    - **MMaps**: Los MMaps son ** opcionales, pero muy recomendables **. Para ampliar los límites físicos, los MMaps ("Mapas de movimiento") imponen límites físicos a los personajes que no son jugadores, p. Ej. NPC, ya que su colisión no es manejada por el cliente. También mejoran la generación de rutas.
    - **DBC**: Los DBC son **necesarios para ejecutar AzerothCore**. Los DBC ("Data Base Client [Archivos]") dan valores esenciales que interpreta el cliente de World of Warcraft. Definen razas, texturas, modelos locales y más. AzerothCore los interpreta y los carga.
  - Compilar AzerothCore con "TOOLS" siempre creará las herramientas necesarias para extraer y crear estos archivos.

- Tengo problemas para extraer mapas, VMaps, MMaps, DBC (y he intentado usar versiones anteriores de los extractores). ¿Qué ocurre?
  - Las herramientas más antiguas están obsoletas y no funcionarán.
  - Debe utilizar una línea de comandos para poder ejecutar las herramientas.

- ¿Me faltan las bibliotecas para MySQL y parece que no puedo encontrarlas en el repositorio?
  - La biblioteca se llama "mysql.lib" y no la proporciona AzerothCore.
  - Asegúrese de haber instalado su MySQL-Server con DEVELOPMENT HEADERS.
  - Puede seguir la guía [Instalación básica](core-installation) para encontrar las bibliotecas.

- ¿Me faltan las bibliotecas para OpenSSL y parece que no puedo encontrarlas en el repositorio?
  - Para las versiones de OpenSSL anteriores a 1.1.0, se denominarán "libeay32.dll" y "ssleay32.dll".
  - Para las versiones 1.1.0 y más recientes de OpenSSL se denominan:
    - Para instalaciones de 32 bits: "libssl-1_1.dll" y "libcrypto-1_1.dll".
    - Para instalaciones de 64 bits: "libssl-1_1-x64.dll" y "libcrypto-1_1-x64.dll".
  - Puede seguir la guía [Instalación básica](core-installation) para encontrar las bibliotecas.

## Preguntas frecuentes relacionadas con la depuración

- ¿Cómo puedo obtener un buen registro de fallos en Windows?
  - Compile su núcleo en RelWithDebInfo o Debug. Un registro de fallos de Release será inútil.
  - Puede depurarlo usted mismo si [Ejecuta worldserver y autherserver en Visual Studio](run-worldserver-and-authserver-in-visual-studio).

## Preguntas frecuentes relacionadas con el módulo

- Necesito un nuevo hook para mi módulo personalizado, ¿qué puedo hacer?
  - Puede agregar el gancho a su propia fork (cf: [crear un nuevo hook](hooks-script)) y crear una nueva solicitud de extracción al repositorio oficial para que podamos validarlo y fusionarlo.

- ¿Es posible convertir un parche central en un módulo?
  - Sí. [¿Es posible convertir un parche básico en un módulo para AzerothCore? - StackOverflow](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore/66340683#66340683).

## Preguntas frecuentes relacionadas con funciones

- ¿Qué instancias/arenas/campos de batalla están funcionando?
  - La mayoría de ellos funcionan perfectamente, algunos funcionan peor.
  - Siempre se trabaja en el Núcleo, los datos más precisos provendrán de que los pruebe usted mismo.

- ¿Funciona Warden?
  - Sí, pero no con una tasa de éxito del 100%. Warden no detecta todos los hacks, ni siquiera en Retail.

- ¿Cómo cierro una instancia o campo de batalla? ¿Cómo puedo desactivar un hechizo?
  - Todas las inhabilitaciones se manejan en la [tabla de inhabilitaciones](disables).

| ¿Estas preguntas frecuentes no respondieron a sus preguntas? Lea [Cómo pedir ayuda](how-to-ask-for-help) sobre cómo proceder con su pregunta de la mejor manera. |
| --- |
