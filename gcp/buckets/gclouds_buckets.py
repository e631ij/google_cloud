from gcp.setup.Config import *
import logging
from google.api_core.exceptions import *

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()


def create_buckets(bucket_name, location_zone="US-WEST1"):

	try:
		bucket = init_bucket_connect().bucket(bucket_name)
		bucket.service = "COLDLINE"

		if bucket:
			request = init_bucket_connect().create_bucket(bucket, location=location_zone)
			print("\nBucket: {}".format(request.name))
			print("Bucket Location: {}".format(request.location))
		else:
			print("something went wrong")
	except ClientError as e:
		logger.error(e)
		return False
	return True, True


def list_buckets():

	try:
		# Make an authenticated API request
		buckets = init_bucket_connect().list_buckets()

		for bucket in buckets:
			print("\nID: {}".format(bucket.id))
			print("Name: {}".format(bucket.name))
			print("Storage Class: {}".format(bucket.storage_class))
			print("Location: {}".format(bucket.location))
			print("Location Type: {}".format(bucket.location_type))
			print("Cors: {}".format(bucket.cors))
			print("Default KMS Key Name: {}".format(bucket.default_kms_key_name))
			print("Metageneration: {}".format(bucket.metageneration))
			print("Time Created: {}".format(bucket.time_created))
			print("Retention Policy Locked: {}".format(bucket.retention_policy_locked))
			print()

	except ConnectionError as e:
		logger.error(e)
		return False
	return True



def delete_buckets(bucket_name):

	try:
		find_buckets = init_bucket_connect().get_bucket(bucket_name)
		if find_buckets:
			find_buckets.delete()
		else:
			print("{} not found in the .... ".format(bucket_name))
	except ClientError as e:
		logger.error(e)
		return False
	return True


def show_buckets():

	# Make an authenticated API request
	buckets1 = init_bucket_connect().list_buckets()

	for bucket in buckets1:
		print("\nBucketName: {}".format(bucket.name))


def get_bucket_info(bucket_name):

	list_buckets()
	buckets = init_bucket_connect().list_buckets()

	while True:
		action_buckets = init_bucket_connect().get_bucket(bucket_name)

		if action_buckets.name == bucket_name:
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


def list_blobs(bucket_name):



	try:
		print("[+] Getting blobs from %s " % bucket_name)
		blobs = init_bucket_connect().list_blobs(bucket_name)
		for blob in blobs:
			print("\n" + blob.name)

	except ClientError as e:
		return False
	return True


def upload_object(bucket_name, local_filename, upload_to_blob):

	list_buckets()

	try:

		bucket = init_bucket_connect().bucket(bucket_name)
		blob = bucket.blob(upload_to_blob)
		blob.upload_from_filename(local_filename)

		print("BucketName: {}\nBlob:  {}".format(bucket_name, upload_to_blob))

	except ClientError as e:
		logger.error(e)
		return False
	return True


def download_object(bucket_name, local_filename, download_from_blob):

	try:
		bucket = init_bucket_connect().bucket(bucket_name)
		blob = bucket.blob(download_from_blob)
		blob.download_to_filename(local_filename)

		print("BucketName: {}\nBlob: {}".format(bucket_name, download_from_blob))

	except ClientError as e:
		logger.error(e)
		return False
	return True



def update_object_class(bucket_name, blob_name, new_blob_class):


	try:
		bucket = init_bucket_connect().bucket(bucket_name)
		blob = bucket.blob(blob_name)
		blob.update_object_class(new_blob_class)

		print("Blob Object Class {} is has now changed to  {}".format(bucket_name, new_blob_class))

	except ClientError as e:
		logger.error(e)
		return False
	return True


def delete_blob(bucket_name, blob_name):

	list_buckets()
	try:
		bucket = init_bucket_connect().bucket(bucket_name)
		blob = bucket.blob(blob_name)
		blob.delete()

		print("\nDeleted Blob: {}".format(blob_name))

	except ClientError as e:
		logger.error(e)
		return False
	return True
