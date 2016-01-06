#!/bin/bash


echo Install Virtualenv
echo ============

# Route port 80 traffic to port 8000

sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000

apt-get install -q -y python-virtualenv python-dev libpq-dev
(
    sudo -u vagrant /usr/bin/virtualenv --system-site-packages /home/vagrant/env ;
    su -c ". /home/vagrant/env/bin/activate; pip install -r /vagrant/requirements.txt;" vagrant
)

cp /vagrant/setup/server/local_settings_development.py /vagrant/pigaboo/local_settings.py

source /home/vagrant/env/bin/activate
