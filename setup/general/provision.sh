#!/bin/bash

echo General configuration
echo =====================

test=`grep /vagrant/setup/general/.bashrc ~vagrant/.bashrc`
if [ "$test" = "" ]; then
    echo ". /vagrant/setup/general/.bashrc" >> /home/vagrant/.bashrc
fi;

cp /vagrant/setup/general/.bash_aliases /home/vagrant/.bash_aliases
source /home/vagrant/.bash_aliases

echo "pigaboo" > /etc/hostname
hostname -F /etc/hostname

sudo sed -i "3i127.0.0.1  pigaboo" /etc/hosts

apt-get -y -q install \
    avahi-daemon \
    checkinstall \
    git-core \
    build-essential
