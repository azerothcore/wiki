# character\_achievement

[<-Back-to:Characters](database-characters.md)

**The \`character\_achievement\` table**

This table holds information on the achievements a character has earned / completed.

**Note:** if you delete a "realm first" achievement from the characters database, you have to reboot the server to take it into account.

**Structure**

<table>
<tbody>
<tr class="odd">
<td><p><strong>Field</strong></p></td>
<td><p><strong>Type</strong></p></td>
<td><p><strong>Attributes</strong></p></td>
<td><p><strong>Key</strong></p></td>
<td><p><strong>Null</strong></p></td>
<td><p><strong>Default</strong></p></td>
<td><p><strong>Extra</strong></p></td>
<td><p><strong>Comment</strong></p></td>
</tr>
<tr class="even">
<td><p><a href="#guid">guid</a></p></td>
<td><p>int(10)</p></td>
<td><p>unsigned</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="odd">
<td><p><a href="#achievement">achievement</a></p></td>
<td><p>smallint(5)</p></td>
<td><p>unsigned</p></td>
<td><p>PRI</p></td>
<td><p>NO</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
<tr class="even">
<td><p><a href="#date">date</a></p></td>
<td><p>int(10)</p></td>
<td><p>unsigned</p></td>
<td><p><br />
</p></td>
<td><p>NO</p></td>
<td><p>0</p></td>
<td><p><br />
</p></td>
<td><p><br />
</p></td>
</tr>
</tbody>
</table>

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters_table_)

### achievement

The ID of the achievement from [Achievement.dbc](Achievement).

### date

The date/time when this achievement was earned, in Unix time. See [Unix Timestamp Calculator](http://www.unixtimestamp.com/index.php)