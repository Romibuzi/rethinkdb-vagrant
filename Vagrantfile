# -*- mode: ruby -*-
# vi: set ft=ruby :

# Configure using Vagrant's version 2 API/syntax.
Vagrant.configure(2) do |config|
  config.vm.box = 'wheezy64'
  config.vm.box_url = "http://downloads.shadoware.org/wheezy64.box"

  config.vm.network :private_network, ip: "192.168.65.10"
  config.vm.synced_folder ".", "/home/vagrant/rethinkdb", type: "nfs"

  # Provider
  config.vm.provider :virtualbox do |vb|
    vb.customize ['modifyvm', :id, '--memory', '2048']
  end

  # Port Forwarding
  config.vm.network :forwarded_port, guest: 8080,  host: 8080
  config.vm.network :forwarded_port, guest: 28015, host: 28015
  config.vm.network :forwarded_port, guest: 29015, host: 29015

  # Provisioning
  config.vm.provision :shell do |sh|
    sh.inline = <<-EOF
      export DEBIAN_FRONTEND=noninteractive;

      # Add RethinkDB Source
      apt-key adv --fetch-keys http://download.rethinkdb.com/apt/pubkey.gpg 2>&1;
      echo "deb http://download.rethinkdb.com/apt $(lsb_release -sc) main" > /etc/apt/sources.list.d/rethinkdb.list;
      apt-get update --assume-yes;

      # RethinkDB Install & Setup
      apt-get install --assume-yes rethinkdb;
      sed -e 's/# bind=127.0.0.1/bind=all/g' /etc/rethinkdb/default.conf.sample > /etc/rethinkdb/instances.d/default.conf;
      rethinkdb create -d /var/lib/rethinkdb/instances.d/default 2>&1;
      service rethinkdb start;

      #Install python driver
      apt-get install --assume-yes python-dev python-pip;
      pip install rethinkdb;
    EOF
  end
end
