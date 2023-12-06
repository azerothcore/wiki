# Windows Requirements

| Installation Guide                                                                                                                      |                                                      |
| :-------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |                                                      |
| [<< Start: Installation Guide](installation.md)                                                                                         | [Step 2: Core Installation >>](core-installation.md) |

{% include callout.html content="Windows ≥ 10<br/>
Boost ≥ 1.78<br/>
MySQL ≥ 5.7.0 (Recommended version: ≥ 8.0)<br/>
OpenSSL ≥ 3.0.x (Ver. 3.1 and above are not supported.)<br/>
CMake ≥ 3.16<br/>
MS Visual Studio (Community) ≥ 17 (2022) (Desktop) (No preview)" type="info" %}

1. [Git](https://git-scm.com/download/win)

    1. Download the standalone installer
    
        - During Git installation - Adjust your PATH environment. Pick "Git from the command line and also from 3rd-party software".

2. [Github Desktop](https://desktop.github.com/)

    1. Download the installer and follow the steps to set it up.

3. Install the compiler / IDE [Visual Studio Community 2022 (ver 17)](https://visualstudio.microsoft.com/downloads/)

   You will need to install the C++ compiler.
   
   To do this, select **Desktop development for C++** under **Workloads -> Desktop & Mobile**.

   <a href="/wiki/images/visualstudio.jpg" target="_blank">
   <img src="/wiki/images/visualstudio.jpg" height="50%" width="50%">
   </a>

4. [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/8.0.html)

{% include note.html content="MySQL ≥ 8.0 is recommended. Version 5.7 is deprecated and will soon not be supported." %}

    1. Download the Windows MSI Installer.
    
    2. Scroll down to the bottom and click on "No thanks, just take me to the downloads!"
    
    3. When the installation is almost done, make sure "Launch the MySQL Instance Configuration Wizard" is checked, then click "Finish".
    
    4. When the MySQL Instance Configuration Wizard launches, most default options are fine, but remember the username and password you use (root // whatever). You will need them to log into your chosen database management tool (below) in order to import SQL files later.
    
    5. To test if MySQL is set up correctly, hit CTRL+ALT+DEL on your keyboard, enter the Task Manager, and select the "Services" tab. In the list of services you should see "MySQL" with a status of "Running".

    6. Add MySQL to Environment Variables.
    
        1. Go to Control Panel -> System
        
        2. Go to Advanced System Settings

        3. Go to Environment Variables
        
        4. Under "Systemvariables" select **Path**
        
        5. Edit and add your install path of MySQL, i.e **C:\Program Files\MySQL\MySQL Server 8.0\bin\\**

5. Choose a database management tool

    - MySQL cli (Fastest)
    
    - [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)
    
    - [HeidiSQL](https://www.heidisql.com/download.php) (Best for beginners)
    
    - MySQL Workbench (already installed if you chose to install the full MySQL package)
    
    - [DBeaver](https://dbeaver.io/) (Multiplatform Database Management Tool)

    1. Try connecting to your database. You may be looking for "Connect to Host", "New Connection" or "Session Manager" depending on which program you use.

    2. Create a new connection/session. The Hostname/IP address of "127.0.0.1" or "localhost" is fine if you installed MySQL on the same computer that you installed HeidiSQL or SQLYog. Simply fill in your root // whatever password and you should now be able to connect to your database.

6. [CMake](https://cmake.org/download/)

    1. Download and install the **Latest Release** windows-x86_64.msi file, **NEVER the RC (Release Candidate) versions.**
    
    2. We recommend to compile in 64 bits mode. 

7. MySQL development files

    1. These files are shipped with MySQL Server, search for them in the program files directory, MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib.

8. [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) Download the 64bit version.

{% include important.html content="Use version 1.1 or 3.0. 3.1 and above is not supported." %}

    - Find the 64-bit version by finding the latest 3.0.x Win64 OpenSSL that is NOT the "light" version. (Example: Win64 OpenSSL v3.0.7)

{% include note.html content="If you get the error 'Missing Microsoft Visual C++ .... Redistributable' while installing OpenSSL, download the <a href="https://aka.ms/vs/17/release/vc_redist.x64.exe">Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x64) (Direct Download)</a> (1.7MB Installer) and install it." %}

{% include note.html content="While installing OpenSSL, choose The OpenSSL binaries (/bin) directory (NOT "The Windows system directory") when given the choice of where to copy the OpenSSL DLLs. These DLLs will need to be located easily for <a href="windows-core-installation">Core Installation</a>." %}
  
1. [Boost](https://www.boost.org/).

    1. Download the prebuilt Windows Binary for Visual Studio 2022

    2. [64bit](https://sourceforge.net/projects/boost/files/boost-binaries/1.81.0/boost_1_81_0-msvc-14.3-64.exe/download)

    3. Add an environment variable to the "System" variable named "BOOST_ROOT" and with the value being your Boost installation directory, e.g. `C:/local/boost_1_81_0`. Important is to use '**/**', not '**\\**'  when pointing to the directory. (Make sure that it does not have a trailing slash (end of the path). If you still get problems, add the same variable in the `USER` variables section too, as shown in the image below.)

    <a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
    </a>

{% include note.html content="Notice that this image shows the version number 1.72.0 - use your actual version number in your settings." %}
  
<br>

## Help

If you are still having problems, check:

* [FAQ](faq.md)

* [Common Errors](common-errors.md)

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide                                                                                                                      |                                                      |
| :-------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |                                                      |
| [<< Start: Installation Guide](installation.md)                                                                                         | [Step 2: Core Installation >>](core-installation.md) |
