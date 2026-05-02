---
redirect_from: "/MySQLtypesC++"
---

# MySQL Types C++

| MySQL type         | Core type                                     | Example code                                                                                | Variable operators |
| ------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------ |
| BIGINT             | int64                                         | `int64 val = fields[n].GetInt64();`                                                         | %I64d (Capital i)  |
| BIGINT UNSIGNED    | uint64                                        | `uint64 val = fields[n].GetUInt64();`                                                       | %I64u (Capital i)  |
| INT                | int32                                         | `int32 val = fields[n].GetInt32();`                                                         | %u                 |
| INT UNSIGNED       | uint32                                        | `uint32 val = fields[n].GetUInt32();`                                                       | %u                 |
| MEDIUMINT          | int32                                         | `int32 val = fields[n].GetInt32();`                                                         | %u                 |
| MEDIUMINT UNSIGNED | uint32                                        | `uint32 val = fields[n].GetUInt32();`                                                       | %u                 |
| SMALLINT           | int16                                         | `int16 val = fields[n].GetInt16();`                                                         |                    |
| SMALLINT UNSIGNED  | uint16                                        | `uint16 val = fields[n].GetUInt16();`                                                       |                    |
| TINYINT            | int8                                          | `int16 val = fields[n].GetInt16();`                                                         |                    |
| TINYINT UNSIGNED   | uint8                                         | `uint8 val = fields[n].GetUInt8();`                                                         |                    |
| FLOAT              | float                                         | `float val = fields[n].GetFLOAT();`                                                         |                    |
| FLOAT UNSIGNED     | float                                         | `float val = fields[n].GetFLOAT();`                                                         |                    |
| DOUBLE             | double                                        | `double val = fields[n].GetDouble();`                                                       |                    |
| DOUBLE UNSIGNED    | double                                        | `double val = fields[n].GetDouble();`                                                       |                    |
| text               | string (std::string) or cstring (char const*) | `std::string text = fields[n].GetString();`<br>`char const* text = fields[n].GetCString();` | %s                 |
| longtext           | string (std::string) or cstring (char const*) | `std::string text = fields[n].GetString();`<br>`char const* text = fields[n].GetCString();` | %s                 |
| tinytext           | string (std::string) or cstring (char const*) | `std::string text = fields[n].GetString();`<br>`char const* text = fields[n].GetCString();` | %s                 |
| char(k)            | string (std::string) or cstring (char const*) | `std::string text = fields[n].GetString();`<br>`char const* text = fields[n].GetCString();` | %s                 |
| VARCHAR(k)         | string (std::string) or cstring (char const*) | `std::string text = fields[n].GetString();`<br>`char const* text = fields[n].GetCString();` | %s                 |
| blob               | string (std::string) or cstring (char const*) | `std::string text = fields[n].GetString();`<br>`char const* text = fields[n].GetCString();` | %s                 |
| COUNT(x)           | uint64                                        | `uint64 count = fields[n].GetUInt64();`                                                     | %UI64FMT*          |
| MAX(x)             | uint32 or int32                               | `uint32 minmax = fields[n].GetUInt32();`<br>`int32 minmax = fields[n].GetInt32();`          | %u                 |
| MIN(x)             | uint32 or int32                               | `uint32 minmax = fields[n].GetUInt32();`<br>`int32 minmax = fields[n].GetInt32();`          | %u                 |
| SUM(x)             | string (std::string) or cstring (char const*) | `INT sum;`<br>`if (const char* ch = fields[n].GetCString())`<br>`    sum = atoi(ch);`       | %s                 |
| UNIX_TIMESTAMP(x)  | uint64                                        | `uint64 unix_time = fields[n].GetUInt64();`                                                 |                    |

\* %UI64FMT does not work with acore_string

```cpp
// world database query                           0      1      2      3        4
QueryResult result = WorldDatabase.Query("SELECT guid, entry, name, period, ScriptName FROM transports");
do
{
    Field* fields    = result->Fetch();
    uint32 lowguid   = fields[0].GetUInt32();
    uint32 entry     = fields[1].GetUInt32();
    std::string name = fields[2].GetString();
    uint32 period    = fields[3].GetUInt32();
    uint32 scriptId  = sObjectMgr->GetScriptId(fields[4].GetCString());

    // ...
}
while (result->NextRow());
```
