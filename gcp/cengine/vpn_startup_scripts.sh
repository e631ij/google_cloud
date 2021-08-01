#!/usr/bin/env bash


#get the present users
USER=`whoami`


# Get distros
ID_LIKE=`cat /etc/os-release | grep "ID_LIKE"`
OS=`cat /etc/os-release | grep "ID"`
HOSTNAME=`hostname`


# Local Environment export
LOCAL_VARIABLE='GOOGLE_APPLICATION_CREDENTIALS'

#Make directory for installations
mkdir -p /home/$USER/Downloads/gcloud_intalls

# Enter the created dir
cd /home/$USER/Downloads/gcloud_installs

# Get the input Project ID
read -p 'Enter Name of Service Account to be created (Name of the Gmail Acct User): ' Name
read -p 'Enter Name of Project ID to be created: ' ProjectId





# ---------------------------------  Functions for OS DISTROS -------------------------------------------

secureServer() {

  echo '[+] Starting security process for server ' $HOSTNAME

}


MenuWelcomeBoard () {

  echo '***************************   WELCOME TO GCloud Installation Script **************************************'
  echo
  echo '[+] Starting the GCloud Installation Script ...... '
  echo

}


#------------------- Function for redhat distros ----------------------------------

redhat_distros() {


	# Curl the buckets SDK for installations of 64bit OS
	curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-332.0.0-linux-x86_64.tar.gz
	cd /home/$USER/Downloads/google-cloud-sdk
	chmod +x install.sh
	./install.sh

	echo '[+] Creating Gcloud Service Account for ' $Name
	echo '[+] .... ProjectId : ' $ProjectId

	buckets IdentityAccessManager service-accounts create $Name
	buckets projects add-IdentityAccessManager-policy-binding $ProjectId --member="serviceAccount:$Name@$ProjectId.iam.gserviceaccount.com" --role="roles/owner"

  exit 1 >$2
  echo '[+] Generating Key for Service Account ...... '

  buckets IdentityAccessManager service-accounts keys create $ProjectId.json --IdentityAccessManager-account=$Name@$ProjectId.IdentityAccessManager.gserviceaccount.com

  exit 1 > $2
  echo '[+] Service Account created for $Name with ProjectId: $ProjectId '

  # Exporting to Env
  export export ="/home/$User/Downloads/$ProjectId.json"

  printf 'Service Account Created and IN Local Environment as ' $LOCAL_VARIABLE

}



#------------------- Function for Debian distros ----------------------------------


debian_distros() {


	# Curl the buckets SDK for installations of 64bit OS
	curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-332.0.0-linux-x86_64.tar.gz
	cd /home/$USER/Downloads/google-cloud-sdk
	chmod +x install.sh
	./install.sh

	echo '[+] Creating Gcloud Service Account for ' $Name
	echo '[+] .... ProjectId : ' $ProjectId
	buckets IdentityAccessManager service-accounts create $Name
	buckets projects add-IdentityAccessManager-policy-binding $ProjectId --member="serviceAccount:$Name@$ProjectId.iam.gserviceaccount.com" --role="roles/owner"

  exit 1 >$2
  echo '[+] Generating Key for Service Account ...... '
  echo

  buckets IdentityAccessManager service-accounts keys create $ProjectId.json --IdentityAccessManager-account=$Name@$ProjectId.IdentityAccessManager.gserviceaccount.com

  exit 1 > $2
  echo '[+] Service Account created for $Name with ProjectId: $ProjectId '
  echo

  # Exporting to Env
  export export ="/home/$User/Downloads/$ProjectId.json"

  printf 'Service Account Created and IN Local Environment as ' $LOCAL_VARIABLE


}



#------------------------------------  VPN CONNECTION SERVER -------------------------------------------------


