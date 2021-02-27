# Getting started with AzerothCore

## Introduction

If you want to learn about AzerothCore (AC), setup your WoW server for the first time, understand how to modify it and become able to contribute? You came to the right place!

Getting started with WoW emulation might be tricky at first, but don't worry, we will be there to help you in case you encounter any issue or have any questions to ask. Just read [this page](https://www.azerothcore.org/wiki/How-to-ask-for-help) before asking for help.

If while reading any of the tutorials linked on this page you find something that is not clear: let us know. We'll do our best to rephrase it and make it easier to be understood for beginners. Improving the docs is also a way to contribute!

![AzerothCore learning code](https://user-images.githubusercontent.com/75517/109369720-b6fa7d00-789d-11eb-86b4-5fe15d6ab834.png)


## Knowledge requirements

There are **NO** technical requirements. You just need to be patient and willing to learn.

If you already have some programming knowledge it would surely be an advantage for you. However, trust me, you don't need any pre-existing knowledge to learn about WoW servers.

*Personal note from the author of this tutorial: when I first installed my first WoW server I was 15, I had no programming knowledge at all, I was using Windows XP and barely understood English. I'm sure if you are reading this, you have already more skills than I used to have when I was trying to install MaNGOS+UDB+ScriptDev2 and get a decent WoW server to run on my local machine.
Initially, I spent hours trying to read and understand tutorial from different people written on different websites, but eventually, I succeeded. AzerothCore is an all-in-one project so it's going to be easier than that, bear with me and you'll get there!*

## Installing AzerothCore on your computer

The first step is always installing a local WoW server in your own machine. And there are several ways to do it, which can vary according to the operating system.

### Your operating system

Let me be clear about one thing: **ALL operating systems are supported by AzerothCore**.
So you can successfully install AzerothCore GNU/Linux, macOS or Windows without any issue.

However, I can tell you if you use a Linux distribution such as **Ubuntu 20.04**, the process is going to be easier. If you would like to install Ubuntu, you can download it from [here](https://ubuntu.com/download/desktop) and you can find plenty of tutorials online about how to do it. There is a nice tutorial about running WoW on Linux [here](https://www.mangosrumors.org/how-to-run-wow-on-linux/).

Would you like to stick with **Windows** or **macOS**? That's absolutely fine.

![AzerothCore supports GNU/Linux, macOS and Windows](https://user-images.githubusercontent.com/75517/109369213-e5775880-789b-11eb-8356-99a4ab842bfb.png)


### Different ways to install AzerothCore

Basically, there are 3 main ways to install AC:

- the "**classic setup**": this is the traditional setup you would normally use to install a common WoW emulator. **All operating systems are supported.** Doing this setup also probably gives you a better overview of the components of the server.
- the "**docker setup**": this is a simplified setup that uses Docker to automate a lot of things for you. This setup is typically easier. **You can use this setup in all operating systems where you can install [Docker](https://www.docker.com/products/docker-desktop).**
- the "**dashboard setup**": this is an **EXTREMELY EASY** way of installing AzerothCore in your machine, based on a collection of bash scripts created by [Yehonal](https://github.com/Yehonal). However, **you can only use this setup in Ubuntu** or similar platforms. Windows is not supported, and probably we are not there yet with macOS as well.

You can choose one setup, or even try more than one. You can find all the instructions here:

- [azerothcore.org/wiki/Installation](https://www.azerothcore.org/wiki/Installation)

Should you encounter any issue or doubt while trying to install your AC server, [ask us for help](https://github.com/azerothcore/wiki/blob/master/docs/How-to-ask-for-help.md).

Got your WoW server installed? Congratulations! Now let's see what you can do next.

![AzerothCore server running on macOS](https://user-images.githubusercontent.com/75517/109369101-80236780-789b-11eb-900c-bcc17a3cf13c.png)


## Access the game, learn the GM commands

First of all, `set realmlist localhost` and join your own server using the `test1` account with password `a` (yes, one-letter password). This account is already `GM` so you can use the commands from this list:

- [azerothcore.org/wiki/GM-Commands](https://www.azerothcore.org/wiki/GM-Commands)

Get confident with the commands, you will need them for any administration, testing or development activities.

![AzerothCore GM](https://user-images.githubusercontent.com/75517/109369940-ba423880-789e-11eb-88d6-e6d8f7b8a723.png)


## Consider learning git

You can just blindly copy-paste the `git` commands that you'll see in the tutorials linked here, most likely you will not have issues with them.
However, properly learning `git` will make you really aware of what you're doing, and this knowledge can help you with whatever other software development project you may work with.
Yes, because `git` is one of the most important tools used in many software engineering projects. Learning its basics will not only help you a lot with AzerothCore, but it's also something very good to put in your CV.

You can find plenty of resources online about learning `git`, for example [try.github.io](https://try.github.io/)

![AzerothCore learning git](https://user-images.githubusercontent.com/75517/109370018-fb3a4d00-789e-11eb-8532-1ab1bf8fba60.png)


## Learn how to update your WoW server

We release improvements to AzerothCore on a daily basis. You should learn how to update your server and keep updating it often. We recommend avoiding working on older versions of AzerothCore because they can have bugs that we already resolved and you don't want to stay behind.

So it is **very important** that you update your AzerothCore server regularly. We recommend you to do it at least once a week. Read this guide:

- [azerothcore.org/wiki/Update](https://www.azerothcore.org/wiki/Update)

After you follow the update procedure, it is important to **verify** that:

- your server application (core) has been properly updated, use the `server info` command to make sure of it
- your DB has been properly updated and aligned to your core version, [read this answer on stackoverflow](https://stackoverflow.com/a/55282168/3497671)

![AzerothCore server info](https://user-images.githubusercontent.com/75517/109370296-00e46280-78a0-11eb-9ed0-b9df14f2008b.png)


## Learn to check out PRs

A great way to start contributing is by testing PRs made by other contributors. This is not only quite easy to do, but it is extremely helpful for the project and can help you to get into our development process.

This topic is so important that there is a dedicated tutorial for it:

- [azerothcore.org/wiki/How-to-test-a-PR](https://www.azerothcore.org/wiki/How-to-test-a-PR)

![image](https://user-images.githubusercontent.com/75517/109370244-d397b480-789f-11eb-9ac7-64d98ca0d33c.png)


## Learning how to work with the Database

The Database is the best place to start developing a WoW server. Because it's easier than the other components, and there are tools that are able to automatically generate the code for you. For example, Keira3.

### Download Keira3

Keira3 is a DB editor for AzerothCore which allows you to edit or add contents to the world very easily, we recommend to install and play with it:

- [azerothcore.org/Keira3](https://www.azerothcore.org/Keira3)

Keira3 automatically generates the SQL code needed to create or change stuff in the database.
Sounds complicated? Give it a try and you'll see how it works.

![AzerothCore Keira3](https://user-images.githubusercontent.com/75517/109370160-769bfe80-789f-11eb-9958-dc17ff48f39a.png)

### Download a MySQL client

You'll need a generic database client too in order to manage tables and their contents.

- [azerothcore.org/wiki/Database-client](https://www.azerothcore.org/wiki/Database-client)

![AzerothCore world database viewed with sequel-ace](https://user-images.githubusercontent.com/75517/109370368-42750d80-78a0-11eb-946c-c0831a02b52b.png)


### The DB documentation is your friend

Always read the documentation about every table that you deal with:

- [azerothcore.org/wiki/database-world](https://www.azerothcore.org/wiki/database-world)

### SmartAI

With SmartAI you can do a lot of things. You can add special behaviour to an element of the game such as a creature, without ever touching a single line of C++.

In a nutshell, with SmartAI you can make an entity (for example a Creature) perform a certain **action** when a certain **event** occurs, optionally specifying a **target**. In other words, you can make entities react to events with behaviour defined by you.

For example, you can make a creature cast a spell (action), when its health goes below 50% of its total health (event), against a random member of the party group (target).

Technically the `smart_script` is just a table inside the world database (and its documentation can be found [here](https://www.azerothcore.org/wiki/smart_scripts)). Tools like Keira3 help you working with SmartAI using a practical graphic interface.

Try to open Keira3, look for any creature that has "SmartAI" as "AIName", open it and click on "SmartAI" on the right menu.
You'll be prompted with a visual editor that will assist you when working with SmartAI.

![AzerothCore SmartAI with Keira3](https://user-images.githubusercontent.com/75517/109367698-1bfea480-7897-11eb-9cf0-f047b3dcdb85.png)

Experiment with the SmartAI and get confident with it. It's a simple but very powerful tool.
After getting some knowledge of it, you will be able to do many things. Many bugs can be fixed just using the SmartAI.

The AI of most of the creatures you'll find in the world is done with SmartAI. While more complex creatures (typically raid bosses) are scripted in C++.

![SmartAI vs C++](https://user-images.githubusercontent.com/75517/109369529-e78de700-789c-11eb-97d5-02ecc6c85a0a.png)


### Learn the SQL language

Usually, you'll need only the basics of the SQL language, and in most cases, you'll probably figure it out by yourself, however, it's not a bad idea to read about the SQL language. You can find a lot of resources online, for example:

- [https://www.w3schools.com/sql/sql_intro.asp](https://www.w3schools.com/sql/sql_intro.asp)

if you understand how basic statements such as `SELECT`, `UPDATE`, `INSERT` and `DELETE` work, that's usually enough. You don't need to go too deep into SQL in order to be able to contribute.

## Start contributing!

If you mastered some of the above parts, there is already **A LOT** you can do to help our project and becoming a contributor.
For example:

- help the developers by testing PRs and giving your feedback
- do some bug triaging by confirming issues and helping us to identify and close the invalid reports
- you can also help by [triaging the bugs coming from the players of ChromieCraft](https://github.com/chromiecraft/chromiecraft) (our child-project)
- report any bug that you may find yourself
- try to fix bugs, a lot of them can just be fixed with some SQL and you can use Keira3 for that (e.g. using SmartAI or other embedded editors). Being this an open-source project, you can find plenty of examples on our main GitHub repository

Would you like to talk to us? Join [the AzerothCore Discord server](https://discordapp.com/invite/gkt4y2x).

![Contributing to AzerothCore](https://user-images.githubusercontent.com/75517/109370461-b44d5700-78a0-11eb-916c-81c8500fa969.png)

## Conclusion and next steps

Never stop learning. Go to learn the basics behind Object-Oriented Programming (OOP).
Get some C++ tutorial, start experimenting with the core source code. Look at other people PR's as examples.

Study the basic mechanisms of the game server (read articles like [this](https://stackoverflow.com/questions/62249204/how-does-the-update-diff-work-in-azerothcore)). Try to [create modules](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore).

Or learn another programming language, there are plenty of tools you might build for AzerothCore users or developers using your favourite programming language.

Whatever you are going to do, always remember: **StackOverflow is your friend**.

-------------------------------------------------

In this tutorial, I wanted to help beginners and demonstrate how much you can learn and contribute without even knowing C++. All you need is some time and patience.

Happy coding!

-- Shin aka Francesco
