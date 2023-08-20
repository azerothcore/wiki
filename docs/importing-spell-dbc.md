# ARCHIVED - NOT IN USE. SAVED FOR HISTORY LESSONS

# Importing data to the spell_dbc table

## Introduction

The [spell_dbc](spell_dbc.md) contains data regarding serverside spells which are not to be found in Client DBC files as well as **overrides** of the DBC that are meant to improve or fix any spell.

In order to add overrides for a spell in the `spell_dbc` table, you first need to import the base data about that spell from the Client DBC files (unless that spell has already been imported).

There are around 50k spells in the Client DBC files, you can import one spell or the whole set to the `spell_dbc` table of your local AC database in order to be able to work on them and add your overrides.

When you import the spell from the DBC, you'll get an `INSERT IGNORE` query with all the default values. Save this query somewhere, you'll need it to submit your PR fix.
After you have imported the spell(s), you can use tools such as [Keira3](https://www.azerothcore.org/Keira3/) to easily get the `UPDATE` query containing your overrides.

When submitting a PR with a `spell_dbc` fix for a certain spell, if that spell was not present in the `spell_dbc` table before, you have to include both the `INSERT IGNORE` and the `UPDATE` query in your PR.

## How to import spells from the DBC files to the spell_dbc table

To import data from Spell.dbc to our spell_dbc table, you can take a look at the general guide on [how to import data from DBC files](how-to-import-dbc-data-in-db.md).
You just need to use the same guidelines with by using the Spell.dbc file instead.
