# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

vagrant_dir = File.expand_path(File.dirname(__FILE__))

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "fabric"
  config.vm.hostname = "vagrant.host"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.ssh.forward_agent = true

  config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
  end

  config.vm.network :private_network, ip: "192.168.56.101"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
end

