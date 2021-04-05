# Windows Requirements

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](installation-guide.md) | [Step 2: Core Installation >>](core-intallation.md) |

| |
| :- |
| MySQL ≥ 5.7.0 |
| OpenSLL ≥ 1.0.x |
| CMake ≥ 3.16 |
| MS Visual Studio (Community) ≥ 16.4 (2019) (Desktop) (No preview)

1. Git Extensions

    a. You will need Git installed. You can get the latest version here https://git-scm.com/download/win

2. Install the compiler / IDE [Visual Studio (16) Community 2019](https://visualstudio.microsoft.com/downloads/)

   You will need to install the C++ compiler.
   
   To do this, select **Custom** in the type of installation and pick **Common Tools for Visual C++ 2019** in **Programming Languages -> Visual C++**
   
3. [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/8.0.html) (**Use version ≥ 5.7** with mysql server configuration)

    a. Download the Windows MSI Installer.
    
    b. Scroll down to the bottom and click on "No thanks, just take me to the downloads!"
    
    c. When the installation is almost done, make sure "Launch the MySQL Instance Configuration Wizard" is checked, then click "Finish".
    
    d. When the MySQL Instance Configuration Wizard launches, most default options are fine, but remember the username and password you use (root // whatever). You will need them to log into your chosen database management tool (below) in order to import SQL files later.
    
    e. To test if MySQL is set up correctly, hit CTRL+ALT+DEL on your keyboard, enter the Task Manager, and select the "Services" tab. In the list of services you should see "MySQL" with a status of "Running".

4. Choose a database management tool

    a. mysql cli (Fastest)
    
    b. [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)
    
    c. [HeidiSQL](https://www.heidisql.com/download.php) (Best for beginners)
    
    d. MySQL Workbench (already installed if you chose to install full MySQL package)
    
    e. [DBeaver](https://dbeaver.io/) (Multiplattform Database Management Tool)
 
* Install [Visual Studio](https://visualstudio.microsoft.com/downloads/) VS 2019 Community

* Install [CMake](https://cmake.org/) version 3.16 or higher

* Install latest version of [Git Extensions](https://git-scm.com/download/win)

* [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/) (version 8.0 or 5.7, older versions are not supported)

* Install [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) version 1.0.x or 1.1.x (Do not install the Light version) 
  
  Download the 64bit version. Or you can get both if you plan to compile both 32 and 64bit, they can coexist side by side.

1. Find the 64bit version by finding the _latest _ **Win64 OpenSSL** that is **NOT** the "light" version.
    1. Example: **Win64 OpenSSL v1.0.1p**

2. Find the 32bit version by finding the _latest _ **Win32 OpenSSL** that is **NOT** the "light" version.
    1. Example: **Win32 OpenSSL v1.0.1p**

3. _Note #1: If you get a "Missing Microsoft Visual C++ 2008 Redistributables" error message while installing OpenSSL, download the ** [Microsoft Visual C++ 2008 Redistributable Package (x64)](http://www.microsoft.com/en-us/download/details.aspx?id=29) ** (1.7MB Installer) and install it. If you need 32bit support, download and install the [ **Microsoft Visual C++ 2008 Redistributable Package (x86)** ](http://www.microsoft.com/en-us/download/details.aspx?id=15336)._
4. _Note #2: While installing OpenSSL, choose **The OpenSSL binaries (/bin) directory** (NOT "The Windows system directory") when given the choice on where to copy the OpenSSL DLLs. These DLLs will need to be located easily for Core Installation._

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Start: Installation Guide](installation-guide.md) | [Step 2: Core Installation >>](core-intallation.md) |
