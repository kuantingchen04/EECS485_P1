#!/usr/bin/env bash

# Update apt first (system package installer)
sudo apt update

# Install the only editors you'll ever need.
sudo apt install vim emacs --yes

sudo apt install git

# Install Python pip with --yes as the default argument

# Install virtualenv used for 485 projects
sudo apt install python3 python3-pip --yes
pip3 install virtualenv

# By default, while installing MySQL, there will be a blocking prompt asking you to enter the password
# Next two lines set the default password of root so there is no prompt during installation
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'

# Install MySQL server with the default argument --yes
sudo apt install mysql-server --yes
sudo apt install build-essential python-dev libmysqlclient-dev --yes

# So that we can load XML infile for SQL purposes (used in project 1)
sudo printf "\n[mysqld]\nlocal-infile\n\n[mysql]\nlocal-infile\n" >> /etc/mysql/my.cnf

