---
redirect_from: "/How-to-spot-db-struct-diff-commits"
---

# Cómo localizar commits de diferencias en la estructura de la BD

**1)** Clona un [TrinityCore 3.3.5](https://github.com/TrinityCore/TrinityCore/tree/3.3.5) y ábrelo con [Visual Studio Code](https://code.visualstudio.com/) o cualquier otro IDE que tenga la función **annotate** (p. ej. IntellIJ y similares).

Si usas Visual Studio Code, puedes instalar el plugin [Annotator](https://github.com/ryu1kn/vscode-annotator).

**2)** Empieza desde un diff, que puede ser cualquiera de [estos](https://github.com/azerothcore/azerothcore-wotlk/milestone/3)/

Por ejemplo:

![](https://user-images.githubusercontent.com/75517/50727531-78813180-111c-11e9-8a6b-37f098df8dff.png)

**3)** Selecciona el nombre de un campo modificado y cópialo, por ejemplo `BaseAttackTime`, y búscalo en Visual Studio Code

**4)** Desplázate hasta encontrar el archivo que lo modifica, por ejemplo:

![](https://user-images.githubusercontent.com/75517/50727603-66ec5980-111d-11e9-8aed-fb376874bba8.png)

**5)** Pulsa CTRL+SHIFT+P (o CMD+SHIFT+P en macOS) y escribe Annotator

![](https://user-images.githubusercontent.com/75517/50727622-af0b7c00-111d-11e9-8423-1c42bc89a297.png)

**6)** Elige "Annotate the current file...", abrirá algo como esto:

![](https://user-images.githubusercontent.com/75517/50727632-c9ddf080-111d-11e9-9bd0-9e3673bcd93b.png)

**7)** Pasa el ratón por encima de la línea del cambio del que quieres localizar el commit

![](https://user-images.githubusercontent.com/75517/50727642-0873ab00-111e-11e9-9c5c-aaf166adb972.png)

**8)** Copia el hash del commit y pégalo en:

https://github.com/TrinityCore/TrinityCore/commit/PASTE-THE-COMMIT-HASH-HERE

ese será el commit que estabas buscando.

**IMPORTANTE**: también es útil revisar el/los archivo(s) que se modificaron en la [última revisión](https://github.com/TrinityCore/TrinityCore/tree/3.3.5) porque podrían haber sido modificados en commits más recientes.
