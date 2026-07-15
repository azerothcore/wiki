# Ingeniería agéntica en AzerothCore

{% include important.html content="Use AI as much as you like. Stay in control: review, understand, test and take responsibility for every line you submit. PRs that are clearly unreviewed AI output may be closed without a detailed review." %}

## La IA en AzerothCore

Estamos viviendo uno de los mayores cambios en cómo se construye el software desde que internet se popularizó.
La IA está cambiando rápidamente la forma en que trabajan los desarrolladores, y ha venido para quedarse.

En AzerothCore preferimos dirigir este cambio antes que fingir que no está ocurriendo. Vemos la IA como una herramienta que nos ayuda a movernos más rápido *y* a construir mejor software.
En el momento en que la velocidad empieza a costar calidad, lo estamos haciendo mal.

No necesitas confiar en la IA. Necesitas mantener el control sobre ella. Esta página muestra cómo lo hacemos aquí.

## Las reglas básicas

Las contribuciones asistidas por IA son bienvenidas, y se someten al mismo listón que cualquier otra contribución. Antes de abrir un PR:

1. **Hazte dueño de tu código.** Revisa y entiende cada línea antes de enviarla. Durante la revisión, eres tú quien responde a las preguntas, no tu agente. Si no puedes explicar un cambio, no está listo.
2. **Prueba de verdad.** Compílalo, ejecútalo, verifícalo en el juego. "Compila" no es hacer pruebas.
3. **Sé transparente.** La plantilla de PR pregunta si se involucró la IA; responde honestamente.
4. **Suena como un humano.** Los issues, las descripciones de PR y las respuestas de revisión deberían leerse como si los hubieras escrito tú. A nadie le gusta hablar con un muro de texto generado.
5. **Respeta el tiempo de los revisores.** Los PRs generados por IA de bajo esfuerzo crean más trabajo del que ahorran. Los PRs que son claramente output de IA sin revisar pueden cerrarse sin una revisión detallada.

¿Por qué tan explícito? En el pasado, recibimos una oleada de PRs generados por IA que nunca fueron correctamente diseñados, ni siquiera entendidos, por sus autores.
Apreciamos cada esfuerzo de contribución, pero esto crea caos y una carga pesada sobre el staff que los revisa. El resto de esta página muestra una forma mejor.

## ¿Nuevo en la IA? ¿Nuevo en C++? Bien.

Estás en buena compañía. Los proyectos de emulación de código abierto, desde los primeros días de MaNGOS hasta hoy, siempre han sido, ante todo, proyectos de aprendizaje.
Un lugar donde la gente escribe sus primeras líneas de código toqueteando su juego favorito.
La IA no ha cambiado eso. Si acaso, reduce la barrera de entrada aún más.

El truco es tratar a tu agente como un compañero de programación, no como una máquina expendedora. Pídele que explique qué está haciendo y por qué. Cuestiona sus decisiones.
**Cuando algo no esté claro, pídele que lo reexplique con palabras más simples**.
Usada de esta forma, la IA es uno de los mejores tutores de programación que tendrás jamás, y cada tarea te deja un poco más habilidoso que antes.

## Ingeniería agéntica estructurada, no Vibe Coding

Lanzar un prompt de una línea a un agente y publicar lo que salga es cómo acabas en la regla 5 de arriba.
Lo que funciona es un proceso estructurado donde *tú* tomas las decisiones y el agente hace el trabajo pesado.

