# How to work with Conf Files

## How configuration files are composed

All configuration files load their properties under 2 macro groups (you must have one of them on your configuration file header) :

[authserver] -> For authserver configurations

[worldserver] -> For worldserver configurations

A property is composed of a name and a value that will be loaded inside an object at server startup/config reloading.

## How are the config files loaded?

All config properties can be found in the .conf.dist file, however, this file is never read.

At server startup, we read first the .conf files and load all properties under sConfig object. Any values not present in .conf file will be taken by the default values in the core.

This allows you to create a smaller .conf file that DOES NOT REQUIRE you to have all config properties from the .conf.dist file. As the default values will be taken from the values defined in the core.

For example, if you want to keep all default conf but you've to change just the database properties, you can create a worldserver.conf file with just:

```
[worldserver]
LoginDatabaseInfo     = "127.0.0.1;3306;root;root;azerothcore_test_auth"
WorldDatabaseInfo     = "127.0.0.1;3306;root;root;azerothcore_test_world"
CharacterDatabaseInfo = "127.0.0.1;3306;root;root;azerothcore_test_chars"
```

## Loading config values from environment variables

It is possible to load config values from env vars, which is explained [here](config-overrides-with-env-var.md).

## Modules configuration

After normal `.conf` and `.conf.dist` files have been loaded, you are able to load an infinite number of configuration files using scripts/modules API. They will have the same behaviour as described above. 

**Note:** We do not recommend you to overwrite server configuration properties since you can have concurrency issues with other modules that use them too. Instead, **create new namespaced properties**.

For example, if you want to modify the "disable water breath" functionality in your module. Instead of using the existing property from `worldserver.conf.dist`:

```
DisableWaterBreath = x
```

Use a namespace like:

`MyModuleName.DisableWaterBreath = x`

and work with that.


## Can I use relative paths in the configuration files?

Yes, but it's not recommended. Each path is relative to the directory from where you launched the authserver/worldserver, whether you launch it manually or through a script. So if you do this (linux example):

```bash
cd /tmp/test
./path/to/worldserver
```

And you have relative paths in the worldserver.conf like `LogsDir = "../logs/worldserver/"`
It will create the logs inside `/logs/worldserver`.

## Conclusion

Configuration files will be loaded following this flow:

```
1. Env vars
2. authserver.conf
3. worldserver.conf
4. modules *.conf
5. Core default values
```
