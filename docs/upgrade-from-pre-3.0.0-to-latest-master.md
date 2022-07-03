# Upgrade from pre 3.0.0 to latest master

This is the tutorial to upgrade any existing server from a version prior to the [3.0.0 release](https://github.com/azerothcore/azerothcore-wotlk/releases/tag/v3.0.0) to the latest `master` version.

**Note**: it is always recommended to backup your database before doing ANY update.

### Step 1. Upgrade to last 3.0.0 commit

You need first to update your server to [this commit](https://github.com/azerothcore/azerothcore-wotlk/commit/2d609e9e48b2e516e4a555015b2662cab15b0c38), running:

```
git pull; git checkout 2d609e9e48b2e516e4a555015b2662cab15b0c38
```

Now update your **database** as you usually do (e.g. using the db-assembler)

### Step 2. Upgrade to latest master

Update to latest master:

`git checkout master; git pull;`

**Note**: if you are using your own fork of AC, as usual, you have to [sync it](Syncing-your-fork)

Now update your **core and database** (again) as [you normally do](Update).
