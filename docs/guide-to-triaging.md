# Guide to Triaging

## Introduction

This guide is intended to give an overview of bug triaging for the AzerothCore project. It will cover goals, the triaging process, a summary of tools and sources, and other useful links. 

## Goals

Our goal is to take a bug report that has been submitted to the ChromieCraft issue tracker, and decide in a timely, accurate and documented manner whether it is a valid report or not. If it is, we forward it on to the AzerothCore issue tracker with added notes and documentation.

So what determines a valid bug report? A bug report is valid if it demonstrates behaviour in AzerothCore that does not match with how a retail Blizzard WoW server would have behaved during the 'Wrath of the Lich King' era. Some dates to help with this: 
- Wrath released with patch 3.02 on October 14, 2008.
- The final Wrath patch was 3.3.5a, released June 29, 2010.
- Wrath ended with the release of Cataclysm on October 12, 2010. 

## How to Triage

### 1. Pick an issue
You start by going to the ChromieCraft issue tracker here: https://github.com/chromiecraft/chromiecraft/issues
Pick an issue that is labelled with the orange 'Needs Triage' tag. 

### 2. Check for duplicates
Once you have chosen an issue, start by searching for duplicates - quest names, character names, even individual game object GUIDs can all be checked to make sure they haven't already been reported. In a project with such a large and growing player base, many reported issues have already been seen before. They may have been checked and found not to be bugs already, or they may have been fixed already, in a patch that hasn't been been deployed to CC. Also, finding other related issues, while not duplicates, can still help you understand a problem better.

### 3. Validate the issue
So now we have made sure this is a new bug, decide whether this is obviously incorrect behaviour, or if this might be caused by misunderstanding, misinterpretation, or ignorance of the game. This is often done by checking against the sources as listed below to determine if it is actually a bug at all. Some apparent bugs are intended behaviour, and other reports are caused by changes in the game - for example, what was correct behaviour in Vanilla might be incorrect in Wrath due to balancing changes.

### 4. Try to reproduce it
If this is a genuine issue, try to follow the user's instructions to duplicate it. You can do this either in the CC PTR or your own AC local server. If the user didn't give you enough information to reproduce the problem, you can always ask them to clarify and tag the issue on the CC tracker as "Waiting for Feedback".

If you can't make the behaviour reoccur on your own server, be aware that a vanilla AC server does not always behave the same way as the ChromieCraft server. There are numerous mods and other customisations on CC that can have unpredictable effects, and as a result bugs that are not reproduceable on a vanilla AC server are reported reasonably often. 

#### Bugs with CC mods and progression
Chromie runs a number of mods for the player base's convenience. These include CFBG, the cross-faction battleground mod, cross-faction dungeons, the duel reset mod, low-level arenas, and so on. Faults with these, while not uncommon, are not directly relevant to the AC project. If you have identified a bug report as originating from a CC mod, it should be reported to that mod's own GitHub issues page where possible. You can search GitHub to find it.

In particular, if an issue is about items that should not be available to a certain level range (for example, vendors selling level 60 gear when CC's current content bracket is 40-49) then that is a progression system issue and can be reported here: https://github.com/azerothcore/progression-system

#### Client-side issues
Be aware that the Wow client is far from perfect, and user interface displays for things like tooltips and character statistics can sometimes be inaccurate. If this is the case, first check that the user is running the enUS client, as the enGB client is rather more prone to these sorts of issues. If they are running the correct client, then try to verify that the only issue is the display rather than real. For example there's a known client issue with some low level items selling for what seems to be 0 copper. If you actually check the sale, the item is being sold for the correct price and the user credited with the right amount of money, but it doesn't show that. These sorts of issues, being client-side, are ultimately not fixable by the AC project. 

A fair number of users also run client-side mods that change models, textures, etc. They will also almost never mention it. But if you see an issue that looks like a client-side graphics issue, i.e. this NPC looks weird/has the wrong model/is invisible, remember to ask the reporter about any graphics mods they may be running.

### 5. Describe and document the issue
If the bug is real and valid, you can add the the original reporter's description if they missed any important details. Try to give additional useful information like database IDs and spawn GUIDs when describing objects and creatures.

Simply noting that the bug report has been confirmed is often enough. However, if you want to make the evidence as clear as possible then a screenshot or a video of the faulty behaviour is often a good way to do so. Screenshots of combat logs can be especially useful. For video, I've found OBS Studio (https://obsproject.com/download) to be good for screen capture, and Shotcut (https://www.shotcut.org/) to be a good video editor for working on the results. (It helps that both of these are FOSS (Free and Open Source Software), and as a FOSS project ourselves it's nice to support others.)

### 6. Record how to reproduce it
Show how it can be reproduced, preferably using GM commands. So instead of 'accept the quest "Kill Ten Foozles"', say `.quest add 1234`. The commands `.go c XXXX` and `.go o XXXX` (to go to creatures and objects respectively) will be useful here as they let you teleport directly to whatever the problem is. `.additem [itemname]` can also be handy.

