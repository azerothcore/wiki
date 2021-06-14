---
redirect_from: "/Project-Versioning"
---

## Project Versioning

We are using the semantic versioning standard:

http://semver.org/spec/v2.0.0.html

For instance, we can have: **1.5.1-dev.1** that corresponds to: **MAJOR.MINOR.PATCH-PRERELEASE**

More in depth:

**MAJOR** version when you make incompatible API / DB structure changes

**MINOR** version when you add functionality in a backwards-compatible manner

**PATCH** version when you make backwards-compatible bug fixes.

**PRERELEASE** this is such called "metadata" in semver standard. We use this part of the versioning while we work on **master** branch. Everytime a new feature or breaking change is released, this number is increased to notify you regarding possible actions to take. Check [how to use the changelog](how-to-use-changelog.md).

## Dev stages

* **PHASE 1: Developing Phase**: During the developing phase, we will use the master branch where we can freely make changes to API, DB and all things that could break compatibility with old revisions. 
At the beginning of each development phase, we will clean the sql/updates folders archiving old SQLs.

  N.B. 
  * Some big jobs, such as rewriting/implementing features, could be not ready for next revision and eventually they will be planned for a future one, so they will be kept in dedicated branches instead of master. 
  * Using master branch you will have immediate access to new awesome features, but you must take care since some commits can break stability in some rare cases.


* **PHASE 2: Only Stability and security fixes**: In this phase we will stop to import mechanic / content fix and we will offer support to only security and stability issues. For example: if a function generates a crash for a null pointer, we will fix it.

  We could eventually extends this phase if requested by many people.

* **PHASE 3: End of Life ( EOL )**: We will archive that release keeping documentation and branch ofc. You can continue to use/download it, but we won't offer any official support of any kind

## List of releases

NOTE: this is outdated, check our [releases](https://github.com/azerothcore/azerothcore-wotlk/releases) on github
  
| version/branch | codename  | description | current state | release data | end of support|
|     --         |    --     |      --     |           --  |       --     |      --       |
|     0.x        |  Sunwell|  small reworks for sunwell  |EOL|      2016 Q3 |      2017  Q1 |
|     1.x        |  Mimiron | first version to introduce the module system | EOL|     2017 Q1 |      2019  Q1 |
|     2.x        |  Gunship | Integrated CI/CD and tons of fixes  | Security & Stability   |     2019 Q1 |      ~ |
|     master (3.x)        |  ~ | ~ | developing |     ~ |      ~|
