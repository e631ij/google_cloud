import time
from gcp.setup.Config import *


# ------------------------------- GLOBAL VARIABLE DECLARED --------------------------------------------

def create_instance(instance_project, instance_name, zones):
	# The name of the instances to be created ( default and easy names do good)

	# The name of the image project
	project = InstanceProject[0]

	# The family of the image to be used
	familiar = Family[4]

	# The image of the instance to be added
	image = init_services("compute").images().getFromFamily(project=project, family=familiar)

	source_disk_image = image['selfLink']

	server_scripts = open(os.path.join(os.path.dirname(__file__), startup_scripts[0]), 'r').read()

	config = {

		"name": instance_name[5],
		"machineType": MachineType[1] % zones,
		"canIPForward": True,

		"disks": [{

			"boot": True,
			"autoDelete": True,
			"mode": mode[0],

			"initializeParam": {

				"sourceImage": '',
				"diskSizeGb": sizeGB[1],
				"sourceImage": source_disk_image

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
					"value": server_scripts
				}
			]
		}
	}

	return init_services().insert(project=instance_project, zone=zones, body=config).execute()


def start_instance(instance_project, instance_name, zones):
	# Check the status of the Instances with the list method/object
	check = init_services("compute").instances().list(project=instance_project, zone=zones)

	# Implement the user_input() method here

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


def stop_instance(instance_project, instance_name, zones):
	# Check the status of the Instances with the list method/object
	check = init_services().instances().list(project=InstanceProject, zone=zones)


	while check not in None:
		request = check.execute()

		for i in request['items']:
			# If the status of the instance is in terminate mode then exit with 0
			if i.items['name'] == instance_name and i.items['status'] == "TERMINATED":
				print("[+] %s is not running and is in TERMINATED State ... " % instance_name)
				exit(0)

			# If the status of the instance is in running state then stop instance
			elif i.items['name'] == instance_name and i.items['status'] == "RUNNING":
				request = init_services().stop(project=instance_project, zone=zones, instance=instance_name)
				action = request.execute()
				time.sleep(5)

			else:
				print("[-] Something went wrong ...... >><<<>>><<<>>>\n")
				exit(1)

			return action


def delete_instance(instance_project, instance_name, zones):
	# Checking instance status with the list method
	instance_status = init_services().instances().list(project=instance_project, zone=zones)

	while instance_status is not None:
		request = instance_status.execute()

		for i in request['items']:

			if i.items['name'] == instance_name and i.items['status'] == "RUNNING":

				print("[+] Instance is still RUNNING will proceed to stop %s" % instance_name)
				instance_stopping = init_services().instances().stop(project=instance_name, zones=zones,
				                                                     instance=instance_name)
				action_stop = instance_stopping.execute()
				time.sleep(7)
				print(action_stop)

			elif i.items['name'] == instance_name and i.items['status'] == "TERMINATED":

				print("[+] Deleting %s in %s location ...." % (instance_name, zones))
				instance_terminate = init_services().instances().delete(project=instance_project, zone=zones,
				                                                        instance=instance_name)
				action_terminate = instance_terminate.execute()

			else:

				print("[-] Something went wrong ..... ")
				exit(1)
			return action_terminate


def attach_disk(instance_project, instance_name, zones):
	# Checking the instance with the list method
	instance_status = init_services("compute").instances().list(project=instance_project, zone=zones)


	# Config of the disks
	config = {

		"disks": [{

			"boot": True,
			"autoDelete": True,
			"mode": mode[0],

			"initializeParam": {

				"sourceImage": '',
				"diskSizeGb": sizeGB[1],
			}

		}],

	}

	# Run it through a loop
	while instance_status is None:

		request = instance_status.execute()

		for i in request['items']:

			if i.items['name'] == instance_name and i.items['status'] == "RUNNING":

				instance_stopping = init_services().instances().stop(project=instance_project, zone=zones,
				                                                     instance=instance_name)
				action_stop = instance_stopping.execute()
				time.sleep(7)
				print(action_stop)

			elif i.items['name'] == instance_name and i.items['status'] == "TERMINATED":
				disk_attached = init_services().instances().attachDisk(project=instance_project, zone=zones,
				                                                       body=config)
				action_attached = disk_attached.execute()

			else:

				print("Something went wrong ...... ")

			return action_attached


def detach_disk(instance_project, instance_name,  zones, device_name):
	# Getting the status of the instances available or the list of instances
	check_instances = init_services().instances().list(project=instance_project, zone=zones)

	while check_instances not in None:
		request = check_instances.execute()

		for i in request['items']:

			if i.items['name'] == instance_name and i.items['status'] == "RUNNING":

				# Stop the instance if the instance is running

				instance_stop = init_services().instances().stop(project=instance_project, zone=zones,
				                                                 instance=instance_name)
				action_stop = instance_stop.execute()
				time.sleep(7.7)

				print("[+] Stopped %s: " % action_stop)
				exit(0)

			elif i.items['name'] == instance_name and i.items['status'] == "TERMINATED":

				print("[+] %s is now TERMINATED STATUS and will detach %s ..... " % (instance_name, device_name))
				instance_detach = init_services().instances().detachDisk(project=instance_project, zone=zones,
				                                                         instance=device_name)
				action_detach = instance_detach.execute()

			else:

				print(" Something went wrong ...... ")

			return action_detach
