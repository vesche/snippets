#!/usr/bin/env bash

# install bro with GeoIP on CentOS/RHEL 7.x

# check for root
if [ "$EUID" -ne 0 ]
  then echo "This script must be run as root."
  exit
fi

# yum stuff
yum makecache fast
yum -y update
yum -y install epel-release

# optional packages
yum -y install net-tools htop nano vim

# bro packages
yum -y install cmake make gcc gcc-c++ git flex bison libpcap-devel openssl-devel python-devel swig wget zlib-devel

# geoip
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/GeoLiteCityv6.dat.gz
gunzip GeoLiteCity.dat.gz
gunzip GeoLiteCityv6.dat.gz
mkdir -p /usr/local/share/GeoIP
mv GeoLiteCity.dat /usr/local/share/GeoIP/
mv GeoLiteCityv6.dat /usr/local/share/GeoIP/
wget http://www.maxmind.com/download/geoip/api/c/GeoIP.tar.gz
tar xzf GeoIP.tar.gz
pushd GeoIP-1.4.8/
./configure && make && make install
popd

# bro
git clone --recursive git://git.bro.org/bro
pushd bro
./configure && make && make install
popd

# set interface in node.cfg
ls /sys/class/net
read -p 'Interface to use?' interface
sed -i "s/eth0/$interface/g" /usr/local/bro/etc/node.cfg

# install and start bro
/usr/local/bro/bin/broctl install
/usr/local/bro/bin/broctl start
/usr/local/bro/bin/broctl status

echo Done
