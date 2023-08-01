<div id="git-wiki-content">
                <h1 id="smartscripts">smart_scripts</h1>
<p><a href="/wiki/database-world">&lt;-Back-to:World</a></p>
<p>The <code>smart_scripts</code> table has 30 attributes. It serves to make scripts in SQL language. The important thing is always to analyze, who is the event that motivates the execution of an action and of course, who is the objective. As a recommendation, you can review the scripts that are already inside the table, to understand how it works. The advantage, for which several use this method, is that it is not required to compile, when adding records, with restarting the server, if it is well programmed, you can appreciate the changes. Another reason is the portability, but it depends on the point of view of the developer, the response you can get.</p>
<p><strong>Table Structure</strong></p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Attributes</th>
<th>Key</th>
<th>Null</th>
<th>Default</th>
<th>Extra</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#entryorguid">entryorguid</a></td>
<td>INT</td>
<td>SIGNED</td>
<td>PRI</td>
<td>NO</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#sourcetype">source_type</a></td>
<td>TINYINT</td>
<td>UNSIGNED</td>
<td>PRI</td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#id">id</a></td>
<td>SMALLINT</td>
<td>UNSIGNED</td>
<td>PRI</td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#link">link</a></td>
<td>SMALLINT</td>
<td>UNSIGNED</td>
<td>PRI</td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventtype">event_type</a></td>
<td>TINYINT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventphasemask">event_phase_mask</a></td>
<td>SMALLINT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventchance">event_chance</a></td>
<td>TINYINT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>100</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventflags">event_flags</a></td>
<td>SMALLINT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventtype">event_param1</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventtype">event_param2</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventtype">event_param3</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventtype">event_param4</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#eventtype">event_param5</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#actiontype">action_type</a></td>
<td>TINYINT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#actiontype">action_param1</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#actiontype">action_param2</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#actiontype">action_param3</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#actiontype">action_param4</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#actiontype">action_param5</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#actiontype">action_param6</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_type</a></td>
<td>TINYINT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_param1</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_param2</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_param3</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_param4</a></td>
<td>INT</td>
<td>UNSIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_x</a></td>
<td>FLOAT</td>
<td>SIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_y</a></td>
<td>FLOAT</td>
<td>SIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_z</a></td>
<td>FLOAT</td>
<td>SIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#targettype">target_o</a></td>
<td>FLOAT</td>
<td>SIGNED</td>
<td></td>
<td>NO</td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="#comment">comment</a></td>
<td>text</td>
<td></td>
<td></td>
<td>NO</td>
<td></td>
<td></td>
<td>Event Comment</td>
</tr>
</tbody>
</table>
<p><strong>Description of the fields</strong></p>
<h3 id="entryorguid">entryorguid</h3>
<ul>
<li>EntryOrGuid &gt; 0: <code>entry</code> of the creature / game object / etc.</li>
<li>EntryOrGuid &lt; 0: <code>guid</code> of the creature / game object / etc.</li>
<li><strong>Depends on source_type.</strong></li>
</ul>
<p>When using GUID-specific SAI, the extra_flag DONT_OVERRIDE_SAI_ENTRY allows us to not require duplicating rows shared between all creatures of the same entry.</p>
<p>For example, you can keep all movement-related scripting in the GUID script, while combat scripting is handled by the ENTRY script.</p>
<p>For creatures that use this flag, SAI row IDs cannot overlap, thus we use row IDs starting with 1000 and incrementing it (e.g. 1000, 1001, 1002, ...).</p>
<h3 id="sourcetype">source_type</h3>
<p>Object type: creature, game object, spell. see table below for values</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMART_SCRIPT_TYPE_CREATURE</td>
<td>0</td>
</tr>
<tr>
<td>SMART_SCRIPT_TYPE_GAMEOBJECT</td>
<td>1</td>
</tr>
<tr>
<td>SMART_SCRIPT_TYPE_AREATRIGGER</td>
<td>2</td>
</tr>
<tr>
<td>SMART_SCRIPT_TYPE_TIMED_ACTIONLIST</td>
<td>9</td>
</tr>
</tbody>
</table>
<h3 id="id">id</h3>
<p>Incremental id <em>bound</em> to each entryorguid &amp; source_type (0, 1, 2, ...).</p>
<h3 id="link">link</h3>
<p>Simple event linking;</p>
<ul>
<li>Example: if id = 0 and link = 1; id 1 will only be able to occur if id = 0 was triggered (id 1 has to use event_type SMART_EVENT_LINK).</li>
<li>Smart_event to be used.</li>
</ul>
<p><strong>Thanks to the use of links, you can execute several actions, keeping the same event.</strong></p>
<h3 id="eventphasemask">event_phase_mask</h3>
<p>When dealing with phases, <em>phase IDs</em> have to be used. There are 13 (12+1) different phases: 1, 2, ... 12 and the default 0.</p>
<p><strong>Example:</strong> The script is in phase 0 by default - If we want it to go to phase 1, we got two choices:</p>
<ul>
<li>SMART_ACTION_INC_PHASE by 1 or SMART_ACTION_SET_PHASE 1</li>
</ul>
<p>If the script is in phase 0 and want to skip to phase 2:</p>
<ul>
<li>SMART_ACTION_INC_PHASE by 2 or SMART_ACTION_SET_PHASE 2</li>
</ul>
<p>If the script is in phase 1 and want to skip to phase 2:</p>
<ul>
<li>SMART_ACTION_INC_PHASE by 1 or SMART_ACTION_SET_PHASE 2</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Flag</th>
<th>Hex</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMART_EVENT_PHASE_ALWAYS_BIT</td>
<td>0</td>
<td>0x000</td>
<td>Means all phases (1 ... 12)</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_1</td>
<td>1</td>
<td>0x001</td>
<td>Phase 1 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_2</td>
<td>2</td>
<td>0x002</td>
<td>Phase 2 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_3</td>
<td>4</td>
<td>0x004</td>
<td>Phase 3 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_4</td>
<td>8</td>
<td>0x008</td>
<td>Phase 4 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_5</td>
<td>16</td>
<td>0x010</td>
<td>Phase 5 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_6</td>
<td>32</td>
<td>0x020</td>
<td>Phase 6 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_7</td>
<td>64</td>
<td>0x040</td>
<td>Phase 7 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_8</td>
<td>128</td>
<td>0x080</td>
<td>Phase 8 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_9</td>
<td>256</td>
<td>0x100</td>
<td>Phase 9 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_10</td>
<td>512</td>
<td>0x200</td>
<td>Phase 10 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_11</td>
<td>1024</td>
<td>0x400</td>
<td>Phase 11 only.</td>
</tr>
<tr>
<td>SMART_EVENT_PHASE_12</td>
<td>2048</td>
<td>0x800</td>
<td>Phase 12 only.</td>
</tr>
</tbody>
</table>
<ul>
<li>Event will only be able to occur if creature/GO is in this phase.</li>
<li>Example: If we want an event to only be able to occure in phase 1 and 4, <strong>event_phase_mask</strong> = 1+8 = 9</li>
</ul>
<h3 id="eventchance">event_chance</h3>
<p>This is the probability of the event to occur as a percentage from 0-100. So, if you want the event to occur roughly half of the time, then set this to 50.</p>
<h3 id="eventflags">event_flags</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Flag</th>
<th>Hex</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMART_EVENT_FLAG_NOT_REPEATABLE</td>
<td>1</td>
<td>0x01</td>
<td>Event can not repeat</td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_DIFFICULTY_0</td>
<td>2</td>
<td>0x02</td>
<td>Event only occurs in normal dungeon</td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_DIFFICULTY_1</td>
<td>4</td>
<td>0x04</td>
<td>Event only occurs in heroic dungeon</td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_DIFFICULTY_2</td>
<td>8</td>
<td>0x08</td>
<td>Event only occurs in normal raid</td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_DIFFICULTY_3</td>
<td>16</td>
<td>0x10</td>
<td>Event only occurs in heroic raid</td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_RESERVED_5</td>
<td>32</td>
<td>0x20</td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_RESERVED_6</td>
<td>64</td>
<td>0x40</td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_DEBUG_ONLY</td>
<td>128</td>
<td>0x80</td>
<td>Event only occurs in debug build</td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_DONT_RESET</td>
<td>256</td>
<td>0x100</td>
<td>Event will not reset in SmartScript::OnReset()</td>
</tr>
<tr>
<td>SMART_EVENT_FLAG_WHILE_CHARMED</td>
<td>512</td>
<td>0x200</td>
<td>Event occurs even if AI owner is charmed</td>
</tr>
</tbody>
</table>
<ul>
<li>Sets if the event should not repeat or should only happen in a given instance/dungeon difficulty (if applicable);</li>
<li>Values can be added together (bitwise math).</li>
</ul>
<h3 id="eventtype">event_type</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Value</th>
<th>Param1</th>
<th>Param2</th>
<th>Param3</th>
<th>Param4</th>
<th>Param5</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMART_EVENT_UPDATE_IC</td>
<td>0</td>
<td>InitialMin</td>
<td>InitialMax</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>In combat.</td>
</tr>
<tr>
<td>SMART_EVENT_UPDATE_OOC</td>
<td>1</td>
<td>InitialMin</td>
<td>InitialMax</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>Out of combat.</td>
</tr>
<tr>
<td>SMART_EVENT_HEALTH_PCT</td>
<td>2</td>
<td>HPMin%</td>
<td>HPMax%</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>Health Percentage</td>
</tr>
<tr>
<td>SMART_EVENT_MANA_PCT</td>
<td>3</td>
<td>ManaMin%</td>
<td>ManaMax%</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>Mana Percentage</td>
</tr>
<tr>
<td>SMART_EVENT_AGGRO</td>
<td>4</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Creature Aggro</td>
</tr>
<tr>
<td>SMART_EVENT_KILL</td>
<td>5</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td>Player only (0/1)</td>
<td>Creature entry (if param3 is 0)</td>
<td></td>
<td>On Creature Kill</td>
</tr>
<tr>
<td>SMART_EVENT_DEATH</td>
<td>6</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Creature Death</td>
</tr>
<tr>
<td>SMART_EVENT_EVADE</td>
<td>7</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Creature Evade Attack</td>
</tr>
<tr>
<td>SMART_EVENT_SPELLHIT</td>
<td>8</td>
<td>SpellID</td>
<td>School</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td>On Creature/Gameobject Spell Hit</td>
</tr>
<tr>
<td>SMART_EVENT_RANGE</td>
<td>9</td>
<td>MinDist</td>
<td>MaxDist</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td>0/1 onlyFireOnRepeat</td>
<td>On Victim In Range</td>
</tr>
<tr>
<td>SMART_EVENT_OOC_LOS</td>
<td>10</td>
<td>NoHostile</td>
<td>MaxRange</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td>0/1 Player Only</td>
<td>On Target In Distance Out of Combat</td>
</tr>
<tr>
<td>SMART_EVENT_RESPAWN</td>
<td>11</td>
<td>type (None = 0, Map = 1, Area = 2)</td>
<td>MapId</td>
<td>ZoneId</td>
<td></td>
<td></td>
<td>On Creature/Gameobject Respawn</td>
</tr>
<tr>
<td>SMART_EVENT_TARGET_HEALTH_PCT</td>
<td>12</td>
<td>HPMin%</td>
<td>HPMax%</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>On Target Health Percentage</td>
</tr>
<tr>
<td>SMART_EVENT_VICTIM_CASTING</td>
<td>13</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td>Spell id (0 any)</td>
<td></td>
<td></td>
<td>On Target Casting Spell</td>
</tr>
<tr>
<td>SMART_EVENT_FRIENDLY_HEALTH</td>
<td>14</td>
<td>HPDeficit</td>
<td>Radius</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>On Friendly Health Deficit</td>
</tr>
<tr>
<td>SMART_EVENT_FRIENDLY_IS_CC</td>
<td>15</td>
<td>Radius</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_FRIENDLY_MISSING_BUFF</td>
<td>16</td>
<td>SpellId</td>
<td>Radius</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td>onlyInCombat</td>
<td>On Friendly Lost Buff</td>
</tr>
<tr>
<td>SMART_EVENT_SUMMONED_UNIT</td>
<td>17</td>
<td>CretureId (0 all)</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td>On Creature/Gameobject Summoned Unit</td>
</tr>
<tr>
<td>SMART_EVENT_TARGET_MANA_PCT</td>
<td>18</td>
<td>ManaMin%</td>
<td>ManaMax%</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>On Target Mana Percentage</td>
</tr>
<tr>
<td>SMART_EVENT_ACCEPTED_QUEST</td>
<td>19</td>
<td>QuestID (0 any)</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td>On Target Accepted Quest</td>
</tr>
<tr>
<td>SMART_EVENT_REWARD_QUEST</td>
<td>20</td>
<td>QuestID (0 any)</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td>On Target Rewarded Quest</td>
</tr>
<tr>
<td>SMART_EVENT_REACHED_HOME</td>
<td>21</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Creature Reached Home</td>
</tr>
<tr>
<td>SMART_EVENT_RECEIVE_EMOTE</td>
<td>22</td>
<td>EmoteId</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td>On Receive Emote.</td>
</tr>
<tr>
<td>SMART_EVENT_HAS_AURA</td>
<td>23</td>
<td>SpellID</td>
<td>Stacks</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>On Creature Has Aura</td>
</tr>
<tr>
<td>SMART_EVENT_TARGET_BUFFED</td>
<td>24</td>
<td>SpellID</td>
<td>Stacks</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>On Target Buffed With Spell</td>
</tr>
<tr>
<td>SMART_EVENT_RESET</td>
<td>25</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>After Combat, On Respawn or Spawn</td>
</tr>
<tr>
<td>SMART_EVENT_IC_LOS</td>
<td>26</td>
<td>NoHostile</td>
<td>MaxRange</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td>0/1 Player Only</td>
<td>On Target In Distance In Combat</td>
</tr>
<tr>
<td>SMART_EVENT_PASSENGER_BOARDED</td>
<td>27</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_PASSENGER_REMOVED</td>
<td>28</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_CHARMED</td>
<td>29</td>
<td>onRemove (0 - on apply, 1 - on remove)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Creature Charmed</td>
</tr>
<tr>
<td>SMART_EVENT_CHARMED_TARGET</td>
<td>30</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Target Charmed</td>
</tr>
<tr>
<td>SMART_EVENT_SPELLHIT_TARGET</td>
<td>31</td>
<td>SpellId</td>
<td>School</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>On Target Spell Hit</td>
</tr>
<tr>
<td>SMART_EVENT_DAMAGED</td>
<td>32</td>
<td>MinDmg</td>
<td>MaxDmg</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>On Creature Damaged</td>
</tr>
<tr>
<td>SMART_EVENT_DAMAGED_TARGET</td>
<td>33</td>
<td>MinDmg</td>
<td>MaxDmg</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td>On Target Damaged</td>
</tr>
<tr>
<td>SMART_EVENT_MOVEMENTINFORM</td>
<td>34</td>
<td>MovementType (0=any)</td>
<td>PointID</td>
<td></td>
<td></td>
<td></td>
<td>ESCORT_MOTION_TYPE = 17, POINT_MOTION_TYPE = 8</td>
</tr>
<tr>
<td>SMART_EVENT_SUMMON_DESPAWNED</td>
<td>35</td>
<td>Entry</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td>On Summoned Unit Despawned</td>
</tr>
<tr>
<td>SMART_EVENT_CORPSE_REMOVED</td>
<td>36</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Creature Corpse Removed</td>
</tr>
<tr>
<td>SMART_EVENT_AI_INIT</td>
<td>37</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_DATA_SET</td>
<td>38</td>
<td>Field</td>
<td>Value</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td>On Creature/Gameobject Data Set, Can be used with SMART_ACTION_SET_DATA</td>
</tr>
<tr>
<td>SMART_EVENT_WAYPOINT_START</td>
<td>39</td>
<td>PointId (0 any)</td>
<td>pathId (0 any)</td>
<td></td>
<td></td>
<td></td>
<td>On Creature Waypoint ID Started</td>
</tr>
<tr>
<td>SMART_EVENT_WAYPOINT_REACHED</td>
<td>40</td>
<td>PointId (0 any)</td>
<td>pathId (0 any)</td>
<td></td>
<td></td>
<td></td>
<td>On Creature Waypoint ID Reached</td>
</tr>
<tr>
<td>SMART_EVENT_AREATRIGGER_ONTRIGGER</td>
<td>46</td>
<td>TriggerId (0 any)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_TEXT_OVER</td>
<td>52</td>
<td>creature_text.GroupID</td>
<td>creature.id (0 any)</td>
<td></td>
<td></td>
<td></td>
<td>On TEXT_OVER Event Triggered After SMART_ACTION_TALK</td>
</tr>
<tr>
<td>SMART_EVENT_RECEIVE_HEAL</td>
<td>53</td>
<td>MinHeal</td>
<td>MaxHeal</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td>On Creature Received Healing</td>
</tr>
<tr>
<td>SMART_EVENT_JUST_SUMMONED</td>
<td>54</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Creature Just spawned</td>
</tr>
<tr>
<td>SMART_EVENT_WAYPOINT_PAUSED</td>
<td>55</td>
<td>PointId (0 any)</td>
<td>pathID (0 any)</td>
<td></td>
<td></td>
<td></td>
<td>On Creature Paused at Waypoint ID</td>
</tr>
<tr>
<td>SMART_EVENT_WAYPOINT_RESUMED</td>
<td>56</td>
<td>PointId (0 any)</td>
<td>pathID (0 any)</td>
<td></td>
<td></td>
<td></td>
<td>On Creature Resumed after Waypoint ID</td>
</tr>
<tr>
<td>SMART_EVENT_WAYPOINT_STOPPED</td>
<td>57</td>
<td>PointId (0 any)</td>
<td>pathID (0 any)</td>
<td></td>
<td></td>
<td></td>
<td>On Creature Stopped On Waypoint ID</td>
</tr>
<tr>
<td>SMART_EVENT_WAYPOINT_ENDED</td>
<td>58</td>
<td>PointId (0 any)</td>
<td>pathID (0 any)</td>
<td></td>
<td></td>
<td></td>
<td>On Creature Waypoint Path Ended</td>
</tr>
<tr>
<td>SMART_EVENT_TIMED_EVENT_TRIGGERED</td>
<td>59</td>
<td>Id</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_UPDATE</td>
<td>60</td>
<td>InitialMin</td>
<td>InitialMax</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_LINK</td>
<td>61</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Used to link together multiple events as a chain of events.</td>
</tr>
<tr>
<td>SMART_EVENT_GOSSIP_SELECT</td>
<td>62</td>
<td>gossip_menu_option.MenuID</td>
<td>gossip_menu_option.OptionID</td>
<td></td>
<td></td>
<td></td>
<td>On gossip clicked (gossip_menu_option).</td>
</tr>
<tr>
<td>SMART_EVENT_JUST_CREATED</td>
<td>63</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_GOSSIP_HELLO</td>
<td>64</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On Right-Click Creature/Gameobject that have gossip enabled.</td>
</tr>
<tr>
<td>SMART_EVENT_FOLLOW_COMPLETED</td>
<td>65</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_EVENT_PHASE_CHANGE</td>
<td>66</td>
<td>event phase mask</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On event phase mask set</td>
</tr>
<tr>
<td>SMART_EVENT_IS_BEHIND_TARGET</td>
<td>67</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td></td>
<td>On Creature is behind target.</td>
</tr>
<tr>
<td>SMART_EVENT_GAME_EVENT_START</td>
<td>68</td>
<td>game_event.eventEntry</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On game_event started.</td>
</tr>
<tr>
<td>SMART_EVENT_GAME_EVENT_END</td>
<td>69</td>
<td>game_event.eventEntry</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>On game_event ended.</td>
</tr>
<tr>
<td>SMART_EVENT_GO_STATE_CHANGED</td>
<td>70</td>
<td>State (0 - Active, 1 - Ready, 2 - Active alternative)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_GO_EVENT_INFORM</td>
<td>71</td>
<td>EventId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_ACTION_DONE</td>
<td>72</td>
<td>EventId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_ON_SPELLCLICK</td>
<td>73</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_FRIENDLY_HEALTH_PCT</td>
<td>74</td>
<td>minHpPct</td>
<td>maxHpPct</td>
<td>repeatMin</td>
<td>repeatMax</td>
<td>Range</td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_DISTANCE_CREATURE</td>
<td>75</td>
<td>database guid</td>
<td>database entry</td>
<td>distance</td>
<td>repeat interval (ms)</td>
<td></td>
<td>On creature guid OR any instance of creature entry is within distance.</td>
</tr>
<tr>
<td>SMART_EVENT_DISTANCE_GAMEOBJECT</td>
<td>76</td>
<td>database guid</td>
<td>database entry</td>
<td>distance</td>
<td>repeat interval (ms)</td>
<td></td>
<td>On gameobject guid OR any instance of gameobject entry is within   distance.</td>
</tr>
<tr>
<td>SMART_EVENT_COUNTER_SET</td>
<td>77</td>
<td>counterID</td>
<td>value</td>
<td>cooldownMin</td>
<td>cooldownMax</td>
<td></td>
<td>If the value of specified counterID is equal to a specified value</td>
</tr>
<tr>
<td>SMART_EVENT_SUMMONED_UNIT_DIES</td>
<td>82</td>
<td>CreatureId(0 all)</td>
<td>CooldownMin</td>
<td>CooldownMax</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_EVENT_NEAR_PLAYERS</td>
<td>101</td>
<td>minPlayers</td>
<td>Range (yards)</td>
<td>FirstCheck (ms)</td>
<td>RepeatMin (ms)</td>
<td>RepeatMax (ms)</td>
<td>Event will trigger if there are more or equal than minPlayers in range.</td>
</tr>
<tr>
<td>SMART_EVENT_NEAR_PLAYERS_NEGATION</td>
<td>102</td>
<td>maxPlayers</td>
<td>Range (yards)</td>
<td>FirstCheck (ms)</td>
<td>RepeatMin (ms)</td>
<td>RepeatMax (ms)</td>
<td>Event will trigger if there are less than maxPlayers in range.</td>
</tr>
<tr>
<td>SMART_EVENT_NEAR_UNIT</td>
<td>103</td>
<td>Unit type to check (0: creature 1: gob)</td>
<td>Entry (template)</td>
<td>Count</td>
<td>Range</td>
<td>Timer (ms)</td>
<td>Will check for &gt;= count of specified entry within range</td>
</tr>
<tr>
<td>SMART_EVENT_NEAR_UNIT_NEGATION</td>
<td>104</td>
<td>Unit type to check (0: creature 1: gob)</td>
<td>Entry (template)</td>
<td>Count</td>
<td>Range</td>
<td>Timer (ms)</td>
<td>Will check for &lt; count of specified entry within range</td>
</tr>
<tr>
<td>SMART_EVENT_AREA_CASTING</td>
<td>105</td>
<td>InitialMin</td>
<td>InitialMax</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td>Range</td>
<td>Check threat list for hostiles casting. If none are found, repeat in 1200ms</td>
</tr>
<tr>
<td>SMART_EVENT_AREA_RANGE</td>
<td>106</td>
<td>InitialMin</td>
<td>InitialMax</td>
<td>RepeatMin</td>
<td>RepeatMax</td>
<td>Range</td>
<td>Check threat list for hostiles in range. If none are found, repeat in 1200ms</td>
</tr>
</tbody>
</table>
<h3 id="actiontype">action_type</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Value</th>
<th>Param1</th>
<th>Param2</th>
<th>Param3</th>
<th>Param4</th>
<th>Param5</th>
<th>Param6</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMART_ACTION_NONE</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Do nothing</td>
</tr>
<tr>
<td>SMART_ACTION_TALK</td>
<td>1</td>
<td>creature_text.GroupID</td>
<td>Duration to wait before SMART_EVENT_TEXT_OVER is triggered.</td>
<td>0 It will try to trigger talk of the target<br>1 Set target as   talk target (used for $vars in texts and whisper target)</td>
<td></td>
<td></td>
<td></td>
<td>Param2 in Milliseconds.</td>
</tr>
<tr>
<td>SMART_ACTION_SET_FACTION</td>
<td>2</td>
<td>FactionID (or 0 for default)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Sets faction to creature.</td>
</tr>
<tr>
<td>SMART_ACTION_MORPH_TO_ENTRY_OR_MODEL</td>
<td>3</td>
<td>creature_template.entry(param1)</td>
<td>creature_template.modelidx(param2)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Take DisplayID of creature (param1) OR Turn to DisplayID (param2) OR Both   = 0 for Demorph</td>
</tr>
<tr>
<td>SMART_ACTION_SOUND</td>
<td>4</td>
<td>SoundId</td>
<td>onlySelf (0/1)</td>
<td>distance</td>
<td></td>
<td></td>
<td></td>
<td>Play Sound; onlySelf = 1 only sends sound to self, onlySelf = 0 sends   sound to everyone in visibility range</td>
</tr>
<tr>
<td>SMART_ACTION_PLAY_EMOTE</td>
<td>5</td>
<td>EmoteId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Makes the target perform an Emote</td>
</tr>
<tr>
<td>SMART_ACTION_FAIL_QUEST</td>
<td>6</td>
<td>QuestID</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Fail Quest of Target</td>
</tr>
<tr>
<td>SMART_ACTION_OFFER_QUEST</td>
<td>7</td>
<td>quest_template.id</td>
<td>directAdd (0/1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Add Quest to Target</td>
</tr>
<tr>
<td>SMART_ACTION_SET_REACT_STATE</td>
<td>8</td>
<td>ReactState</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>React State. Can be Passive (0), Defensive (1), Aggressive (2).</td>
</tr>
<tr>
<td>SMART_ACTION_ACTIVATE_GOBJECT</td>
<td>9</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Activate Object</td>
</tr>
<tr>
<td>SMART_ACTION_RANDOM_EMOTE</td>
<td>10</td>
<td>EmoteId1</td>
<td>EmoteId2</td>
<td>EmoteId3</td>
<td>EmoteId4</td>
<td>EmoteId5</td>
<td>EmoteId6</td>
<td>Play Random Emote</td>
</tr>
<tr>
<td>SMART_ACTION_CAST</td>
<td>11</td>
<td>SpellId</td>
<td><a href="#cast-flags">castFlags</a></td>
<td><a href="#triggered-flags">triggeredFlags</a></td>
<td>limitTargets (0 = all)</td>
<td></td>
<td></td>
<td>Cast Spell ID at Target(s)</td>
</tr>
<tr>
<td>SMART_ACTION_SUMMON_CREATURE</td>
<td>12</td>
<td>creature_template.entry</td>
<td>Summon type</td>
<td>duration in ms</td>
<td>attackInvoker (0/1/2)</td>
<td>attackScriptOwner (0/1)</td>
<td></td>
<td>Summon Unit; attackInvoker 1: attack target; attackInvoker 2: attack   actual invoker</td>
</tr>
<tr>
<td>SMART_ACTION_THREAT_SINGLE_PCT</td>
<td>13</td>
<td>Threat% inc</td>
<td>Threat% dec</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Change Threat Percentage for Single Target</td>
</tr>
<tr>
<td>SMART_ACTION_THREAT_ALL_PCT</td>
<td>14</td>
<td>Threat% inc</td>
<td>Threat% dec</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Change Threat Percentage for All Enemies</td>
</tr>
<tr>
<td>SMART_ACTION_CALL_AREAEXPLOREDOREVENTHAPPENS</td>
<td>15</td>
<td>quest_template.id</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_EMOTE_STATE</td>
<td>17</td>
<td>EmoteId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Play Emote Continuously</td>
</tr>
<tr>
<td>SMART_ACTION_SET_UNIT_FLAG</td>
<td>18</td>
<td>(may be more than one field OR'd together)</td>
<td>type<br>If false   set creature_template.unit_flags<br>If true   set creature_template.unit_flags2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Can set Multi-able flags at once</td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_UNIT_FLAG</td>
<td>19</td>
<td>(may be more than one field OR'd together)</td>
<td>type<br>If false   set creature_template.unit_flags<br>If true   set creature_template.unit_flags2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Can Remove Multi-able flags at once</td>
</tr>
<tr>
<td>SMART_ACTION_AUTO_ATTACK</td>
<td>20</td>
<td>AllowAttackState (0 = Stop attack, anything else means continue   attacking)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Stop or Continue Automatic Attack.</td>
</tr>
<tr>
<td>SMART_ACTION_ALLOW_COMBAT_MOVEMENT</td>
<td>21</td>
<td>AllowCombatMovement (0 = Stop combat based movement, anything else   continue attacking)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Allow or Disable Combat Movement</td>
</tr>
<tr>
<td>SMART_ACTION_SET_EVENT_PHASE</td>
<td>22</td>
<td>event_phase_mask</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Set event phase 0-12 (the actual values, no bit mask!)</td>
</tr>
<tr>
<td>SMART_ACTION_INC_EVENT_PHASE</td>
<td>23</td>
<td>Increment</td>
<td>Decrement</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Set param1 OR param2 (not both). Value 0 has no effect.</td>
</tr>
<tr>
<td>SMART_ACTION_EVADE</td>
<td>24</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Evade Incoming Attack</td>
</tr>
<tr>
<td>SMART_ACTION_FLEE_FOR_ASSIST</td>
<td>25</td>
<td>0/1 (If you want the fleeing NPC to say attempts to flee text on flee,   use 1 on param1. For no message use 0.)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>If you want the fleeing NPC to say '%s attempts to run away in fear' on   flee, use 1 on param1. 0 for no message.</td>
</tr>
<tr>
<td>SMART_ACTION_CALL_GROUPEVENTHAPPENS</td>
<td>26</td>
<td>quest_template.id</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_COMBAT_STOP</td>
<td>27</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_REMOVEAURASFROMSPELL</td>
<td>28</td>
<td>Spellid (0 removes all auras)</td>
<td>charges (0 removes aura)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_FOLLOW</td>
<td>29</td>
<td>Distance (0 = Default value)</td>
<td>Angle (0 = Default value)</td>
<td>End creature_template.entry</td>
<td>credit</td>
<td>creditType (0 monsterkill, 1 event)</td>
<td></td>
<td>Follow Target. If target type is NONE or SELF, Stop Follow</td>
</tr>
<tr>
<td>SMART_ACTION_RANDOM_PHASE</td>
<td>30</td>
<td>event_phase_mask 1</td>
<td>event_phase_mask 2</td>
<td>event_phase_mask 3</td>
<td>event_phase_mask 4</td>
<td>event_phase_mask 5</td>
<td>event_phase_mask 6</td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_RANDOM_PHASE_RANGE</td>
<td>31</td>
<td>event_phase_mask minimum</td>
<td>event_phase_mask maximum</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_RESET_GOBJECT</td>
<td>32</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Reset Gameobject</td>
</tr>
<tr>
<td>SMART_ACTION_CALL_KILLEDMONSTER</td>
<td>33</td>
<td>creature_template.entry</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>This is the ID from quest_template.RequiredNpcOrGo</td>
</tr>
<tr>
<td>SMART_ACTION_SET_INST_DATA</td>
<td>34</td>
<td>Field</td>
<td>Data</td>
<td></td>
<td>Type (0 = SetData, 1 = SetBossState)</td>
<td></td>
<td></td>
<td>Set Instance Data</td>
</tr>
<tr>
<td>SMART_ACTION_SET_INST_DATA64</td>
<td>35</td>
<td>Field</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Set Instance Data uint64</td>
</tr>
<tr>
<td>SMART_ACTION_UPDATE_TEMPLATE</td>
<td>36</td>
<td>creature_template.entry</td>
<td>Update Level</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Updates creature_template to given entry</td>
</tr>
<tr>
<td>SMART_ACTION_DIE</td>
<td>37</td>
<td>Milliseconds</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Kill Target, if param1 is set, it will die after param1 milliseconds. 0: no delay, the target will die instantly</td>
</tr>
<tr>
<td>SMART_ACTION_SET_IN_COMBAT_WITH_ZONE</td>
<td>38</td>
<td>Range in yards for all players to be forced into combat with the   creature. Only used in the open world. Leave as 0 if used in an instance.</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Sets the creature in combat with its zone, can be used in instances and   open world. Useful for creatures inside instances so all players will be set   in combat until the fight ends.</td>
</tr>
<tr>
<td>SMART_ACTION_CALL_FOR_HELP</td>
<td>39</td>
<td>Radius in yards that other creatures must be to acknowledge the cry for   help.</td>
<td>0/1 (say calls for help text)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>If you want the NPC to say '%s calls for help!'. Use 1 on param1, 0 for   no message.</td>
</tr>
<tr>
<td>SMART_ACTION_SET_SHEATH</td>
<td>40</td>
<td>Sheath (0-unarmed, 1-melee, 2-ranged)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_FORCE_DESPAWN</td>
<td>41</td>
<td>Despawn timer "ms"</td>
<td>Respawn Timer "s"</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Despawn Target after param1 in Milliseconds. Respawn after param2 in seconds.</td>
</tr>
<tr>
<td>SMART_ACTION_SET_INVINCIBILITY_HP_LEVEL</td>
<td>42</td>
<td>flat hp value</td>
<td>percent hp value</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>If you use both params, only percent will be used.</td>
</tr>
<tr>
<td>SMART_ACTION_MOUNT_TO_ENTRY_OR_MODEL</td>
<td>43</td>
<td>creature_template.entry</td>
<td>creature_template.modelidx</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Mount to Creature Entry (param1) OR Mount to Creature Display (param2) Or   both = 0 for Unmount</td>
</tr>
<tr>
<td>SMART_ACTION_SET_INGAME_PHASE_MASK</td>
<td>44</td>
<td>creature.phaseMask</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_DATA</td>
<td>45</td>
<td>Field</td>
<td>Data</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Set Data For Target, can be used with SMART_EVENT_DATA_SET</td>
</tr>
<tr>
<td>SMART_ACTION_MOVE_FORWARD</td>
<td>46</td>
<td>distance</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>move self forward for the specified distance (point movement)</td>
</tr>
<tr>
<td>SMART_ACTION_SET_VISIBILITY</td>
<td>47</td>
<td>0/1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Makes creature Visible = 1 or Invisible = 0</td>
</tr>
<tr>
<td>SMART_ACTION_SET_ACTIVE</td>
<td>48</td>
<td>0/1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>If a creature or GO is set active it will stay active even if no player   is near. Take care, though, as it needs additional ressources (CPU/RAM) to   keep them active (other objects/creatures nearby stay active).</td>
</tr>
<tr>
<td>SMART_ACTION_ATTACK_START</td>
<td>49</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Allows basic melee swings to creature.</td>
</tr>
<tr>
<td>SMART_ACTION_SUMMON_GO</td>
<td>50</td>
<td>gameobject_template.entry</td>
<td>De-spawn time in seconds.</td>
<td>targetSummon (0/1)</td>
<td>summonType (0 - after a specified time OR when the summoner dies, 1 - after a specified time)</td>
<td></td>
<td></td>
<td>Spawns Gameobject, use target_type to set spawn position; if an entity is   specified as target and also coordinates are set (target x,y,z) those   coordinates are handled as offset from the target's position; if targetSummon   is 1 then the target will summon the GO on the position of the actor</td>
</tr>
<tr>
<td>SMART_ACTION_KILL_UNIT</td>
<td>51</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Kills Creature.</td>
</tr>
<tr>
<td>SMART_ACTION_ACTIVATE_TAXI</td>
<td>52</td>
<td>TaxiID</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Sends player to flight path. You have to be close to Flight Master, which   gives Taxi ID you need.</td>
</tr>
<tr>
<td>SMART_ACTION_WP_START</td>
<td>53</td>
<td>0 = walk / 1 = run</td>
<td>waypoints.entry</td>
<td>canRepeat</td>
<td>quest_template.id</td>
<td>despawntime</td>
<td>reactState</td>
<td>Creature starts Waypoint Movement. Use waypoints table to   create movement.</td>
</tr>
<tr>
<td>SMART_ACTION_WP_PAUSE</td>
<td>54</td>
<td>time (in ms)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Creature pauses its Waypoint Movement for given time.</td>
</tr>
<tr>
<td>SMART_ACTION_WP_STOP</td>
<td>55</td>
<td>despawnTime</td>
<td>quest_template.id</td>
<td>fail (0/1)</td>
<td></td>
<td></td>
<td></td>
<td>Creature stops its Waypoint Movement.</td>
</tr>
<tr>
<td>SMART_ACTION_ADD_ITEM</td>
<td>56</td>
<td>item_template.entry</td>
<td>count</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Adds item(s) to player.</td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_ITEM</td>
<td>57</td>
<td>item_template.entry</td>
<td>count</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Removes item(s) from player.</td>
</tr>
<tr>
<td>SMART_ACTION_INSTALL_AI_TEMPLATE</td>
<td>58</td>
<td>TemplateID (see Predefined SAI templates below)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_RUN</td>
<td>59</td>
<td>0 = Off / 1 = On</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_FLY</td>
<td>60</td>
<td>fly (0/1)</td>
<td>speed</td>
<td>disable gravity (0/1)</td>
<td></td>
<td></td>
<td></td>
<td>Only works for creatures with inhabit air.</td>
</tr>
<tr>
<td>SMART_ACTION_SET_SWIM</td>
<td>61</td>
<td>0 = Off / 1 = On</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_TELEPORT</td>
<td>62</td>
<td>MapID</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continue this action with the TARGET_TYPE column. Use any target_type   (except 0), and use target_x, target_y, target_z, target_o as the coordinates</td>
</tr>
<tr>
<td>SMART_ACTION_SET_COUNTER</td>
<td>63</td>
<td>counterID</td>
<td>value</td>
<td>reset (0/1)</td>
<td></td>
<td></td>
<td></td>
<td>If reset is 0 the counter with the specified ID is increased by the given   value; if reset is 1 the counter is set to the value.</td>
</tr>
<tr>
<td>SMART_ACTION_STORE_TARGET_LIST</td>
<td>64</td>
<td>varID</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_WP_RESUME</td>
<td>65</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Creature continues in its Waypoint Movement.</td>
</tr>
<tr>
<td>SMART_ACTION_SET_ORIENTATION</td>
<td>66</td>
<td>Quick Change</td>
<td>Random orientation? (0/1)</td>
<td>Turning Angle (degrees) - The value will turn the creature counterclockwise. target_type must be NONE</td>
<td></td>
<td></td>
<td></td>
<td>Used to alter the source's orientation. Depends on the script target. If SMART_TARGET_SELF, facing will be the   same as in HomePosition, For SMART_TARGET_POSITION you need to set target_o :   0 = North, West = 1.5, South = 3, East = 4.5</td>
</tr>
<tr>
<td>SMART_ACTION_CREATE_TIMED_EVENT</td>
<td>67</td>
<td>id</td>
<td>InitialMin</td>
<td>InitialMax</td>
<td>RepeatMin(only if it repeats)</td>
<td>RepeatMax(only if it repeats)</td>
<td>chance</td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_PLAYMOVIE</td>
<td>68</td>
<td>entry</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_MOVE_TO_POS</td>
<td>69</td>
<td>PointId</td>
<td>isTransport (0 or 1)</td>
<td>controlled (0 or 1)</td>
<td>ContactDistance</td>
<td></td>
<td></td>
<td>PointId is called by SMART_EVENT_MOVEMENTINFORM. Continue this action   with the TARGET_TYPE column. Use any target_type, and use target_x, target_y,   target_z as the coordinates; if an entity is specified as target and also   coordinates are set (target x,y,z) those coordinates are handled as offset   from the target's position</td>
</tr>
<tr>
<td>SMART_ACTION_RESPAWN_TARGET</td>
<td>70</td>
<td>Respawntime in seconds</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_EQUIP</td>
<td>71</td>
<td>creature_equip_template.ID</td>
<td>Slotmask</td>
<td>Slot1 (item_template.entry)</td>
<td>Slot2 (item_template.entry)</td>
<td>Slot3 (item_template.entry)</td>
<td></td>
<td>only slots with mask set will be sent to client, bits are 1, 2, 4,   leaving mask 0 is defaulted to mask 7 (send all), Slots1-3 are only used if   no Param1 is set</td>
</tr>
<tr>
<td>SMART_ACTION_CLOSE_GOSSIP</td>
<td>72</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Closes gossip window.</td>
</tr>
<tr>
<td>SMART_ACTION_TRIGGER_TIMED_EVENT</td>
<td>73</td>
<td>id(&gt;1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_TIMED_EVENT</td>
<td>74</td>
<td>id(&gt;1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_ADD_AURA</td>
<td>75</td>
<td>SpellId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Adds aura to player(s). Use target_type 17 to make AoE aura.</td>
</tr>
<tr>
<td>SMART_ACTION_OVERRIDE_SCRIPT_BASE_OBJECT</td>
<td>76</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>WARNING: CAN CRASH CORE, do not use if you dont know what you are doing</td>
</tr>
<tr>
<td>SMART_ACTION_RESET_SCRIPT_BASE_OBJECT</td>
<td>77</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_CALL_SCRIPT_RESET</td>
<td>78</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_RANGED_MOVEMENT</td>
<td>79</td>
<td>attackDistance</td>
<td>attackAngle</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Sets movement to follow at a specific range to the target.</td>
</tr>
<tr>
<td>SMART_ACTION_CALL_TIMED_ACTIONLIST</td>
<td>80</td>
<td>EntryOrGuid * 100 (entryorguid with 00 added after the entry, or 01,   02, 03 etc. for multiple action lists)</td>
<td>timer update type(0 OOC, 1 IC, 2 ALWAYS)</td>
<td>allowOverride (0 - Must finish current actionlist, 1 - Allow starting new actionlist during previous actionlist)</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_NPC_FLAG</td>
<td>81</td>
<td>creature_template.npcflag</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_ADD_NPC_FLAG</td>
<td>82</td>
<td>creature_template.npcflag</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_NPC_FLAG</td>
<td>83</td>
<td>creature_template.npcflag</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SIMPLE_TALK</td>
<td>84</td>
<td>creature_text.GroupID</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Makes a player say text. SMART_EVENT_TEXT_OVER is not triggered and   whispers can not be used.</td>
</tr>
<tr>
<td>SMART_ACTION_SELF_CAST</td>
<td>85</td>
<td>SpellId</td>
<td><a href="#cast-flags">castFlags</a></td>
<td><a href="#triggered-flags">triggeredFlags</a></td>
<td>limitTargets (0 = all)</td>
<td></td>
<td></td>
<td>Makes the target cast spell on self.</td>
</tr>
<tr>
<td>SMART_ACTION_CROSS_CAST</td>
<td>86</td>
<td>SpellID</td>
<td>castFlags</td>
<td>CasterTargetType (caster is selected here, use it as target_type)</td>
<td>CasterTarget (target_param1)</td>
<td>CasterTarget (target_param2)</td>
<td>CasterTarget (target_param3)</td>
<td>This action is used to make selected caster (in CasterTargetType) to cast   spell. Actual target is entered in target_type as normally.</td>
</tr>
<tr>
<td>SMART_ACTION_CALL_RANDOM_TIMED_ACTIONLIST</td>
<td>87</td>
<td>EntryOrGuid 1 (entryorguid * 100 + n)</td>
<td>EntryOrGuid 2 (entryorguid * 100 + n)</td>
<td>EntryOrGuid 3 (entryorguid * 100 + n)</td>
<td>EntryOrGuid 4 (entryorguid * 100 + n)</td>
<td>EntryOrGuid 5 (entryorguid * 100 + n)</td>
<td>EntryOrGuid 6 (entryorguid * 100 + n)</td>
<td>Will select one entry from the ones provided. 0 is ignored.</td>
</tr>
<tr>
<td>SMART_ACTION_CALL_RANDOM_RANGE_TIMED_ACTIONLIST</td>
<td>88</td>
<td>EntryOrGuid 1 (entryorguid * 100 + n)</td>
<td>EntryOrGuid 2 (entryorguid * 100 + n)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0 is ignored.</td>
</tr>
<tr>
<td>SMART_ACTION_RANDOM_MOVE</td>
<td>89</td>
<td>Radius</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Creature moves to random position in given radius. If radius is 0, then stop movement</td>
</tr>
<tr>
<td>SMART_ACTION_SET_UNIT_FIELD_BYTES_1</td>
<td>90</td>
<td>Value</td>
<td>Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_UNIT_FIELD_BYTES_1</td>
<td>91</td>
<td>Value</td>
<td>Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_INTERRUPT_SPELL</td>
<td>92</td>
<td>With delay (0/1)</td>
<td>SpellId</td>
<td>Instant (0/1)</td>
<td></td>
<td></td>
<td></td>
<td>This action allows you to interrupt the current spell being cast. If you   do not set the spellId, the core will find the current spell depending on the   withDelay and the withInstant values.</td>
</tr>
<tr>
<td>SMART_ACTION_SEND_GO_CUSTOM_ANIM</td>
<td>93</td>
<td>animprogress (0-255)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_DYNAMIC_FLAG</td>
<td>94</td>
<td>creature_template.dynamicflags</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_ADD_DYNAMIC_FLAG</td>
<td>95</td>
<td>creature_template.dynamicflags</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_DYNAMIC_FLAG</td>
<td>96</td>
<td>creature_template.dynamicflags</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_JUMP_TO_POS</td>
<td>97</td>
<td>Speed XY</td>
<td>Speed Z</td>
<td>selfJump (0/1)</td>
<td></td>
<td></td>
<td></td>
<td>If selfJump is 1 the actor will jump to the target (you can add an offset   from the target's position by also specifying target coordinates); if   selfJump is 0 the targeted creature will jump to the target position</td>
</tr>
<tr>
<td>SMART_ACTION_SEND_GOSSIP_MENU</td>
<td>98</td>
<td>gossip_menu.entry</td>
<td>gossip_menu.text_id<br>(same value as npc_text.ID)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Can be used together with 'SMART_EVENT_GOSSIP_HELLO' to set custom   gossip.</td>
</tr>
<tr>
<td>SMART_ACTION_GO_SET_LOOT_STATE</td>
<td>99</td>
<td>LootState (0 - Not ready, 1 - Ready, 2 - Activated, 3 - Just deactivated)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SEND_TARGET_TO_TARGET</td>
<td>100</td>
<td>Id</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Send targets previously stored with SMART_ACTION_STORE_TARGET, to another   npc/go, the other npc/go can then access them as if it was its own stored   list</td>
</tr>
<tr>
<td>SMART_ACTION_SET_HOME_POS</td>
<td>101</td>
<td>0: if the target is a creature, set it's current position as it's new   home position; if the target is SMART_TARGET_POSITION, use this position as   new home position for the actor<br>1: if the target is a creature,   reset it's home position to the one from the DB; if the target is   SMART_TARGET_POSITION, reset the actor's home position to the one from the DB   (the actual values of the target position are ignored)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_HEALTH_REGEN</td>
<td>102</td>
<td>0/1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Sets the current creatures health regen on or off.</td>
</tr>
<tr>
<td>SMART_ACTION_SET_ROOT</td>
<td>103</td>
<td>0/1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Enables or disables creature movement</td>
</tr>
<tr>
<td>SMART_ACTION_SET_GO_FLAG</td>
<td>104</td>
<td>gameobject_template_addon.flags</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>oldFlag = newFlag</td>
</tr>
<tr>
<td>SMART_ACTION_ADD_GO_FLAG</td>
<td>105</td>
<td>gameobject_template_addon.flags</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>oldFlag |= newFlag</td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_GO_FLAG</td>
<td>106</td>
<td>gameobject_template_addon.flags</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>oldFlag &amp;= ~newFlag</td>
</tr>
<tr>
<td>SMART_ACTION_SUMMON_CREATURE_GROUP</td>
<td>107</td>
<td>creature_summon_groups.groupId</td>
<td>attackInvoker (0/1)</td>
<td>attackScriptOwner (0/1)</td>
<td></td>
<td></td>
<td></td>
<td>Use creature_summon_groups table. SAI target has no effect, use 0</td>
</tr>
<tr>
  <td>SMART_ACTION_SET_POWER</td>
  <td>108</td>
  <td>
    <span class="tip-icon" title="
Mana: ID 0
Rage: ID 1
Focus: ID 2
Energy: ID 3
Happiness: ID 4 (usato per alcuni famigli da combattimento)
Runes: ID 5 (usato dai Death Knights)
Runic Power: ID 6 (usato dai Death Knights)
Vita (Health): ID 13
Runes: ID 27 (usato dai Death Knights, diverso da quello del punto 6)
Combo Points: ID 32 (usato dai Rogues e Druids Feral)">Power type (?)</span>
  </td>
  <td>New power</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
</tr>
<tr>
<td>SMART_ACTION_ADD_POWER</td>
<td>109</td>
<td>Power type</td>
<td>Power to add</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_POWER</td>
<td>110</td>
<td>Power type</td>
<td>Power to remove</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_GAME_EVENT_STOP</td>
<td>111</td>
<td>game_event.eventEntry</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_GAME_EVENT_START</td>
<td>112</td>
<td>game_event.eventEntry</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_START_CLOSEST_WAYPOINT</td>
<td>113</td>
<td>wp1</td>
<td>wp2</td>
<td>wp3</td>
<td>wp4</td>
<td>wp5</td>
<td>wp6</td>
<td>Make target follow closest waypoint to its location</td>
</tr>
<tr>
<td>SMART_ACTION_RISE_UP</td>
<td>114</td>
<td>distance</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>move up for the specified distance (warning: TC 3.3.5 uses another action   here: SMART_ACTION_MOVE_OFFSET)</td>
</tr>
<tr>
<td>SMART_ACTION_RANDOM_SOUND</td>
<td>115</td>
<td>soundId1</td>
<td>soundId2</td>
<td>soundId3</td>
<td>soundId4</td>
<td>onlySelf (0/1)</td>
<td>distance</td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_CORPSE_DELAY</td>
<td>116</td>
<td>timer (secs)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_DISABLE_EVADE</td>
<td>117</td>
<td>0/1 (1 = disabled, 0 = enabled)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_GO_SET_GO_STATE</td>
<td>118</td>
<td>state</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_SIGHT_DIST</td>
<td>121</td>
<td>SightDistance</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_FLEE</td>
<td>122</td>
<td>FleeTime</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_ADD_THREAT</td>
<td>123</td>
<td>+threat</td>
<td>-threat</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_LOAD_EQUIPMENT</td>
<td>124</td>
<td>Id</td>
<td>force</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_TRIGGER_RANDOM_TIMED_EVENT</td>
<td>125</td>
<td>id min range</td>
<td>id max range</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_ALL_GAMEOBJECTS</td>
<td>126</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_INVOKER_CAST</td>
<td>134</td>
<td>SpellId</td>
<td>CastFlags</td>
<td>TriggerFlags</td>
<td>LimitTargets - 0: all targets</td>
<td></td>
<td></td>
<td>Make our action invoker type cast a spell to our target type</td>
</tr>
<tr>
<td>SMART_ACTION_PLAY_CINEMATIC</td>
<td>135</td>
<td>entry</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_MOVEMENT_SPEED</td>
<td>136</td>
<td>movementType</td>
<td>speedInteger</td>
<td>speedFraction</td>
<td></td>
<td></td>
<td></td>
<td>MOVE_WALK = 0, MOVE_RUN  = 1, MOVE_RUN_BACK = 2, MOVE_SWIM = 3, MOVE_SWIM_BACK= 4, MOVE_TURN_RATE= 5, MOVE_FLIGHT = 6, MOVE_FLIGHT_BACK = 7, MOVE_PITCH_RATE = 8</td>
</tr>
<tr>
<td>SMART_ACTION_SET_HEALTH_PCT</td>
<td>142</td>
<td>percent</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_MOVE_TO_POS_TARGET</td>
<td>201</td>
<td>pointId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_EXIT_VEHICLE</td>
<td>203</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_UNIT_MOVEMENT_FLAGS</td>
<td>204</td>
<td>flags</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_COMBAT_DISTANCE</td>
<td>205</td>
<td>combatDistance</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_CASTER_COMBAT_DIST</td>
<td>206</td>
<td>followDistance</td>
<td>resetToMax</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_HOVER</td>
<td>207</td>
<td>0/1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_ADD_IMMUNITY</td>
<td>208</td>
<td>type</td>
<td>id</td>
<td>value</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_REMOVE_IMMUNITY</td>
<td>209</td>
<td>type</td>
<td>id</td>
<td>value</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_FALL</td>
<td>210</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_SET_EVENT_FLAG_RESET</td>
<td>211</td>
<td>0/1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_STOP_MOTION</td>
<td>212</td>
<td>stopMoving</td>
<td>movementExpired</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_NO_ENVIRONMENT_UPDATE</td>
<td>213</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_ZONE_UNDER_ATTACK</td>
<td>214</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_LOAD_GRID</td>
<td>215</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_MUSIC</td>
<td>216</td>
<td>SoundId</td>
<td>onlySelf</td>
<td>type</td>
<td></td>
<td></td>
<td></td>
<td>Plays the specified sound file as music. Type can be one of these   values:<br>0: Play music for the specified target(s)<br>1: Play   music for all players in the entire zone<br>2: Play music for all   players in the area.</td>
</tr>
<tr>
<td>SMART_ACTION_RANDOM_MUSIC</td>
<td>217</td>
<td>SoundId1</td>
<td>SoundId2</td>
<td>SoundId3</td>
<td>SoundId4</td>
<td>onlySelf</td>
<td>type</td>
<td>Plays randomly one of the specified sound files as music. Type can be one   of these values:<br>0: Play music for the specified   target(s)<br>1: Play music for all players in the entire   zone<br>2: Play music for all players in the area.</td>
</tr>
<tr>
<td>SMART_ACTION_CUSTOM_CAST</td>
<td>218</td>
<td>spellId</td>
<td>castFlag</td>
<td>bp0</td>
<td>bp1</td>
<td>bp2</td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_ACTION_CONE_SUMMON</td>
<td>219</td>
<td>entry</td>
<td>Duration (ms)<br>0 = permanent</td>
<td>Distance between rings (yards)</td>
<td>Distance between each summons in a row (yards)</td>
<td>Length of the cone (yards)</td>
<td>Width of the cone (angle 1°-360°)</td>
<td>Allows you to spawn creatures in a cone (As seen in later expansions).   Useful for custom cone aoes</td>
</tr>
<tr>
<td>SMART_ACTION_PLAYER_TALK</td>
<td>220</td>
<td>acore_string.id</td>
<td>yell? (0/1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Make the player say something</td>
</tr>
<tr>
<td>SMART_ACTION_VORTEX_SUMMON</td>
<td>221</td>
<td>entry</td>
<td>Duration (ms)<br>0 = permanent</td>
<td>Spiral scaling</td>
<td>Spiral appearance</td>
<td>range max</td>
<td>phi_delta</td>
<td>Allows you to summon creature in a customizable spiral(/vortex).   Parameters can be confusing, exmaple parameters for testing: 5000 - summon   duration, 5 - Spiral Scaling, 25 - spiral appearance, 60 - range max, 40 -   phi delta</td>
</tr>
<tr>
<td>SMART_ACTION_CU_ENCOUNTER_START</td>
<td>222</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Resets all cooldowns and removes exhausted debuffs when action is called</td>
</tr>
<tr>
<td>SMART_ACTION_DO_ACTION</td>
<td>223</td>
<td>ActionId</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Allows to call for a DoAction in code</td>
</tr>
<tr>
<td>SMART_ACTION_ATTACK_STOP</td>
<td>224</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Stop melee, spell casting during combat, chasing the target and facing</td>
</tr>
<tr>
<td>SMART_ACTION_SET_GUID</td>
<td>225</td>
<td>0/1 (0 = Self Guid, 1 = Invoker Guid)</td>
<td>Index</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Allows the target to perform an action similar to DO_ACTION, but allows a guid to be sent</td>
</tr>
<tr>
<td>SMART_ACTION_DISABLE</td>
<td>226</td>
<td>0/1 (0 = Disable, 1 = Enable)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Disable the targeted creatures, setting them Invisible and Immune to All</td>
</tr>
<tr>
<td>SMART_ACTION_SET_SCALE</td>
<td>227</td>
<td>scale - this value is the percentage of the new scale the targets will take. 100 = default</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Sets the scale for the targeted creatures</td>
</tr>
<tr>
<td>SMART_ACTION_SUMMON_RADIAL</td>
<td>228</td>
<td>summonEntry - CreatureID to be summoned</td>
<td>summonDuration - duration in ms which the summons will despawn after, if 0 then despawn on death</td>
<td>repetitions - amount of creatures to be summoned</td>
<td>startAngle - offset in degrees, 0: same as source</td>
<td>stepAngle - how many degrees to turn for each summon</td>
<td>dist - distance offset</td>
<td>Summons a set of creatures in a radial pattern, with orientation change specified in parameters</td>
</tr>
<tr>
<td>SMART_ACTION_PLAY_SPELL_VISUAL</td>
<td>229</td>
<td>visualId - can be found within SpellVisual.dbc</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Makes the targets play the VisualKit ID specified</td>
</tr>
</tbody>
</table>
<h3 id="predefined-sai-templates">Predefined SAI templates</h3>
<table>
<thead>
<tr>
<th>Description Name</th>
<th>Value (Param1)</th>
<th>Param2</th>
<th>Param3</th>
<th>Param4</th>
<th>Param5</th>
<th>Param6</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMARTAI_TEMPLATE_BASIC</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMARTAI_TEMPLATE_CASTER</td>
<td>1</td>
<td>spellid</td>
<td>repeatMin</td>
<td>repeatMax</td>
<td>range</td>
<td>manaPCT</td>
<td>+JOIN: target_param1 as castFlag</td>
</tr>
<tr>
<td>SMARTAI_TEMPLATE_TURRET</td>
<td>2</td>
<td>spellid</td>
<td>repeatMin</td>
<td>repeatMax</td>
<td>range</td>
<td>manaPCT</td>
<td>+JOIN: target_param1 as castflag</td>
</tr>
<tr>
<td>SMARTAI_TEMPLATE_PASSIVE</td>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMARTAI_TEMPLATE_CAGED_GO_PART</td>
<td>4</td>
<td>creatureID</td>
<td>give credit at point end (0/1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMARTAI_TEMPLATE_CAGED_NPC_PART</td>
<td>5</td>
<td>gameObjectID</td>
<td>despawntime</td>
<td>run (0/1)</td>
<td>dist</td>
<td>TextGroupID</td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="targettype">target_type</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Value</th>
<th>target_param1</th>
<th>target_param2</th>
<th>target_param3</th>
<th>target_param4</th>
<th>target_x</th>
<th>target_y</th>
<th>target_z</th>
<th>target_o</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMART_TARGET_NONE</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>None.</td>
</tr>
<tr>
<td>SMART_TARGET_SELF</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Self cast.</td>
</tr>
<tr>
<td>SMART_TARGET_VICTIM</td>
<td>2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Our current target. (ie: highest aggro)</td>
</tr>
<tr>
<td>SMART_TARGET_HOSTILE_SECOND_AGGRO</td>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Second highest aggro.</td>
</tr>
<tr>
<td>SMART_TARGET_HOSTILE_LAST_AGGRO</td>
<td>4</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Dead last on aggro.</td>
</tr>
<tr>
<td>SMART_TARGET_HOSTILE_RANDOM</td>
<td>5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Just any random target on our threat list.</td>
</tr>
<tr>
<td>SMART_TARGET_HOSTILE_RANDOM_NOT_TOP</td>
<td>6</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Any random target except top threat.</td>
</tr>
<tr>
<td>SMART_TARGET_ACTION_INVOKER</td>
<td>7</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Unit who caused this Event to occur.</td>
</tr>
<tr>
<td>SMART_TARGET_POSITION</td>
<td>8</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>x</td>
<td>y</td>
<td>z</td>
<td>o</td>
<td>Use xyz from event params.</td>
</tr>
<tr>
<td>SMART_TARGET_CREATURE_RANGE</td>
<td>9</td>
<td>creature_template.entry (0 any)</td>
<td>minDist</td>
<td>maxDist</td>
<td>alive state (1 alive, 2 dead, 0 both)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>All creatures with the specified ID within the specified range and the   specified alive state.</td>
</tr>
<tr>
<td>SMART_TARGET_CREATURE_GUID</td>
<td>10</td>
<td>creature.guid</td>
<td>creature_template.entry</td>
<td>getFromHashMap (0/1, this does not work in instances!)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Creature with specified GUID and/or specified creature template ID.</td>
</tr>
<tr>
<td>SMART_TARGET_CREATURE_DISTANCE</td>
<td>11</td>
<td>creature_template.entry (0 any)</td>
<td>maxDist</td>
<td>alive state (1 alive, 2 dead, 0 both)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>All creatures with the specified ID within the specified distance and the   specified alive state.</td>
</tr>
<tr>
<td>SMART_TARGET_STORED</td>
<td>12</td>
<td>id</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Uses pre-stored target(list)</td>
</tr>
<tr>
<td>SMART_TARGET_GAMEOBJECT_RANGE</td>
<td>13</td>
<td>gameobject_template.entry (0 any)</td>
<td>minDist</td>
<td>maxDist</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>All game objects with the specified ID within the specified range.</td>
</tr>
<tr>
<td>SMART_TARGET_GAMEOBJECT_GUID</td>
<td>14</td>
<td>gameobject.guid</td>
<td>gameobject_template.entry</td>
<td>getFromHashMap (0/1, this does not work in instances!)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Object with specified GUID and/or specified game object template ID.</td>
</tr>
<tr>
<td>SMART_TARGET_GAMEOBJECT_DISTANCE</td>
<td>15</td>
<td>gameobject_template.entry (0 any)</td>
<td>maxDist</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>All objects with the specified ID within the specified distance.</td>
</tr>
<tr>
<td>SMART_TARGET_INVOKER_PARTY</td>
<td>16</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Invoker's party members</td>
</tr>
<tr>
<td>SMART_TARGET_PLAYER_RANGE</td>
<td>17</td>
<td>minDist</td>
<td>maxDist</td>
<td>maxCount</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>When target.o is set and it didnt find any targets in min-max range, it   will try all possible targets in max range instead.</td>
<td>All players up to maxCount within the specified range. Excluding GMs and   Dead.</td>
</tr>
<tr>
<td>SMART_TARGET_PLAYER_DISTANCE</td>
<td>18</td>
<td>maxDist</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>All players within the specified distance.</td>
</tr>
<tr>
<td>SMART_TARGET_CLOSEST_CREATURE</td>
<td>19</td>
<td>creature_template.entry (0 any)</td>
<td>maxDist (Can be from 0-100 yards)</td>
<td>dead? (0/1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Closest creature with the specified ID within the specified range.</td>
</tr>
<tr>
<td>SMART_TARGET_CLOSEST_GAMEOBJECT</td>
<td>20</td>
<td>gameobject_template.entry (0 any)</td>
<td>maxDist (Can be from 0-100 yards)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Closest object with specified ID within specified range.</td>
</tr>
<tr>
<td>SMART_TARGET_CLOSEST_PLAYER</td>
<td>21</td>
<td>maxDist</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Closest player within specified range.</td>
</tr>
<tr>
<td>SMART_TARGET_ACTION_INVOKER_VEHICLE</td>
<td>22</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Unit's vehicle who caused this Event to occur</td>
</tr>
<tr>
<td>SMART_TARGET_OWNER_OR_SUMMONER</td>
<td>23</td>
<td>use owner of owner (0/1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Unit's owner or summoner</td>
</tr>
<tr>
<td>SMART_TARGET_THREAT_LIST</td>
<td>24</td>
<td>maxDist (0 any)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>All units on creature's threat list within the specified distance if   maxDist &gt; 0</td>
</tr>
<tr>
<td>SMART_TARGET_CLOSEST_ENEMY</td>
<td>25</td>
<td>maxDist</td>
<td>playerOnly (0/1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Any attackable target (creature or player) within maxDist</td>
</tr>
<tr>
<td>SMART_TARGET_CLOSEST_FRIENDLY</td>
<td>26</td>
<td>maxDist</td>
<td>playerOnly (0/1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Any friendly unit (creature, player or pet) within maxDist</td>
</tr>
<tr>
<td>SMART_TARGET_LOOT_RECIPIENTS</td>
<td>27</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>All players that have tagged this creature (for kill credit)</td>
</tr>
<tr>
<td>SMART_TARGET_FARTHEST</td>
<td>28</td>
<td>maxDist</td>
<td>playerOnly (0/1)</td>
<td>isInLos (0/1)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Farthest unit on the threat list</td>
</tr>
<tr>
<td>SMART_TARGET_VEHICLE_PASSENGER</td>
<td>29</td>
<td>seat number (vehicle can target it's own accessory)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_TARGET_PLAYER_WITH_AURA</td>
<td>201</td>
<td>spellID</td>
<td>Negative (0/1)</td>
<td>MaxDist</td>
<td>MinDist</td>
<td></td>
<td></td>
<td></td>
<td>Number to resize the target list</td>
<td>Target players with or without aura</td>
</tr>
<tr>
<td>SMART_TARGET_RANDOM_POINT</td>
<td>202</td>
<td>range (yards)</td>
<td>amount (for summoning creature)</td>
<td>self as middle (0/1)<br>else use xyz</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>This only works with SMART_ACTION_SUMMON_CREATURE,   SMART_ACTION_MOVE_TO_POS and SMART_ACTION_JUMP_TO_POS</td>
</tr>
<tr>
<td>SMART_TARGET_ROLE_SELECTION</td>
<td>203</td>
<td>rangeMax (yards)</td>
<td>TargetMask (Tanks (1), Healer (2) Damage (4))</td>
<td>Resize list</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Target a Tank/Healer/DPS role. Based on the players spec.</td>
</tr>
<tr>
<td>SMART_TARGET_SUMMONED_CREATURES</td>
<td>204</td>
<td><a href="creature_template#entry">creature_template.Entry</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>SMART_TARGET_INSTANCE_STORAGE</td>
<td>205</td>
<td>data index</td>
<td>Type (creature (1), gameobject (2))</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="comment">comment</h3>
<p>Commenting on SAI uses a template which is the following: (with an example)</p>
<p>"Creature name - Event - Action"</p>
<p>"Minion of Gurok - On spawn - Set Random Movement"</p>
<p><strong>Quick notes:</strong></p>
<ul>
<li>Always update <em>creature_template</em>,<em>gameobject_template</em> or <em>areatrigger_scripts</em> with:</li>
</ul>
<div class="language-sql highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">UPDATE</span> <span class="nv">`creature_template`</span> <span class="k">SET</span> <span class="nv">`AIName`</span> <span class="o">=</span> <span class="s1">'SmartAI'</span> <span class="k">WHERE</span> <span class="nv">`entry`</span> <span class="o">=</span> <span class="n">y</span><span class="p">;</span>

<span class="k">UPDATE</span> <span class="nv">`gameobject_template`</span> <span class="k">SET</span> <span class="nv">`AIName`</span> <span class="o">=</span> <span class="s1">'SmartGameObjectAI'</span> <span class="k">WHERE</span> <span class="nv">`entry`</span> <span class="o">=</span> <span class="n">y</span><span class="p">;</span>

<span class="k">INSERT</span> <span class="k">INTO</span> <span class="nv">`areatrigger_scripts`</span> <span class="p">(</span><span class="nv">`entry`</span><span class="p">,</span> <span class="nv">`ScriptName`</span><span class="p">)</span> <span class="k">VALUES</span> <span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="s1">'SmartTrigger'</span><span class="p">);</span>
</code></pre></div></div>
<ul>
<li>If the creature or GO is inside a dungeon, set <em>event_flags</em> accordingly to the instance difficulty (heroic, 25 man, etc.).</li>
</ul>
<p><strong>In case of doubt about an <em>Event</em>, <em>Action_or _Target,_check source code (_src/server/game/AI/SmartScripts</em> files; mainly *SmartScript.cpp</strong>)</p>
<h3 id="cast-flags">Cast Flags</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Flag</th>
<th>Hex</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMARTCAST_INTERRUPT_PREVIOUS</td>
<td>1</td>
<td>0x01</td>
<td>Interrupt any spell casting</td>
</tr>
<tr>
<td>SMARTCAST_TRIGGERED</td>
<td>2</td>
<td>0x02</td>
<td>Triggered (this makes spell cost zero mana and have no cast time)</td>
</tr>
<tr>
<td>CAST_AURA_NOT_PRESENT</td>
<td>32</td>
<td>0x20</td>
<td>Only casts the spell if the target does not have an aura from the spell</td>
</tr>
<tr>
<td>SMARTCAST_COMBAT_MOVE</td>
<td>64</td>
<td>0x40</td>
<td>Prevent combat movement on cast, allow on fail range, mana, LOS</td>
</tr>
</tbody>
</table>
<h3 id="triggered-flags">Triggered Flags</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Flag</th>
<th>Hex</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>TRIGGERED_NONE</td>
<td>0</td>
<td>0x00000000</td>
<td>Not triggered</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_GCD</td>
<td>1</td>
<td>0x00000001</td>
<td>Will ignore GCD</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_SPELL_AND_CATEGORY_CD</td>
<td>2</td>
<td>0x00000002</td>
<td>Will ignore Spell and Category cooldowns</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_POWER_AND_REAGENT_COST</td>
<td>4</td>
<td>0x00000004</td>
<td>Will ignore power and reagent cost</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_CAST_ITEM</td>
<td>8</td>
<td>0x00000008</td>
<td>Will not take away cast item or update related achievement criteria</td>
</tr>
<tr>
<td>RIGGERED_IGNORE_AURA_SCALING</td>
<td>16</td>
<td>0x00000010</td>
<td>Will ignore aura scaling</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_CAST_IN_PROGRESS</td>
<td>32</td>
<td>0x00000020</td>
<td>Will not check if a current cast is in progress</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_COMBO_POINTS</td>
<td>64</td>
<td>0x00000040</td>
<td>Will ignore combo point requirement</td>
</tr>
<tr>
<td>TRIGGERED_CAST_DIRECTLY</td>
<td>128</td>
<td>0x00000080</td>
<td>In Spell::prepare, will be cast directly without setting containers for executed spell</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_AURA_INTERRUPT_FLAGS</td>
<td>256</td>
<td>0x00000100</td>
<td>Will ignore interruptible aura's at cast</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_SET_FACING</td>
<td>512</td>
<td>0x00000200</td>
<td>Will not adjust facing to target (if any)</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_SHAPESHIFT</td>
<td>1024</td>
<td>0x00000400</td>
<td>Will ignore shapeshift checks</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_CASTER_AURASTATE</td>
<td>2048</td>
<td>0x00000800</td>
<td>Will ignore caster aura states including combat requirements and death state</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_CASTER_MOUNTED_OR_ON_VEHICLE</td>
<td>8192</td>
<td>0x00002000</td>
<td>Will ignore mounted/on vehicle restrictions</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_CASTER_AURAS</td>
<td>65536</td>
<td>0x00010000</td>
<td>Will ignore caster aura restrictions or requirements</td>
</tr>
<tr>
<td>TRIGGERED_DISALLOW_PROC_EVENTS</td>
<td>131072</td>
<td>0x00020000</td>
<td>Disallows proc events from triggered spell (default)</td>
</tr>
<tr>
<td>TRIGGERED_DONT_REPORT_CAST_ERROR</td>
<td>262144</td>
<td>0x00040000</td>
<td>Will return SPELL_FAILED_DONT_REPORT in CheckCast functions</td>
</tr>
<tr>
<td>TRIGGERED_FULL_MASK</td>
<td>524287</td>
<td>0x0007FFFF</td>
<td>All triggered flags</td>
</tr>
<tr>
<td>TRIGGERED_IGNORE_EQUIPPED_ITEM_REQUIREMENT</td>
<td>524288</td>
<td>0x00080000</td>
<td>Will ignore equipped item requirements</td>
</tr>
<tr>
<td>TRIGGERED_NO_PERIODIC_RESET</td>
<td>1048576</td>
<td>0x00100000</td>
<td>Periodic aura tick wont be reset on override</td>
</tr>
<tr>
<td>TRIGGERED_FULL_DEBUG_MASK</td>
<td>4294967295</td>
<td>0xFFFFFFFF</td>
<td></td>
</tr>
</tbody>
</table>
<p><strong>NOTICE:</strong> If triggeredFlags = 0, cast will trigger with TRIGGERED_FULL_MASK = 524287.</p>
<h3 id="react-states">React States</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Value</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>REACT_PASSIVE</td>
<td>0</td>
<td>Does not defend or attack at all. Does nothing.</td>
</tr>
<tr>
<td>REACT_DEFENSIVE</td>
<td>1</td>
<td>Only attacks back when attacked.</td>
</tr>
<tr>
<td>REACT_AGGRESSIVE</td>
<td>2</td>
<td>Will attack if on threat list and in threat radius. (default)</td>
</tr>
</tbody>
</table>
<h3 id="summon-types">Summon Types</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Value</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>TEMPSUMMON_TIMED_OR_DEAD_DESPAWN</td>
<td>1</td>
<td>Despawns after a specified time OR when the creature disappears.</td>
</tr>
<tr>
<td>TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN</td>
<td>2</td>
<td>Despawns after a specified time OR when the creature dies.</td>
</tr>
<tr>
<td>TEMPSUMMON_TIMED_DESPAWN</td>
<td>3</td>
<td>Despawns after a specified time.</td>
</tr>
<tr>
<td>TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT</td>
<td>4</td>
<td>Despawns after a specified time after the creature is out of combat.</td>
</tr>
<tr>
<td>TEMPSUMMON_CORPSE_DESPAWN</td>
<td>5</td>
<td>Despawns instantly after death.</td>
</tr>
<tr>
<td>TEMPSUMMON_CORPSE_TIMED_DESPAWN</td>
<td>6</td>
<td>Despawns after a specified time after death.</td>
</tr>
<tr>
<td>TEMPSUMMON_DEAD_DESPAWN</td>
<td>7</td>
<td>Despawns when the creature disappears.</td>
</tr>
<tr>
<td>TEMPSUMMON_MANUAL_DESPAWN</td>
<td>8</td>
<td>Despawns when UnSummon() (or Force Despawn action) is called.</td>
</tr>
</tbody>
</table>
<h3 id="invoker">Invoker:</h3>
<blockquote>
<p>white list of events that actually have an invoker passed to them</p>
</blockquote>
<blockquote>
<p>Actions like SMART_ACTION_INVOKER_CAST and targets like SMART_TARGET_ACTION_INVOKER will work only if the event is in this list:</p>
</blockquote>
<ul>
<li>SMART_EVENT_AGGRO</li>
<li>SMART_EVENT_DEATH</li>
<li>SMART_EVENT_KILL</li>
<li>SMART_EVENT_SUMMONED_UNIT</li>
<li>SMART_EVENT_SPELLHIT</li>
<li>SMART_EVENT_SPELLHIT_TARGET</li>
<li>SMART_EVENT_DAMAGED</li>
<li>SMART_EVENT_RECEIVE_HEAL</li>
<li>SMART_EVENT_RECEIVE_EMOTE</li>
<li>SMART_EVENT_JUST_SUMMONED</li>
<li>SMART_EVENT_DAMAGED_TARGET</li>
<li>SMART_EVENT_SUMMON_DESPAWNED</li>
<li>SMART_EVENT_PASSENGER_BOARDED</li>
<li>SMART_EVENT_PASSENGER_REMOVED</li>
<li>SMART_EVENT_GOSSIP_HELLO</li>
<li>SMART_EVENT_GOSSIP_SELECT</li>
<li>SMART_EVENT_ACCEPTED_QUEST</li>
<li>SMART_EVENT_REWARD_QUEST</li>
<li>SMART_EVENT_FOLLOW_COMPLETED</li>
<li>SMART_EVENT_ON_SPELLCLICK</li>
<li>SMART_EVENT_GO_LOOT_STATE_CHANGED</li>
<li>SMART_EVENT_AREATRIGGER_ONTRIGGER</li>
<li>SMART_EVENT_IC_LOS</li>
<li>SMART_EVENT_OOC_LOS</li>
<li>SMART_EVENT_DISTANCE_CREATURE</li>
<li>SMART_EVENT_FRIENDLY_HEALTH</li>
<li>SMART_EVENT_FRIENDLY_HEALTH_PCT</li>
<li>SMART_EVENT_FRIENDLY_IS_CC</li>
<li>SMART_EVENT_FRIENDLY_MISSING_BUFF</li>
<li>SMART_EVENT_ACTION_DONE</li>
<li>SMART_EVENT_TARGET_HEALTH_PCT</li>
<li>SMART_EVENT_TARGET_MANA_PCT</li>
<li>SMART_EVENT_RANGE</li>
<li>SMART_EVENT_VICTIM_CASTING</li>
<li>SMART_EVENT_TARGET_BUFFED</li>
<li>SMART_EVENT_IS_BEHIND_TARGET</li>
<li>SMART_EVENT_INSTANCE_PLAYER_ENTER</li>
<li>SMART_EVENT_TRANSPORT_ADDCREATURE</li>
<li>SMART_EVENT_DATA_SET</li>
</ul>

</div>
