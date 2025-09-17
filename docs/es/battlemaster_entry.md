# battlemaster\_entry

[<-Volver a:World](database-world)

**Tabla \`battlemaster\_entry\`**

Contiene información sobre qué NPC puede iniciar qué campo de batalla o arena.

**Estructura**

| Campo            | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                                          |
| ---------------- | --------- | --------- | ----- | ---- | ----------- | ----- | --------------------------------------------------- |
| [entry][1]       | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       | Entrada de una criatura                             |
| [bg_template][2] | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       | Identificación de la plantilla del campo de batalla |

[1]: #entry
[2]: #bg_template

**Descripción de los campos**

### entry

El ID de la criatura. Véase creature\_template.entry

### bg\_template

El battleground\_template.id.
