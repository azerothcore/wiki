## Introduction
This tutorial will walk you through the entire AzerothCore server setup process, and will help get you familiar with using Debian and Command Line Interfaces (CLI). In this tutorial, we'll be going over the following:
- Looking at various tools to help you get your server up and running, such as MySQL Clients, SSH Clients, SFTP Clients, and powerful file editors. 
- Configuring a Droplet on DigitalOcean from scratch
- Building the Core
- Loading the Database

There is a Step-by-Step YouTube Video which walks you through this entire process. It's encouraged you follow along with that video, while using this tutorial as a reference guide.

## PC Apps You May Need:
#### MySQL Clients:
- HeidiSQL
- MySQL Workbench
- SQLYog (Paid)

#### SSH Clients:
- DigitalOcean’s Console
- PuTTY
- Terminus (Paid)

#### FTP Clients:
- Filezilla
- Terminus (Paid)

#### File Editors:
- Notepad++

## Choosing our Droplet
#### Setup new Droplet
- 8GB RAM / 4 Cores
- Debian 9
- Choose Region
- Enable Monitoring
- One-time Password
- Name Droplet | AzerothCore

## Droplet Initial Configuration
#### Change your Time Zone
- Enter the command `timedatectl` to confirm the Droplet is set to UTC (00:00) time.
- Before we can set the time zone, we first need to figure out what the code is for your time zone. Enter the command `timedatectl list-timezones` to see a list of all time zones. Hit Enter until you find your time zone, and make note of it. Hit *Control+C* once you're done looking for time zones.
- Once you're back at the command line, enter `sudo timedatectl set-timezone YOUR_TIME_ZONE`
- Verify that the Time Zone set correctly by entering `timedatectl`

#### Add a new User
- It's best practice to not use the *root* user for applications. Because of this, we're going create a user that will be responsible for all AzerothCore activities. Enter `adduser azcore` to create a new user.
- Next, let's make sure this user has sudo permissions. Provision those permissions by using the following command `usermod -aG sudo azcore`

