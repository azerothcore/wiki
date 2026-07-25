# Proceso de merge de AzerothCore

### Ritmo de merge de PRs

En AzerothCore, hacemos merge solo de unos pocos PRs al día, eligiéndolos de la lista [[To Be Merged]](https://github.com/azerothcore/azerothcore-wotlk/pulls?q=is%3Apr+is%3Aopen+label%3A%22To+Be+Merged%22).

Cada día elegimos los PRs más antiguos para hacer merge, a menos que haya PRs más urgentes que deban integrarse antes por alguna razón.

Los usuarios pueden pedir al Staff de AC que dé mayor prioridad a un PR si realmente necesitan que se integre pronto; somos bastante flexibles con eso (ej: un hook).

Este proceso puede parecer "lento", sin embargo hay razones para ello:

- Todos tienen la posibilidad de revisar los PRs antes de que se integren en master; la estabilidad es importante para nosotros.

- Los testers y desarrolladores todavía tienen la oportunidad de decir "¡no chicos, no hagáis merge de esto todavía! Acabo de encontrar un bug inesperado con este PR" antes de que se integre definitivamente.

- Tenemos un proceso muy estricto para aceptar PRs (requerimos al menos 1 aprobación de code review y 1 aprobación de un tester manual), pero siempre puede ocurrir que lleguen bugs a la rama master. 
Si hacemos merge de demasiados PRs a la vez, es difícil entender cuál de ellos fue el defectuoso. 
Hacer merge de una cantidad baja de PRs por día nos permite identificar rápidamente los commits defectuosos y arreglarlos/revertirlos lo antes posible.
