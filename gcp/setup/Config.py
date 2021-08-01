import os
import sys
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient import discovery
import httplib2
from google.cloud import storage



def init_bucket_connect():

	storage_connect = storage.Client()
	return storage_connect


def init_services(service):

	creds_connection = ServiceAccountCredentials.from_json_keyfile_name(creds, scopes)

	connection_service = discovery.build(service, "v1", http=creds_connection.authorize(httplib2.Http()))

	return connection_service


def displays(menu):
	for i in menu:
		print(i)


def shell(command):
	sh = os.system(command)
	return sh


def choices(user_input):
	return input(user_input)


# Ref: Python3 OOP Second Edition
def valid_inputs(input_string, valid_input):
	input_string += (" ({}) ".format(", ".join(valid_input)))
	response = input(input_string)
	while response.lower() not in valid_input:
		response = input(input_string)
	return response


# Scopes to be used for authentications
scopes = [

	"https://www.googleapis.com/auth/bigquery",
	"https://www.googleapis.com/auth/iam",
	"https://www.googleapis.com/auth/cloud-platform",
	"https://www.googleapis.com/auth/source.full_control",
	"https://www.googleapis.com/auth/compute",
	"https://www.googleapis.com/auth/datastore",
	"https://www.googleapis.com/auth/logging.write",
	"https://www.googleapis.com/auth/monitoring.write",
	"https://www.googleapis.com/auth/pubsub",
	"https://www.googleapis.com/auth/servicecontrol",
	"https://www.googleapis.com/auth/logging.write",
	"https://www.googleapis.com/auth/monitoring",
	"https://www.googleapis.com/auth/monitoring.write",
	"https://www.googleapis.com/auth/sqlservice.admin",
	"https://www.googleapis.com/auth/devstorage.full_control",
	"https://www.googleapis.com/auth/devstorage.read_write"

]

mode = [

	"READ_WRITE",
	"READ_ONLY"
]

sizeGB = [

	"25GB",
	"50GB",
	"100GB",
	"150GB"
]

Family = [

	"ubuntu-1604-lts",
	"ubuntu-1804-lts",
	"ubuntu-pro-1604-lts",
	"ubuntu-pro-1804-lts",
	"ubuntu-pro-2004-lts"
	"centos-7",
	"centos-8",

]

InstanceProject = [

	"ubuntu-os-cloud",
	"ubuntu-os-cloud",
	"ubuntu-os-cloud",
	"ubuntu-os-cloud",
	"ubuntu-os-cloud",
	"ubuntu-os-cloud",
	"centos-cloud",
	"centos-cloud",

]

MachineType = [

	"zones/%s/machineTypes/e2-micro",
	"zones/%s/machineTypes/e2-small",
	"zones/%s/machineTypes/e2-medium",
	"zones/%s/machineTypes/e2-standard"

]

Zones = {

	"europe1": [
		"europe-central1-a",
		"europe-central1-b",
		"europe-central1-c"],

	"europe2": [
		"europe-north2-a",
		"europe-north2-b",
		"europe-north2-c",

	],

	"europe3": [

		"europe-west3-a",
		"europe-west3-b",
		"europe-west3-c"
	],

	"northamerica1": [

		"northamerica-east1-a",
		"northamerica-east1-b",
		"northamerica-east1-c"
	],

	"asia1": [

		"asia-northeast1-a",
		"asia-northeast1-b",
		"asia-northeast1-c"

	],

	"asia2": [

		"asia-northeast2-a",
		"asia-northeast2-b",
		"asia-northeast2-c"

	],

	"asia3": [

		"asia-northeast3-a",
		"asia-northeast3-b",
		"asia-northeast3-c"

	],

	"asia4": [

		"asia-southeast1-a",
		"asia-southeast1-b",
		"asia-southeast1-c"

	]

}

# Environment variable for authentications
creds = os.environ[
	"GOOGLE_APPLICATION_CREDENTIALS"] = "/home/elias777/PycharmProjects/google_cloud/grams-321422-8e064676a60f.json"

