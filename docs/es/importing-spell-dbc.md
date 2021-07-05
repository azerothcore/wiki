# Importando datos a la tabla spell_dbc

## Introducci�n

El [spell_dbc](spell_dbc.md) contiene datos sobre los hechizos del lado del servidor que no se encuentran en los archivos DBC del cliente, as� como ** anulaciones ** del DBC que est�n destinadas a mejorar o corregir cualquier hechizo.

Para agregar anulaciones para un hechizo en la tabla `spell_dbc`, primero necesita importar los datos base sobre ese hechizo desde los archivos DBC del Cliente (a menos que ese hechizo ya haya sido importado).

Hay alrededor de 50k hechizos en los archivos DBC del cliente, puede importar un hechizo o el conjunto completo a la tabla `spell_dbc` de su base de datos AC local para poder trabajar en ellos y agregar sus anulaciones.

Cuando importe el hechizo del DBC, obtendr� una consulta `INSERT IGNORE` con todos los valores predeterminados. Guarde esta consulta en alg�n lugar, la necesitar� para enviar su correcci�n de PR.
Despu�s de haber importado los hechizos, puede usar herramientas como [Keira3](https://www.azerothcore.org/Keira3/) para obtener f�cilmente la consulta `UPDATE` que contiene sus anulaciones.

Cuando env�as un PR con una correcci�n de `spell_dbc` para un hechizo determinado, si ese hechizo no estaba presente en la tabla` spell_dbc` antes, debes incluir tanto la consulta `INSERT IGNORE` como la consulta` UPDATE` en tu PR.

## C�mo importar hechizos de los archivos DBC a la tabla spell_dbc

Para importar datos de Spell.dbc a nuestra tabla spell_dbc, puede consultar la gu�a general sobre [c�mo importar datos de archivos DBC](how-to-import-dbc-data-in-db.md).
Solo necesita usar las mismas pautas con el uso del archivo Spell.dbc en su lugar.
