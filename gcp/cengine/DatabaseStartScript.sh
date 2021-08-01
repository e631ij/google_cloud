#!/usr/bin/env bash


#get the present users
USER=`whoami`


# Get distros
ID_LIKE=`cat /etc/os-release | grep "ID_LIKE"`
ID=`cat /etc/os-release | grep "ID"`
#CENTOS=$(cat /etc/os-release | grep "rhel")
HOSTNAME=`hostname`



MenuWelcomeBoard () {

  echo '***************************   WELCOME TO HBOARD SERVER Installation Script **************************************'
  echo
  echo '[+] Starting the Database Installation Script ......'
  echo

}


#------------------- Function for Linux distros ----------------------------------

mysql_database_installs_test() {

  mkdir -p /home/$USER/Downloads/mysql_dir

  #
  cd /home/$USER/Downloads/mysql_dir

  echo ""
  wget https://repo.mysql.com/mysql80-community-release-el7-1.noarch.rpm
  yum repolist enabled | grep "mysql.*-community.*"
  yum install mysql-community-server

  # MYSQL
  yum-config-manager --disable mysql57-community
  yum-config-manager --enable mysql56-community

  #Service

  service mysqld start
  service mysqld status

  /bin/systemctl status  mysqld.service

  # Check --Version
  mysql --version


}


debian_security_settings() {

  echo "Opening ports ==>  (Defaults ports [80, 22, 443])"
  echo
  echo

  # shellcheck disable=SC1069
  # shellcheck disable=SC1020

  sudo apt-get -y update && sudo apt-get -y install ufw
  sudo systemctl enable ufw.service
  sudo systemctl start ufw.service

  ports="22 80 443 53 3306"
  for i in $ports
  do
    sudo ufw allow $i
    if [ $? = 0 ];
    then
      echo "Complete =============>>>>>>>>>>>"
      echo
      echo

    else

      echo "Negative <<<<<<<<<<=============="
      echo
      echo

    fi
  done

}


rhel_security_settings () {




    echo "Opening ports ==>  (Defaults ports [80, 22, 443])"
    sudo yum update -y && sudo sudo yum install -y firewalld
    sudo systemctl enable firewalld

    # Services to be added permanently

    service="bgp bitcoin bitcoin-rpc ctdb dhcp distcc dns docker-registry docker-swarm
    git http https mysql openvpn pop3 pop3s postgresql puppetmaster rsh rsyncd vnc-server"

    for i in $service
    do

      sudo firewall-cmd --zone=trusted --add-service $i
      sudo firewall-cmd --zone=trusted --add-service $i --permanent

      if [ $? -eq 0 ];
      then
        echo
        echo "Command not working ...."
      else
        echo
        echo " Success ......."
      fi
    done


}


packages_installation () {

  packages="bpython netcat ncat python3-pip python-shodan python-setuptools python3-setuptools
  torsocks rkhunter python-setuptools bzip2 ipcal python-virtualenv python3-virtualenv
  python-aws-requests-auth python-argparse python-bitbucket python-couchdb whois aircrack-ng nmap
  openvpn wget gedit acct zsh build-essential sendmail proxychains git apache2"


  for i in $packages
  do
    # shellcheck disable=SC2109
    if [ $ID_LIKE == "ID_LIKE=debian" ]; then
      echo "[+] Installing packages for debian ........"
      echo

      sudo apt-get -y update && sudo DEBIAN_FRONTEND=noninteractive apt-get -y install $i
      echo
      echo

      if [ $? = 0 ];
      then
        echo "Success ================>>>>>>"
        echo
      else
        echo "Negative <<<<<==============="
        echo
      fi

    else

      echo "[+] Installing packages for RHEL DISTROS ...."
      echo
      echo
      sudo yum update -y && sudo  yum -y install $i

      if [ $? = 0 ];

      then
          echo " Success =============>>>>>>>>"
          echo

      else

          echo " NEGATIVE <<<<<<<<==========="
          echo
      fi
    fi

  done

}



# -------------------------------- MAIN SCRIPT -------------------------------------------
# Get input for Name of Service Account


if [ $ID_LIKE == "ID_LIKE=debian" ];
then

  MenuWelcomeBoard

  echo '[+] Debian packages installation ......'
  echo
  echo

  # ** App **
  packages_installation
  github
  debian_security_settings

elif [ $ID == "ID=debian" ]; then

  MenuWelcomeBoard

  echo '[+] Debian packages installation ......'
  echo
  echo

  # ** App **
  packages_installation
  github
  debian_security_settings


else

  MenuWelcomeBoard

  echo 'Redhat Installation packages ......'
  echo
  echo

  packages_installation
  github
  rhel_security_settings

fi