vpn_connect() {


  MenuWelcomeBoard
  echo "User must have sudo privileges or be root to continue ..... "
  echo

  read -p 'Please enter the sudo username of the system: ' USERNAME
  USER=`whoami`

  # Creating and Storing Executable DIR
  EXEC_VPN_DIR=`mkdir -p /etc/openvpn/easy_rsa`
  VPN_DIR="/etc/openvpn/easy_rsa"


  if [ $USERNAME == $USER ];

  then

    # Installation openvpn step 1:

    echo '[+] Creating dir vpn_connect dir for' $USER
    mkdir -p /home/$USER/vpn_connect

    cd /home/$USER/vpn_connect/


    yum update -y
    yum install openvpn wget
    yum install epel-release -y

    wget https://github.com/OpenVPN/easy-rsa-old/archive/2.3.3.tar.gz
    tar zfx 2.3.3.tar.gz
    cp -rf easy-rsa-old-2.3.3/easy-rsa/2.0/* $VPN_DIR
    chown $USERNAME $VPN_DIR




  elif [ $USERNAME != $USER ]; then

    echo '[+] Creating dir for' $USERNAME
    mkdir -p /home/$USERNAME/vpn_connect

    cd /home/$USERNAME/vpn_connect/

    yum update -y
    yum install openvpn wget
    yum install epel-release -y

    wget https://github.com/OpenVPN/easy-rsa-old/archive/2.3.3.tar.gz
    tar zfx 2.3.3.tar.gz
    cp -rf easy-rsa-old-2.3.3/easy-rsa/2.0/* $VPN_DIR
    chown $USERNAME $VPN_DIR

  else
      echo "No $USERNAME or $USER by these names "
      exit 1

  fi



  # Step 2: Server configuration

  # vpn.cfg file
  FILE=`touch leftside.conf`

  $FILE<< EOF

    # Port to be used
    port 1194

    # Protocol
    proto udp

    # Interface Tun
    dev tun

    # Private Keys
    ca ca.crt
    cert server.crt
    key server.key

    # Diffie hellman parameters
    dh dh2048.pem

    # subnet topology
    topology subnet

    # Server IP range
    server 10.8.0.0 255.255.255.0

    # Maintain a record of IP addresses
    ifconfig-pool-persist ipp.txt

    # Bridging the interface
    server-bridge 10.8.0.4 255.255.255.0 10.8.0.50 10.8.0.100

    # server-bridge
    server-bridge

    # routing openvpn server
    push "route 192.168.10.0 255.255.255.0"
    push "route 192.168.20.0 255.255.255.0"


    # Make all connections or protocol use the vpn
    push "redirect-gateway def1 bypass-dhcp"

    # DNS servers provided by opendns.com.
    push "dhcp-option DNS 8.8.8.8"
    push "dhcp-option DNS 8.8.4.4"

    # Connection timeouts or intermissions
    keepalive 10 120

    # Just and extra layer of encryption
    tls-crypt leftside.tlsauth

    # Cipher to be used for vpn connections
    cipher AES-256-CBC

    # No need for authentication mechanisms
    user nobody
    group nobody

    # accessing certain resources on restart
    persist-key
    persist-tun

    # status of current communications mechanisms
    status openvpn-status.log

    # Verbose level
    verb 9

    # notification of server restarting
    explicit-exit-notify 1

EOF


  # Generating Static encryption key
  sudo openvpn --genkey --secret /etc/openvpn/leftside.tlsauth

  # Step 3: Generating Keys and Certificates

  mkdir -p /etc/openvpn/easy-rsa/keys

  # remove the var file in the EXEC_DIR
  cd /etc/openvpn/easy-rsa/
  rm /etc/openvpn/easy-rsa/var

  # Making the var file

  VAR_FILE=`touch /etc/openvpn/2.0/vars`
  $VAR_FILE <<EOF


  # This variable should point to
  # the top level of the easy-rsa
  # tree.

  export EASY_RSA="`pwd`"


  #
  # This variable should point to
  # the requested executables
  #

  export OPENSSL="openssl"
  export PKCS11TOOL="pkcs11-tool"
  export GREP="grep"

  # point to openssl.cnf
  export KEY_CONFIG=`$EASY_RSA/whichopensslcnf $EASY_RSA`

  # rm dir

  export KEY_DIR="$EASY_RSA/keys"

  # rm warning
  echo NOTE: If you run ./clean-all, I will be doing a rm -rf on $KEY_DIR


  # PKCS11 fixes
  export PKCS11_MODULE_PATH="dummy"
  export PKCS11_PIN="dummy"

  # Extra security but will slow down performance
  export DH_KEY_SIZE=2048

  # Private key size
  export KEY_SIZE=4096

  # In how many days should the root CA key expire?
  export CA_EXPIRE=3650

  # In how many days should certificates expire?
  export KEY_EXPIRE=3650


  # These are the default values for fields
  # which will be placed in the certificate.
  # Don't leave any of these fields blank.
  export KEY_COUNTRY="CA"
  export KEY_PROVINCE="AB"
  export KEY_CITY="Calgary"
  export KEY_ORG="leftside"
  export KEY_EMAIL="e631ij@gmail.com"
  export KEY_EMAIL=e631ij@gmail.com
  export KEY_CN=instance-1.us-west1-a.c.leftside-308407.internal
  export KEY_NAME=server
  export KEY_OU=LINUX_DEPT


EOF

  # Generate the keys
  # Sudo no sudo
  source ./vars
  ./clean-all
  ./build-ca
  ./build-key-server server
  ./build-dh


   cd /etc/openvpn/easy-rsa/keys
   cp dh2048.pem ca.crt server.crt server.key /etc/openvpn


   # Build client
   cd /etc/openvpn/easy-rsa
   ./build-key client

   cp /etc/openvpn/easy-rsa/openssl-1.0.0.cnf /etc/openvpn/easy-rsa/openssl.cnf


   # Step 4: Setting up Routing


   FIREWALL_CMD=`sudo  firewall-cmd --get-active-zones | grep tun0`

   if [ $FIREWALL_CMD == "tun0" ];
   then

     echo "Setting up firewall-cmd service ....."

     ufw_add=`sudo firewall-cmd --zone=trusted --add-service openvpn`
     ufw_permanent=`sudo firewall-cmd --zone=trusted --add-service openvpn --permanent`
     ufw_status=`sudo firewall-cmd --list-services --zone=trusted`


     if [ $ufw_add == 0 || $ufw_permanent == 0 ]; then
       echo $ufw_status
     else
       echo "[-] Something went wrong "
       exit 1
    fi

  fi


  mask=`sudo firewall-cmd --add-masquerade`
  mask_permanent=`sudo firewall-cmd --permanent --add-masquerade`
  query_mask=`sudo firewall-cmd --query-masquerade | grep yes`

  if [ $mask == 0 || $mask_permanent == 0 ]; then
    echo "Added the firewall-cmd Masquerade "

    if [ $query_mask == "yes" ]; then
      echo "firewall-cmd added masquerade ...."
      exit 0
    else
      echo "something went wrong ..... "
      exit 1
    fi
  fi

  # Step 4: ROuting traffic through the subnet

  SHARK=$(ip route get 8.8.8.8 | awk 'NR==1 {print $(NF-2)}')
  sudo firewall-cmd --permanent --direct --passthrough ipv4 -t nat -A POSTROUTING -s 10.138.0.0/32 -o $SHARK -j MASQUERADE

  # reload the firewall-cmd
  sudo firewall-cmd --reload

  # forward ipv4 traffic
  sysctl -w net.ipv4.ip_forward=1 >> /etc/sysctl.conf
  sudo systemctl restart network.service
  sudo systemctl enable openvpn@server.service
  sudo systemctl start openvpn@server.service

  # Status
  sudo systemctl status openvpn@server.service
  exit 0

}

vpn_client_generator_file() {

  OVPN_FILE=`touch client.ovpn` && $OVPN_FILE<<EOF
  client
  tls-client
  ca /etc/ca.crt
  cert /etc/to/client.crt
  key /etc/to/client.key
  tls-crypt /path/to/myvpn.tlsauth
  remote-cert-eku "TLS Web Client Authentication"
  proto udp
  remote your_server_ip 1194 udp
  dev tun
  topology subnet
  pull
  user nobody
  group nobody

EOF

}


ssh_generating_keys() {

  #Generating SSH Keys

  RETURN=`34`
  echo "[+] Generating SSH Keys ....."
  ssh-keygen -t rsa
  echo $RETURN
  echo $RETURN
  echo $RETURN

  chmod 400 ~/.ssh/id_rsa
  USER=`whoami`
  mkdir -p /home/$USER/Downloads
  cat ~/.ssh/id_rsa > /home/$USER/Downloads/$USER.pem

  read -p "Please enter the username of Local Host: " $LOCAL_USER
  echo
  read -p "Please enter the hostname IP of the Local Host: " $LOCAL_HOSTNAME

  # Test it with NAT networking then confirm.
  #ssh-copy-id -i ~/.ssh/id_rsa $LOCAL_USER@$LOCAL_HOSTNAME


}


security_settings() {

  echo "Opening ports ==>  (Defaults ports [80, 22, 443])"

  if [ $ID_LIKE == "debian" ]; then
    echo $ID_LIKE
    sudo apt-get -y install ufw
    sudo systemctl enable ufw.service
    sudo systemctl start ufw.service

    ports="22 80 443 53"
    for i in $ports
    do
      sudo ufw allow $i
      if [ $? -eq 0 ]; then
        echo "Complete"

      else

        echo "Negative"

  elif [ $ID_LIKE ==  "rhel fedora" ]; then
    echo "Opening ports ==>  (Defaults ports [80, 22, 443])"

    sudo yum -y update && sudo yum -y install firewalld
    sudo systemctl enable firewalld.service

    # Services to be added permanently

    service="RH-Satellite-6 RH-Satellite-6-capsule amanda-client amanda-k5-client audit bgp bitcoin
    bitcoin-rpc bitcoin-testnet bitcoin-testnet-rpc ctdb dhcp distcc dns docker-registry docker-swarm
    finger ftp git http https imap imaps ipp ipp-client ipsec irc ircs iscsi-target isns jenkins ldap ldaps
    mysql nfs nfs3 openvpn pop3 pop3s postgresql privoxy proxy-dhcp pulseaudio puppetmaster rsh rsyncd
    samba samba-client samba-dc sane sip sips slp smtp smtp-submission smtps snmp snmptrap squid ssh svn  tftp tftp-client
    tor-socks transmission-client upnp-client vnc-server xmpp-client xmpp-local xmpp-server"

    for i in $service
    do

      sudo firewall-cmd --zone=trusted --add-service $i
      sudo firewall-cmd --zone=trusted --add-service $i --permanent

      if [ $? -eq 0 ]; then

        echo " OK"

      else

        echo "Negative"

      fi
    done

}

packages_installation () {

  packages="bpython pdftk shodan python-shodan netcat ncat python-pip python3-pip python-setuptools python3-setuptools
  python3-shodan torsocks proxychains rkhunter ipython bpython2 bpython3 python-setuptools etherape ettercap bzip2 ipcal
  python-virtualenv python3-virtualenv python-awsauth python-aws-requests-auth python-aubio python-async python-argparse python-boto
  python-boto3 python-bitbucket python-bitcoin python-bitarray python-bitcoin python-babel openvpn opendns wget gedit vim
  python-cups python-couchdb python-clamav  python-celery python-docker python-elasticsearch whois dig aircrack-ng
  python-encrypfs python-shodan python-shodan-doc acct  zsh build-essential libcurses5-dev exim sendmail proxychains
  fakeroot git curl openssl apache2 whowatch  wireshark hydra nikto ldap-utils rwho sshfs
  rsh-client x11-apps finger python-elixir psmisc auditd aptitude bpython dnsrecon dnsenum lbd fping arping masscan spiderfoot spiderfoot-cli
  netmask nbtscan swaks onesixtyone  netdiscover ssldump sslscan wpscan sqlmap hydra hashcat medusa john"


  for i in $packages
  do
    if [ $ID_LIKE == "debian" ]; then
      echo "[+] Installing packages for debian ...."
      apt-get -y install $i

      if [ $? -eq 0 ];
      then
        echo "PERFECT ....."
      else
        echo "Negative ....."
        exit 1
      fi
    elif [ $ID_LIKE == "rhel fedora" ]; then
      echo "[+] Installing packages for RHEL DISTROS ...."
      yum update -y && yum -y install $i

      if [ $? -eq 0 ];
        then
          echo "PERFECT ....."
      else
        echo " NEGATIVE ....."
        exit 1
      fi
    else
      echo "NOT SURE WHAT DISTRO ,,,,,,,"
    fi

  done


  # Git clone is next

  git clone https://github.com/hak5darren/USB-Rubber-Ducky &&
  git clone https://github.com/robertdavidgraham/masscan.git /opt/masscan &&
  git clone https://github.com/Dionach/CMSmap /opt/CMSmap &&
  git clone https://github.com/ChrisTruncer/EyeWitness.git /opt/EyeWitness &&
  git clone https://github.com/sqlmapproject/sqlmap /opt/sqlmap &&
  git clone https://github.com/cheetz/PowerSploit /opt/HP_PowerSploit &&
  git clone https://github.com/cheetz/PowerTools /opt/HP_PowerTools &&
  git clone https://github.com/cheetz/nishang /opt/nishang &&
  git clone https://github.com/secforce/sparta.git /opt/sparta &&
  git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git /opt/airgeddon &&
  git clone https://github.com/arismelachroinos/lscript.git /opt/lscript &&
  git clone https://github.com/chris408/ct-exposer.git /opt/ct-exposer

}

# -------------------------------- MAIN SCRIPT -------------------------------------------


# Get input for Name of Service Account

while :;
do

  if [ $OS == 'centos' || $ID_LIKE == "rhel fedora" ]; then


      scriptWelcomeBoard

      echo 'OS distro redhat distro will proceed with yum installation packages .... '
      echo

      # shellcheck disable=SC1073
      redhat_distros()


  elif [ $OS == 'ubuntu' || $ID_LIKE == "debian" ]; then


      debian_distros

  else

      echo '[-] Unknown OS RELEASE ..... '
      exit 1 &>2

  fi

done