startup_scripts = [

	"/home/eliaz777/PycharmProjects/google_cloud/cengine/GeneralStartupScript.sh",
	"/home/eliaz777/PycharmProjects/google_cloud/cengine/gengine_connect.sh"

]

email = ["el9-600@lunar-pact-320923.IdentityAccessManager.gserviceaccount.com"]


ProjectID = "grams-321422"

Roles = {

	"ComputeEngine": [

		"roles/compute.admin",
		"roles/compute.imageUser",
		"roles/compute.instanceAdmin",
		"roles/compute.instanceAdmin.v1",
		"roles/compute.loadBalancerAdmin",
		"roles/compute.networkAdmin",
		"roles/compute.networkUser",
		"roles/compute.networkViewer",
		"roles/compute.orgFirewallPolicyAdmin",
		"roles/compute.orgFirewallPolicyUser",
		"roles/compute.orgSecurityPolicyAdmin",
		"roles/compute.orgSecurityPolicyUser",
		"roles/compute.orgSecurityResourceAdmin",
		"roles/compute.osAdminLogin",
		"roles/compute.osLogin",
		"roles/compute.osLoginExternalUser",
		"roles/compute.packetMirroringAdmin",
		"roles/compute.packetMirroringUser",
		"roles/compute.publicIpAdmin",
		"roles/compute.securityAdmin",
		"roles/compute.storageAdmin",
		"roles/compute.viewer",
		"roles/compute.xpnAdmin",
		"roles/osconfig.guestPolicyAdmin",
		"roles/osconfig.guestPolicyEditor",
		"roles/osconfig.guestPolicyViewer",
		"roles/osconfig.patchDeploymentAdmin",
		"roles/osconfig.patchDeploymentViewer",
		"roles/osconfig.patchJobExecutor",
		"roles/osconfig.patchJobViewer",

	],

	"IdentityAccessManager": [

		"roles/IdentityAccessManager.securityAdmin",
		"roles/IdentityAccessManager.securityReviewer",
	],

	"ServiceAccount": [

		"roles/IdentityAccessManager.serviceAccountAdmin",
		"roles/IdentityAccessManager.serviceAccountCreator",
		"roles/IdentityAccessManager.serviceAccountDeleter",
		"roles/IdentityAccessManager.serviceAccountKeyAdmin",
		"roles/IdentityAccessManager.serviceAccountTokenCreator",
		"roles/IdentityAccessManager.serviceAccountUser",
		"roles/IdentityAccessManager.workloadIdentityUser",

	],

	"Recommender": [

		"roles/recommender.billingAccountCudAdmin",
		"roles/recommender.billingAccountCudViewer",
	],

	"ResourceManager": [

		"roles/resourcemanager.organizationAdmin",
		"roles/resourcemanager.organizationViewer",
		"roles/resourcemanager.projectIamAdmin",

	],

	"CloudStorage": [

		"roles/storage.admin",
		"roles/storage.hmacKeyAdmin",
		"roles/storage.objectAdmin",
		"roles/storage.objectCreator",
		"roles/storagetransfer.admin",
		"roles/storagetransfer.viewer",
		"roles/storagetransfer.user",
		"roles/storagetransfer.viewer",

	],

	"VPC_Access": [

		"roles/vpcaccess.admin",
		"roles/vpcaccess.user",
		"roles/vpcaccess.viewer"

	],

	"KMS": [

		"roles/cloudkms.admin",
		"roles/cloudkms.cryptoKeyDecrypter",
		"roles/cloudkms.cryptoKeyEncrypter",
		"roles/cloudkms.cryptoKeyEncrypterDecrypter",
		"roles/cloudkms.importer",
		"roles/cloudkms.publicKeyViewer",
		"roles/cloudkms.signer",
		"roles/cloudkms.signerVerifier",
	],

}

google_services = [

	'ai',
	'api-gateway',
	'compute',
	'container',
	'deployment-manager',
	'firebase',
	'IdentityAccessManager',
	'identity',
	'kms',
	'logging',
	'network-management',
	'cloudresourcemanager'
]