Nuestro workflow recomendado se llama [**RPA (Refine-Plan-Act)**](https://medium.com/engineering-in-the-age-of-ai/the-refine-plan-act-pattern-for-agentic-ai-coding-59ee013e4427): divide el trabajo en fases, cada una produciendo un pequeño documento que lees, corriges y apruebas antes de continuar.
Cada fase se ejecuta en una sesión nueva y enfocada, lo que te da mejor output y cuesta menos tokens (más sobre esto abajo).

## Elige tu agente

Todo en esta página es agnóstico respecto al agente. La mayoría de nuestros devs usan herramientas CLI como **Claude Code**; las alternativas incluyen [**OpenCode**](https://opencode.ai/) y herramientas similares que incluyen modelos gratuitos, si una suscripción de pago no es una opción. Si prefieres trabajar dentro de tu editor, VS Code u otras extensiones de IDE también funcionan.

## El agent-toolkit

El [agent-toolkit](https://github.com/eai-org/agent-toolkit/) es una pequeña colección de código abierto de skills y reglas que implementan este workflow.
Lo mantienen los fundadores de AC junto con mantenedores externos, y vive fuera de la organización de GitHub de AC porque otros proyectos también lo usan.
Ha sido probado a fondo con Claude Code y está diseñado para funcionar con cualquier agente; si algo no funciona con el tuyo, por favor [abre un reporte de bug](https://github.com/eai-org/agent-toolkit/issues).

Instálalo con un solo comando:

```bash
git clone https://github.com/eai-org/agent-toolkit.git && cd agent-toolkit && ./install.sh
```

Mantenlo actualizado con:

```bash
cd agent-toolkit && git pull && ./install.sh
```

Otros métodos de instalación (marketplace de plugins de Claude Code, [skills.sh](https://www.skills.sh/), [agentwheel](https://www.nestdev.it/agentwheel/)) están listados en el [README](https://github.com/eai-org/agent-toolkit/#how-to-install).

## Recorrido: del ticket al PR

Digamos que quieres trabajar en un bug o funcionalidad registrado en `https://github.com/azerothcore/azerothcore-wotlk/issues/XXXXX` (reemplaza `XXXXX` por el número real del ticket).

**1. Obtén el ticket.** Abre una nueva sesión y escribe:

```
/fetch-ticket https://github.com/azerothcore/azerothcore-wotlk/issues/XXXXX
```

Esto descarga el ticket y cualquier información útil adjunta a él (comentarios, tickets relacionados) en un directorio de planificación:

```
.claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.TICKET.md
```

No te preocupes por el nombre del directorio si usas un agente diferente: es solo una carpeta.
Si tu tarea no tiene ticket de GitHub, crea un archivo `md` similar a mano en el mismo lugar.

**2. Refina: decide el *qué*.** Ejecuta `/clear`, luego:

```
/refine-ticket .claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.TICKET.md
```

Esto inicia una sesión interactiva: el agente revisa el código y te hace preguntas para concretar los objetivos del ticket, y luego escribe un `REQUIREMENTS.md` junto a él.

**3. Planifica: decide el *cómo*.** Ejecuta `/clear`, luego:

```
/create-implementation-plan .claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.REQUIREMENTS.md
```

Otra sesión interactiva, esta vez sobre detalles de implementación, produciendo un `PLAN.md`.

Opcionalmente, `/create-manual-test-instructions` puede derivar instrucciones de prueba paso a paso a partir del ticket o los requisitos, útil para tus propias pruebas en el juego y para los revisores.

**4. Actúa: ejecuta el plan.** Ejecuta `/clear`, luego:

```
Execute the plan `.claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.PLAN.md`
```

Si quieres una pasada de revisión extra, encadénala:

```
Execute the plan `.claude/plans/XXXXX-some-issue-title/XXXXX-some-issue-title.PLAN.md` then run /fresh-eyes-review and address the feedback where it makes sense
```

(o ejecuta la revisión en un prompt posterior).

**5. Abre el PR.** Cuando estés listo, el agente puede rellenar la plantilla de PR de AC por ti:

```
/generate-pr-description
```

Luego haz la parte que el agente no puede: prueba tu cambio en el juego, lee el diff final de principio a fin, y abre el PR.

**6. Gestiona la revisión.** Cuando lleguen los comentarios, `/fetch-pr-review` los recopila en un documento y `/refine-pr-review` te los repasa uno por uno (atender, atender parcialmente, o rebatir) con respuestas redactadas.

## Hábitos que dan sus frutos

### Mantén tu contexto afilado

Habrás notado que seguimos ejecutando `/clear`. Un contexto nuevo y enfocado hace que los agentes sean notablemente mejores *y* más baratos: menos desorden significa output de mayor calidad y menos tokens desperdiciados.

Si usas Claude Code, recomendamos activar el indicador de uso de contexto para que siempre sepas cuán llena está tu ventana:

![Claude Code context usage indicator](https://miro.medium.com/v2/resize:fit:640/format:webp/1*NlQRpqFBz7FTlY01QG-B8Q.png)

La configuración para ello está disponible [aquí](https://gist.github.com/FrancescoBorzi/ac9d6afd5dbb2ef3dd0499cd7caba5dc).

### Gasta los tokens donde importan

Si estás en una suscripción limitada, cambia de modelo según la fase (en Claude Code: `/model model-name`):

- **Fetch:** un modelo barato (p. ej. Haiku o Sonnet) es más que suficiente
- **Refine y plan:** usa un modelo inteligente (p. ej. Fable u Opus); aquí es donde se decide la calidad
- **Execute:** un modelo más barato (p. ej. Sonnet) suele bastar cuando el plan es bueno

### No hagas de niñera de tu agente

Las sesiones de agente pueden ejecutarse durante un rato, y cambiar de ventana cada minuto para revisarlas mata tu concentración. [ai-notify](https://github.com/Helias/ai-notify), un pequeño script multiplataforma de [Helias](https://github.com/Helias), te avisa cuando tu agente termina o necesita tu input, pero solo si no estás ya mirando esa terminal.
Funciona con Claude Code, Codex, OpenCode y más.

Puntos extra: puedes configurarlo para que reproduzca el "Work, work" del peón de **Warcraft 3** como sonido de notificación, lo cual encaja de maravilla aquí.

## Ir más allá

### Ayuda con las revisiones de PR

Revisar los PRs de otras personas es una de las mejores formas de contribuir al proyecto y aprender al mismo tiempo. Esta skill puede ayudarte:

```
/review-code-assistant https://github.com/azerothcore/azerothcore-wotlk/pull/XXXXX
```

Escanea los cambios y sugiere una lista de comentarios de revisión. **NO los copies y pegues a ciegas**: lee cada uno, asegúrate de entender el razonamiento detrás de él, y pídele al agente que lo explique con palabras más simples siempre que no lo entiendas.
Publica solo los comentarios que creas que ayudarán genuinamente al autor a mejorar su código.

Esta es también una forma excelente de profundizar tus propias habilidades de programación, e incluso puedes ejecutarla en tu propia rama antes de abrir un PR.

### Mantén sana tu configuración local

- **[context-checkup](https://github.com/eai-org/agent-toolkit/blob/main/skills/context-checkup/SKILL.md)**: audita qué se autocarga en el contexto de una sesión y detecta qué se puede recortar para reducir los tokens de arranque.
- **[memory-doctor](https://github.com/eai-org/agent-toolkit/blob/main/skills/memory-doctor/SKILL.md)**: limpia la memoria que tus agentes van acumulando, moviendo las partes relevantes al lugar correcto. Hay más detalles sobre el memory-doctor disponibles [aquí](https://medium.com/engineering-in-the-age-of-ai/keep-your-ai-agents-memory-clean-and-organized-with-memory-doctor-a79f7174f257).

### Escribe nuevas docs y skills, y haz que tus agentes aprendan de sus errores

- **[compact-docs-writer](https://github.com/eai-org/agent-toolkit/blob/main/skills/compact-docs-writer/SKILL.md)**: escribe docs con la máxima economía de tokens.
- **[compact-skill-creator](https://github.com/eai-org/agent-toolkit/blob/main/skills/compact-skill-creator/SKILL.md)**: crea o edita skills, manteniéndolas ligeras y eficientes.
- **[self-improve](https://github.com/eai-org/agent-toolkit/blob/main/skills/self-improve/SKILL.md)**: cada vez que tu agente comete un error, corrígelo y luego ejecuta esta skill en la misma sesión. La lección se almacena permanentemente en la skill o doc correcta, así el error no se repite.

### El MCP de AzerothCore

[azerothMCP](https://github.com/blinkysc/azerothMCP), creado por [Blinky](https://github.com/blinkysc), da a tu agente acceso de solo lectura a las bases de datos y a la documentación de la wiki de AzerothCore. Eso significa que puede consultar scripts de creatures, lógica de SmartAI, esquemas de BD y mecánicas del juego directamente en lugar de adivinar.

## Lectura adicional

El workflow y los hábitos de esta página se cubren con más profundidad en estos artículos:

- [Keep your AI agent's context window sharp](https://medium.com/engineering-in-the-age-of-ai/keep-your-ai-agents-context-window-sharp-7255d83a8949): por qué importan tanto `/clear` y los contextos ligeros
- [An approach to agentic skills](https://medium.com/engineering-in-the-age-of-ai/my-approach-to-agentic-skills-e08dc6c0d1cd): la filosofía detrás de self-improve y de enseñar continuamente a tus agentes
- [Context-aware notifications for multi-tasking developers](https://medium.com/engineering-in-the-age-of-ai/ai-notify-context-aware-notifications-for-multi-tasking-developers-3614635398ec): la historia detrás de ai-notify
- [Keep your AI agent’s memory clean and organized with memory-doctor](https://medium.com/engineering-in-the-age-of-ai/keep-your-ai-agents-memory-clean-and-organized-with-memory-doctor-a79f7174f257)
- El patrón agéntico **Refine-Plan-Act** (RPA): explicado [en teoría](https://medium.com/engineering-in-the-age-of-ai/the-refine-plan-act-pattern-for-agentic-ai-coding-59ee013e4427) y [en la práctica](https://medium.com/engineering-in-the-age-of-ai/how-i-use-ai-agents-to-solve-programming-tasks-daily-2a68a5828b8e)

## Conclusión

La IA no reemplaza el entender el codebase; lo recompensa. Usada con el workflow de arriba, hace que contribuir a AzerothCore sea más rápido, más divertido y, honestamente, una de las mejores formas de subir de nivel como desarrollador.

¿Preguntas, ideas o feedback? Ven a hablar con nosotros en Discord. Esta página seguirá evolucionando, y las sugerencias para mejorarla siempre son bienvenidas.