Bear in mind that when a pull request is made to fix this issue, the fixer and the PR's tester will both be relying on the information you provide here to make their lives easier.

### 7. Copy across to AC tracker with link back to CC
So now you have established this is a valid bug, you can move it across to the AzerothCore issue tracker. This is done by creating a new blank issue here: https://github.com/azerothcore/azerothcore-wotlk/issues/new?assignees=&labels=&template=
You can then copy the data from the original CC ticket. You can do this by clicking the three horizontal dots in the top right corner of the report's text box and selecting Edit. You can then copy the ticket text and paste that information into the AC ticket, and then add your own comments and findings to generate the final ticket. 

Title it appropriately - something clear and consistent is best. Then add the link to the original issue reported to ChromieCraft ("Originally reported LINK-TO-CHROMIECRAFT-ISSUE"). GitHub will automatically link the two reports. 

You should also check to make sure the CC report has a server version hash included. (The version hash is a little string of random numbers and letters, like `3d4befd`.) If it doesn't the AC tracker will complain. If it is missing for some reason, the current ChromieCraft version info can be found [here](https://github.com/chromiecraft/azerothcore-wotlk), or if you have replicated the issue on your own test server, you can use your own hash. This can be found by typing `server info` at the `AC>` command prompt of your running AC world server.

