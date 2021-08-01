#!/bin/bash

SUDO=`whoami`



 if [ $SUDO != "root" ];
 then

	echo "Need to be root "
	exit 0
 fi


#apt-get install apt-transport-https ca-certificates gnupg

#echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

#curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

#sudo apt-get update && sudo apt-get install google-cloud-sdk

curl https://sdk.cloud.google.com | bash

GOOGLE_PACKAGES="apt-transport-https ca-certificates google-cloud-datastore gnupg google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-python-extras google-cloud-sdk-app-engine-java google-cloud-sdk-app-engine-go google-cloud-sdk-bigtable-emulator google-cloud-sdk-cbt google-cloud-sdk-cloud-build-local google-cloud-sdk-datalab google-cloud-sdk-datastore-emulator google-cloud-sdk-firestore-emulator google-cloud-sdk-pubsub-emulator kubectl"

for package in $GOOGLE_PACKAGES
do
	echo "[+] Installing Packages ......."
	apt-get -y update && apt-get -y install $package 
done

echo "[+] Installation Completed ..... "






