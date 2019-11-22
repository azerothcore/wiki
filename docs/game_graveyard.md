# game_graveyard

[<-Back-to:World](database-world.md)

<table>
<tbody>
<tr class="even">
<td><p><strong>Field</strong></p></td>
<td><p><strong>Type</strong></p></td>
<td><p><strong>Attributes</strong></p></td>
<td><p><strong>Key</strong></p></td>
<td><p><strong>Null</strong></p></td>
<td><p><strong>Default</strong></p></td>
</tr>
<tr class="even">
<td><p><a href="#id">ID</a></p></td>
<td><p>int(8)</p></td>
<td><p>unasigned</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><a href="#ghost_zone">Map</a></p></td>
<td><p>int(10)</p></td>
<td><p>unasigned</p></td>
<td><p></p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><a href="#faction">x</a></p></td>
<td><p>float</p></td>
<td><p>unasigned</p></td>
<td><p></p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><a href="#faction">y</a></p></td>
<td><p>float</p></td>
<td><p>unasigned</p></td>
<td><p></p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><a href="#faction">z</a></p></td>
<td><p>float</p></td>
<td><p>unasigned</p></td>
<td><p></p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><a href="#faction">Comment</a></p></td>
<td><p>varchar(255)</p></td>
<td><p>unasigned</p></td>
<td><p></p></td>
<td><p>Yes</p></td>
<td><p>0</p></td>
</tr>
</tbody>
</table>

**Description of the fields**

### ID
Graveyard's ID. See [WorldSafeLocs.dbc](WorldSafelocs)

### Map
Zone's ID of ghost position before teleportation to graveyard. See Map.dbc column 1

### posX

The X position of graveyard where the character's ghost gets teleported to.

### posY

The Y position of graveyard where the character's ghost gets teleported to.

### posZ

The Z position of graveyard where the character's ghost gets teleported to.

### Comment

Custom comment for this line.

