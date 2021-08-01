#!/usr/bin/env bash


#---------------- Variables ---------------------------

instance_connect() {

  echo "[+] Connection to Google Compute Instance ....."
  echo

  #read -p "Enter the Instance ProjectID for connection: " projectId
  read -p "Enter the Instance name for connection: " Instance_name
  read -p "Enter the Zone for connection:  " instance_zone

  gcloud compute ssh $instance_name  --zone=$instance_zone

}


instance_scp () {


  read -p "Enter the Instance name to connect too: " Instance_name
  read -p "Enter the zone location for Instance:  " instance_zone

  echo
  echo

  echo "1) Enter 1 to copy to remote server."
  echo "2) Enter 2 to copy to local server from remote."
  read -p "OPTION: " option

  echo "DIR's and Zone locations:"
  read -p "Enter the Path for local DIR: " LOCAL_DIR
  read -p "Enter the Path for REMOTE DIR: " REMOTE_DIR
  read -p "Enter the Zone Location:  " instance_zone


  if [ $option == "1"  ]; then

    echo
    echo "[+] Copy files to the remote hosts ....."
    gcloud compute scp $LOCAL_DIR  $instance_name:$REMOTE_DIR --zone=$instance_zone

  elif [ $option == "2" ]; then

    echo
    echo "[+] Copy files from the remote hosts to the local hosts ...... "
    gcloud compute scp $instance_name:$REMOTE_DIR  $LOCAL_DIR --zone=$instance_zone

  else

    echo "[-] Something went Wrong ......"
    echo 1

  fi

}


instance_connect

