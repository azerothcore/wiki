---
redirect_from: "/Live-e2e"
---

# Pruebas e2e en vivo

AzerothCore puede ejecutar **pruebas de extremo a extremo (end-to-end) en vivo** en un reino 3.3.5a real. Son clientes de protocolo, no un simulacro del core ni una ejecución en seco (dry-run) de worldserver.

Los bots provienen de [AzerothGhost](https://github.com/azerothcore/AzerothGhost). Inician sesión a través de auth, entran al mundo y ejecutan los mismos opcodes que utiliza un cliente oficial (inicio de sesión, teletransportes, lanzamientos de hechizos, combate, misiones, botín, etc.). Las aserciones revisan el protocolo, la caché de objetos y, a veces, la base de datos de personajes.

Esto **no** reemplaza el [Cómo probar un PR en el juego.](how-to-test-a-pr). Es una cobertura adicional en el stack en vivo, principalmente para que un PR no se pueda fusionar si una ruta visible para el jugador ya está rota.

## Qué hace la CI

En un pull request contra `azerothcore/azerothcore-wotlk` (no en bifurcaciones ni borradores), y nuevamente en cada push a `master`:

1. El trabajo habitual `nopch-build` compila los servidores reales `authserver` y `worldserver` (sin PCH) y sube esos binarios.
2. El trabajo `e2e full` inicia MySQL y aplica la configuración normal de la base de datos de AC y los datos del cliente.
3. Arranca **esos mismos binarios**. `worldserver` escucha en el puerto 8085, `authserver` en el 3724. El trabajo espera hasta que ambos puertos acepten conexiones.
4. Ejecuta `go test -tags=e2e` desde `e2e/` contra ese reino.

Por lo tanto, el flujo de trabajo ejecuta un stack **completo** de AC desde esos binarios y luego se comunica con él como un cliente. No hay un worldserver parcial ni un combate simulado.

Un comentario en el flujo de trabajo sobre "dry-run" es solo sobre la ruta de CMake/compilación. Las pruebas en sí siempre se ejecutan contra un proceso en vivo.

La ejecución en `master` es la suite completa, no un subconjunto de prueba rápida (smoke). Eso detecta fallas intermitentes y casos en los que un PR más antiguo estaba en verde contra un `master` anterior, pero se rompe una vez que se integra con commits posteriores.

También puedes iniciar la suite a mano con `workflow_dispatch` (`scope=full` o `scope=smoke`).

## Qué son las pruebas

Se encuentran en el repositorio de AzerothCore bajo `e2e/` (`smoke/` y `suites/`). Importan el entorno de pruebas desde [AzerothGhost](https://github.com/azerothcore/AzerothGhost) (`e2e/e2eharness`).

Flujo típico:

1. Crear una cuenta de prueba de MJ (GM) y un personaje.
2. Iniciar sesión y esperar hasta que la sesión esté en el mundo.
3. Ubicar al bot (llamado tele, pad, o `.go creature`).
4. Opcionalmente, preparar el combate (`.gm off`, trucos, bandera de JvJ).
5. Ejecutar una acción real del cliente (lanzar hechizo, atraer enemigo, comerciar, reconectar, …).
6. Verificar algo que un jugador vería (el aura desapareció, los PS bajaron, sigue en el puente, la siguiente oleada no llegó antes de tiempo, el mundo sigue vivo).

La configuración puede usar comandos de MJ. El resultado de referencia debe ser lo que ve el jugador, no "el comando de MJ funcionó".

Los errores abiertos del core permanecen comentados con `OPEN(e2e)` y un enlace al problema (issue). No se compilan, por lo que no pueden dar un falso positivo (soft-pass).

## Cómo ejecutarlas localmente

Necesitas un authserver, worldserver y MySQL en ejecución, además de Go 1.26+.

```bash
cd e2e
cp .env.example .env   # editar dirección de auth + DSNs
set -a; source .env; set +a
go test -tags=e2e ./... -count=1 -v -timeout 120m -parallel 1 -p 1
```

Sin `-tags=e2e`, `go test ./...` omite estos paquetes.

Mantén `-parallel 1 -p 1` a menos que sepas que cada paquete concurrente tiene su propia zona de aislamiento. Compartir una zona hace que los bots interfieran entre sí.

Detalles de autoría: `e2e/README.md` en el repositorio del core, además de las guías de AzerothGhost [`LLM_GUIDE.md`](https://github.com/azerothcore/AzerothGhost/blob/main/e2e/LLM_GUIDE.md) y [`EXAMPLES.md`](https://github.com/azerothcore/AzerothGhost/blob/main/e2e/EXAMPLES.md).
