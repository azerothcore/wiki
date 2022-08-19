---
redirect_from: "/Add-a-module"
---

# Add a module

1. Get the module from the catalogue: [https://www.azerothcore.org/catalogue](https://www.azerothcore.org/catalogue) (For this example, we'll be using this module: [mod-npc-services](https://www.azerothcore.org/catalogue.html#/details/177019524))

2. - Clone it using Git as you did during the [core installation](core-installation.md). Set the `Destination` to "C:\Azerothcore\modules\mod-npc-services" (Recommended method) [Jump to step 9 to make sure it cloned correctly]
	- Use the download button on the catalogue page
	- Use `Download ZIP` button on the module's Github page

3. If in the previous step you chose not to clone the repo, you'll need to extract the downloaded ZIP archive. Once this is done, your resulting folder should look like this:
![img1](https://user-images.githubusercontent.com/38561765/173752887-c4fae113-2615-4a6e-b5f7-33ebb61d024d.PNG)

4. Due to a discrepancy between the way AzerothCore loads modules and how Github names ZIP code archives, you will need to rename the directory name. The folder will have the branch name placed onto the end of it, as in mod-npc-services-_master_. You will need to remove this branch name, leaving only mod-npc-services:
![img2 edit](https://user-images.githubusercontent.com/38561765/173754536-947a7477-c06f-407d-a6c0-54b366ad17cb.png)

5. Copy the renamed folder, as you'll be pasting it into the modules folder

6. Navigate to your AzerothCore modules folder (C:\Azerothcore)

7. You will see in that directory the modules folder:
![img3 edit](https://user-images.githubusercontent.com/38561765/173755109-c5243fcc-2940-4a11-9e42-edd1d7016dca.png)

8. Open the modules folder, it should look quite sparse:
![img4](https://user-images.githubusercontent.com/38561765/173755212-11d86754-0ef5-4dd8-af8d-68dbe033f71c.PNG)

9. Paste the module folder into the modules folder, it should now look like this:
![img5](https://user-images.githubusercontent.com/38561765/173755380-9c46a74c-8342-46bb-83ae-df31d0532bfd.PNG)

10. Now to recompile! Open CMake and configure. If the module has loaded correctly, you should now see it in the CMake log as well:
![img6 edit](https://user-images.githubusercontent.com/38561765/173755762-8dbc188a-9d32-4629-ad51-834666f90b29.png)

11. Then generate:
![img7 edit](https://user-images.githubusercontent.com/38561765/173755809-62235d05-cdcd-45ec-beb2-6d59f5dc76bd.png)

12. Now open the generated project file, clean, and build the solution

## SQL Queries

- If your module contains a `sql` folder, you will need to run the queries inside for the module to function correctly:
![img8 edit](https://user-images.githubusercontent.com/38561765/173756389-d3b5e465-8083-4296-b28e-ce0f4de30e8d.png)

	- Opening this folder, we should then see any of these three folders: auth, characters, or world. In the example module, it contains a world folder:
![img9](https://user-images.githubusercontent.com/38561765/173756643-40bfee42-5160-47b8-8999-6e7bdd24c476.PNG)

	- Depending on the module, there could be more than one query file you would need to execute. Refer to the readme of the module for information regarding this. In our case, there is only one `.sql` file to run, so our job is easy:
![img10](https://user-images.githubusercontent.com/38561765/173757090-f2ac528f-ccba-4e70-b1c0-9a4b3bac7d0d.PNG)

13. Open your SQL editor of choice. In this case, we will be using HeidiSQL. You will need to select the database the query applies to on the left before you run the query. Since our query was in the world folder, we will select `acore_world`. Once the database is selected, we will then load the SQL file:
![img11](https://user-images.githubusercontent.com/38561765/173757454-9033e605-c026-49a9-a030-5baf384900e7.PNG)

14. Once you navigate to the SQL file and open it up, it will open the query in a new tab. Double check that the database tab is pointing to the right database, then run the query using the marked button above the tabs:
![img12 edit](https://user-images.githubusercontent.com/38561765/173758117-6f500fb3-a8a5-4819-a608-1222b7bc9802.png)

With that, the module is installed! In the case of mod-npc-services, we'd then launch our server and run the command `.npc add 55002` (The NPC Entry) to spawn the NPC.

## DBC Patches

If your module contains DBC files (Such as [mod-arac](https://github.com/azerothcore/mod-arac) or [mod-worgoblin](https://github.com/heyitsbench/mod-worgoblin)) there are a couple extra steps you need to take to install them correctly. The DBC files included with the module will need to be copied to your server's DBC folder in its Data directory. If you're unsure where this directory is, it is set in your worldserver.conf under the `DataDir` option.

You will also need to add these patches to your client. In the case of mod-arac, it's small enough that you can grab the `Patch-A.MPQ` file directly from the repository. You can then copy it into the `Data` folder of your Wow client. However, in the case of a bigger patch like mod-worgoblin, you'll need to take the whole `patch-contents` folder and copy it to the `Data` folder of your Wow client, but you'll also need to rename the folder to `Patch-A.MPQ`. **You will need to do this step for every user connecting to your server with these changes.**

You don't necessarily have to use the letter A specifically. If you use the common HD patch for example, you may find that you have many patches in your Wow Data folder already, and if Patch-A is already taken, the client will also accept numbers 1-9 and letters A-Z. Be aware, however, that the client has an order in which it will read patches, specifically it will read patches 1-9,A-Z, with the contents of 1 being the first and the contents of Z being the last loaded by the client.

If you're using a client other than enUS, you may have to place the patch file in your locale folder and name it accordingly. For example, using a deDE client, the path would look like `Data/deDE/patch-deDE-A.MPQ`. This is due to other localizations of the client having differences in patch load order.
