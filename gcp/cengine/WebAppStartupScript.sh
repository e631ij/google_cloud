#!/usr/bin/env bash


#get the present users
USER=`whoami`


# Get distros
ID_LIKE=`cat /etc/os-release | grep "ID_LIKE"`
ID=`cat /etc/os-release | grep "ID"`
HOSTNAME=`hostname`
HTMLFILE=`touch index.html`


MenuWelcomeBoard () {

  echo '***************************   WELCOME TO HBOARD SERVER Installation Script **************************************'
  echo
  echo '[+] Starting the WepAppStartupScript Installation Script ......'
  echo

}


#------------------- Function for Linux distros ----------------------------------

Centos7wepAppStartupScript() {

  sudo yum clean all
  sudo yum update -y

  sudo yum install httpd
  sudo systemctl enable httpd
  sudo systemctl start httpd

  if [ $? eq "0"];
  then

    sudo firewall-cmd --add-service=http
    sudo firewall-cmd --add-port=80/tcp

    cp -iv /var/www/html/index.html /var/www/html/index.html.bak

    cd /var/www/html/
    $HTMLFILE <<EOF

    <html>
<head>
<title>Welcome to the LeftsideVision</title>
</head>
<body>
<h1>Olimpus</h1>
<p>Welcome to the LeftsideVision Have a nice stay.</p>
</body>
</html>
EOF

  else

    echo "SOMETHING WENT WRONG ...... "

  fi


}


DebianWebAppStartupScript() {

  sudo aptitude clean all
  sudo apt-get update -y

  sudo apt-get -y install apache2
  sudo systemctl enable apache2.service
  sudo systemctl start apache2.service

  if [ $? eq "0"];
  then

    cp -iv /var/www/html/index.html /var/www/html/index.html.bak
    cd /var/www/html


    $HTMLFILE <<EOF

    <html>
<head>
<title>Welcome to the LeftsideVision</title>
</head>
<body>
<h1>LeftsideVision</h1>
<p>Welcome to the LeftsideVision Have a nice stay.</p>
</body>
</html>
EOF

  else

    echo "SOMETHING WENT WRONG ....."

  fi

}

debian_security_settings() {

  echo "Opening ports ==>  (Defaults ports [80, 22, 443, 8080])"
  echo
  echo

  # shellcheck disable=SC1069
  # shellcheck disable=SC1020

  sudo apt-get -y update && sudo apt-get -y install ufw
  sudo systemctl enable ufw.service
  sudo systemctl start ufw.service

  ports="22 80 443 53"
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
  torsocks proxychains rkhunter python-setuptools bzip2 ipcal python-virtualenv python3-virtualenv
  python-aws-requests-auth python-argparse python-bitbucket python-couchdb whois aircrack-ng nmap
  openvpn wget gedit acct zsh build-essential sendmail proxychains git apache2 whowatch
  hydra ldap-utils rwho tcpdump aptitude"


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
  debian_security_settings
  DebianWebAppStartupScript

elif [ $ID == "ID=debian" ]; then

  MenuWelcomeBoard

  echo '[+] Debian packages installation ......'
  echo
  echo

  # ** App **
  packages_installation
  debian_security_settings
  DebianWebAppStartupScript


else

  MenuWelcomeBoard

  echo 'Redhat Installation packages ......'
  echo
  echo

  packages_installation
  rhel_security_settings
  Centos7wepAppStartupScript

fi
