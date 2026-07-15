# item\_enchantment\_template

[<-Volver a: World](database-world)

**Tabla \`item\_enchantment\_template\`**

Esta tabla contiene la información de probabilidad de encantamiento para objetos que deban tener una propiedad aleatoria o un sufijo aleatorio adjunto.

**Estructura**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]  | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ench][2]   | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [chance][3] | FLOAT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #entry
[2]: #ench
[3]: #chance

**Descripción de los campos**

### entry

Este campo se vincula con el campo RandomProperty O BIEN RandomSuffix de la tabla [item\_template](item_template). Un objeto no puede tener ambos campos con valores distintos de cero.

### ench

El encantamiento a aplicar sobre el objeto. Si el entry de la fila actual se usa en RandomProperty, entonces este campo apunta al ID en ItemRandomProperties.dbc. Si el entry se usa en RandomSuffix, entonces este campo apunta al ID en [ItemRandomSuffix.dbc](itemrandomsuffix).

### chance

La probabilidad de que una propiedad o sufijo aleatorio se aplique al objeto. Para cada entry de esta tabla, las probabilidades combinadas de todas las propiedades/sufijos deben sumar 100; de lo contrario, el objeto puede no recibir un encantamiento aleatorio.

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `item_enchantment_template_chk_1`.
