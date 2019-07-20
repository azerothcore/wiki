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
- Before we Enter the command `timedatectl list-timezones` 
- sudo timedatectl set-timezone your_time_zone
- sudo timedatectl set-timezone America/Los_Angeles

#### Add a new User
- adduser azcore
- usermod -aG sudo azcore

#### Verify Sudo access for the new User
- sudo su azcore
- sudo whoami
- exit


#### Installing Key Libraries & Additional Apps
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl1.0-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libace-6.* libace-dev
sudo apt-get update
sudo apt-get install screen
sudo apt install curl
sudo mysql_secure_installation
[no pass]/N/Y/Y/Y/Y
sudo apt install unzip
Sudo apt install
Configure MariaDB
sudo mysql
GRANT ALL ON *.* TO 'dbadmin'@'%' IDENTIFIED BY 'password1' WITH GRANT OPTION;
Flush Privileges;
exit
cd /etc/mysql/mariadb.conf.d
nano 50-server.cnf
Update Bind Address to: 0.0.0.0
Ctrl + X, Y, Ctrl + T Select 50-server.cnf
sudo /etc/init.d/mysql restart
Configure ufw
sudo apt update
sudo apt install ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 3306
sudo ufw allow 3724
sudo ufw allow 8085
sudo ufw enable
Git Clone
sudo su azcore
cd 
git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
cd azerothcore
mkdir build
cd build
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DTOOLS=0 -DSCRIPTS=1
make -j 4
make install
Data Files
cd
cd azeroth-server
curl https://wow.heyaapl.com/data.zip --output data.zip
unzip data.zip
cd data
unzip ‘*.zip’
Set up the server config files
Using SFTP, update authserver and worldserver
Configure the DataDir folder to: “/home/azcore/azeroth-server/data”
Database Setup
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
