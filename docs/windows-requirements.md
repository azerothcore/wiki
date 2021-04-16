# Windows Requirements

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](Installation.md) | [Step 2: Core Installation >>](core-installation.md) |

| |
| :- |
| MySQL ≥ 5.7.0 |
| OpenSLL ≥ 1.0.x |
| CMake ≥ 3.16 |
| MS Visual Studio (Community) ≥ 16.4 (2019) (Desktop) (No preview)

1. Git Extensions
    1. You will need Git installed. You can get the latest version here https://git-scm.com/download/win

1. Install the compiler / IDE [Visual Studio (16) Community 2019](https://visualstudio.microsoft.com/downloads/)

   You will need to install the C++ compiler.
   
   To do this, select **Custom** in the type of installation and pick **Common Tools for Visual C++ 2019** in **Programming Languages -> Visual C++**
1. [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/8.0.html) (**Use version ≥ 5.7** with mysql server configuration)

    1. Download the Windows MSI Installer.
    
    1. Scroll down to the bottom and click on "No thanks, just take me to the downloads!"
    
    1. When the installation is almost done, make sure "Launch the MySQL Instance Configuration Wizard" is checked, then click "Finish".
    
    1. When the MySQL Instance Configuration Wizard launches, most default options are fine, but remember the username and password you use (root // whatever). You will need them to log into your chosen database management tool (below) in order to import SQL files later.
    
    1. To test if MySQL is set up correctly, hit CTRL+ALT+DEL on your keyboard, enter the Task Manager, and select the "Services" tab. In the list of services you should see "MySQL" with a status of "Running".

1. Choose a database management tool

    1. mysql cli (Fastest)
    
    1. [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)
    
    1. [HeidiSQL](https://www.heidisql.com/download.php) (Best for beginners)
    
    1. MySQL Workbench (already installed if you chose to install full MySQL package)
    
    1. [DBeaver](https://dbeaver.io/) (Multiplattform Database Management Tool)

1. Try connecting to your database. You may be looking for "Connect to Host" or "New Connection" or "Session Manager" depending on which program you use.

1. Create a new connection/session. The Hostname/IP address of "127.0.0.1" or "localhost" is fine if you installed MySQL on the same computer that you installed HeidiSQL or SQLYog. Simply fill in your root // whatever password and you should now be able to connect to your database.

1. [CMake](https://cmake.org/)

    1. Download and install the **Latest Release** win32-x86.exe file, **NEVER the RC (Release Candidate) versions.**
    
    1. We recommend to compile in 64 bits mode. 
    
    1. Note: If used different MySQL server e.g Wampserver with included MySQL or any other software, then is needed to point cmake to that directory. Add an environment variable to "System" variable named "MYSQL_ROOT" and as value your MySQL installation directory, e.g "c:/wamp/bin/mysql/mysql5.7.19". Important is to use "/", not "\"  when pointing to directory.

1. MySQL development files

    1. These files are shipped with MySQL Server, search for them at program files directory, MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib.

1. [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) Download the 64bit version. Or you can get both if you plan to compile both 32 and 64bit, they can coexist side by side.

    1. Find the 64bit version by finding the latest 1.0.x or 1.1.x Win64 OpenSSL that is NOT the "light" version. (Example: Win64 OpenSSL v1.1.1g)
    
    1. Find the 32bit version by finding the latest 1.0.x or 1.1.x Win32 OpenSSL that is NOT the "light" version. (Example: Win32 OpenSSL v1.1.1g)

    1. *Note #1: If you get a "Missing Microsoft Visual C++ 2008 Redistributable" error message while installing OpenSSL,*
       *download the [Microsoft Visual C++ 2008 Redistributable Package (x64)](http://www.microsoft.com/en-us/download/details.aspx?id=29) (1.7MB Installer) and install it.*
       *If you need 32bit support, download and install the [Microsoft Visual C++ 2008 Redistributable Package (x86)](http://www.microsoft.com/en-us/download/details.aspx?id=15336).*
       
    1. *Note #2: While installing OpenSSL, choose The OpenSSL binaries (/bin) directory (NOT "The Windows system directory")*
       *when given the choice on where to copy the OpenSSL DLLs. These DLLs will need to be located easily for [Core Installation](windows-core-installation).*

<br>

## Help

If you are still having problems, check:

* [How to ask for help](How-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](Installation.md) | [Step 2: Core Installation >>](core-installation.md) |
