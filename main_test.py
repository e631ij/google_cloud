# This is a sample Python script.
import os
from gcp.setup.Config import Family, startup_scripts, sizeGB
from gcp.setup.Config import mode, scopes
import httplib2
from googleapiclient import discovery
from gcp.setup.Config import email, google_services, creds
from oauth2client.service_account import ServiceAccountCredentials
from google.cloud import storage
from time import time
from gcp.setup.Config import ProjectID


def init_storage():
    storage_conn = storage.Client()

    return storage_conn


def create_buckets(name, location_zone="US-WEST1"):
    service = init_storage()
    bucket = service.bucket(name)
    bucket.service = "COLDLINE"
    request = service.create_bucket(bucket, location=location_zone)

    print("Bucket: {}".format(request.name))
    print("Bucket Location: {}".format(request.location))

    return request


# Init Connection
def init_services(service):
    creds_connection = ServiceAccountCredentials.from_json_keyfile_name(creds, scopes)

    connection_service = discovery.build(service, "v1", http=creds_connection.authorize(httplib2.Http()))

    return connection_service


def list_roles_errors(name_project=None):
    iam_services = google_services[6]

    name_project = ProjectID

    parent = "projects/" + name_project

    request = iam_services.roles().list(parent=parent)

    while True:

        action_request = request.execute()

        for i in action_request.get('roles', []):
            print(i)

        request = iam_services.projects().roles().list_next(previous_request=request, previous_response=i)

        if request is None:
            break


def write_pem(self):
    username = "USER=whoami"

    current_dir = "pwd"
    filepath = "/home/$USER/Downloads"
    os_filepath = "if [ -d /home/$USER/Downloads ]; then cd /home/$USER/Downloads else mkdir -p /home/$USER/Downloads && cd /home/$USER/Downloads"

    os.system(username + current_dir + filepath + os_filepath)

    with open(self.request, "r") as f:
        f.write()


def create_bucket_error_code(name, location_zone="US-WEST1"):
    service = init_storage()
    bucket = service.bucket(name)
    bucket.service = "COLDLINE"
    request = service.create_bucket(bucket, location=location_zone)

    while request not in None:
        # CBTR
        if request == 1:
            print("Conflict ,.. PLease enter a diff name with lowercase ...")
        else:

            print("\nBucketName: {}".format(request.name))
            print("BucketLocation: {}".format(request.location))

    return request


def show_buckets():
    # Explicitly use service account credentials by specifying the private key
    service = init_storage()

    # Make an authenticated API request
    buckets = service.list_buckets()

    for bucket in buckets:
        print("\n" + bucket.name)


def list_blobs():
    # Explicitly use service account credentials by specifying the private key
    service = init_storage()

    show_buckets()

    user_input = input("\nEnter S3 Name: ")
    # Make an authenticated API request
    # if user_input == show_buckets().bucket.name:
    blobs = service.list_blobs(user_input)
    for blob in blobs:
        print("\n" + blob.name)


def get_bucket_info(bucket_name):
    connect = init_storage()

    buckets = connect.list_buckets()

    for buck in buckets:
        print("\n" + str(buck))

    while True:
        action_buckets = connect.get_bucket(bucket_name)

        if action_buckets.name == bucket_name:
            print("\nBucketName: {}\n".format(bucket_name))
            print("ID: {}".format(action_buckets.id))
            print("Name: {}".format(action_buckets.name))
            print("Storage Class: {}".format(action_buckets.storage_class))
            print("Location: {}".format(action_buckets.location))
            print("Location Type: {}".format(action_buckets.location_type))
            print("Cors: {}".format(action_buckets.cors))
            print("Default KMS Key Name: {}".format(action_buckets.default_kms_key_name))
            print("Metageneration: {}".format(action_buckets.metageneration))
            print("Time Created: {}".format(action_buckets.time_created))
            print("Retention Policy Locked: {}".format(action_buckets.retention_policy_locked))
            print("Labels:")
            print(action_buckets.labels)

        else:

            print("{} not found in the Lists ..... ")
        return action_buckets


def list_buckets():
    # Explicitly use service account credentials by specifying the private key
    service = init_storage()

    # Make an authenticated API request
    buckets = service.list_buckets()

    for bucket in buckets:
        print(bucket.name)


def upload_object(bucket_name, local_filename, upload_to_blob):
    service = init_storage()

    show_buckets()

    bucket = service.bucket(bucket_name)
    blob = bucket.blob(upload_to_blob)
    blob.upload_from_filename(local_filename)

    print("BucketName: {} "
          "UploadFolder: {}".format(bucket_name, upload_to_blob))



def download_object(bucket_name, local_filename, download_from_blob):
    service = init_storage()

    bucket = service.bucket(bucket_name)
    blob = bucket.blob(download_from_blob)
    blob.download_to_filename(local_filename)

    print("{} {}".format(bucket_name, download_from_blob))


def delete_blob(bucket_name, blob_name):
    service = init_storage()

    bucket = service.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print("Deleted Blob: {}".format(blob_name))


