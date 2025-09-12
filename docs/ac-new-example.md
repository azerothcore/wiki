# Example of NEW Windows Requirements

| Installation Guide                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |                                                           |
| [<< Start: Installation Guide](classic-installation)                                                                                 | [Step 2: Core Installation >>](windows-core-installation) |

{% include callout.html content="Windows ≥ 10<br/>
Boost ≥ 1.78<br/>
MySQL ≥ 8.0 (Recommended 8.4)<br/>
OpenSSL ≥ 3.x.x<br/>
CMake ≥ 3.16<br/>
MS Visual Studio (Community) ≥ 17 (2022) (Desktop) (No preview)" type="info" %}

|                            Header                             |
| :-----------------------------------------------------------: |
|                          [Git](#git)                          |
|               [Github Desktop](#github-desktop)               |
| [Visual Studio Community 2022](#visual-studio-community-2022) |
|                        [MySQL](#mysql)                        |
|                 [MySQL Client](#mysql-client)                 |
|                        [CMake](#cmake)                        |
|                      [OpenSSL](#openssl)                      |
|                        [Boost](#boost)                        |

## [Git](#git)

### Download

- https://git-scm.com/download/win

### Installation

- Run the standalone installer

{% include note.html content="During the installation, you will be prompt to Adjust your PATH environment. Pick 'Git from the command line and also from 3rd-party software'." %}

## [Github Desktop](#github-desktop)

### Download

- https://desktop.github.com

### Installation

- Download the installer and follow the steps to set it up.

## [Visual Studio Community 2022](#visual-studio-community-2022)

### Download

- https://visualstudio.microsoft.com/downloads

{% include note.html content="Make sure you're getting 'Visual Studio 2022 Community' and not 'Visual Studio Code'." %}

### Instalation

- Install the C++ compiler.
  You will need to install the C++ compiler.

  To do this, select **Desktop development for C++** under **Workloads -> Desktop & Mobile**.

   <a href="/wiki/images/visualstudio.jpg" target="_blank">
    <img src="/wiki/images/visualstudio.jpg" height="50%" width="50%">
   </a>

## [MySQL](#mysql)

### Download

- https://dev.mysql.com/downloads/mysql/8.4.html

### Installation

1. Run the Windows MSI Installer.
2. Scroll down to the bottom and click on "No thanks, just take me to the downloads!"
3. When the installation is almost done, make sure "Launch the MySQL Instance Configuration Wizard" is checked, then click "Finish".
4. When the MySQL Instance Configuration Wizard launches, most default options are fine, but remember the username and password you use (root // whatever). You will need them to log into your chosen database management tool (below) in order to import SQL files later.
5. To test if MySQL is set up correctly, hit CTRL+ALT+DEL on your keyboard, enter the Task Manager, and select the "Services" tab. In the list of services you should see "MySQL" with a status of "Running".

6. Add MySQL to Environment Variables.

   1. Go to Control Panel -> System
   2. Go to Advanced System Settings

   3. Go to Environment Variables
   4. Under "Systemvariables" select **Path**
   5. Edit and add your install path of MySQL. For example: **C:\Program Files\MySQL\MySQL Server 8.0\bin\\**

{% include note.html content="MySQL development files: These files are shipped with MySQL Server. Search for them in the program files directory: MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib. You will need them later on for the server." %}

## [MySQL Client](#mysql-client)

### Download

- [HeidiSQL](https://www.heidisql.com/download.php) (Best for beginners)

- MySQL CLI (Fastest, comes with your MySQL Instalation)

- [DBeaver](https://dbeaver.io/) (Multi-platform Database Management Tool)

- [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)

{% include note.html content="You only have to pick one of the options on top." %}

### Installation

1. Try connecting to your database. You may be looking for "Connect to Host", "New Connection" or "Session Manager" depending on which program you use.

2. Create a new connection/session. The Hostname/IP address of "127.0.0.1" or "localhost" is fine if you installed MySQL on the same computer that you installed HeidiSQL or SQLYog. Simply fill in your root // whatever password and you should now be able to connect to your database. It's the information used in this step [MySQL](#mysql)

## [CMake](#cmake)

### Download

- https://cmake.org/download

{% include note.html content="NEVER download and install the RC (Release Candidate), ALWAYS the Latest Release" %}

### Installation

- Run the Windows MSI Installer.

{% include note.html content="We recommend compiling in 64-bit mode." %}

## [OpenSSL](#openssl)

### Download

- http://www.slproweb.com/products/Win32OpenSSL.html

{% include note.html content="Find the 64-bit version by finding the latest 3.x.x Win64 OpenSSL that is NOT the `light` version." %}

### Installation

- Run the Windows EXE/MSI Installer.

{{site.data.alerts.note}}
If you get the error 'Missing Microsoft Visual C++ .... Redistributable' while installing OpenSSL, download the <a href="https://aka.ms/vs/17/release/vc_redist.x64.exe">Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x64) (Direct Download)</a> (1.7MB Installer) and install it.
{{site.data.alerts.end}}

{{site.data.alerts.note}}
While installing OpenSSL, choose The OpenSSL binaries (/bin) directory (NOT "The Windows system directory") when given the choice of where to copy the OpenSSL DLLs. These DLLs will need to be located easily for <a href="windows-core-installation">Core Installation</a>.
{{site.data.alerts.end}}

## [Boost](#boost)

### Download

- https://www.boost.org

- [1.81.0](https://sourceforge.net/projects/boost/files/boost-binaries/1.81.0/boost_1_81_0-msvc-14.3-64.exe/download)

{% include note.html content="You only have to pick one of the options on top. The one that has the specific number, it's direct download to that version." %}

### Installation

- Add an environment variable to the "System" variable named "BOOST_ROOT" and with the value being your Boost installation directory, e.g. `C:/local/boost_1_81_0`. Important is to use '**/**', not '**\\**' when pointing to the directory. (Make sure that it does not have a trailing slash (end of the path). If you still get problems, add the same variable in the `USER` variables section too, as shown in the image below.)

<a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
</a>

{% include note.html content="Notice that this image shows the version number 1.72.0 - use your actual version number in your settings." %}

{% include note.html content="Make sure your BOOST_ROOT variable value has it's / facing the correct way. Like/this/that not\this\that" %}

<br>

|                            Header                             |
| :-----------------------------------------------------------: |
|                          [Git](#git)                          |
|               [Github Desktop](#github-desktop)               |
| [Visual Studio Community 2022](#visual-studio-community-2022) |
|                        [MySQL](#mysql)                        |
|                 [MySQL Client](#mysql-client)                 |
|                        [CMake](#cmake)                        |
|                      [OpenSSL](#openssl)                      |
|                        [Boost](#boost)                        |

## Help

If you are still having problems, check:

- [FAQ](faq)

- [Common Errors](common-errors)

- [How to ask for help](how-to-ask-for-help)

- [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |                                                           |
| [<< Start: Installation Guide](classic-installation)                                                                                 | [Step 2: Core Installation >>](windows-core-installation) |