#### Verify Sudo access for the new User
- Let's log in as our new user `sudo su azcore`
- Enter `sudo whoami` and then enter the password you chose for this user (may be different from your root password.
- If it says *root*, then you're all set! Enter the command `exit` to return to your root user for the next steps.

#### Installing Key Libraries & Additional Apps
- Next we need to install a bunch of important libraries, applications, and tools needed to Azerothcore. Run the following command: `sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev` Choose 'Y' for any prompts asking for additional space for the installation.
- Let's refresh our App List once again before we continue `sudo apt-get update`
- Let's install Screen, an application that will let us have multiple applications open at once and persist after we log out of the console `sudo apt-get install screen`
- Next up is curl - we'll be using this to get the VMAP, MMAP, and other required data for the server `sudo apt install curl`
- Let's install the unzip utility, so we can unzip the data files `sudo apt install unzip`
- Finally, let's wrap up with `sudo apt install`

#### Complete the MariaDB Secure Installation
- Let's begin the process `sudo mysql_secure_installation`
- For the following prompts, answer `[no pass]/N/Y/Y/Y/Y`
- Once we're back in the command line, type `sudo mysql` to enter the MariaDB Console
- Once in the MariaDB Console, let's create our User `GRANT ALL ON *.* TO 'dbadmin'@'%' IDENTIFIED BY 'password1' WITH GRANT OPTION;` Choose a Username you want - it can be anything you'd like, it doesn't have to be `dbadmin`. Also, please make sure you choose a very secure password, as `password1` should *NEVER* be used.
- Let's refresh the permissions for MariaDB `Flush Privileges;`
- Return to the main Debian console `exit`

#### Configure Remote Connections to MariaDB
- Navigate to the folder holding the file we need `cd /etc/mysql/mariadb.conf.d`
- Launch the nano file editor for the configuration file `nano 50-server.cnf`
- Navigate to the Bind Address, and update it to: `0.0.0.0`
- To save your changes, press *Ctrl + X*, then *Y*, followed by *Ctrl + T*. Then use your arrow keys to select `50-server.cnf`
- Now that we've updated a key MariaDB Configuration file, we need to restart the MariaDB process. Enter `sudo /etc/init.d/mysql restart`

#### Configure the Uncomplicated Firewall (UFW)
- Let's refresh our catalog of apps `sudo apt update`
- Let's install UFW `sudo apt install ufw`
- Next, we're going to blanket-block all Incoming connections. This is an important step to protecting your server. We'll open up ports in the following steps `sudo ufw default deny incoming`
- Next, let's blanket-allow all Outgoing connections. This should allow your server to make callouts without issue. `sudo ufw default allow outgoing`
- We need to make sure we don't get locked out of the Console, so we need to unblock port 22, which is the port SSH uses. To do this, enter `sudo ufw allow ssh`
- Let's allow the MariaDB Port to accept incoming connections `sudo ufw allow 3306`
- Let's enable the Authentication Server to accept incoming connections `sudo ufw allow 3724`
- And now the Worldserver port `sudo ufw allow 8085`
- Verify that you've enabled all the above ports, and then turn on UFW with this: `sudo ufw enable`

## AzerothCore Installation
#### Let's clone the AzerothCore Git
- Log in as our sudo user `sudo su azcore`
- Navigate to our home directory `cd` 
- Let's download and clone the latest version of AzerothCore `git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore`
- Once the clone is complete, let's navigate to the top level folder of the git directory `cd azerothcore`
- We need to make a folder called *build* `mkdir build`
- Navigate to the new build folder `cd build`
- Now we run the cmake command, this is the pre-compile step to ensure all cpp files are accounted for before we compile, and it tells the compile what to compile. `cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DTOOLS=0 -DSCRIPTS=1`
- Now we compile AzerothCore - this can take some time, depending on the number of cpu cores your Droplet has. This tutorial is based on the 4 cpu core Droplet, so we'll use `make -j 4`. If you've got a different number of cores, replace the 4 with the number of cpu cores you have.
- Once the compile is complete, let's assemble the final files and move them to their final home `make install`

#### Data Files
- Let's navigate back to the home directory `cd`
- Now we need to go to the compile server folder `cd azeroth-server`
- Let's download the data files required. `curl https://wow.heyaapl.com/data.zip --output data.zip`
- Let's unzip the main data directory `unzip data.zip`
- We need to navigate to the data folder to continue unzipping the child folders `cd data`
- No we will unzip all child zip files `unzip ‘*.zip’`


#### Set up the server config files
- Using SFTP, navigate to `/home/azcore/azeroth-server/etc' and download the authserver.conf.dist and worldserver.conf.dist. 
- Rename them on your local machine to remove the .dist from the file name. 
- Update the Database information in both the Authserver and Worldserver configuration files to use the username and password you created in the earlier steps.
- In the Worldserver config, configure the DataDir folder to: `“/home/azcore/azeroth-server/data"`
- Upload the .conf files back to the etc directory using your SFTP client.

#### Database Setup
Clone /home/azcore/azerothcore/conf/config.sh.dist to config.sh
Update the section DB EXPORTER/IMPORTER CONFIGURATIONS with DB Information
Save and upload back
Run bash apps/db_assembler/db_assembler.sh
Select import-all: Assemble & Import All
Update Realmlist Table
Open HeidiSQL or MySQL Workbench and connect to DB
Update the acore_auth.realmlist to the ip of the DigitalOcean server
Start up the server
As root, navigate to: cd /home/azcore/azeroth-server/bin
screen -AmdS auth ./authserver
screen -AmdS world ./worldserver
Create your In-Game Account
Navigate to the World screen: screen -r world
account create [accountname] [password]
account set gmlevel [accountname] 3 -1
Set your realmlist.wtf to your DigitalOcean IP, and log in!
