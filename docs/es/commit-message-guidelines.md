# Pautas para los mensajes de confirmación

# 📌 Título
**Tipo (Alcance/Subalcance):** _Explicación ultra breve del compromiso_

| ✅ Ejemplos (máximo 50 caracteres) |
|--------------------------------|
| fix(DB/SAI): Hechizo faltante para el NPC Hogger |
| fix(Scripts/Raid): Fase 2 de Ragnaros |
| feat(Core/Players): Implementar banderas de jugadores faltantes |

**Preste atención para no dejar mensajes de confirmación rotos (por ejemplo, espacios aleatorios)**

---

# 📖 Descripción
Explique **por qué** se está realizando este cambio y **qué** corrige.

| ✅ Ejemplos (máximo 72 caracteres por línea)                             |
|--------------------------------------------------------------------------|
| Hogger (id: 492) no estaba cargando al jugador cuando estaba en combate. |

---

# ✍️ Coautor
Si hay más autores se pueden mencionar así:
```

Co-authored-by: Name [name@example.com](mailto:name@example.com)

```

**Si está seleccionando cuidadosamente las confirmaciones, es obligatorio hacer referencia al autor original en su confirmación.**

Cuando creas una confirmación (usando la terminal GIT Bash), escribe:

``` 
git commit --author="John Doe <john@example.com>" -m "Su mensaje de confirmación"
```

✔️ Esto establece el campo Autor en la confirmación a John Doe <john@example.com>
✔️ Su configuración normal de Git, user.name y user.email, se seguirán utilizando para el campo Committer.

Si está utilizando GitHub Desktop, puede completar el campo de coautor, debajo del cuadro de descripción de la confirmación.

---

# 📌 Información adicional

# ✅ Types
- **feat**: nueva característica 
- **fix**: corrección de errores  
- **refactor**: Refactorización del código de producción (no se esperan cambios en la funcionalidad)
- **style**: formato, punto y coma faltantes, etc.; sin cambios de código
- **docs**: cambios en la documentación
- **chore**: Actualización de scripts bash, archivos git, etc.; sin cambios en el código de producción

**Recordar:**
- ✅ Escriba con mayúscula la línea de asunto
- ✅ Utilice el **modo imperativo** en la línea de asunto
- ✅ Do not end the subject line with a period
- ✅ Separe el asunto del cuerpo con una línea en blanco
- ✅ Utilice el cuerpo para explicar **qué** y **por qué** en lugar de **cómo**
- ✅ Se pueden utilizar varias líneas con `-` para viñetas en el cuerpo

**Más información:** [Commits convencionales](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)

---

# 📦 Alcance y 🔧 Subámbito
El alcance define el área principal afectada:

- Núcleo (archivos relacionados con el núcleo y del marco)
- Scripts (relacionados con el núcleo, archivos de script)
- DB (relacionado con bases de datos, SQL)

Siga los nombres de los archivos o el tipo de contenido:

- fix(Scripts/Ulduar): Objetivo de la descarga de cohetes Mimiron

- fix(DB/SAI): Añade hechizos faltantes a Howling Prowler

👉 Para confirmaciones de SQL:
Si el contenido es mixto, elija el tipo de tabla más predominante.
Ejemplo: la mayoría de las ediciones se realizan en scripts inteligentes, utilice SAI.
Si los cambios están demasiado diluidos, utilice un subámbito general como Misc.

Por ejemplo:
```
fix(Scripts/Ulduar): Objetivo de la descarga de cohetes Mimiron
```

O

```
fix(DB/SAI): Añade hechizos faltantes a Howling Prowler
```
