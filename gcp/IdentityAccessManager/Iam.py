#!/bin/env python3
from gcp.setup.Config import *


def create_sa(name, display_name):

	body = {

		"accountId": name,
		"serviceAccount": {

			'displayName': display_name
		}
	}

	request = init_services("IdentityAccessManager").projects().serviceAccounts().create(

		name='projects/' + ProjectID,
		body=body
	).execute()

	print("Create Service Account: " + request['email'])
	return request



def list_sa(projectID):
	# Using project ID's for UUID

	request = init_services("IdentityAccessManager").projects().serviceAccounts().list(

		name='projects/' + projectID,

	).execute()

	while True:

		for i in request['accounts']:
			print("\nName: %s" % i['name'],
			      "\nEmail: %s\n" % i['email']
			      )

		return request



def delete_sa(email):

	list_sa()

	request = init_services("IdentityAccessManager").projects().serviceAccounts().delete(

		name="projects/-/serviceAccounts/" + email

	).execute()

	print("Deleted ServiceAccount: " + email)



def enable_sa(email):

	list_sa()

	request = init_services("IdentityAccessManager").projects().serviceAccounts().enable(

		name="projects/-/serviceAccounts/" + email

	).execute()

	print("Deleted ServiceAccount: " + email)



def disable_sa(_email_):

	list_sa()

	request = init_services("IdentityAccessManager").projects().serviceAccounts().disable(

		name="projects/-/serviceAccounts/" + _email_

	).execute()

	print("Deleted ServiceAccount: " + email)



"""
			IdentityAccessManager ROLES AND PERMISSION 
"""


def list_rolesKeys():
	for i in Roles:
		print("\n" + i)



def list_roles():
	roles_ = ["ComputeEngine",
	          "IdentityAccessManager",
	          "ServiceAccount",
	          "Recommender",
	          "ResourceManage",
	          "CloudStorage",
	          "VPC_Access",
	          "KMS"]

	list_rolesKeys()
	Empty_list = []
	user_input = input("\nEnter Option: ")
	for i in roles_:
		if user_input in i:

			Empty_list.append(i)
			for k in Roles[Empty_list[0]]:
				print("\nROLES: " + k)



def create_saKey(self, serviceAccount):

	name_resource = "projects/" + ProjectID + "/serviceAccounts/" + serviceAccount

	request = init_services("IdentityAccessManager").projects().serviceAccounts().keys().create(

		name=name_resource

	).execute()

	print("{}".format(self, request))



def write_pemfile(self, filename):
	import subprocess

	username = "USER=whoami"

	current_dir = "pwd"
	filepath = "/home/$USER/Downloads"
	os_filepath = "if [ -d /home/$USER/Downloads ]; then cd /home/$USER/Downloads else mkdir -p /home/$USER/Downloads && cd /home/$USER/Downloads"

	subprocess.run(username + current_dir + filepath + os_filepath)

	with open(self.request, "r") as f:
		print(f)


# ---------------------------------------------------------------------------------------------------------------------
def list_keys(email, myKey):

	request = init_services("IdentityAccessManager").projects().serviceAccounts().delete(

		name="projects/" + ProjectID + "/serviceAccounts/" + email + "/keys/" + myKey
	).execute()

	return request



def delete_keys():


	myKey = str("0305c14c535c714a7a7dd63b56ab91a16f5bc814")
	request = init_services("IdentityAccessManager").projects().serviceAccounts().delete(

		name="projects/" + ProjectID + "/serviceAccounts/" + email + "/keys/" + myKey
	).execute()

	return request
