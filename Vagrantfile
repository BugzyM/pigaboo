# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.package.name = "precise.box"
    config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"

    #localhost forwarding
    config.vm.network "forwarded_port", guest: 8000, host: 8080

    #postgres forwarding
    config.vm.network "forwarded_port", guest: 5432, host: 8081


    config.vm.network :private_network, ip: "192.168.33.10"

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", 256]
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end


    config.vm.provision :shell, :path => "setup/make_vagrant.sh"
end