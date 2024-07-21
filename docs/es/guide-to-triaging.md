# Guía de evaluación de errores

## Introducción

Esta guía pretende dar una visión general de la clasificación de errores para el proyecto AzerothCore. Cubrirá los objetivos, el proceso de evaluación de errores, un resumen de herramientas y fuentes, y otros enlaces útiles.

## Objetivos

- Nuestro objetivo es tomar un informe de error que ha sido enviado al rastreador de problemas de ChromieCraft, y decidir de manera oportuna, precisa y documentada si es un informe válido o no. Si lo es, lo remitimos al gestor de incidencias de AzerothCore con notas y documentación añadidas.

Entonces, ¿qué determina un informe de error válido? Un informe de error es válido si demuestra un comportamiento en AzerothCore que no coincide con el comportamiento de un servidor de `WoW de Blizzard` durante la época de `Wrath of the Lich King`. Algunas fechas para ayudar con esto:

- Wrath se lanzó con el parche 3.02 el 14 de octubre de 2008.
- El parche final de Wrath fue el 3.3.5a, publicado el 29 de junio de 2010.
- Wrath terminó con el lanzamiento de Cataclysm el 12 de octubre de 2010.

## Cómo hacer una evaluación de errores

### 1. Elige un tema

- Comienza por ir al rastreador de problemas de ChromieCraft [aquí](https://github.com/chromiecraft/chromiecraft/issues)
- Escoge una incidencia que esté etiquetada con la etiqueta naranja "Necesita tratamiento".

### 2. Comprobar si hay duplicados

- Una vez que hayas elegido un problema, empieza a buscar duplicados: los nombres de las misiones, los nombres de los personajes e incluso los GUIDs de los objetos individuales del juego pueden ser comprobados para asegurarte de que no han sido ya reportados. En un proyecto con una base de jugadores tan grande y creciente, muchos de los problemas reportados ya se han visto antes. Es posible que se hayan comprobado y se haya determinado que no son errores, o que se hayan corregido ya, en un parche que no se ha desplegado en CC (ChromieCraft). Además, encontrar otros problemas relacionados, aunque no sean duplicados, puede ayudar a entender mejor un problema.

### 3. Validar la cuestión

- Así que ahora que nos hemos asegurado de que se trata de un nuevo bug, hay que decidir si se trata de un comportamiento obviamente incorrecto, o si puede ser causado por un malentendido, una mala interpretación o la ignorancia del juego. Esto se suele hacer comprobando las fuentes que se indican a continuación para determinar si se trata realmente de un fallo. Algunos errores aparentes son comportamientos previstos, y otros informes están causados por cambios en el juego; por ejemplo, lo que era un comportamiento correcto en Vanilla puede ser incorrecto en Wrath debido a cambios de equilibrio (balance).

### 4. Intenta reproducirlo

- Si se trata de un problema genuino, intenta seguir las instrucciones del usuario para duplicarlo. Si el usuario no te ha dado suficiente información para reproducir el problema, siempre puedes pedirle que lo aclare y etiquetar la incidencia en el rastreador CC como "Esperando comentarios".
- Si no puedes hacer que el comportamiento se repita en tu propio servidor, ten en cuenta que un servidor de AC vanilla no siempre se comporta de la misma manera que el servidor de ChromieCraft. Hay numerosos mods y otras personalizaciones en CC que pueden tener efectos impredecibles, y como resultado se reportan con bastante frecuencia errores que no son reproducibles en un servidor de AC vanilla.

#### Errores con los mods de CC y la progresión

- Chromie cuenta con una serie de mods para la comodidad de los jugadores. Entre ellos están el CFBG, el mod de campo de batalla entre facciones, las mazmorras entre facciones, el mod de reinicio de duelos, las arenas de bajo nivel, etc. Los fallos con estos, aunque no son infrecuentes, no son directamente relevantes para el proyecto AC. Si has identificado un informe de error que se origina en un mod de CC, debería informarse en la propia página de problemas de GitHub de ese mod cuando sea posible. Puedes buscar en GitHub para encontrarla.
- En particular, si un problema tiene que ver con objetos que no deberían estar disponibles para un determinado rango de nivel (por ejemplo, vendedores que venden equipo de nivel 60 cuando el rango de contenido actual de CC es de 40-49), entonces se trata de un problema del sistema de progresión y puede ser reportado [aquí](https://github.com/azerothcore/progression-system)

#### Problemas del lado del cliente

- Ten en cuenta que el cliente Wow está lejos de ser perfecto, y las pantallas de la interfaz de usuario para cosas como la información sobre herramientas y las estadísticas de los personajes a veces pueden ser inexactas. Si este es el caso, primero comprueba que el usuario está ejecutando el cliente enUS, ya que el cliente enGB es bastante más propenso a este tipo de problemas. Si está ejecutando el cliente correcto, entonces intente verificar que el único problema es la pantalla y no el real. Por ejemplo, hay un problema conocido del cliente con algunos artículos de bajo nivel que se venden por lo que parece ser 0 cobre. Si realmente compruebas la venta, el artículo se vende por el precio correcto y se acredita al usuario con la cantidad correcta de dinero, pero no lo muestra. Este tipo de problemas, al ser del lado del cliente, no pueden ser solucionados por el proyecto AC.
- Un buen número de usuarios también ejecuta mods del lado del cliente que cambian los modelos, las texturas, etc. Además, casi nunca lo mencionan. Pero si ves un problema que parece ser un problema de gráficos del lado del cliente, es decir, este NPC se ve raro / tiene el modelo equivocado / es invisible, recuerda preguntar al reportero acerca de cualquier mods gráficos que puedan estar ejecutando.

### 5. Describa y documente el problema

- Si el fallo es real y válido, puedes añadir la descripción del reportero original si se le pasó algún detalle importante. Intenta dar información útil adicional, como los ID de la base de datos y los GUID de las creaciones, cuando describas los objetos y las criaturas.
- A menudo basta con señalar que el informe de error ha sido confirmado. Sin embargo, si quieres dejar las pruebas lo más claras posible, una captura de pantalla o un vídeo del comportamiento defectuoso suele ser una buena manera de hacerlo. Las capturas de pantalla de los registros de combate pueden ser especialmente útiles. Para el vídeo, he encontrado que OBS Studio (https://obsproject.com/download) es bueno para la captura de pantalla, y Shotcut (https://www.shotcut.org/) es un buen editor de vídeo para trabajar en los resultados. (Ayuda que ambos sean FOSS (Free and Open Source Software), y como proyecto FOSS nosotros mismos es bueno apoyar a otros).

### 6. Registrar cómo reproducirlo

- Muestra cómo se puede reproducir, preferiblemente utilizando comandos de GM. Así, en lugar de "aceptar la quest "Matar a diez Foozles"", di `.quest add 1234`. Los comandos `.go c XXXX` y `.go o XXXX` (para ir a las criaturas y a los objetos respectivamente) serán útiles aquí ya que te permiten teletransportarte directamente a lo que sea el problema. El comando `.additem [itemname]` también puede ser útil.
- Ten en cuenta que cuando se haga un pull request para arreglar este problema, tanto el solucionador como el probador del PR se basarán en la información que proporciones aquí para facilitarles la vida.

### 7. Copiar en el rastreador AC con un enlace a CC

- Ahora que has establecido que se trata de un error válido, puedes trasladarlo al gestor de incidencias de AzerothCore. Esto se hace creando una nueva incidencia en blanco aquí: https://github.com/azerothcore/azerothcore-wotlk/issues/new?assignees=&labels=&template=
- A continuación, puedes copiar los datos del ticket original de CC. Para ello, haga clic en los tres puntos horizontales de la esquina superior derecha del cuadro de texto del informe y seleccione Editar. A continuación, puede copiar el texto del ticket y pegar esa información en el ticket de AC, y luego añadir sus propios comentarios y conclusiones para generar el ticket final.
- Ponle un título apropiado: algo claro y coherente es lo mejor. A continuación, añade el enlace a la incidencia original comunicada a ChromieCraft ("Originalmente comunicada LINK-TO-CHROMIECRAFT-ISSUE"). GitHub vinculará automáticamente los dos informes.
- También debe comprobar que el informe CC tiene un hash de la versión del servidor incluido. (El hash de la versión es una pequeña cadena de números y letras al azar, como `3d4befd`). Si no lo tiene, el rastreador de AC se quejará. Si falta por alguna razón, la información de la versión actual de ChromieCraft se puede encontrar [aquí](https://github.com/chromiecraft/azerothcore-wotlk), o si has replicado el problema en tu propio servidor de pruebas, puedes usar tu propio hash. Esto se puede encontrar escribiendo `server info` en la línea de comandos `AC>` de tu servidor mundial de AC.

### 8. Añadir etiquetas a los temas de AC y CC

- Ahora puede añadir las etiquetas pertinentes tanto a la nueva incidencia de AC que ha creado como a la incidencia de CC desde la que ha estado trabajando. Etiqueta adecuadamente - "Genérico" es el último recurso, para problemas que afectan a un amplio rango de niveles. De lo contrario, etiqueta un problema por el nivel de la zona en la que ocurre, o el nivel de la misión o PNJ al que afecta. Si no estás seguro del nivel de una zona, puedes encontrar una lista de zonas de la época de Wrath por nivel [aquí](https://wowpedia.fandom.com/wiki/Zones_by_level_(original)).
- Para el tema de AC, si estás copiando un tema de CC, puedes añadir la etiqueta "Confirmado". También puedes añadir otras etiquetas relevantes, como "Quest", "Loot", "DB", "PVP", o una de las etiquetas específicas de cada clase.
- Para el tema de la CC, puedes etiquetarlo con "Confirmado", "Vinculado a la AC", y una etiqueta que indique el rango de nivel o Genérico si no se aplica. De nuevo, si hay otras etiquetas relevantes como "Asunto de clase", no dudes en añadirlas.
- Si tiene los permisos adecuados, añada también la nueva edición de AC a cualquier proyecto que sea relevante, normalmente el que coincida con el rango de nivel de la edición.

#### Etiquetas prioritarias

También puede establecer la prioridad percibida de una cuestión mediante etiquetas. Éstas son:

| Tag Level    | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| **Critical** | Sólo debe utilizarse en caso de que se produzcan fallos en el servidor    |
| **High**     | Bugs que rompen el juego y no tienen solución                             |
| **Medium**   | Errores que rompen el juego y que tienen una solución                     |
| **Low**      | Bugs más típicos con misiones/objetos/NPCs, etc. Un error "estándar"      |
| **Trivial**  | Errores que no tienen un impacto real en el juego, normalmente cosméticos |

## Directrices

- **Usa tu criterio.** Estamos ahí para ejercer nuestro mejor juicio, no sólo como fotocopiadoras. Tenemos acceso a herramientas e información que la mayoría de los jugadores no tienen, por lo que deberíamos ser capaces de ver más profundamente un problema que ellos y tomar decisiones en consecuencia.
- **Generaliza el problema.** Intenta generalizar o ampliar el problema. Si un tipo inusual de objeto, NPC o hechizo no funciona correctamente, intenta comprobar otros objetos del mismo tipo general para ver si también están rotos. Lo ideal es captar el mayor número posible de errores que podamos.
- **Sé escéptico.** Los usuarios pueden tener una opinión muy fuerte sobre estos temas. A menudo verás afirmaciones como "siempre ha sido así" o "he jugado con mi clase desde vanilla y así es como debe ser". Estas afirmaciones, sin ninguna otra evidencia, deben ser tratadas con un nivel apropiado de escepticismo. Un jugador experimentado probablemente sabrá cosas sobre su clase que tú no sabes, pero eso no significa que sus afirmaciones deban ser aceptadas como un hecho sin ninguna otra evidencia.
- **Combina problemas similares.** Si encuentras problemas relacionados mientras buscas, considera enlazar los dos con una nota. (Puede ser algo tan sencillo como "Ver también (URL)". Esto ayudará a quien acabe solucionando el problema al hablarle de problemas similares).
- **Trata de priorizar:** los fallos más graves sobre los menores, los frecuentes sobre los raros. De forma contraria a la intuición, los problemas más nuevos pueden necesitar prioridad sobre los más antiguos, basándose en que si un fallo ha durado mucho tiempo sin ser solucionado, es muy probable que no sea muy importante.
- Si no puedes encontrar ninguna fuente, al menos dilo en lugar de no decir nada.
- **Sé educado.** Cuando alguien envía un informe de error, nos está haciendo un favor. Se han tomado el tiempo de hacerse una cuenta en GitHub y escribir un informe de error para intentar ayudarnos. Lo menos que podemos hacer es ser profesionales y corteses a cambio.

## Fuentes

Esta es una mirada general (y de ninguna manera exhaustiva) a las fuentes que podemos utilizar para tratar de entender si un error es válido o no. Entre ellas se encuentran:

- [TBC Wowhead](http://tbc.wowhead.com/) o [Current Wowhead](https://www.wowhead.com/) - Wowhead es una fuente de datos importante, aunque defectuosa, tanto por los propios datos del sitio como por los comentarios que los usuarios han hecho en él. Los comentarios de Wowhead son probablemente el mayor conjunto de información sobre misiones y objetos individuales que tenemos, por lo que es una pena que gran parte de ellos sean una completa basura. Sin embargo, es demasiado fácil caer en la suposición de que los datos de Wowhead son correctos y completos, cuando en realidad no lo son. Los datos de Wowhead proceden de los envíos de los usuarios y, por tanto, tienen sus propios problemas con cosas como las tasas de caída. Sus datos también han sido contaminados por personas que han enviado datos desde servidores privados. Por lo tanto, a pesar de su aparente autoridad, los datos de Wowhead pueden ser fragmentarios, incompletos y engañosos si no se interpretan con cuidado. Ten en cuenta las dos versiones que aparecen aquí. TBC Wowhead suele ser más útil, pero la versión actual de Wowhead también contiene comentarios de los usuarios de la época de Wrath, cosa que TBC WH no hace.

- [Wowpedia](https://wowpedia.fandom.com/wiki/Special:Search) - Wowpedia puede ser una buena fuente, ya que tiene una función de historia que te permite ver un artículo tal y como era durante la época de WotLK. Para acceder a ella, ve al artículo correspondiente y mira a la derecha del título del artículo. Al lado de "Ver fuente" verás 3 puntos dispuestos verticalmente. Si haces clic en ellos, podrás acceder al historial del artículo. Lo normal es que quieras el último artículo escrito antes del 12 de octubre de 2010 (fecha de lanzamiento de Cata).

Wowpedia a menudo agrega notas de parche relacionadas con un talento o habilidad en particular, lo cual es frecuentemente útil. También suele registrar el texto de las misiones y los diálogos de los buscadores, por lo que puede ser una fuente útil para ese tipo de cosas. Ten en cuenta que los contenidos más antiguos de la época de Wrath también se pueden encontrar en su sitio hermano [WowWiki](https://wowwiki-archive.fandom.com/wiki/Wiki).

- Datos de sniffs - Los "sniffs" son paquetes de datos interceptados que los jugadores han capturado cuando juegan a Wow al por menor. Tienen la ventaja de utilizar datos reales de venta al por menor y hacerlos disponibles en SQL, y por lo tanto ampliamente utilizables. Las desventajas son que los datos de sniffs sólo contienen datos visibles para el cliente, a menudo están incompletos y son irregulares, y a menudo son difíciles de verificar. Para un sitio útil que hace uso de estos datos, ver el [AzerothCore SpeedChecker](https://azerothcore-speedchecker.web.app/) por @Efymer en Discord - si quieres verificar la velocidad de movimiento de una criatura u otras banderas frente a los datos de venta al por menor, esto lo hará por ti.

- YouTube - puede ser una excelente fuente de información, ya que hay un montón de vídeos de gente haciendo misiones en Classic/TBC. Lamentablemente, hay pocos de la era original de WotLK. El otro problema de YT es que los jugadores minoristas no son los únicos que suben vídeos de Wow. Los jugadores de otros servidores privados también hacen vídeos (fíjate en uno en particular llamado Bue, que a menudo será el primer resultado al buscar una búsqueda en YouTube). Estos vídeos de servidores privados son, por supuesto, inútiles como fuentes de comportamiento correcto de Blizz.

- [TrinityCore](https://github.com/TrinityCore/TrinityCore/issues) - Trinity es más antiguo y más grande que AC, y su propio rastreador de errores y base de datos de problemas es correspondientemente más grande que la nuestra. Como resultado, a menudo es un buen lugar para buscar otros informes de un problema si el rastreador de AC no tiene ningún resultado. A menudo también se puede encontrar una solución para el problema. Ten en cuenta que TC tiene múltiples ramas, de las cuales sólo una tiene como objetivo la 3.3.5a.

- [Wayback Machine/Internet Archive](https://web.archive.org/) - si realmente te quedas atascado para las fuentes contemporáneas y necesitas ver el estado de un sitio en 2010, entonces Wayback Machine puede ser bueno, si sabes la URL del sitio que quieres ver. Por ejemplo, tienen una instantánea de 2010 del sitio de mascotas de cazadores Petopia, que en ocasiones ha sido útil.

- [Los foros de World of Warcraft](https://us.forums.blizzard.com/en/wow/): los foros de Wow pueden ser útiles cuando se discuten temas relacionados con Vanilla o TBC, pero suelen estar llenos de gente que se contradice y se enardece, así que no son fuentes muy fiables.

- Del mismo modo, [MMO Champion](https://www.mmo-champion.com/forum.php) tiene foros que pueden ser útiles porque han estado funcionando, esencialmente sin cambios, desde antes de Wrath. Esto significa que a veces puedes encontrar información útil de primera mano allí. Sin embargo, como en la mayoría de los foros, separar la información útil de la paja puede ser difícil.

- [WowGaming](https://wowgaming.altervista.org/aowow/) - este es un sitio que actúa como el front end de una instantánea de nuestra propia base de datos de AC. Como resultado, proporciona una forma rápida de ver los detalles de la versión actual de AzerothCore.

- Base de datos de World of Warcraft WotLK](https://wotlkdb.com/). Otra fuente de datos de terceros de la época de Wrath, aunque la calidad de sus datos es a veces cuestionable. No es una fuente primaria.

- El canal de Discord #need-help es muy útil en este caso.

## Herramientas

- El servidor AC/entorno de pruebas, Esta es la herramienta básica de pruebas. Intenta mantener tu servidor AC tan actualizado como puedas. Las actualizaciones diarias son una buena idea, y no deberías pasar más de una semana sin actualizar.

- [Comandos GM](gm-commands) y macros - Como mínimo, debes estar familiarizado con los distintos trucos (sin daño, velocidad, vuelo), `.go`, `.additem`, `.quest add`, etc. También puede ser útil configurar varias macros de trucos y potenciadores en tu cuenta de prueba, para que puedas configurar y entrenar al instante un nuevo personaje. Cuando se prueban varios problemas de clase y raza, te encuentras haciendo y luego borrando un montón de personajes diferentes, por lo que la automatización de la configuración de nuevos personajes con macros puede amortizar el tiempo invertido muy rápidamente.

- [Keira3](https://www.azerothcore.org/Keira3/) - es la herramienta indispensable para el triaje. Cinco minutos con Keira te ahorrarán una hora de correr por el mundo abierto. Viene con un editor SQL incorporado que puedes utilizar para ejecutar consultas personalizadas. También tiene información sobre las herramientas incorporadas en la mayoría de los campos de datos que pueden ayudar a entender lo que estás viendo. También puedes usarlo para generar SQL para arreglar cosas, aunque el SQL que genera sólo debe usarse como punto de partida. Esto se debe a que a menudo no cumple con las normas SQL preferidas para los RP en cuanto a la duplicación de consultas.

- Un editor SQL genérico como [HeidiSQL](https://www.heidisql.com/) (aviso, sólo para Windows) también es útil. Keira no accede a todas las tablas de la base de datos de AC, sólo a las más útiles, así que una herramienta como Heidi que te da vistas de todo puede ser buena para las tablas más oscuras.

- [Base de datos: World](database-world), especialmente las que cubren la base de datos del mundo. En ellas encontrarás información importante sobre la estructura y los campos de la base de datos. Si tienes dudas sobre cómo debería funcionar algo o qué significa una bandera, la respuesta suele estar aquí.

- [Fragmentos útiles de SQL](useful-sql) - están diseñados para ser herramientas rápidas y fáciles de usar para obtener información sobre varios problemas potenciales de la BD.

- Aprende a filtrar las cuestiones de GitHub:
    - `type:issue label: "Needs Triage"` - encuentra todas las cuestiones abiertas.
    - `author:Username` - encuentra todos los temas creados por el autor.
    - `involves:Username` - encuentra todos los temas que han iniciado o comentado.

## Otros enlaces

- [Versión actual de ChromieCraft](https://github.com/chromiecraft/azerothcore-wotlk)
- [Mods de ChromieCraft](https://raw.githubusercontent.com/chromiecraft/chromiecraft/main/.github/CC_SERVER_INFO)
- [Cómo hacer la evaluación de errores](https://github.com/chromiecraft/chromiecraft#for-contributors-how-to-triagereport-bugs)
