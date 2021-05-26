# IP2LOCATION

With IP2LOCATION we can approximately see which country a player might be coming from using the `.pinfo <player>` command.

To be able to use this system you have to provide the **ip2location lite database** to your Authserver.

Download **IP2LOCATION-LITE-DB1.CSV** from https://download.ip2location.com/lite/

Unzip the file and place it in the directory of your choice.

In Worldserver.conf you need to set the full directory path including the .CSV under IPLocationFile.

On the Auth- and Worldserver start you will be able to see the .CSV file being loaded in the log.
