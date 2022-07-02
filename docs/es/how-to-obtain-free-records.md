# Cómo obtener registros libres

En algunas ocasiones, necesitamos obtener o conocer registros cuyos valores no están siendo ocupados.

Ya sea porque queremos insertar un nuevo valor, o porque queremos reestructurar nuestra tabla después de un tiempo.

Para ello, puede utilizar el siguiente script:

```sql
SELECT t.id + 1
FROM Table1 t
WHERE NOT EXISTS (
    SELECT * 
    FROM Table1 t2
    WHERE t2.id = t.id + 1
)
LIMIT 1
```

Debemos sustituir el nombre de la tabla, y los atributos que buscamos.

Ahora veamos un ejemplo. Supongamos que queremos buscar el primer registro libre dentro de `creature`.

Lo primero que tenemos que identificar es su clave primaria: `guid`.

```sql
SELECT t.`guid` + 1
FROM `creature` t
WHERE NOT EXISTS (
    SELECT * 
    FROM `creature` t2
    WHERE t2.`guid` = t.`guid` + 1
)
LIMIT 1
```

Al ejecutar la consulta, obtendremos como resultado en este caso, el número **15**.

**Nota:** Actualmente el valor cambio, y ahora es otro. Pero en su momento era el numero 15.

Lo que debemos hacer ahora es comprobar que este valor no se está utilizando, mediante un `SELECT`.

```sql
SELECT * FROM `creature` WHERE `guid`=15;
```

Para corroborar que la información es correcta, les dejamos los 16 primeros registros.

| guid | id    | map | zoneId |
|------|-------|-----|--------|
| 1    | 2843  | 0   | 0      |
| 2    | 7853  | 0   | 0      |
| 3    | 2499  | 0   | 0      |
| 4    | 2838  | 0   | 0      |
| 5    | 2839  | 0   | 0      |
| 6    | 2626  | 0   | 0      |
| 7    | 2482  | 0   | 0      |
| 8    | 8123  | 0   | 0      |
| 9    | 9459  | 0   | 0      |
| 10   | 9520  | 0   | 0      |
| 11   | 1215  | 0   | 0      |
| 12   | 1218  | 0   | 0      |
| 13   | 30140 | 571 | 0      |
| 14   | 30156 | 571 | 0      |
| 16   | 32442 | 571 | 0      |

Como puede ver, el número 15 está disponible.

**Note:** la tabla tiene muchos más atributos, pero sólo mostramos algunos, para que la tabla no sea tan extensa.
