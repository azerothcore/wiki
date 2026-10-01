---
redirect_from: "/cn/Waypoints-Information"
---

# 路径点与路径

### 不同类型的路径点路径

- 通过 [creature_addon.path_id](creature_addon#pathid) 直接附加到生物上的路径点路径，使用 [waypoint_data](waypoint_data) 和 [waypoint_scripts](scripts) 表。它们可以通过 GM '.wp' 命令添加和操作。
- [SmartAI](smart_scripts) 使用定义在 [waypoints](waypoints) 表中的路径点路径。
- [script_waypoint](script_waypoint) 表包含用于 [CreatureAI](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/AI/ScriptedAI/ScriptedCreature.h#L159) 的路径点路径。

### GM '.wp' 命令概览

- ```.wp add``` [waypoint_data.id](waypoint_data#id)：为指定的路径 ID 添加一个新点。建议使用生物 GUID * 10 或 GUID * 100 作为路径 ID，但也可以是任意随机数字。
- ```.wp reload``` [waypoint_data.id](waypoint_data#id)：重新加载指定的路径 ID（对于新路径，必须在 ```.wp load``` 之前执行）。
- ```.wp load``` [waypoint_data.id](waypoint_data#id)：为选中的生物加载指定的路径 ID。
- ```.wp unload```：卸载所选生物的路径。
- ```.wp show on``` [waypoint_data.id](waypoint_data#id)：显示指定路径的所有路径点（需要开启 GM 才能实际看到）。如果未指定路径 ID，则显示所选生物的路径点。
- ```.wp show off```：隐藏所有可视路径点。
- ```.wp show info```：显示所选路径点的信息。
- ```.wp modify```：修改选中的路径点，选项：
  - ```del```：删除选中的路径点。
  - ```move```：将选中的路径点移动到 GM 所在的位置。
  - ```delay```：更改所选路径点的 [delay](waypoint_data#delay)。
  - ```action```：更改所选路径点的 [action](scripts#id)。
  - ```action_chance```：更改所选路径点的 [action_chance](waypoint_data#actionchance)。
  - ```move_type```：更改所选路径点的 [move_type](waypoint_data#movetype)（0：步行，1：奔跑，2：飞行）。
- ```.wp event```：修改路径点的 [动作](scripts#id)，选项：
  - ```add``` [guid](scripts#guid)：添加一个具有指定 GUID 的新动作（不要与生物 GUID 混淆！）。如果未指定 GUID，将自动生成一个新的。
  - ```listid``` [action](scripts#id)：显示指定动作 ID 的信息。
  - ```del``` [guid](scripts#guid)：删除具有指定 GUID 的动作。
  - ```mod``` [guid](scripts#guid)：修改具有指定 GUID 的动作，进一步选项：
    - ```setid``` [action](scripts#id)：设置新的动作 ID。
    - ```delay``` [delay](scripts#delay)：设置脚本激活前的特定延迟。
    - ```command``` [command](scripts#command)：为此脚本设置命令。
    - ```datalong``` [datalong](scripts#datalong)：为此脚本设置 datalong。
    - ```datalong2``` [datalong2](scripts#datalong2)：为此脚本设置 datalong2。
    - ```dataint``` [dataint](scripts#dataint)：为此脚本设置 dataint。
    - ```posx``` [posx](scripts#posx)：为此脚本设置 posx。
    - ```posy``` [posy](scripts#posy)：为此脚本设置 posy。
    - ```posz``` [posz](scripts#posz)：为此脚本设置 posz。
    - ```orientation``` [orientation](scripts#orientation)：为此脚本设置 orientation。

### 使用 GM '.wp' 命令创建路径的示例

示例生物 GUID：1234567，示例路径 ID：123456700

- 使用以下命令创建一个宏 'wp1'：
  ```
  .wp add 123456700
  ```
- 使用以下命令创建一个宏 'wp2'：
  ```
  .wp reload 123456700
  .wp load 123456700
  ```
- 使用以下命令创建一个宏 'wp3'：
  ```
  .wp show on 123456700
  ```
- 使用以下命令创建一个宏 'wp4'：
  ```
  .wp show off 123456700
  ```
- 传送到生物处：
  ```
  .go creature 1234567
  ```
- 使用宏 'wp1'
- 创建路径：
  - 移动到下一个路径点应该所在的位置，然后使用宏 'wp1'
  - 重复操作，直到所有路径点都设置完毕（别忘了还要创建一条回到起始位置的路径）
  - 使用宏 'wp3' 和 'wp4' 来显示/隐藏路径（需要开启 GM 才能实际看到路径）
  - 确保路径点彼此之间不要相距太远，尤其是当生物要翻越山丘等地形时，因为它会尝试直接移动到下一个路径点，即使这意味着会穿过地面
- 选中生物并使用宏 'wp2'；它现在应该开始移动了

### 一些有用的 SQL 语句

#### 删除路径

- 选中生物，然后卸载路径：
  ```
  .wp unload
  ```

- 从数据库中删除路径，例如 123456700：
  ```sql
  DELETE FROM `waypoint_data` WHERE `id` = 123456700;
  ```

#### 将路径点从 'waypoint_data' 迁移到 'waypoints'（SmartAI）

如果你需要用于 SmartAI 的路径点，则必须将 [waypoint_data](waypoint_data) 表中的路径点复制到 [waypoints](waypoints) 表中，然后删除原始路径点（如果之前已加载，则通过 ```.wp unload``` 为生物卸载该路径）。以下是路径 123456700 的示例：
```sql
INSERT INTO `waypoints` (`entry`,`pointid`,`position_x`,`position_y`,`position_z`)
SELECT `id`,`point`,`position_x`,`position_y`,`position_z` FROM `waypoint_data` WHERE `id` = 123456700;
DELETE FROM `waypoint_data` WHERE `id` = 123456700;
```

#### 将路径点从 'waypoint_data' 迁移到 'script_waypoint'（CreatureAI）

与上述相同，不过这次是迁移到 [script_waypoint](script_waypoint) 而不是 [waypoints](waypoints)。[script_waypoint](script_waypoint) 的 entry 必须是 [creature_template.entry](creature_template#entry)，以下以 1234567 为例：
```sql
INSERT INTO `script_waypoint` (`entry`,`pointid`,`location_x`,`location_y`,`location_z`)
SELECT 1234567 AS `entry`,`point`,`position_x`,`position_y`,`position_z` FROM `waypoint_data` WHERE `id` = 123456700;
DELETE FROM `waypoint_data` WHERE `id` = 123456700;

```
如果之前已为生物加载过该路径，别忘了将其卸载。

### 路径点寻路最佳实践
在沿斜坡创建路径时，通过保持视线（line-of-sight）可以最大限度地减少地面穿插（ground clipping）。

![waypoints](https://i.imgur.com/s045BKp.png)
