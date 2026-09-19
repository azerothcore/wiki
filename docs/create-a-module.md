---
redirect_from: "/Create-a-Module"
---

# Create a Module

## **How to create a module**

Before start we suggest you to read [Documentation about modular structure](the-modular-structure) to understand the way AzerothCore works.

### Resources

- Module template (heavily recommended): [https://github.com/azerothcore/skeleton-module](https://github.com/azerothcore/skeleton-module)
- Script template: https://github.com/azerothcore/azerothcore-boilerplates
- All the hooks in the core are listed in [ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h). If you need custom hooks, they can be added to the core by [sending a PR](how-to-create-a-pr).
- Existing modules listed in the catalogue: [https://www.azerothcore.org/catalogue.html](https://www.azerothcore.org/catalogue.html)
- If you need to create a new hook for your module, please follow this guide: [How to create a new hook](hooks-script)

### **The Basis**

1. Create a folder inside `modules/` directory

2. Now you can develop add anything to the main project, such as some scripts or
even an entire library

Note: we suggest to use the [directory structure](directory-structure) standards of AzerothCore to better organize your modules and be familiar with main project.

### **Add the first script**

1. Before continue, we suggest you to follow our guide on how to create a script for AzerothCore

2. After you’ve created your script you’ve to create a .cpp file to handle the script loading.

  For example ( Assuming you’ve created an src folder ):

  `my_custom_loader.cpp`

 ```cpp
// From SC
void AddMyCustomScripts();

// Add all
// cf. the naming convention https://github.com/azerothcore/azerothcore-wotlk/blob/master/doc/changelog/master#how-to-upgrade-4
// additionally replace all '-' in the module folder name with '_' here
void Addmod_my_customScripts()
{
    AddMyCustomScripts();
}
```

  NOTE: AddMyCustomScripts is composed by:

  Add (Prefix)

  MyCustom (An unique name identifier for your script to avoid function collisions)

  Scripts ( Suffix )

### **Create a custom configuration file**

if you need to add a custom configuration file to your module that will be installed with server, the steps are very simple.

1. Add a file with the extension `.conf.dist` in folder `./conf`
2. Done. Yes, really, that's all there is to it.

### **Add your own database**

Modules can now own a complete database without any core-side registration.

The usual flow is:

1. Derive your pool from `ModuleDatabasePool`
2. Set the connection string with `SetConnectionInfo(...)`
3. Open the pool in `DatabaseScript::OnModuleDatabasesLoading()`
4. Run `ModuleDBUpdater::Create(...)`, `ModuleDBUpdater::Populate(...)` and `ModuleDBUpdater::Update(...)`
5. Call `PrepareStatements()` after the schema is ready
6. Keep the pool alive with `OnModuleDatabasesKeepAlive()` and close it with `OnModuleDatabasesClosing()`

```cpp
class MyModuleDatabasePool : public ModuleDatabasePool
{
protected:
    MySQLConnection* CreateConnection(MySQLConnectionInfo& info) override
    {
        return new MyModuleDatabaseConnection(info);
    }
};

class MyModuleDatabaseScript : public DatabaseScript
{
public:
    MyModuleDatabaseScript() : DatabaseScript("MyModuleDatabaseScript") { }

    bool OnModuleDatabasesLoading() override
    {
        std::string const modulePath = ResolveModulePath();

        _pool.SetConnectionInfo("127.0.0.1;3306;acore;acore;mod_my_module", 1);

        if (_pool.Open() != 0)
            return false;

        if (!ModuleDBUpdater::Create(_pool))
            return false;

        DBUpdaterInfo const info
        {
            "MyModule",
            modulePath,
            modulePath + "/data/sql/base/",
            "mymodule"
        };

        if (!ModuleDBUpdater::Populate(_pool, info) || !ModuleDBUpdater::Update(_pool, info))
            return false;

        return _pool.PrepareStatements();
    }

    void OnModuleDatabasesKeepAlive() override
    {
        _pool.KeepAlive();
    }

    void OnModuleDatabasesClosing() override
    {
        _pool.Close();
    }

private:
    std::string ResolveModulePath() const;
    MyModuleDatabasePool _pool;
};
```

Keep the SQL files inside your module repository and point `DBUpdaterInfo` to them. In the example above, `ResolveModulePath()` stands for whichever mechanism your module already uses to locate its own source tree. The updater follows the same base/update workflow used by the core databases, so your module can create, populate and update its own schema during startup.

### **Finished creating your module?**

Publish your module to our catalogue: https://www.azerothcore.org/catalogue.html#/how-to