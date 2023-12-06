---
redirect_from: "/How-to-obtain-free-records"
---

# How to obtain free records

On some occasions, we need to obtain or know records whose values are not being occupied.

Either because we want to insert a new value, or we want to restructure our table after a while.

To do this, you can use the following script

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

We must replace the name of the table, and the attributes we are looking for.

Now let's look at an example. Let's suppose that we want to search the first free record within `creature`

The first thing we have to identify is your primary key: `guid`

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

When running the query, we will get as a result in this case, the number **15**.

{% include note.html content="Currently, the value has changed, and now it is different. But at the time it was number 15." %}

What we must do now is to check that this value is not being used, by means of a `SELECT`

```sql
SELECT * FROM `creature` WHERE `guid`=15;
```

To corroborate that the information is correct, I leave you the first 16 records.

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

As you can see, number 15 is available.

{% include note.html content="The table has many more attributes, but we show only some, so that the table would not be so extensive." %}
