# Getting started with AzerothCore

## Introduction

If you want to learn about AzerothCore (AC), setup your WoW server for the first time, understand how to modify it and become able to contribute, you came to the right place!

Getting started with WoW emulation might be tricky at first, but don't worry, we will be there to help you in case you encounter any issue or have any questions to ask. Just read [this page](https://www.azerothcore.org/wiki/How-to-ask-for-help) before asking for help.

If while reading any of the tutorials linked on this page you find something that is not clear: let us know. We'll do our best to rephrase it and make it easier to be understood for beginners. Improving the docs is also a way to contribute!

## Knowledge requirements

There are **NO** technical requirements. You just need to be patient and willing to learn.

If you already have some programming knowledge it would surely be an advantage for you. However, trust me, you don't need any pre-existing knowledge to learn about WoW servers.

**Personal note from the author of this tutorial:** when I first installed my first WoW server I was 15, I had no programming knowledge at all, I was using Windows XP and barely understood English. I'm sure if you are reading this, you have already more skills than I used to have when I was trying to install MaNGOS+UDB+ScriptDev2 and get a decent WoW server to run on my local machine.
Initially, I spent hours trying to read and understand tutorial from different people written on different websites, but eventually, I succeeded. AzerothCore is an all-in-one project so it's going to be easier than that, bear with me and you'll get there!

## Installing AzerothCore on your computer

The first step is always installing a local WoW server in your own machine. And there are several ways to do it, which can vary according to your operating system.

### Your operating system

Let me be clear about one thing: **ALL operating systems are supported by AzerothCore**.
So you can successfully install AzerothCore GNU/Linux, macOS or Windows without any issue.

