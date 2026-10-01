# Directrices para los mensajes de commit

# 📌 Título
**Type(Scope/Subscope):** _Explicación ultra corta del commit_

| ✅ Ejemplos (máx. 50 caracteres) |
|--------------------------------|
| fix(DB/SAI): Missing spell to NPC Hogger |
| fix(Scripts/Raid): Phase 2 of Ragnaros |
| feat(Core/Players): Implement missing player flags |

**Presta atención para no dejar mensajes de commit rotos (p. ej. espacios aleatorios)**

---

# 📖 Descripción
Explica **por qué** se hace este cambio y **qué** arregla.

| ✅ Ejemplos (máx. 72 caracteres por línea) |
|-------------------------------------|
| Hogger (id: 492) was not charging player when being engaged. |

---

# ✍️ Co-autor(es)
Si hay más autores, se pueden mencionar así:
```

Co-authored-by: Name [name@example.com](mailto:name@example.com)

```

**Si estás haciendo cherry-picking de commits, es obligatorio referenciar al autor original en tu commit.**

Cuando creas un commit (usando la terminal GIT Bash), escribe:

``` 
git commit --author="John Doe <john@example.com>" -m "Your commit message"
```

✔️ Esto establece el campo Author del commit a John Doe <john@example.com>
✔️ Tu configuración normal de Git user.name y user.email se seguirá usando para el campo Committer.

Si usas GitHub Desktop, puedes rellenar el campo de co-autor, debajo del cuadro de descripción del commit.

---

# 📌 Info extra

# ✅ Tipos
- **feat**: nueva funcionalidad  
- **fix**: corrección de bug  
- **refactor**: refactorización de código de producción (no se espera cambio de funcionalidad)
- **style**: formato, punto y coma faltantes, etc; sin cambio de código  
- **docs**: cambios en la documentación  
- **chore**: actualización de scripts bash, archivos de git, etc; sin cambio de código de producción  

**Recuerda:**
- ✅ Capitaliza la línea del asunto  
- ✅ Usa el **modo imperativo** en la línea del asunto  
- ✅ No termines la línea del asunto con un punto  
- ✅ Separa el asunto del cuerpo con una línea en blanco  
- ✅ Usa el cuerpo para explicar **qué** y **por qué** en lugar de **cómo**  
- ✅ Puedes usar varias líneas con `-` para viñetas en el cuerpo  

**Más info:** [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)

---

# 📦 Scope y 🔧 Subscope
El Scope define el área principal afectada:

- Core (relacionado con el core, archivos del framework)
- Scripts (relacionado con el core, archivos de script)
- DB (relacionado con la base de datos, SQL)

Sigue los nombres de archivo o el tipo de contenido:

- fix(Scripts/Ulduar): Mimiron rocket barrage targeting

- fix(DB/SAI): Add missing spells to Howling Prowler

👉 Para commits de SQL:
Si el contenido es mixto, elige el tipo de tabla más predominante.
Ejemplo: si la mayoría de las ediciones están en smart_scripts, usa SAI.
Si los cambios están demasiado diluidos, usa un sub-scope general como Misc.

Por ejemplo:
```
fix(Scripts/Ulduar): Mimiron rocket barrage targeting
```

O

```
fix(DB/SAI): Add missing spells to Howling Prowler
```
