# How to change the WoW Breaking News

To connect the WoW client Breaking News we need to add a new patch MPQ that overwrite the WoW Interface and a wow.exe "cracked" with the GlueXML check removed, you can download it [here](https://mega.nz/#!Q5QR1SjJ!Arg1O1F7Mr5U6tE9aZcH0iFndYcGBK_AmfvZTn4kUjg) (without this you can run WoW with this patch).

This MPQ patch should be structured like:

![WoW patch as directory](https://i.postimg.cc/tJy8NSYX/patch-structure.pnghttps://i.postimg.cc/L5YgvT7b/Wo-W-structure.png)

**Note: the patch MUST HAVE this name "patch-?.MPQ" with a letter or number instead of ?.**

The content of GlueStrings.lua file should be like [this](https://pastebin.com/8T6XfPxX).

You need to change the line 782 with the URL of your website like:

```
SERVER_ALERT_URL = "http://usefulness.altervista.org/azerothcore/index.html";
```

I strongly suggest you to modify also the line 418, responsible of the text "Enter your email address", may replace it with:
```
ENTER_EMAIL = "Enter your account name";
```

The content of the page should be like:

```
SERVERALERT:
CONTENT;
```

Remember that the last character will be removed, so place it a useless character like a semicolon.
Example message:

```
SERVERALERT:

Hello from AzerothCore!

AzerothCore is growing up day by day, it becomes more strong in years.

Have a nice Play!;
```

Now we have all the files to make the Breaking News, we should only make the MPQ file with [MPQ Editor](http://www.zezula.net/en/mpq/download.html) and put it in WoW/Data/ directory.

Or just use directory instead of MPQ file like this way:

![WoW patch as directory](https://i.postimg.cc/L5YgvT7b/Wo-W-structure.png)

Result:

![AzerothCore WoW Breaking News](https://i.postimg.cc/9Fb7WD20/Breaking-News.png)

Here the [patch-m.MPQ](https://mega.nz/#!NhYjSKQC!w1CxZwqie5HJPgAtj_0J5stBPUU_wo8AM-tjHZrJ4Yg) or just the [directory zipped](https://mega.nz/#!JlIziI5R!Hh-MZqDd0sujCGHZ5sBSLaVbN8uLUdlHXPZbxnyjF4s).