### 8. Add tags to AC and CC issues
Now you can add relevant tags to both the new AC issue you have created, and the CC issue you have been working from. Tag appropriately - 'Generic' is last resort, for issues that affect a broad range of levels. Otherwise, tag an issue by the level of the zone it occurs in, or the level of the quest or NPC it affects. If you're not sure of a zone's level, you can find a Wrath-era list of zones by level [here](https://wowpedia.fandom.com/wiki/Zones_by_level_(original)).

For the AC issue, if you are copying an issue from CC then you can add the 'Confirmed' tag. Also feel free to add other relevant tags, such as 'Quest', 'Loot', 'DB', 'PVP', or one of of the class-specific tags. 

For the CC issue, you can tag it with 'Confirmed', 'Linked to AC', and a tag indicating level range or Generic if that doesn't apply. Again, if there are other relevant tags such as 'Class Issue', feel free to add them.

If you have the right permissions, also add the new AC issue to whichever project is relevant, usually the one matching the issue's level range.

## Guidelines
- **Use your judgement.** We are there to exercise our best judgement, not just as photocopiers. We have access to tools and information that most players don't, so we should be able to see more deeply into a problem than they can and make decisions accordingly.
- **Generalize the problem.** Try to generalise or broaden a problem. If one unusual kind of item, NPC or spell is not working correctly, try checking other items of the same general type to see if they are broken as well. Ideally we want to capture the broadest possible range of errors that we can.
- **Be sceptical.** Users can feel very strongly about these issues. You will quite often see claims such as "it has always been this way" or "I've played my class since vanilla and this is how it should be." These assertions, with no other evidence, should be treated with an appropriate level of scepticism. An experienced player will probably know things about their class that you don't, but that does not mean their statements should be accepted as fact without any other evidence.
- **Combine similar problems.** If you find related problems while searching, consider linking the two with a note. (It can be as simple as "See also <ticket URL>." This will help whoever ends up fixing the issue by telling them of similar issues.) 
- **Try to prioritize.** More severe bugs over lesser ones, frequent bugs over rare ones. Counter-intuitively, newer issues may need priority over older ones, on the grounds that if a bug has lasted a long time without being fixed, there's a good chance it's not very important.
- If you can't find any sources, at least say so instead of saying nothing.
- **Be polite.** When someone submits a bug report, they are doing us a favour. They've taken the time to make a GitHub account and type up a bug report to try to help us. The least we can do is be professional and courteous in return. 

## Sources
This is a general (and by no means exhaustive) look at the sources we can use to try to understand if a bug is valid or not. They include:

- [TBC Wowhead](http://tbc.wowhead.com/) or [Current Wowhead](https://www.wowhead.com/) - Wowhead is a important if flawed source of data, both because of the site's own data and the comments that users have made on it. The Wowhead comments are probably the largest single set of information on individual quests and items we have, which is why it's a pity that so much of it is utter rubbish. 
    However, it is a bit too easy to fall into the assumption that Wowhead data is correct and complete when it really isn't. Wowhead's data comes from user submissions, and has its own issues with things like drop rates as a result. Its data has also been contaminated by people submitting data from private servers. Thus, for all its apparent authority, Wowhead's data can be fragmentary, incomplete and misleading if not interpreted with care.
	Note the two versions listed here. TBC Wowhead is usually more helpful, but the current live version of Wowhead does also contain user comments from the Wrath era, which TBC WH doesn't.  

- [Wowpedia](https://wowpedia.fandom.com/wiki/Special:Search) - Wowpedia can be a pretty good source, as it has a history function that lets you view an article as it was during the WotLK era. To access it, go to the relevant article, and look to the right of the article title. Next to 'View Source' you will see 3 vertically arranged dots. Clicking that allows access to the History of the article. You typically want the last article written before the date of 12 October 2010 (Cata's release date).

    Wowpedia often aggregates patch notes relating to a particular talent or ability, which is frequently useful. It also often records quest text and quest-giver dialogue, so can be a handy source for that sort of thing. Note that older Wrath-era content can also be found on its sibling site [WowWiki](https://wowwiki-archive.fandom.com/wiki/Wiki). 
	
- Sniffs data - 'Sniffs' are intercepted data packets players have captured when playing retail Wow. They have the advantage of using real retail data and making it available in SQL, and thus broadly useable. The disadvantages are that the sniff data only contains client-visible data, it is often incomplete and patchy, and is often difficult to otherwise verify. 
    For one useful site that makes use of this data, see the [AzerothCore SpeedChecker](https://azerothcore-speedchecker.web.app/) by @Efymer on Discord - if you want to verify a creature's movement speed or other flags versus sniffed retail data, this will do it for you.

- YouTube - can be an excellent source of information, as there are lots of videos of people doing quests in Classic/TBC. Sadly there are few from the original WotLK era. The other problem with YT is that retail players are not the only ones putting Wow videos up. Players on other private servers also make videos (watch out for one in particular called Bue, who will often be top result when searching for a quest on YouTube.) These private server videos are of course largely useless as sources for correct Blizz-like behaviour.

- [TrinityCore](https://github.com/TrinityCore/TrinityCore/issues) - Trinity is older and larger than AC, and their own bug tracker and issues database is correspondingly larger than ours. As a result it is often a good place to check for other reports of an issue if the AC tracker doesn't have any results. You can also quite often find a solution for the issue as well. Be aware that TC has multiple branches, only one of which is targeting 3.3.5a.

- [Wayback Machine/Internet Archive](https://web.archive.org/) - if you really get stuck for contemporary sources and need to see the state of a site in 2010, then Wayback Machine can be good, if you know the URL of the site you want to see. For example, they have a 2010 snapshot of the hunter pet site Petopia which has occasionally been useful.

- World of Warcraft's own [Forums](https://us.forums.blizzard.com/en/wow/) - the Wow forums can occasionally be useful when they discuss vanilla or TBC issues, but are usually full of people contradicting and flaming each other, so aren't very reliable as sources.

- Similarly, [MMO Champion](https://www.mmo-champion.com/forum.php) has forums that can be useful because they have been going, essentially unchanged, since before Wrath. This means you can sometimes find useful firsthand information there. However, like most forums, sorting the useful information from the random chaff can be difficult.

- [WowGaming](https://wowgaming.altervista.org/aowow/) - this is a site acting as the front end to a snapshot of our own AC database. As a result, it provides a rapid way of seeing details about the current version of AzerothCore.

- [World of Warcraft WotLK Database](https://wotlkdb.com/) - another third-party snapshot of Wrath-era data, although the quality of its data is occasionally questionable. Not a primary source.

- The triaging Discord's #need-help channel is very useful here.

## Tools
- The AC server/test environment, This is the basic testing tool. Try to keep your AC server as up-to-date as you can manage. Daily updates are a good idea, and you shouldn't go more than a week without updating. 

- [GM commands](gm-commands) and macros - At a bare minimum you want to be familiar with the various cheats (no damage, speed, fly), `.go`, `.additem`, `.quest add` and so on. It can also be useful to setup various cheat and boost macros on your test account, so you can instantly setup and train a new character. When testing various class and racial issues you find yourself making and then deleting a lot of different characters, so automating the new character setup with macros can repay the time invested quite quickly. 

- [Keira3](https://www.azerothcore.org/Keira3/) - this is the indispensable tool for triaging. Five minutes with Keira will save an hour of running around in the open world. It comes with a built-in SQL editor that you can use to run custom queries. It also has built-in tooltips on most data fields that can help understand what you're looking at. You can also use it to generate SQL for fixing things, although the SQL it generates should only be used as a starting point. This is because it often does not meet the preferred SQL standards for PRs regarding duplication of queries.

- A generic SQL editor like [HeidiSQL](https://www.heidisql.com/) (warning, Windows only) is also useful. Keira doesn't access every single table in the AC database, just the most useful ones, so a tool like Heidi that gives you views of everything can be good for more obscure tables.

- [AC Wiki tables](database-world), especially those covering the world database. These give you mportant information about the structure and fields of the DB. If you're puzzled about how something should work or what a flag means, the answer is often here.

- [Useful SQL snippets](useful-sql) - these are designed to be fast, easy to use tools for getting information about various potential issues out of the DB.

- Learn to filter GitHub issues:
    - `type:issue label:"Needs Triage"` - finds all open issues
    - `author:Username` - finds all issues created by author
    - `involves:Username` - find all issues they have started or commented on.

## Other Links
- [Current ChromieCraft version](https://github.com/chromiecraft/azerothcore-wotlk)
- [ChromieCraft mods](https://github.com/chromiecraft/chromiecraft/blob/main/.github/CC_SERVER_INFO.md)
- [How to triage](https://github.com/chromiecraft/chromiecraft#for-contributors-how-to-triagereport-bugs)
