# How to use changelog

All breaking/notable changes to this project will be documented in the `/docs/changelog/master` file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](project-versioning).

**This changelog should provide an easy way for the developers to upgrade their own code which is connected to AzerothCore** (e.g. modules, APIs, scripts etc.)
It's not a way to keep track of ALL the changes made (we have the git history for that). Therefore, just 2 golden rules to follow:

- **DO WRITE** changelog when you added breaking changes, security fixes or important new features that other people can use.
- **DO NOT WRITE** changelog when you are adding small fixes or minor improvements.

## How to create a changelog

The creation of a changelog for a PR is similar to the creation of a new sql file.
Under the `doc/changelog/pendings` folder you will find a `create.sh` script.

Run this script to create a new changelog file in the same folder which will be automatically called `changes_<timestamp>.md`.

Once the PR is merged, our pipeline will merge your file into the `doc/changelog/master` by automatically creating a new section inside that file.
This section will be titled with the new version number based on the previous one from the `acore.json` file you can find within the root folder.

So, for instance:

if the current version is `1.0.0-dev.1`, after your PR is merged it will be changed to `1.0.0-dev.2` automatically within the `acore.json` and a new section 
called `## 1.0.0-dev.2` will be created under the `master` changelog.

This approach is pretty useful also for modules to keep track of the compatibility

## How to write a changelog

It's mandatory to use the "[Keep a Changelog](https://keepachangelog.com/en/1.0.0/)" format, by correctly using the following types of section titles:

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Security in case of vulnerabilities.

You have to create a new H3 section ( `###` in markdown) for every different type of changes.

For example:

```
### Added

- new hooks X, Y
- new formula for Z

### Changed

- return value for hook X, now it's boolean instead of void
```

### Document how to upgrade

After the sections above you have to describe the steps needed to upgrade the code. This is the **most important part** and it's particulary useful for module authors to fix their code based on what you changed without struggling reading tons of commits and looking for information around.

To do so, you can use the generated ```### How to upgrade``` section by our `create.sh`. 
Please, be as much as detailed as possible. 
If the guidelines are very long and they require more than few lines (an entire wiki page for instance), you can just link that page then.

Example:

```
### How to upgrade

- The hook OnCheck of the Achievement script class now returns a boolean instead of a void. Add `return true` to your methods if you don't want to change the original behaviour. 
```

## How to release a new major version

This is a manual process. Everytime we release a new major version (4.0.0, 5.0.0 etc.) we need to move the `master` into the `doc/changelog/previous-versions` folder and rename it using this format: `v[major].x`. After that we have to create a new empty `master` file
