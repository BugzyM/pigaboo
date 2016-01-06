#!/bin/bash


echo Install Postgres
echo ============

apt-get install -y -q postgresql postgresql-contrib
sudo -u postgres createuser -s pigaboo_user
echo "alter user pigaboo_user with password 'pigaboo';" | sudo -u postgres psql

sudo -u postgres createdb -O pigaboo_user pigaboo
