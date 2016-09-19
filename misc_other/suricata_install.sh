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

# suricata packages
sudo yum -y install gcc libpcap-devel pcre-devel libyaml-devel file-devel zlib-devel jansson-devel nss-devel \
libcap-ng-devel libnet-devel tar make libnetfilter_queue-devel lua-devel wget

# download and install suricata
wget http://www.openinfosecfoundation.org/download/suricata-3.1.2.tar.gz
tar xzf suricata-3.1.2.tar.gz
pushd suricata-3.1.2
./configure && make && make install-full
popd

# ssl blacklist rules
wget https://sslbl.abuse.ch/blacklist/sslblacklist.rules
wget https://sslbl.abuse.ch/blacklist/sslipblacklist_aggressive.rules
mv sslblacklist.rules /usr/local/etc/suricata/rules/
mv sslipblacklist_aggressive.rules /usr/local/etc/suricata/rules/

# done
echo Done add rule files to /usr/local/etc/suricata/suricata.yaml
echo then to start do
echo suricata -c /usr/local/etc/suricata/suricata.yaml -i eth0
