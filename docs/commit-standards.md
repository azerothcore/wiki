# Commit Standards

A commit message or PR Title should be short and desciptive.

We follow the [Conventional Commit specification](https://www.conventionalcommits.org/en/v1.0.0/) to provide a lightweight convension on top of the commit message.

## The commit title is structured 

```
<type>(Scope / Subscope): <description>
```

| Type | |
| fix  | Used when we fix a bug |
| feat | Used when we introduce a new feature to the core |
| refactor | Used if we overhaul and rework things to a larger scale |
| chore | For minor changes with minial output |
| ci   | Used when we change something in our workflow |
| docs | When changing any documentation |

Most common Scope that is used:

| Scope | |
| DB | Used for DB only changes |
| Script | Used for Script only changes |
| Core | Used for any changes that involves the core |

Most common Subscope that is used:

| Subscope | DB | Script | Core |
| Creature | x | x | |
| Quest | x | x | |
| Boss | x | x | |
| GameObject | x | | x |
| Spell | x | | x |
| Command | x | | x |
| Event | x | | | x |

## Commit Message

Should include if the commit closes an issue.

The commit message is optional but should contain useful information of the changes that you have made.

Every new point in the message should start with `*`.

If your changes include parts from another project you should include link to the commit and and the original author as co-author.

## Breaking Changes

If your changes are breaking something it is useful if you add that information here using the prefix BREAKING CHANGE: in the Commit Message

You can also include `!` after the <type> in the commit title to indicate it is breaking something.

## Example

```
* A comment

* Describes something

Co-authored-by: name <name@example.com>
```
