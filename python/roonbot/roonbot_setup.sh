#!/usr/bin/env bash

# check for root
if [ "$EUID" -ne 0 ]
    then echo "This script must be run as root."
    exit
fi

# update
apt-get -y update --fix-missing

# install openjdk-7
apt-get -y install software-properties-common
add-apt-repository ppa:openjdk-r/ppa
apt-get -y update && apt-get -y install openjdk-7-jdk

# install the unix-runescape-client
echo "deb http://ppa.launchpad.net/hikariknight/unix-runescape-client/ubuntu trusty main" | tee -a /etc/apt/sources.list
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9BA73CFA
apt-get -y update && apt-get -y install unix-runescape-client

# install autopy
apt-get -y install python-dev python-pip libpng-dev libx11-dev libxtst-dev
pip install autopy

# ssh
apt-get -y install openssh-server
systemctl start ssh
systemctl enable ssh

