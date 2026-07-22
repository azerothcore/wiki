# profanity_name

[<-Back-to:Characters](database-characters)

**The `profanity_name` table**

List of disallowed name fragments used by the profanity name filter to reject character, pet and similar names. See also [reserved_name](reserved_name) for fully reserved names.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [name](#name) | VARCHAR(12) |  | PRI | NO |  |  |  |

**Description of the fields**

### name

Disallowed name fragment (case-insensitive) that is blocked by the profanity filter.