However, I can tell you if you use a Linux distribution such as **Ubuntu 20.04**, the process is going to be easier. If you would like to install Ubuntu, you can download it from [here](https://ubuntu.com/download/desktop) and you can find plenty of tutorials online about how to do it. There is a nice tutorial about running WoW on Linux [here](https://www.mangosrumors.org/how-to-run-wow-on-linux/).

Would you like to stick with **Windows** or **macOS**? That's absolutely fine.

### Different ways to install AzerothCore

Basically, there are 3 main ways to install AC:

- the "**classic setup**": this is the traditional setup you would normally use to install a common WoW emulator. **All operating systems are supported.** Doing this setup also probably gives you a better overview of the components of the server.
- the "**docker setup**": this is a simplified setup that uses Docker to automate a lot of things for you. This setup is typically easier. **You can use this setup in all operating systems where you can install [Docker](https://www.docker.com/products/docker-desktop).**
- the "**dashboard setup**": this is an **EXTREMELY EASY** way of installing AzerothCore in your machine, based on a collection of bash scripts created by [Yehonal](https://github.com/Yehonal). However, **you can only use this setup in Ubuntu** or similar platforms. Windows is not supported, and probably we are not there yet with macOS as well.

You can choose one setup, or even try more than one. You can find all the instructions here:

- [azerothcore.org/wiki/Installation](https://www.azerothcore.org/wiki/Installation)

Should you encounter any issue or doubt while trying to install your AC server, [ask us for help](https://github.com/azerothcore/wiki/blob/master/docs/How-to-ask-for-help.md).

Got your WoW server installed? Congratulations! Now let's see what you can do next.

## Access the game, learn the GM commands

First of all, `set realmlist localhost` and join your own server using the `test1` account with password `a` (yes, one-letter password). This account is already `GM` so you can use the commands from this list:

- [azerothcore.org/wiki/GM-Commands](https://www.azerothcore.org/wiki/GM-Commands)

Get confident with the commands, you will need them for any administration, testing or development activities.

## Consider learning git

You can just blindly copy-paste the `git` commands that you'll see in the tutorials linked here, most likely you will not have issues with them.
However, properly learning `git` will make you really aware of what you're doing, and this knowledge can help you with whatever other software development project you may work with.
Yes, because `git` is one of the most important tools used in many software engineering projects. Learning its basics will not only help you a lot with AzerothCore, but it's also something very good to put in your CV.

You can find plenty of resources online about learning `git`, for example [try.github.io](https://try.github.io/)

## Learn how to update your WoW server

We release improvements to AzerothCore on a daily basis. You should learn how to update your server and keep updating it often. We recommend avoiding working on older versions of AzerothCore because they have can have bugs that we already resolved and you don't want to stay behind.

So it is **very important** that you update your AzerothCore server regularly. We recommend you to do it at least once a week. Read this guide:

- [azerothcore.org/wiki/Update](https://www.azerothcore.org/wiki/Update)

## Learn to check out PRs

A great way to start contributing is by testing PRs made by other contributors. This is not only quite easy to do, but it is extremely helpful for the project and can help you to get into our development process.

This topic is so important that there is a dedicated tutorial for it:

- [azerothcore.org/wiki/How-to-test-a-PR](https://www.azerothcore.org/wiki/How-to-test-a-PR)

## Learning how to work with the Database

The Database is the best place to start developing a WoW server. Because it's easier than the other components, and there are tools that are able to automatically generate the code for you. For example, Keira3.

### Download Keira3

Keira3 is a DB editor for AzerothCore which allows you to edit or add contents to the world very easily, we recommend to install and play with it:

- [azerothcore.org/Keira3](https://www.azerothcore.org/Keira3)

Keira3 automatically generates the SQL code needed to create or change stuff in the database.
Sounds complicated? Give it a try and you'll see how it works.

### Download a MySQL client

- [azerothcore.org/wiki/Database-client](https://www.azerothcore.org/wiki/Database-client)

### The DB documentation is your friend

Always read the documentation about every table that you deal with:

- [azerothcore.org/wiki/database-world](https://www.azerothcore.org/wiki/database-world)

### SmartAI

With SmartAI you can do a lot of things. You can add special behaviour to an element of the game such as a creature, without ever touching a single line of C++.

In a nutshell, with SmartAI you can make an entity (for example a Creature) perform a certain **action** when a certain **event** occurs, optionally specifying a **target**. In other words, you can make entities react to events with a behaviour defined by you.

For example, you can make a creature cast a spell (action), when its health goes below 50% of its total health (event), against a random member of the party group (target).

Technically the `smart_script` is just a table inside the world database (and its documentation can be found [here](https://www.azerothcore.org/wiki/smart_scripts). Tools like Keira3 help you working with SmartAI using a pratical graphic interface.

Try to open Keira3, look for any creature that has "SmartAI" as "AIName", open it and click on "SmartAI" on the right menu.
You'll be prompted with a visual editor that will assist you when working with SmartAI.

![image](https://user-images.githubusercontent.com/75517/109367698-1bfea480-7897-11eb-9cf0-f047b3dcdb85.png)


The AI of most of the creatures you'll find in the world is done with SmartAI. While more complex creatures (typically raid bosses) are scripted in C++.

### Learn the SQL language

In most cases, you'll need only the basics of the SQL language, and in most cases, you'll probably figure it out by yourself, however, it's not a bad idea to read about the SQL language. You can find a lot of resources online, for example:

- [https://www.w3schools.com/sql/sql_intro.asp](https://www.w3schools.com/sql/sql_intro.asp)

if you understand how basic statements such as `SELECT`, `UPDATE`, `INSERT` and `DELETE` work, that's usually enough. You don't need to go too deep into SQL in order to be able to contribute.

## Start contributing!

If you mastered some of the above parts, there is already **A LOT** you can do to help our project and becoming a contributor.
For example:

- help the developers by testing PRs
- do some bug triaging by confirming issues and helping us to identify and close the invalid reports
- report any bug that you may find
- 

## Learn C++

### Learn some OOP basics

TODO

### Do some practice

## Summary

TODO