# get_bucket_info("leftside_vision")

# list_buckets()

# uploadObject("codesoul", "/home/xza1/Documents/Scraps/psalm75", "psalm758")

# delete_blob("codesoul", "psalm758")

def start_instance(InstanceProject, zones):
    # Check the status of the Instances with the list method/object
    check = init_services().instances().list(project=InstanceProject, zone=zones)

    # Implement the user_input() method here
    instance_name = input("Enter Instance Name: ")

    while check not in None:
        request = check.execute()

        for i in request['items']:

            # if the status of the instance is in running mode exit with a 0
            if i.items['status'] == "RUNNING" and i.items['name'] == instance_name:
                print("[+] %s is current running " % instance_name)
                exit(0)

            # elif execute the action to start the instance and also take some time for recovery
            elif i.items['status'] == "TERMINATED" and i.items['name'] == instance_name:

                request = init_services().start(project=InstanceProject, zone=zones, instance=instance_name)
                print("[+] Starting %s now .... " % instance_name)
                start_action = request.execute()
                time.sleep(5)

            else:

                print("[-] Something went wrong ...... >><<<>>><<<>>>\n")
                exit(1)
            return start_action


def check_0(instance_project):
    # The name of the image project

    project = instance_project

    # The family of the image to be used
    familiar = Family[4]

    image = init_services().images().getFromFamily(project=project, family=familiar)
    action = image.execute()
    print(action)


def create_instance():
    # The name of the instances to be created ( default and easy names do good)
    # instance_name = input("Enter the instance Name: ")

    familiar = Family[4]
    project = "ubuntu-os-cloud"
    api_version = "v1"
    instance_name = "instance-7"
    # project_url = "%/%/projects/%" % (scopes[3], api_version, ProjectID)
    # image_project_url = "%/%/projects/%" % (scopes[3], api_version, Family[4])
    image_name = "ubuntu-minimal-1804-bionic-v20210416"
    MachineType = "zones/us-west1-a/machineTypes/e2-standard"

    # The name of the image project

    config = {

        "name": instance_name,
        "machineType": MachineType,
        "canIPForward": True,

        "disks": [{

            "boot": True,
            "autoDelete": True,
            "mode": mode[0],

            "initializeParam": {

                "diskSizeGb": sizeGB[1],
                # "sourceImage": "%s/global/images/%s" % (image_project_url, image_name)

            }

        }],

        'networkInterfaces': [{

            'network': 'global/networks/default',
            'accessConfigs': [

                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        'serviceAccounts': [{
            'email': email,
            'scopes': [

                scopes[3],
                scopes[9]
            ]
        }],

        "metadata": {

            "items": [

                {
                    "key": "startup_scripts",
                    "value": startup_scripts[0]
                }
            ]
        }
    }

    # The family of the image to be used

    # The image of the instance to be added

    return init_services().instances().insert(project=project, zone="us-west1-a", body=config).execute()


# ------------------------------------------------------------------------------------------------------------



# IAM_USER.create_iam_user("ronin1")
# IAM_USER.delete_iam_user("ronin1")
# IAM_USER.create_access_key("ronin1")
# IAM_USER.delete_key("huduee")
# IAM_USER.getKeys("ronin1", 20)
# IAM_USER.getUsers(13)
# create_sa("wrecker33", "wrecker33")
# list_sa()
# delete_sa(input("Enter the email of Service Account to be deleted: "))
# list_roles()
# create_saKey("wrecker33@leftside-48941.IdentityAccessManager.gserviceaccount.com")
# create_buckets("codesoul2", "EUROPE-CENTRAL2")
# create_instance()
# check_instagramAPI()
# create_sa("wrecker33", "wrecker33")
# list_sa()
# delete_sa(input("Enter the email of Service Account to be deleted: "))
# list_roles()
# create_saKey("wrecker33@leftside-48941.IdentityAccessManager.gserviceaccount.com")
# create_buckets("codesoul2", "EUROPE-CENTRAL2")
# create_instance()
# check_instagramAPI()
# boat()
# delete_VPCID3()
# create_VPCID3()
# createSecurityGroup()
# keys101()
# keys102()
# createKeyPairs("tester6")
# startInstance()
# createInstance()
# getKeys()
# deleteKeyPairs("eetdrumoro")
# createKeyPairs("tester55")
# startInstance()
# createInstance()
# checkkeys1("tester6")
# describeSecurityGroups()
# makeSecurityGroups("tester6")
# vpcCreation()
# createInstance()
# getInstances()
# stop_Instances("i-037cda0f0391a2440")
# start_Instances("i-037cda0f0391a2440")
# stop_Instances("i-037cda0f0391a2440")
# start_Instances("i-037cda0f0391a2440")
# send_message("tester88393")
# getAcl()
# downloadAws("tester3390", "Ydl_links.txt", "/home/xza1/Downloads/Ydl_links.txt")
# upload_object("/home/xza1/Documents/Loads1/Ydl_links.txt", "tester3390", "Ydl_links.txt")
# testExists("tester1339099")
