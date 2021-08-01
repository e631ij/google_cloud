#!/usr/bin/env bash


#------------------------------------  VARIABLES ----------------------------------------------


USER=`whoami`

#Make directory for installations
mkdir -p /home/$USER/Downloads/gcloud_intalls

# Enter the created dir
cd /home/$USER/Downloads/gcloud_installs

# ---------------------------------  Functions for OS DISTROS -------------------------------------------

MenuWelcomeBoard () {

  echo '***************************   WELCOME TO GCloud Installation Script **************************************'
  echo
  echo '[+] Starting the GCloud Installation Script ...... '

}

#------------------- Function for redhat distros ----------------------------------

gcloud_installs () {


	# Curl the buckets SDK for installations of 64bit OS
	curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-332.0.0-linux-x86_64.tar.gz
	tar xzvf google-cloud-sdk-332.0.0-linux-x86_64.tar.gz

	cd /home/$USER/Downloads/gcloud_intalls/google-cloud-sdk
	chmod +x install.sh
	./install.sh

	if [ $? eq 0 ]; then

	  echo "Init Time ...."
	  buckets init
	else
	  echo "Some went wrong ...."
	  exit 1
	fi

}

MenuWelcomeBoard
gcloud_intalls