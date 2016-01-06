#!/bin/bash

cd `dirname $0`

BASE_CACHE_DIR=/vagrant_cache/
for f in "apt/archives"; do
    rm -rf /var/cache/$f; #remove symlink
    mkdir -p ${BASE_CACHE_DIR}$f;
    ln -sf ${BASE_CACHE_DIR}$f /var/cache/$f;
done;

export DEBIAN_FRONTEND=noninteractive

echo Ensuring shell files are executable...
echo --------------------------------------
find /vagrant/setup -type f -name '*.sh' -exec chmod -v +x '{}' \+
echo
echo Fixing Locale
echo -------------
export LC_CTYPE=en_US.UTF-8


# Remove universe and multiverse from apt
sed -i -e "s/us./za./g" /etc/apt/sources.list # Use the ZA mirror for software
cat /etc/apt/sources.list | grep multiverse > /etc/apt/sources.list.d/multiverse.list.disabled
cat /etc/apt/sources.list | grep universe > /etc/apt/sources.list.d/universe.list
cat /etc/apt/sources.list | grep -E -v "universe|multiverse" > /etc/apt/sources.list.new
mv /etc/apt/sources.list.new /etc/apt/sources.list
apt-get update

/vagrant/setup/general/provision.sh
/vagrant/setup/postgres/provision.sh
/vagrant/setup/pigaboo/provision.sh

# Complete

clear
echo Installation complete
echo =====================
echo To complete the installation, please add the following to your /etc/hosts file:
echo
echo 192.168.33.10 pigaboo.local
echo 192.168.33.10 <groupname>.pigaboo.local
echo Add the following to /etc/postgresql/9.1/main/pg_hba.conf
echo IPV4
echo host    all             all             0.0.0.0/0            md5
echo IPV6
echo host    all             all             ::/0            md5
echo
echo Then restart postgresql service using this command:
echo sudo service postgresql restart
echo with <groupname> being replaced by the subdomain for the group being tested
echo and being repeated for every group. Alternatively the domain can be overridden
echo as a wildcard (*.pigaboo.local) on a local DNS server if one is available.
echo ---
echo To test the UI:
echo    1 ssh into the vm: vagrant ssh
echo    2 run 'python manage.py syncdb'
echo    3 run 'python manage.py migrate'
echo    4 run 'run_server' # Executes /home/vagrant/env/bin/python /vagrant/manage.py runserver 0.0.0.0:8000
echo    5 Open a browser to http://pigaboo.local
echo ---
echo Start Celery worker by running 'celery -A pigaboo.apps.core.celerytasks.tasks worker -l info'
echo from project root.