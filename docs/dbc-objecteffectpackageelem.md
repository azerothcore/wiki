# ObjectEffectPackageElem.dbc

[`Back-to:DBC`](dbc-index)

**The \`ObjectEffectPackageElem.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field                 | Type   | Comment                                                  |
| :----: | :-------------------- | :----- | :------------------------------------------------------- |
| 0      | ID                    | uint32 |                                                          |
| 1      | ObjectEffectPackageID | uint32 | ID in [ObjectEffectPackage.dbc](dbc-objecteffectpackage) |
| 2      | ObjectEffectGroupID   | uint32 | ID in [ObjectEffectGroup.dbc](dbc-objecteffectgroup)     |
| 3      | StateType             | uint32 |                                                          |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ObjectEffectPackageElem).
