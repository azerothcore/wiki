## Why worldserver and authserver needs .conf.dist files to be present in installation path?

It's because AzerothCore use them as a "fallback" for configurations that you don't have on copied .conf file ( for example if we updated the dist or you've removed a conf )

## How configuration files are composed

All configuration files load their properties under 2 macro groups ( you must have one of them on your configuration file header) :

[authserver] -> for authserver configurations

[worldserver] -> for worldserver configurations

A property is composed by a name and a value that will be loaded inside an object at server startup / config reloading.

## How does the multiple .conf file loading works?

At server startup we read first the .dist files and load all propoerties under sConfig object. The .conf file will be loaded Right after: all new properties will be added to the sConfig object , instead properties with the same name overwrite old one from .dist 

This allow you to create tiny .conf file that DOES NOT REQUIRE to have all .conf.dist properties inside since they have been already loaded before.

For example, if you want to keep all default conf but you've to change just the database properties, you can create a worldserver.conf file with just:

```
[worldserver]
LoginDatabaseInfo     = "127.0.0.1;3306;root;root;azerothcore_test_auth"
WorldDatabaseInfo     = "127.0.0.1;3306;root;root;azerothcore_test_world"
CharacterDatabaseInfo = "127.0.0.1;3306;root;root;azerothcore_test_chars"
```

## Modules configuration

After normal `.conf` and `.conf.dist` files has been loaded, you are able to load an infinite number of configuration files using scripts/modules API. They will have the same behaviour as described above. 

**Note:** we do not recommend you to overwrite server configuration properties since you can have concurrency issues with other modules that use them too. Instead, **create new namespaced properties**.

For example, if you want to modify the "disable water breath" functionality in your module. Instead of using the existing property from `worldserver.conf.dist`:

```
DisableWaterBreath = x
```

Use a namespace like:

`MyModuleName.DisableWaterBreath = x`

and work with that.


## Can I use relative pathes in the configuration files?

Yes, but it's not recommended. Each path is relative to the directory from where you launched the authserver/worldserver, whether you launch it manually or through a script. So if you do this (linux example):

```bash
cd /tmp/test
./path/to/worldserver
```

And you have relative pathes in the worldserver.conf like `LogsDir = "../logs/worldserver/"`
It will create the logs inside `/logs/worldserver`.

## Conclusion

Configuration files will be loaded following this flow:

```
authserver.conf.dist
authserver.conf (overwrite properties from authserver.conf.dist)
worldserver.conf.dist
worldserver.conf (overwrite properties from worldserver.conf.dist)
modules *.conf.dist
modules *.conf (overwrite properties from each module's .conf.dist)
```
