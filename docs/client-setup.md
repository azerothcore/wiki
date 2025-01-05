# Client Setup

| Installation Guide                                                                                                                   |                                                       |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. | Optional                                              |
| [<< Step 7: Keeping the Server Up-to-Date](keeping-the-server-up-to-date)                                                            | [Step 9: Installing a Module >>](installing-a-module) |

AzerothCore does not distribute a client. You will need to find your own clean 3.3.5a client on the internet.

- Open the realmlist.wtf file inside your **WoW\Data** folder. The IP in the realmlist.wtf file should be exactly the same as the IP address you entered in the realmlist table previously.

    - Change the first line to `set realmlist <IP address used in realmlist table>`
    
    - Example: set realmlist 127.0.0.1

- (Optional) If you wish to use the WoW Launcher.exe to run your client then you must change your set patchlist to the same IP/DNS name as your realmlist.

{% include note.html content="Don't use localhost for address, if you need to connect to localhost use 127.0.0.1" %}

<br>

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                                       |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 7: Keeping the Server Up-to-Date](keeping-the-server-up-to-date)                                                            | [Step 9: Installing a Module >>](installing-a-module) |
