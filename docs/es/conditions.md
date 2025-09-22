# Condiciones

[<-Volver a:World](database-world)

**Tabla \`conditions\`**

Esta tabla le permite definir condiciones para varios sistemas: chismes, botín, etc.

**Table Structure**

<table>
<tbody>
<tr class="odd">
<td><p><strong>Campo</strong></p></td>
<td><p><strong>Tipo</strong></p></td>
<td><p><strong>Atributos</strong></p></td>
<td><p><strong>Llave</strong></p></td>
<td><p><strong>Nulo</strong></p></td>
<td><p><strong>Por defecto</strong></p></td>
<td><p><strong>Extra</strong></p></td>
<td><p><strong>Comentario</strong></p></td>
</tr>
<tr class="even">
<td><p><a href="#sourcetypeorreferenceid">SourceTypeOrReferenceId</a></p></td>
<td><p>MEDIUMINT</p></td>
<td><p>SIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="odd">
<td><p><a href="#sourcegroup">SourceGroup</a></p></td>
<td><p>MEDIUMINT</p></td>
<td><p>UNSIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="even">
<td><p><a href="#sourceentry">SourceEntry</a></p></td>
<td><p>MEDIUMINT</p></td>
<td><p>SIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="odd">
<td><p><a href="#condition_source_type_smart_event=22">SourceId</a></p></td>
<td><p>INT</p></td>
<td><p>SIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><a href="http://www.azerothcore.org/wiki/smart_scripts#source_type">smart_scripts.source_type</a> <strong>||</strong> 0 para todo lo demás</p></td>
</tr>
<tr class="even">
<td><p><a href="#elsegroup">ElseGroup</a></p></td>
<td><p>MEDIUMINT</p></td>
<td><p>UNSIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="odd">
<td><p><a href="#conditiontypeorreference">ConditionTypeOrReference</a></p></td>
<td><p>MEDIUMINT</p></td>
<td><p>SIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="even">
<td><p><a href="#conditiontarget">ConditionTarget</a></p></td>
<td><p>TINYINT</p></td>
<td><p>UNSIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="odd">
<td><p><a href="#conditionvalue1">ConditionValue1</a></p></td>
<td><p>INT</p></td>
<td><p>UNSIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="even">
<td><p><a href="#conditionvalue2">ConditionValue2</a></p></td>
<td><p>INT</p></td>
<td><p>UNSIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="odd">
<td><p><a href="#conditionvalue3">ConditionValue3</a></p></td>
<td><p>INT</p></td>
<td><p>UNSIGNED</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="even">
<td><p><a href="#negativecondition">NegativeCondition</a></p></td>
<td><p>TINYINT</p></td>
<td><p>UNSIGNED</p></td>
<td><p><br />
</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p>Boolean 0 or 1 (if <a href="#negativecondition">NegativeCondition</a></p></td>
</tr>
<tr class="odd">
<td><p><a href="#errortype">ErrorType</a></p></td>
<td><p>MEDIUMINT</p></td>
<td><p>UNSIGNED</p></td>
<td><p><br />
</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="even">
<td><p><a href="#errortextid">ErrorTextId</a></p></td>
<td><p>MEDIUMINT</p></td>
<td><p>UNSIGNED</p></td>
<td><p><br />
</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="odd">
<td><p><a href="#scriptname">ScriptName</a></p></td>
<td><p>char(64)</p></td>
<td><p>SIGNED</p></td>
<td><p><br />
</p></td>
<td><p>NO</p></td>
<td><p>' '</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="even">
<td><p><a href="#comment">Comment</a></p></td>
<td><p>VARCHAR(255)</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
<td><p>YES</p></td>
<td><p>NULL</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
</tbody>
</table>

**Descripción de los campos**

### SourceTypeOrReferenceId

Si es negativo, entonces es una plantilla de referencia.

<table>
<thead>
<tr class="header">
<th><h3 id="conditions-SourceTypeOrReferenceId.1">SourceTypeOrReferenceId</h3></th>
<th>ID</th>
<th>SourceGroup</th>
<th>SourceEntry</th>
<th><a href="http://www.azerothcore.org/wiki/conditions#condition_source_type_smart_event=22">SourceId</a></th>
<th>ConditionTarget</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_NONE</td>
<td>0</td>
<td><strong><a href="#referencetemplates">Ver PLANTILLAS DE REFERENCIA</a></strong></td>
<td>(PLANTILLAS DE REFERENCIA)</td>
<td>Siempre 0</td>
<td>(Vea abajo)</td>
<td><strong>Solo se usa en <a href="#referencetemplates">Plantillas de referencia. Ver más abajo.</a></strong></td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_CREATURE_LOOT_TEMPLATE</td>
<td>1</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">creature_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_DISENCHANT_LOOT_TEMPLATE</td>
<td>2</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">disenchant_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_FISHING_LOOT_TEMPLATE</td>
<td>3</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">fishing_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_GAMEOBJECT_LOOT_TEMPLATE</td>
<td>4</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">gameobject_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_ITEM_LOOT_TEMPLATE</td>
<td>5</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">item_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_MAIL_LOOT_TEMPLATE</td>
<td>6</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">mail_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_MILLING_LOOT_TEMPLATE</td>
<td>7</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">milling_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_PICKPOCKETING_LOOT_TEMPLATE</td>
<td>8</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">pickpocketing_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_PROSPECTING_LOOT_TEMPLATE</td>
<td>9</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">prospecting_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_REFERENCE_LOOT_TEMPLATE</td>
<td>10</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_SKINNING_LOOT_TEMPLATE</td>
<td>11</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">skinning_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_SPELL_LOOT_TEMPLATE</td>
<td>12</td>
<td><a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Entry">spell_loot_template.Entry o reference_loot_template.Entry</a></td>
<td>item id (<a href="http://www.azerothcore.org/wiki/loot_template#loot_template-Item">_loot_template.Item o reference_loot_template.Item)</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="even">
<td><br />
CONDITION_SOURCE_TYPE_SPELL_IMPLICIT_TARGET</td>
<td><br />
13</td>
<td>Máscara de efectos que se verán afectados por la condición:<br />
1 = EFFECT_0, 2 = EFFECT_1, 4 = EFFECT_2</td>
<td>Identificador de hechizo de  <a href="Spell">Spell.dbc</a></td>
<td>Siempre 0</td>
<td><p>0 : Objetivo potencial del hechizo<br />
1 : Lanzador de hechizos</p></td>
<td>No uses Wowhead para obtener la cantidad de efectos, los datos de Wowhead a veces no coinciden con la cantidad de efectos reales.</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_GOSSIP_MENU</td>
<td>14</td>
<td><a href="http://www.azerothcore.org/wiki/gossip_menu#MenuID">gossip_menu.MenuID</a></td>
<td><a href="http://www.azerothcore.org/wiki/gossip_menu#TextID">gossip_menu.TextID</a> (points to npc_text.ID)</td>
<td>Siempre 0</td>
<td><p>0 = Jugador<br />
1 = Objeto mundial</p></td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_GOSSIP_MENU_OPTION</td>
<td>15</td>
<td><a href="http://www.azerothcore.org/wiki/gossip_menu_option#MenuID">gossip_menu_option.MenuID</a></td>
<td><a href="http://www.azerothcore.org/wiki/gossip_menu_option#OptionID">gossip_menu_option.OptionID</a></td>
<td>Siempre 0</td>
<td><p>0 = Jugador<br />
1 = Objeto mundial</p></td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_CREATURE_TEMPLATE_VEHICLE</td>
<td>16</td>
<td>Siempre 0</td>
<td>entrada de criatura (<a href="http://www.azerothcore.org/wiki/creature_template#creature_template-entry">creature_template.entry</a>)</td>
<td>Siempre 0</td>
<td><p>0 = Jugador montando vehículo<br />
1 = criatura del vehículo</p></td>
<td><br />
</td>
</tr>
<tr class="even">
<td><br />
<br />
<br />
<br />
<br />
CONDITION_SOURCE_TYPE_SPELL</td>
<td><br />
<br />
<br />
<br />
<br />
17</td>
<td>Siempre 0</td>
<td><br />
<br />
<br />
<br />
<br />
Identificador de hechizo de <a href="http://www.azerothcore.org/wiki/Spell">Spell.dbc</a></td>
<td>Siempre 0</td>
<td><br />
<br />
<br />
0 = Lanzador de hechizos<br />
1 = Objetivo explícito del hechizo (solo para hechizos que tienen en cuenta el objeto seleccionado por el lanzador)</td>
<td><ul>
<li>Este tipo de fuente te permite definir requisitos de lanzador/objetivo explícito para que se lance el hechizo.</li>
<li>El objetivo explícito del hechizo es el objetivo que selecciona el jugador durante el lanzamiento, no todos los hechizos tienen en cuenta ese objetivo. Los objetivos no explícitos del hechizo (los que selecciona el hechizo, como el área o los objetivos cercanos, por ejemplo) no se ven afectados por este tipo de fuente de condición; si quieres afectarlos, utiliza CONDITION_SOURCE_TYPE_SPELL_IMPLICIT_TARGET en su lugar.</li>
<li>Si estás buscando el antiguo CONDITION_SOURCE_TYPE_ITEM_REQUIRED_TARGET, utiliza este tipo de fuente de condición en su lugar (ConditionTarget = 1 te permite establecer requisitos para un hechizo determinado, por lo que para usar este tipo de condición necesitas el id del hechizo lanzado al usar el objeto).</li>
<li>Remember that conditions with the same ElseGroup value will be used to make logical AND check, so to allow different targets for the same spell effect you have to set ElseGroup respectively.</li>
</ul></td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_SPELL_CLICK_EVENT</td>
<td>18</td>
<td>entrada de criatura (<a href="http://www.azerothcore.org/wiki/npc_spellclick_spells#npc_entry">npc_spellclick_spells.npc_entry</a>)</td>
<td>Spell (<a href="http://www.azerothcore.org/wiki/npc_spellclick_spells#spell_id">npc_spellclick_spells.spell_id</a>)</td>
<td>Siempre 0</td>
<td>0 = Taconeador<br />
1 = Hechizo Hacer clic en el objetivo (clicker)</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_QUEST_AVAILABLE</td>
<td>19</td>
<td>Siempre 0</td>
<td><a href="http://www.azerothcore.org/wiki/quest_template#id">ID de misión</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td>Se debe cumplir la condición para que la misión esté disponible para el jugador.</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_UNUSED_20</td>
<td>20</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><br />
CONDITION_SOURCE_TYPE_VEHICLE_SPELL</td>
<td><br />
21</td>
<td>entrada de criatura (<a href="http://www.azerothcore.org/wiki/creature_template#creature_template-entry">creature_template.entry</a>)</td>
<td><br />
Identificador de hechizo de <a href="http://www.azerothcore.org/wiki/Spell">Spell.dbc</a></td>
<td>Siempre 0</td>
<td>0 = Jugador para el que se muestra la barra de hechizos
1 = criatura del vehículo</td>
<td><br />
This will show or hide spells in vehicle spell bar.</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_SMART_EVENT</td>
<td>22</td>
<td>ID (<a href="http://www.azerothcore.org/wiki/smart_scripts#id">smart_scripts.id</a>) + 1</td>
<td>EntryOrGuid (<a href="http://www.azerothcore.org/wiki/smart_scripts#entryorguid">smart_scripts.entryorguid</a>)</td>
<td>SourceType (<a href="http://www.azerothcore.org/wiki/smart_scripts#source_type">smart_scripts.source_type</a>)</td>
<td>0 = Invocador<br />
1 = Objeto</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_NPC_VENDOR</td>
<td>23</td>
<td>entrada del proveedor (<a href="http://www.azerothcore.org/wiki/npc_vendor#entry">npc_vendor.entry</a>)</td>
<td>entrada de artículo (<a href="http://www.azerothcore.org/wiki/npc_vendor#item">npc_vendor.item</a>)</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_SPELL_PROC</td>
<td>24</td>
<td>Siempre 0</td>
<td>ID del hechizo del aura que activa el procedimiento</td>
<td>Siempre 0</td>
<td>0 = Actor<br />
1 = Objetivo de acción</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_PLAYER_LOOT_TEMPLATE</td>
<td>28</td>
<td>player_loot_template.entry</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_CREATURE_RESPAWN</td>
<td>29</td>
<td>enum-no-details|29</td>
<td>enum-no-details|29</td>
<td>enum-no-details|29</td>
<td>enum-no-details|29</td>
<td><br />
</td>
</tr>
<tr class="even">
<td>CONDITION_SOURCE_TYPE_CREATURE_VISIBILITY</td>
<td>29</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td>0/1</td>
<td><br />
</td>
</tr>
<tr class="odd">
<td>CONDITION_SOURCE_TYPE_MAX</td>
<td>31</td>
<td><br />
</td>
<td><br />
</td>
<td><br />
</td>
<td><br />
</td>
<td>(Marcador de posición)</td>
</tr>
</tbody>
</table>

### SourceGroup

Ver arriba.

### SourceEntry

Ver arriba.

### ElseGroup

Permite crear condiciones agrupadas: todas las entradas que pertenecen a la misma condición (mismo [SourceType](#conditions-SourceTypeOrReferenceId), [SourceGroup](#conditions-SourceGroup) y [SourceEntry](#conditions-SourceEntry)) que comparten el mismo número en ElseGroup, definen un grupo. La **condición completa** se cumple cuando se cumple **cualquiera de sus grupos** (OR lógico). El **grupo** se cumple cuando se cumplen **todas sus entradas** (AND lógico).

Ejemplo:

Dos condiciones con el mismo SourceType, SourceGroup y SourceEntry pero con una Condición diferente, la primera tiene ElseGroup = 1 y la segunda tiene ElseGroup = 2, esto crea un OR lógico.

Dos condiciones con el mismo SourceType, SourceGroup y SourceEntry pero con una condición diferente, ambas tienen ElseGroup = 1, esto crea un AND lógico.

### ConditionTypeOrReference
 

<table>
<thead>
<tr class="header">
<th>ConditionTypeOrReference (name)</th>
<th>Value</th>
<th>ConditionValue1</th>
<th>ConditionValue2</th>
<th>ConditionValue3</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CONDITION_NONE</td>
<td>0</td>
<td>(Nunca usado)</td>
<td>(Nunca usado)</td>
<td>(Nunca usado)</td>
</tr>
<tr class="even">
<td>CONDITION_AURA</td>
<td>1</td>
<td>Identificador de hechizo de <a href="http://www.azerothcore.org/wiki/Spell">Spell.dbc</a></td>
<td>Índice de efectos (0-2)</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_ITEM</td>
<td>2</td>
<td>entrada de artículo (<a href="http://www.azerothcore.org/wiki/item_template#entry">item_template.entry</a>)</td>
<td>recuento de artículos</td>
<td>0 = no en el banco, 1 = en el banco</td>
</tr>
<tr class="even">
<td>CONDITION_ITEM_EQUIPPED</td>
<td>3</td>
<td>entrada de artículo (<a href="http://www.azerothcore.org/wiki/item_template#entry">item_template.entry</a>)</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_ZONEID</td>
<td>4</td>
<td>ID de zona donde esta condición será verdadera.</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_REPUTATION_RANK</td>
<td>5</td>
<td><p><br />
<br />
<br />
<br />
<br />
ID de plantilla de facción de <a href="http://www.azerothcore.org/wiki/Faction">Faction.dbc</a></p></td>
<td><pre><code>Rango:
  1 = Odiado
  2 = Hostil
  4 = Antipático
  8 = Neutral
 16 = Amistoso
 32 = Honored
 64 = Venerado
128 = Exaltado</code></pre>
<p>Sume los rangos de destino para que la condición sea verdadera para todos esos rangos.</p></td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_TEAM</td>
<td>6</td>
<td>Identificación del equipo: Alliance = 469 / Horde = 67</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_SKILL</td>
<td>7</td>
<td>Habilidad requerida. Ver <a href="http://www.azerothcore.org/wiki/SkillLine">SkillLine.dbc</a> .</td>
<td>Valor del rango de habilidad (por ejemplo, de 1 a 450 para la rama 3.3.5)</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_QUESTREWARDED</td>
<td>8</td>
<td>ID de misión - ver <a href="http://www.azerothcore.org/wiki/quest_template#id">quest_template.id</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_QUESTTAKEN</td>
<td>9</td>
<td>ID de misión - ver <a href="http://www.azerothcore.org/wiki/quest_template#id">quest_template.id</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_DRUNKENSTATE</td>
<td>10</td>
<td>Sobrio = 0, Achispado = 1, Ebrio = 2, Colocado = 3</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_WORLD_STATE</td>
<td>11</td>
<td>Índice de estado mundial</td>
<td>Valor del estado mundial</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_ACTIVE_EVENT</td>
<td>12</td>
<td>Entrada al evento (<a href="http://www.azerothcore.org/wiki/game_event#evententry">game_event.eventEntry</a>)</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_INSTANCE_INFO</td>
<td>13</td>
<td><strong><br />
entrada</strong> (ver los archivos de script fuente correspondientes para obtener información)</td>
<td><strong><br />
datos</strong> (consulte los archivos fuente del script correspondiente para obtener más información)</td>
<td><p>0 = INSTANCE_INFO_DATA</p>
<p>1 = INSTANCE_INFO_GUID_DATA</p>
<p>2 = INSTANCE_INFO_BOSS_STATE</p>
<p>3 = INSTANCE_INFO_DATA64</p></td>
</tr>
<tr class="odd">
<td>CONDITION_QUEST_NONE</td>
<td>14</td>
<td>ID de misión - ver <a href="http://www.azerothcore.org/wiki/quest_template#id">quest_template.id</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_CLASS</td>
<td>15</td>
<td>Máscara de clase de <a href="http://www.azerothcore.org/wiki/chrclasses">ChrClasses.dbc</a><br />
Agregue banderas juntas para todas las clases donde la condición es verdadera.</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_RACE</td>
<td>16</td>
<td>Máscara de carrera de <a href="http://www.azerothcore.org/wiki/chrraces">ChrRaces.dbc</a> .<br />
Agregue banderas para todas las carreras donde la condición sea verdadera.</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_ACHIEVEMENT</td>
<td>17</td>
<td>Identificación del logro de <a href="http://www.azerothcore.org/wiki/Achievement">Achievement.dbc</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_TITLE</td>
<td>18</td>
<td>Identificación del título de <a href="http://www.azerothcore.org/wiki/CharTitles">CharTitles.dbc</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_SPAWNMASK</td>
<td>19</td>
<td>Máscara de aparición de<br />
<a href="http://www.azerothcore.org/wiki/creature#spawnmask">Creature.spawnMask</a> / <a href="http://www.azerothcore.org/wiki/gameobject#spawnmask">Gameobject.spawnMask</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_GENDER</td>
<td>20</td>
<td>0 = Masculino, 1 = Femenino, 2 = Ninguno</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_UNIT_STATE</td>
<td>21</td>
<td>Estado de la unidad (<a href="https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Entities/Unit/Unit.h#L498">enumeración de Unit.h</a>)</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_MAPID</td>
<td>22</td>
<td><p>Entrada del mapa desde Map.dbc</p>
<p>(0 = Eastern Kingdoms, 1 = Kalimdor, - etcétera.)</p></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_AREAID</td>
<td>23</td>
<td>ID de área de AreaTable.dbc</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_CREATURE_TYPE</td>
<td>24</td>
<td><p>Tipo de criatura de <a href="http://www.azerothcore.org/wiki/creature_template#creature_template-type">creature_template.type</a></p>
<p>Verdadero si creature_template.type == ConditionValue1</p></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_SPELL</td>
<td>25</td>
<td>Identificador de hechizo de <a href="http://www.azerothcore.org/wiki/Spell">Spell.dbc</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_PHASEMASK</td>
<td>26</td>
<td>valor de máscara de fase</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_LEVEL</td>
<td>27</td>
<td>Nivel de jugador (1-80 en 3.3.5)</td>
<td>Opcional: 0 = El nivel debe ser igual, 1 = El nivel debe ser superior, 2 = El nivel debe ser inferior,<br />
3 = El nivel debe ser superior o igual, 4 = El nivel debe ser inferior o igual.</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_QUEST_COMPLETE</td>
<td>28</td>
<td>ID de misión - ver <a href="http://www.azerothcore.org/wiki/quest_template#id">quest_template.id</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_NEAR_CREATURE</td>
<td>29</td>
<td>Entrada de criaturas from <a href="http://www.azerothcore.org/wiki/creature_template#creature_template-entry">creature_template.entry</a></td>
<td>Distancia en yardas</td>
<td>Vivo = 0 / Muerto = 1</td>
</tr>
<tr class="odd">
<td>CONDITION_NEAR_GAMEOBJECT</td>
<td>30</td>
<td>Entrada de objeto de juego desde <a href="http://www.azerothcore.org/wiki/gameobject_template#entry">gameobject_template.entry</a></td>
<td>Distancia en yardas</td>
<td>Go State<br/><br/> 0 = ignorar, 1 = Listo, 2 = No estoy listo</td>
</tr>
<tr class="even">
<td>CONDITION_OBJECT_ENTRY_GUID</td>
<td>31</td>
<td><p>ID de tipo. Tipos de objeto disponibles:<br />
3 : TYPEID_UNIT<br />
4 : TYPEID_PLAYER<br />
5 : TYPEID_GAMEOBJECT<br />
7 : TYPEID_CORPSE (cadáver del jugador, después de la liberación del espíritu)</p></td>
<td><p><br />
0 = Cualquier objeto del tipo ID dado<br />
si TypeID = TYPEID_UNIT =&gt; Entrada de criatura desde <a href="http://www.azerothcore.org/wiki/creature_template#creature_template-entry">creature_template.entry<br />
si TypeID = TYPEID_GAMEOBJECT =&gt; Entrada de objeto de juego desde </a><a href="http://www.azerothcore.org/wiki/gameobject_template#entry">gameobject_template.entry</a></p></td>
<td><p><br />
0 = Cualquier objeto del tipo dado</p>
<p>1 - 500k : GUID de criatura/objeto de juego</p></td>
</tr>
<tr class="odd">
<td>CONDITION_TYPE_MASK</td>
<td>32</td>
<td><p>Máscara de tipo: una máscara de bits de los siguientes tipos de objetos:<br />
0x0008 - TYPEMASK_UNIT (8)<br />
0x0010 - TYPEMASK_PLAYER (16)<br />
0x0020 - TYPEMASK_GAMEOBJECT (32)<br />
0x0080 - TYPEMASK_CORPSE (Cadáver del jugador después de la liberación del espíritu) (128)</p></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_RELATION_TO</td>
<td>33</td>
<td><p>Objetivo con el que se comprueba la relación.<br />
- uno de los ConditionTargets disponibles en la actualidad <a href="#sourcetypeorreferenceid">Tipo de fuente</a></p></td>
<td><p>Tipo de relación: define la relación del objetivo de condición actual con el objetivo especificado en el valor de condición 1.<br />
0 - RELATION_SELF<br />
1 - RELATION_IN_PARTY<br />
2 - RELATION_IN_RAID_OR_PARTY<br />
3 - RELATION_OWNED_BY (El objetivo de condición es propiedad de Condition Value1)<br />
4 - RELATION_PASSENGER_OF (El objetivo de condición es pasajero del valor de condición 1)<br />
5 - RELATION_CREATED_BY (ConditionTarget es invocado por ConditionValue1)</p></td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_REACTION_TO</td>
<td>34</td>
<td><p>Objetivo al que se comprueba la reacción.<br />
- uno de los ConditionTargets disponibles en la actualidad <a href="#sourcetypeorreferenceid">SourceType</a></p></td>
<td><pre><code>rankMask: Esta máscara de bits define las reacciones del ConditionTarget actual al objetivo especificado en ConditionValue1 (que están permitidas).
Las banderas para las reacciones son:
  1 = Odiado
  2 = Hostil
  4 = Antipático
  8 = Neutral
 16 = Amistoso
 32 = Honrado
 64 = Venerado
128 = Exaltado</code></pre></td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_DISTANCE_TO</td>
<td>35</td>
<td><p>Objetivo al que se comprueba la distancia<br />
- Uno de los ConditionTargets disponibles en la actualidad <a href="#sourcetypeorreferenceid">SourceType</a></p></td>
<td>Distancia.<br />
Define la distancia entre el objetivo de condición actual y el objetivo especificado en el valor de condición 1</td>
<td><p>ComparisionType:<br />
0 = La distancia debe ser igual a ConditionValue2<br />
1 = La distancia debe ser mayor que ConditionValue2<br />
2 = La distancia debe ser menor que ConditionValue2<br />
3 = La distancia debe ser igual o mayor que ConditionValue2<br />
4 = La distancia debe ser igual o menor que ConditionValue2</p></td>
</tr>
<tr class="odd">
<td>CONDITION_ALIVE</td>
<td>36</td>
<td>Siempre 0 - Utilice NegativeCondition y las siguientes configuraciones:
<p>Condición negativa = 0 si el objetivo necesita estar VIVO.<br />
Condición Negativa = 1 si el objetivo debe estar MUERTO.<br />
NOTA: Un cadáver de criatura y una criatura que _parece_ muerta<br />
Son dos cosas diferentes. Una está realmente muerta<br />
y el otro simplemente usa un gesto para parecer muerto.</p></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_HP_VAL</td>
<td>37</td>
<td>Valor de HP</td>
<td>Tipo de comparación:
<ul>
<li>0 = Los HP deben ser iguales</li>
<li>1 = Los HP deben ser más altos</li>
<li>2 = Los HP deben ser menores</li>
<li>3 = Los HP deben ser iguales o superiores</li>
<li>4 = Los HP deben ser iguales o menores</li>
</ul></td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_HP_PCT</td>
<td>38</td>
<td>Porcentaje de HP máximo</td>
<td>Tipo de comparación:
<ul>
<li>0 = El porcentaje del HP máximo debe ser igual</li>
<li>1 = El porcentaje de HP máximo debe ser mayor</li>
<li>2 = El porcentaje de HP máximo debe ser menor</li>
<li>3 = El porcentaje del HP máximo debe ser igual o mayor</li>
<li>4 = El porcentaje del HP máximo debe ser igual o menor</li>
</ul></td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_REALM_ACHIEVEMENT</td>
<td>39</td>
<td>Identificación del logro de <a href="http://www.azerothcore.org/wiki/Achievement">Achievement.dbc</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_IN_WATER</td>
<td>40</td>
<td>Siempre 0 - Utilice NegativeCondition y las siguientes configuraciones:NegativeCondition = 0 si el objetivo debe estar en tierraNegativeCondition = 1 si el objetivo debe estar en el agua</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_STAND_STATE</td>
<td>42</td>
<td>StateType (exacto o cualquiera): 0 =<strong>Exacto</strong> estado utilizado en ConditionValue2 1 = <strong>Cualquier</strong> Tipo de estado en ConditionValue2</td>
<td>Estado de pie exacto o estado genérico (de pie/sentado), según el valor 10 = De pie 1 = Sentado</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_DAILY_QUEST_DONE</td>
<td>43</td>
<td>ID de misión - ver <a href="http://www.azerothcore.org/wiki/quest_template#id">quest_template.id</a></td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_CHARMED</td>
<td>44</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_PET_TYPE</td>
<td>45</td>
<td>mask</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_TAXI</td>
<td>46</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_QUESTSTATE</td>
<td>47</td>
<td>ID de misión - ver <a href="http://www.azerothcore.org/wiki/quest_template#id">quest_template.id</a></td>
<td>state_mask:
<li>1 = No tomado</li>
<li>2 = Terminado</li>
<li>8 = En curso</li>
<li>32 = Fallido</li>
<li>64 = Recompensado</li>
</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_QUEST_OBJECTIVE_PROGRESS</td>
<td>48</td>
<td>ID de misión - ver <a href="http://www.azerothcore.org/wiki/quest_template#id">quest_template.id</a></td>
<td>ID del objetivo de la misión: ver <a href="http://www.azerothcore.org/wiki/quest_template#requirednpcorgo">quest_template.RequiredNpcOrGo</a></td>
<td>Conteo de objetivos de la misión</td>
</tr>
<tr class="even">
<td>CONDITION_DIFFICULTY_ID</td>
<td>49</td>
<td>Dificultad</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_QUEST_SATISFY_EXCLUSIVE</td>
<td>101</td>
<td>quest_id</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="even">
<td>CONDITION_HAS_AURA_TYPE</td>
<td>102</td>
<td>aura_type</td>
<td>Siempre 0</td>
<td>Siempre 0</td>
</tr>
<tr class="odd">
<td>CONDITION_WORLD_SCRIPT</td>
<td>103</td>
<td>conditionId</td>
<td>state</td>
<td>Siempre 0</td>
</tr>
</tbody>
</table>

### ConditionTarget

Permite seleccionar un objeto cuyas condiciones se comprobarán. Los objetos disponibles dependen de SourceTypeOrReferenceId; para más detalles, consulte la referencia del tipo de fuente correspondiente.

### ConditionValue1

Vea abajo

### ConditionValue2

Vea abajo

### ConditionValue3

Vea abajo

### NegativeCondition

Si se establece en 1, la condición será "invertida".

Ejemplo: CONDITION\_AURA con NegativeCondition será verdadero cuando el jugador NO tenga el aura.

### ErrorType

Id de [/src/server/game/Miscellaneous/SharedDefines.h#L830](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Miscellaneous/SharedDefines.h#L830). Will be displayed only for the below condition [source type](#conditions-SourceTypeOrReferenceId):

CONDITION\_SOURCE\_TYPE\_SPELL = 17

### ErrorTextId

Identificación de [/src/server/game/Miscellaneous/SharedDefines.h#L1024](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Miscellaneous/SharedDefines.h#L1024). Will be displayed only for the below condition [source type](#conditions-SourceTypeOrReferenceId):

CONDITION\_SOURCE\_TYPE\_SPELL = 17

(ErrorType debe ser SPELL\_FAILED\_CUSTOM\_ERROR (209) de lo contrario 0)

### ScriptName

El nombre del script que utiliza esta condición, si lo hay.

### Comment

Explicación de esta condición o referencia.

### Explicación de los tipos de condiciones

El contenido de los campos [SourceGroup](#conditions-SourceGroup) y [SourceEntry](#conditions-SourceEntry) depende de [SourceTypeOrReferenceId](#conditions-SourceTypeOrReferenceId)

\***CONDITION\_SOURCE\_TYPE\_NONE = 0**

**Solo se usa en plantillas de referencia. Ver más abajo.**

\***CONDITION\_SOURCE\_TYPE\_ \* \_LOOT\_TEMPLATE = 1 - 12**
\***SourceGroup: entrada de botín (**\_loot\_template.Entry or Reference\_loot\_template.Entry)
\***SourceEntry: identificación del artículo (**\_loot\_template.Item or Reference\_loot\_template.Item)

-   -   ConditionTarget: Siempre 0

*Ejemplo: si usa el tipo 1 (criatura\_botín\_plantilla), utilice los campos de entrada y elemento de esa tabla.*

\***CONDITION\_SOURCE\_TYPE\_SPELL\_IMPLICIT\_TARGET = 13**

-   -   SourceGroup:máscara de efectos que se verán afectados por la condición (1 - EFFECT\_0, 2 - EFFECT\_1, 4 - EFFECT\_2 - no use wowhead para obtener el número de efectos, los datos de wowhead a veces no coinciden con el número de efecto real)
    -   SourceEntry: hechizo (Id. de hechizo de [Spell.dbc](Spell).)
    -   ConditionTarget:
        -   0 - Objetivo potencial del hechizo
        -   1 - Lanzador del hechizo

Notas:

-   Este tipo de fuente de condición permite definir un filtro para los posibles objetivos de efectos de hechizo, de modo que solo se seleccionarán como objetivos implícitos del hechizo los objetivos que cumplan la condición. Solo se pueden filtrar los tipos de objetivo *ÁREA*, *CERCA* y *CONO*. Este tipo de fuente afecta solo a los objetivos seleccionados por el hechizo; no afecta al objetivo del hechizo seleccionado por el jugador al lanzarlo. Para afectar a ese objetivo, usa CONDITION\_SOURCE\_TYPE\_SPELL.
-   Para restringir los objetivos a solo los jugadores, use CONDITION\_TYPEMASK con TYPEMASK\_PLAYER + TYPEMASK\_CORPSE para permitir apuntar a jugadores muertos.
-   Recuerda que las condiciones con el mismo valor ElseGroup se utilizarán para realizar la verificación AND lógica, por lo que para permitir diferentes objetivos para el mismo efecto de hechizo debes configurar ElseGroup respectivamente.
-   Si está buscando la antigua CONDITION\_SOURCE\_TYPE\_SPELL\_SCRIPT\_TARGET - utilice este tipo de fuente de condición en su lugar.

\***CONDITION\_SOURCE\_TYPE\_GOSSIP\_MENU = 14**

-   -   SourceGroup: entrada del menú de chismes ([gossip\_menu.MenuID](http://www.azerothcore.org/wiki/gossip_menu#MenuID))
    -   SourceEntry: texto de identificación del menú de chismes ([gossip\_menu.TextID](http://www.azerothcore.org/wiki/gossip_menu#TextID))
    -   ConditionTarget:
        -   0 - Reproductor para el que se muestra el texto de chismes
        -   1 - WorldObject proporcionando chismes

\***CONDITION\_SOURCE\_TYPE\_GOSSIP\_MENU\_OPTION = 15**

-   -   SourceGroup: entrada del menú de chismes ([gossip\_menu\_option.MenuID](http://www.azerothcore.org/wiki/gossip_menu_option#MenuID))
    -   SourceEntry: Opción de menú de chismes ([gossip\_menu\_option.OptionID](http://www.azerothcore.org/wiki/gossip_menu_option#OptionID))
    -   ConditionTarget:
        -   0 - Reproductor para el que se muestra el texto de chismes
        -   1 - WorldObject proporcionando chismes

\***CONDITION\_SOURCE\_TYPE\_CREATURE\_TEMPLATE\_VEHICLE = 16**

-   -   SourceGroup: Siempre 0
    -   SourceEntry: entrada de criatura ([creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry))
    -   ConditionTarget:
        -   0 - Jugador montando un vehículo
        -   1 - Criatura del vehículo

Nota: La criatura debe ser un vehículo. Ejemplo: Si se usa con CONDITION\_AREA, el jugador se bajará del vehículo si el jugador montado abandona esa área.

\***CONDITION\_SOURCE\_TYPE\_SPELL = 17**

-   -   SourceGroup: Siempre 0
    -   SourceEntry: hechizo (Id. de hechizo de [Spell.dbc](Spell))
    -   ConditionTarget:
        -   0 - Caster of the spell
        -   1 - Explicit target of the spell (only for spells which take object selected by caster into account)

Notes:

-   this source type allows you to define caster/explicit target requirements for spell to be cast.
-   explicit target of the spell is the target which is selected by player during cast, not all spells take that target into account. non-explicit targets of the spell (the ones which are selected by spell like area or nearby targets for example) are not affected by this condition source type, if you want to affect those use CONDITION\_SOURCE\_TYPE\_SPELL\_IMPLICIT\_TARGET instead.
-   if you're looking for old CONDITION\_SOURCE\_TYPE\_ITEM\_REQUIRED\_TARGET - use this condition source type instead (ConditionTarget = 1 allows you to set requirements for a given spell, so to use this condition type you need spellid of the spell cast on item use)
-   remember that conditions with the same value ElseGroup will be used to make logical AND check, so to allow different targets for the same spell effect you have to set ElseGroup respectively.

\***CONDITION\_SOURCE\_TYPE\_SPELL\_CLICK\_EVENT = 18**

-   -   SourceGroup: entrada de criatura ([npc\_spellclick\_spells.npc\_entry](http://www.azerothcore.org/wiki/npc_spellclick_spells#npc_entry))
    -   SourceEntry: spell ([npc\_spellclick\_spells.spell\_id](http://www.azerothcore.org/wiki/npc_spellclick_spells#spell_id))
    -   ConditionTarget:
        -   0 - Clicker
        -   1 - Spellclick target (clickee)

\***CONDITION\_SOURCE\_TYPE\_QUEST\_ACCEPT = 19**

-   -   SourceGroup: ?
    -   SourceEntry: Quest [id](http://www.azerothcore.org/wiki/quest_template#id))
    -   ConditionTarget: Siempre 0

\***CONDITION\_SOURCE\_TYPE\_QUEST\_SHOW\_MARK = 20**

-   -   SourceGroup: ?
    -   SourceEntry: Quest [id](http://www.azerothcore.org/wiki/quest_template#id))
    -   ConditionTarget: Siempre 0

\***CONDITION\_SOURCE\_TYPE\_VEHICLE\_SPELL = 21**

-   -   SourceGroup: entrada de criatura ([creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry))
    -   SourceEntry: spell (Id. de hechizo de [Spell.dbc](Spell))
    -   ConditionTarget:
        -   0 - Jugador para el que se muestra la barra de hechizos
        -   1 - Criatura del vehículo

Nota: mostrará u ocultará hechizos en la barra de hechizos del vehículo.

\***CONDITION\_SOURCE\_TYPE\_SMART\_EVENT = 22**

-   -   SourceGroup: Id ([smart\_scripts.id](http://www.azerothcore.org/wiki/smart_scripts#id)) + 1
    -   SourceEntry: EntryOrGuid ([smart\_scripts.entryorguid](http://www.azerothcore.org/wiki/smart_scripts#entryorguid))
    -   SourceId: SourceType ([smart\_scripts.source\_type](http://www.azerothcore.org/wiki/smart_scripts#source_type))
    -   ConditionTarget:
        -   0 - Invocador
        -   1 - Objeto

\***CONDITION\_SOURCE\_TYPE\_NPC\_VENDOR = 23**

-   -   SourceGroup: entrada del proveedor ([npc\_vendor.entry](http://www.azerothcore.org/wiki/npc_vendor#entry))
    -   SourceEntry: entrada de artículo ([npc\_vendor.item](http://www.azerothcore.org/wiki/npc_vendor#item))
    -   SourceId: Siempre 0

\***CONDITION\_SOURCE\_TYPE\_SPELL\_PROC = 24**

-   -   SourceGroup: Siempre 0
    -   SourceEntry: Identificación del hechizo del aura que activa el procedimiento.
    -   ConditionTarget:
        -   0 - Actor
        -   1 - ActionTarget

### Explicación de los campos ConditionValueX

\***CONDITION\_NONE = 0**

**Nunca usado**

\***CONDITION\_AURA = 1**

-   -   ConditionValue1: hechizo (Id. de hechizo de [Spell.dbc](Spell))
    -   ConditionValue2: índice de efecto (0-2)
    -   ConditionValue3: Siempre 0

\***CONDITION\_ITEM = 2**

-   -   ConditionValue1: entrada de artículo ([item\_template.entry](http://www.azerothcore.org/wiki/item_template#entry))
    -   ConditionValue2: recuento de artículos
    -   ConditionValue3: ¿en el banco? (verdadero = 1)

\***CONDITION\_ITEM\_EQUIPPED = 3**

-   -   ConditionValue1: entrada de artículo ([item\_template.entry](http://www.azerothcore.org/wiki/item_template#entry))
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_ZONEID = 4**

-   -   ConditionValue1: ID de zona donde esta condición será verdadera
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_REPUTATION\_RANK = 5**

-   -   ConditionValue1: ID de plantilla de facción (de [Faction.dbc](Faction))
    -   ConditionValue2: Rango (Odiado - 1, Hostil - 2, Antipático - 4, Neutral - 8, Amistoso - 16, Honorable - 32, Venerado - 64, Exaltado - 128) Las banderas se pueden sumar para todos los rangos en los que la condición debe ser verdadera.
    -   ConditionValue3: Siempre 0

\***CONDITION\_TEAM = 6**

-   -   ConditionValue1: identificación del equipo (469 - Alliance, 67 - Horde)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_SKILL = 7**

-   -   ConditionValue1: habilidad requerida, ver [SkillLine.dbc](SkillLine)
    -   ConditionValue2: valor de la habilidad
    -   ConditionValue3: Siempre 0

\***CONDITION\_QUESTREWARDED = 8**

-   -   ConditionValue1: ([quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id))
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_QUESTTAKEN = 9**

-   -   ConditionValue1: ([quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id))
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_DRUNKENSTATE = 10**

-   -   ConditionValue1: Estado de ebriedad: 0 - sobrio; 1 - achispado, 2 - borracho, 3 - borracho
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0
    -   (Formerly AD\_COMMISSION\_AURA)

\***CONDITION\_WORLD\_STATE = 11**

-   -   ConditionValue1: índice de estado mundial
    -   ConditionValue2: valor del estado mundial
    -   ConditionValue3: Siempre 0

\***CONDITION\_ACTIVE\_EVENT= 12**

-   -   ConditionValue1: entrada al evento ([game\_event.eventEntry](http://www.azerothcore.org/wiki/game_event#evententry))
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_INSTANCE\_INFO = 13**

-   -   ConditionValue1: Entrada //ver los archivos fuente del script correspondiente para obtener más información
    -   ConditionValue2: datos //ver los archivos fuente del script correspondiente para obtener más información
    -   ConditionValue3: tipo:
        -   0 - INSTANCE\_INFO\_DATA
        -   1 - INSTANCE\_INFO\_GUID\_DATA
        -   2 - INSTANCE\_INFO\_BOSS\_STATE
        -   3 - INSTANCE\_INFO\_DATA64

\***CONDITION\_QUEST\_NONE = 14**

-   -   ConditionValue1: ([quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id))
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_CLASS = 15**

-   -   ConditionValue1: Máscara de clase. Sumar indicadores para todas las clases. La condición debe ser verdadera. Ver [ChrClasses.dbc](chrclasses)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_RACE = 16**

-   -   ConditionValue1: Máscara de carrera. Sumar banderas para todas las carreras. La condición debe ser verdadera. Ver [ChrRaces.dbc](chrraces)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_ACHIEVEMENT = 17**

-   -   ConditionValue1: Identificación del logro de [Achievement.dbc](Achievement)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_TITLE = 18**

-   -   ConditionValue1: ID de título de [CharTitles.dbc](CharTitles)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_SPAWNMASK = 19**

-   -   ConditionValue1: spawnMask (see [Gameobject.spawnMask](http://www.azerothcore.org/wiki/gameobject#spawnmask)/[Creature.spawnMask](http://www.azerothcore.org/wiki/creature#spawnmask))
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_GENDER = 20**

-   -   ConditionValue1: 0 = Masculino, 1 = Femenino, 2 = Ninguno
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_UNIT\_STATE = 21**

-   -   ConditionValue1: UnitState ([enum](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Entities/Unit/Unit.h#L451)) 
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_MAPID = 22**

-   -   ConditionValue1: Entrada del mapa
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_AREAID = 23**

-   -   ConditionValue1: Identificación de área
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_CREATURE\_TYPE = 24**

-   -   ConditionValue1: Tipo de criatura ([creature\_template.type](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)). La condición es verdadera si creature\_template.type == ConditionValue1
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_SPELL = 25**

-   -   ConditionValue1: hechizo (Id. de hechizo de [Spell.dbc](Spell))
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_PHASEMASK = 26**

-   -   ConditionValue1: valor de máscara de fase
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_LEVEL = 27**

-   -   ConditionValue1: Nivel de jugador
    -   ConditionValue2: Opcional
        - 0 = El nivel debe ser igual
        - 1 = El nivel debe ser mayor
        - 2 = El nivel debe ser menor
        - 3 = El nivel debe ser igual o mayor
        - 4 = El nivel debe ser igual o menor
    -   ConditionValue3: Siempre 0

\***CONDITION\_QUEST\_COMPLETE = 28**

-   -   ConditionValue1: Búsqueda [id](http://www.azerothcore.org/wiki/quest_template#id)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

*Solo si el jugador tiene todos los objetivos de la misión completados, pero aún no ha recibido la recompensa.*

\***CONDITION\_NEAR\_CREATURE = 29**

-   -   ConditionValue1: Criatura [entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)
    -   ConditionValue2: Distancia (yd)
    -   ConditionValue3: 0 = Vivo, 1 = Muerto

\***CONDITION\_NEAR\_GAMEOBJECT = 30**

-   -   ConditionValue1: Gameobject [entry](http://www.azerothcore.org/wiki/gameobject_template#entry)
    -   ConditionValue2: Distance (yd)
    -   ConditionValue3: GoState, 0 = ignore, 1 = Ready, 2 = Not Ready

\***CONDITION\_OBJECT\_ENTRY\_GUID= 31**

-   -   ConditionValue1: TypeID - tipos de objetos disponibles:
        -   3 - TYPEID\_UNIT
        -   4 - TYPEID\_PLAYER
        -   5 - TYPEID\_GAMEOBJECT
        -   7 - TYPEID\_CORPSE (Cadáver del jugador, después del espíritu liberado)
    -   ConditionValue2: Entrada
        -   0 para cualquier objeto del tipo dado
        -   [Entrada de objeto de juego](http://www.azerothcore.org/wiki/gameobject_template#entry) para TypeID = TYPEID\_GAMEOBJECT
        -   [Entrada de criatura](http://www.azerothcore.org/wiki/creature_template#creature_template-entry) para TypeID = TYPEID\_UNIT
    -   ConditionValue3 0 para cualquier objeto del tipo dado, cualquier otro valor que coincida con esa guía

\***CONDITION\_TYPE\_MASK= 32**

-   -   ConditionValue1: TypeMask: una máscara de bits de los siguientes tipos de objetos:
        -   0x0008 - TYPEMASK\_UNIT
        -   0x0010 - TYPEMASK\_PLAYER
        -   0x0020 - TYPEMASK\_GAMEOBJECT
        -   0x0080 - TYPEMASK\_CORPSE (Cadáver del jugador, después del espíritu liberado)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_RELATION\_TO= 33**

-   -   ConditionValue1: objetivo con el que se comprueba la relación: uno de los ConditionTargets disponibles en el SourceType actual.
    -   ConditionValue2: RelationType: define la relación del ConditionTarget actual con el objetivo especificado en ConditionValue1.
        -   0 - RELATION\_SELF
        -   1 - RELATION\_IN\_PARTY
        -   2 - RELATION\_IN\_RAID\_OR\_PARTY
        -   3 - RELATION\_OWNED\_BY (El objetivo de condición es propiedad de ConditionValue1)
        -   4 - RELATION\_PASSENGER\_OF (ConditionTarget es pasajero de ConditionValue1)
        -   5 - RELATION\_CREATED\_BY (ConditionTarget es convocado por ConditionValue1)
    -   ConditionValue3: Siempre 0

\***CONDITION\_REACTION\_TO= 34**

-   -   ConditionValue1: objetivo en el que se comprueba la reacción: uno de los ConditionTargets disponibles en el SourceType actual.
    -   ConditionValue2: Máscara de rango: define las reacciones permitidas del Objetivo de Condición actual al objetivo especificado en el Valor de Condición 1. Esta es una máscara de bits; los indicadores para las reacciones son:
        - 1 - Odiado
        - 2 - Hostil
        - 4 - Antipático
        - 8 - Neutral
        - 16 - Amistoso
        - 32 - Honrado
        - 64 - Venerado
        - 128 - Exaltado
    -   ConditionValue3: Siempre 0

\***CONDITION\_DISTANCE\_TO= 35**

-   -   ConditionValue1: objetivo al que se comprueba la distancia: uno de los ConditionTargets disponibles en el SourceType actual.
    -   ConditionValue2: distancia: define la distancia entre el Objetivo de condición actual y el objetivo especificado en Valor de condición1.
    -   ConditionValue3: ComparisionType:
        - 0 = la distancia debe ser igual a ConditionValue2
        - 1 = la distancia debe ser mayor que ConditionValue2
        - 2 = la distancia debe ser menor que ConditionValue2
        - 3 = la distancia debe ser igual o mayor que ConditionValue2
        - 4 = la distancia debe ser igual o menor que ConditionValue2

\***CONDITION\_ALIVE= 36**

-   -   ConditionValue1: Siempre 0
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0
    -   NegativeCondition:
        -   0 (Si el objetivo necesita estar VIVO)
        -   1 (Si el objetivo necesita estar MUERTO)
            *NOTA: Un cadáver de criatura y una criatura que parece muerta son dos cosas diferentes. Una está realmente muerta y la otra simplemente usa un gesto para parecer muerta.*

\***CONDITION\_HP\_VAL = 37**

-   -   ConditionValue1: HP
    -   ConditionValue2: ComparisionType:
        - 0 = Los HP deben ser iguales
        - 1 = Los HP deben ser mayores
        - 2 = Los HP deben ser menores
        - 3 = Los HP deben ser iguales o mayores
        - 4 = Los HP deben ser iguales o menores
    -   ConditionValue3: Siempre 0

\***CONDITION\_HP\_PCT = 38**

-   
    -   ConditionValue1: Porcentaje de HP máximo
    -   ConditionValue2: ComparisionType:
        - 0 = El porcentaje de HP máximo debe ser igual
        - 1 = El porcentaje de HP máximo debe ser mayor
        - 2 = El porcentaje de HP máximo debe ser menor
        - 3 = El porcentaje de HP máximo debe ser igual o mayor
        - 4 = El porcentaje de HP máximo debe ser igual o menor
    -   ConditionValue3: Siempre 0

\***CONDITION\_REALM\_ACHIEVEMENT = 39**

-   -   ConditionValue1: Identificación del logro de [Achievement.dbc](Achievement)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0

\***CONDITION\_IN\_WATER = 40**

-   -   ConditionValue1: Siempre 0
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: Siempre 0
    -   NegativeCondition:
        - 0 (Si el objetivo debe estar en tierra)
        - 1 (Si el objetivo debe estar en el agua)

**\*CONDITION\_STAND\_STATE **= 42****

-   -   ConditionValue1: stateType (exacto o cualquier)
        -   0 = Estado exacto utilizado en ConditionValue2
        -   1 = Cualquier tipo de estado en ConditionValue2
    -   ConditionValue2: Estado de pie exacto, o estado genérico (de pie/sentado), o según el valor 1
        -   0 = De pie
        -   1 = Sesión
    -   ConditionValue3: Siempre 0

**\*CONDITION\_WORLD\_SCRIPT **= 103****

-   -   ConditionValue1: WorldStateCondition definido en WorldState.h
    -   ConditionValue2: estado o 0 (WORLD_STATE_CONDITION_STATE_NONE)
    -   ConditionValue3: Siempre 0
        *NOTA: la condición es verdadera si WorldState::IsConditionFulfilled devuelve verdadero*

### \***REFERENCE TEMPLATES**

-   -   SourceTypeOrReferenceId : utilizado como negativo, para identificación de referencia
    -   SourceGroup  : Siempre 0
    -   SourceEntry  : Siempre 0
    -   ElseGroup  : O modificador
    -   ConditionTypeOrReference: [ConditionTypeOrReference](#conditions-ConditionTypeOrReference)
    -   ConditionValue1  : ver arriba
    -   ConditionValue2  : ver arriba
    -   ConditionValue3  : ver arriba
    -   ErrorType  : ver arriba
    -   ErrorTextId  : ver arriba
    -   Comment  : ver arriba

<!-- -->

-   0 (Si el objetivo necesita estar en tierra)

