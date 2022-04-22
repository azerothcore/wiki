# Windows Requirements

| Installation Guide                                                                                                                      |                                                      |
| :-------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](installation.md)                                                                                         | [Step 2: Core Installation >>](core-installation.md) |

|                                                                    |
| :----------------------------------------------------------------- |
| Boost ≥ 1.74                                                       |
| MySQL ≥ 5.7.0                                                      |
| OpenSLL ≥ 1.0.x (OpenSSL 3.0 is not supported)                     |
| CMake ≥ 3.16                                                       |
| MS Visual Studio (Community) ≥ 16.11 (2019) (Desktop) (No preview) |

1. [Git Extensions](https://sourceforge.net/projects/gitextensions/)

    1. You will need Git installed. You can get the latest version [https://git-scm.com/download/win](https://git-scm.com/download/win)
    
        - During Git installation - Adjusting your PATH environment. Pick "Git from the command line and also from 3rd-party software".

1. Install the compiler / IDE [Visual Studio (17) Community 2022](https://visualstudio.microsoft.com/downloads/)

   You will need to install the C++ compiler.
   
   To do this, select **Desktop development for C++** under **Workloads -> Desktop & Mobile**.

   <a href="/wiki/images/visualstudio.jpg" target="_blank">
   <img src="/wiki/images/visualstudio.jpg" height="50%" width="50%">
   </a>

1. [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/8.0.html) (**Use version ≥ 5.7** with mysql server configuration)

    1. Download the Windows MSI Installer.
    
    1. Scroll down to the bottom and click on "No thanks, just take me to the downloads!"
    
    1. When the installation is almost done, make sure "Launch the MySQL Instance Configuration Wizard" is checked, then click "Finish".
    
    1. When the MySQL Instance Configuration Wizard launches, most default options are fine, but remember the username and password you use (root // whatever). You will need them to log into your chosen database management tool (below) in order to import SQL files later.
    
    1. To test if MySQL is set up correctly, hit CTRL+ALT+DEL on your keyboard, enter the Task Manager, and select the "Services" tab. In the list of services you should see "MySQL" with a status of "Running".

    1. Increase max_allowed_packet to prevent large updates from causing errors when importing to the database

        1. Navigate to C:\ProgramData\MySQL\MySQL Server 8.0
        
        1. Open my.ini with the text editor of your choice

        1. Find max_allowed_packet=4M

        1. Change to max_allowed_packet=64M and save the file

        1. Open services.msc and find your MySQL Service

        1. Right click the service and choose restart

    1. Add MySQL to Environment Variables.
    
        1. Go to Control Panel -> System
        
        1. Go to Advanced System Settings

        1. Go to Environment Variables
        
        1. Under "Systemvariables" select **Path**
        
        1. Edit and add your install path of MySQL, i.e **C:\Program Files\MySQL\MySQL Server 8.0\bin\\**

1. Choose a database management tool

    - mysql cli (Fastest)
    
    - [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)
    
    - [HeidiSQL](https://www.heidisql.com/download.php) (Best for beginners)
    
    - MySQL Workbench (already installed if you chose to install full MySQL package)
    
    - [DBeaver](https://dbeaver.io/) (Multiplattform Database Management Tool)

    1. Try connecting to your database. You may be looking for "Connect to Host" or "New Connection" or "Session Manager" depending on which program you use.

    1. Create a new connection/session. The Hostname/IP address of "127.0.0.1" or "localhost" is fine if you installed MySQL on the same computer that you installed HeidiSQL or        SQLYog. Simply fill in your root // whatever password and you should now be able to connect to your database.

1. [CMake](https://cmake.org/)

    1. Download and install the **Latest Release** win32-x86.exe file, **NEVER the RC (Release Candidate) versions.**
    
    1. We recommend to compile in 64 bits mode. 

1. MySQL development files

    1. These files are shipped with MySQL Server, search for them at program files directory, MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib.

1. [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) Download the 64bit version. Or you can get both if you plan to compile both 32 and 64bit, they can coexist side by side.

    - **OpenSSL 3.0 is not supported.**

    - Find the 64bit version by finding the latest 1.0.x or 1.1.x Win64 OpenSSL that is NOT the "light" version. (Example: Win64 OpenSSL v1.1.1g)
    
    - Find the 32bit version by finding the latest 1.0.x or 1.1.x Win32 OpenSSL that is NOT the "light" version. (Example: Win32 OpenSSL v1.1.1g)

    - *Note #1: If you get a "Missing Microsoft Visual C++ .... Redistributable" error message while installing OpenSSL,*
      *Download the [Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x64) (Direct Download)](https://aka.ms/vs/17/release/vc_redist.x64.exe) (1.7MB Installer) and install it.*
      *If you need 32bit support, download and install the [Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x86) (Direct Download)](https://aka.ms/vs/17/release/vc_redist.x86.exe).*
       
    - *Note #2: While installing OpenSSL, choose The OpenSSL binaries (/bin) directory (NOT "The Windows system directory")*
      *when given the choice on where to copy the OpenSSL DLLs. These DLLs will need to be located easily for [Core Installation](windows-core-installation).*
  
1. [Boost](https://www.boost.org/).

    1. Download the prebuilt Windows Binary for Visual Studio 2022

    1. [64bit](https://sourceforge.net/projects/boost/files/boost-binaries/1.74.0/boost_1_74_0-msvc-14.2-64.exe/download)

    1. [32bit](https://sourceforge.net/projects/boost/files/boost-binaries/1.74.0/boost_1_74_0-msvc-14.2-32.exe/download)

    1. Add an environment variable to "System" variable named "BOOST_ROOT" and as value your Boost installation directory, e.g `E:/Programs/boost_1_74_0`. Important is to use '**/**', not '**\\**'  when pointing to directory. (Make sure that it does not have a trailing slash (end of path). If you still get problems, add the same variable in the `USER` variables section too, like shown in the image below.)

    <a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
    </a>

    1. Notice that this image shows the version number `1.72.0` - use your actual version number in your settings.
  
<br>

## Help

If you are still having problems, check:

* [FAQ](faq.md)

* [Common Errors](common-errors.md)

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide                                                                                                                      |                                                      |
| :-------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](installation.md)                                                                                         | [Step 2: Core Installation >>](core-installation.md) |
