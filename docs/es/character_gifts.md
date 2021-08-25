# character\_gifts

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_gifts\`**

Esta tabla contiene datos sobre artículos envueltos o de regalo.

**Estructura**

| Field          | Type | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]      | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [item_guid][2] | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [entry][3]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [flags][4]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #itemguid
[3]: #entry
[4]: #flags

**Descripción de los campos**

### guid

El GUID del personaje. Consulte [characters.guid](characters#guid).

### item\_guid

El GUID del artículo. Consulte [item\_instance.guid](item_instance#guid).

### entry

La entrada del artículo. Consulte [item\_template.entry](item_template#entry).

### flags

`campo-sin-descripción|4`

*Nota para futuras investigaciones: max flags 13369920? FieldFlags of ProtoFlags?*
