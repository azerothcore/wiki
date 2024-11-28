---
redirect_from: "/Create-a-Module"
---

# Create a Module

## **How to create a module**

Before start we suggest you to read [Documentation about modular structure](The-Modular-Structure) to understand the way AzerothCore works.

### Resources

- Module template (heavily recommended): [https://github.com/azerothcore/skeleton-module](https://github.com/azerothcore/skeleton-module)
- Script template: https://github.com/azerothcore/azerothcore-boilerplates
- All the hooks in the core are listed in [ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h). If you need custom hooks, they can be added to the core by [sending a PR](How-to-create-a-PR).
- Existing modules listed in the catalogue: [https://www.azerothcore.org/catalogue.html](https://www.azerothcore.org/catalogue.html)
- If you need to create a new hook for your module, please follow this guide: [How to create a new hook](hooks-script)

### **The Basis**

1. Create a folder inside `modules/` directory

2. Now you can develop add anything to the main project, such as some scripts or
even an entire library

Note: we suggest to use the [directory structure](Directory-Structure) standards of AzerothCore to better organize your modules and be familiar with main project.

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

### **Add your db files to db_assembler**

you are able to create base, updates and custom sql that will be automatically loaded in our db_assembler

**work in progress….**

### **Finished creating your module?**

Publish your module to our catalogue: https://www.azerothcore.org/catalogue.html#/how-to