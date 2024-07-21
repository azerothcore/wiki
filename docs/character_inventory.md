# character\_inventory

[<-Back-to:Characters](database-characters)

**The \`character\_inventory\` table**

Contains all the character inventory data, including the bank data.

**Table Structure**

| Field     | Type    | Attributes | Key    | Null | Default | Extra | Comment                       |
| --------- | ------- | ---------- | ------ | ---- | ------- | ----- | ----------------------------- |
| [guid][1] | INT     | UNSIGNED   | Unique | NO   | 0       |       | Global Unique Identifier      |
| [bag][2]  | INT     | UNSIGNED   |        | NO   | 0       |       |                               |
| [slot][3] | TINYINT | UNSIGNED   |        | NO   | 0       |       |                               |
| [item][4] | INT     | UNSIGNED   | PRI    | NO   | 0       |       | Item Global Unique Identifier |

[1]: #guid
[2]: #bag
[3]: #slot
[4]: #item

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### bag

If it isn't 0, then it is the bag's item GUID. See [item\_instance.guid](item_instance#guid).

### slot

If the bag field is non-zero, then the slot is the slot in the bag where the item is kept. The range can differ depending on the number of slots the bag has.

If the bag field is zero, then the slot has a range of 0 to 130 and the value stands for the following:

| Slot    | Value                                  |
| ------- | -------------------------------------- |
| 0       | Head                                   |
| 1       | Neck                                   |
| 2       | Shoulders                              |
| 3       | Body                                   |
| 4       | Chest                                  |
| 5       | Waist                                  |
| 6       | Legs                                   |
| 7       | Feet                                   |
| 8       | Wrists                                 |
| 9       | Hands                                  |
| 10      | Finger 1                               |
| 11      | Finger 2                               |
| 12      | Trinket 1                              |
| 13      | Trinket 2                              |
| 14      | Back                                   |
| 15      | Main Hand                              |
| 16      | Off Hand                               |
| 17      | Ranged                                 |
| 18      | Tabard                                 |
| 19-22   | Equipped Bags                          |
| 23-38   | Main Backpack                          |
| 39-66   | Main Bank                              |
| 67-73   | Bank Bags                              |
| 86-117  | Keys in Keyring                        |
| 118-135 | Currencies (Emblems,badges,marks etc.) |

### item

The item's GUID. See [item\_instance.guid](item_instance#guid).
