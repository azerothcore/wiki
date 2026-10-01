---
redirect_from: "/How-to-find-TrinityCore-commits-of-specific-code-addition"
---

# Cómo encontrar commits de TrinityCore de una adición de código específica

A veces necesitamos importar algo de TrinityCore, por ejemplo vemos una línea o archivo extra en el código, y queremos conocer mejor el contexto de esa adición (es decir, el commit que la introdujo).

Cómo hacerlo:

**1)** Clona un [TrinityCore 3.3.5](https://github.com/TrinityCore/TrinityCore/tree/3.3.5) y ábrelo con [Visual Studio Code](https://code.visualstudio.com/) o cualquier otro IDE que tenga la función **annotate**.

- Si usas Visual Studio Code, puedes instalar el plugin [Annotator](https://github.com/ryu1kn/vscode-annotator).

- Si usas CLion (u otro IDE basado en IntelliJ) la función annotator está ahí por defecto.

- Si usas otro IDE, busca en Google el nombre de tu IDE + "annotate".

**2)** Ve al archivo o línea objetivo

**3)** Usa el Annotator

#### En CLion u otro basado en IntelliJ

Haz click derecho en el número de línea y selecciona "Annotate".

#### En Visual Studio Code

Pulsa CTRL+SHIFT+P (o CMD+SHIFT+P en macOS) y escribe Annotator

![](https://user-images.githubusercontent.com/75517/50727622-af0b7c00-111d-11e9-8423-1c42bc89a297.png)

Elige "Annotate the current file...", abrirá algo como esto:

![](https://user-images.githubusercontent.com/75517/50727632-c9ddf080-111d-11e9-9bd0-9e3673bcd93b.png)

 Pasa el ratón por encima de la línea del cambio del que quieres localizar el commit

![](https://user-images.githubusercontent.com/75517/50727642-0873ab00-111e-11e9-9c5c-aaf166adb972.png)

**4)** Copia el hash del commit y pégalo en:

https://github.com/TrinityCore/TrinityCore/commit/PASTE-THE-COMMIT-HASH-HERE

ese será el commit que estabas buscando.

**IMPORTANTE**: también es útil revisar el/los archivo(s) que se modificaron en la [última revisión](https://github.com/TrinityCore/TrinityCore/tree/3.3.5) porque podrían haber sido modificados en commits más recientes.

**IMPORTANTE 2**: revisa también los comentarios del commit o del PR; normalmente, si hubo problemas, se abordaron como comentarios de GitHub
