# README #

# pigaboo

Pigaboo web chat app by BugzyM

Install Instructions 

1. Install Git
2. Install VirtualBox (https://www.virtualbox.org/wiki/Downloads)
3. Install Vagrant (https://www.vagrantup.com/downloads.html)
4. Clone the project from: git clone https://github.com/BugzyM/pigaboo.git
5. From a terminal in the root directory of the project, run: vagrant init and then vagrant up
6. Follow the instructions printed out at the end of running the command above
7. To complete the installation, please add the following to your /etc/hosts file:
        192.168.33.10 pigaboo.local
        192.168.33.10 <groupname>.pigaboo.local
8. Add the following to /etc/postgresql/9.1/main/pg_hba.conf
    IPV4
        host    all             all             0.0.0.0/0            md5
    IPV6
        host    all             all             ::/0            md5
9. Then restart postgresql service using this command:
        sudo service postgresql restart
10. ssh into the vm: vagrant ssh

        Run these commands to run the server:
            'python manage.py syncdb'
            'python manage.py migrate'
            'run_server' # Executes /home/vagrant/env/bin/python /vagrant/manage.py runserver 0.0.0.0:8000
        Open a browser to http://pigaboo.local
        
11. Start Celery worker by running 'celery -A pigaboo.apps.core.celerytasks.tasks worker -l info'
7. Install node >= v 0.10.0, as grunt fails without it. (For Mac use brew package manager or download installable http://nodejs.org/download/)
