import logging
from colorama import Fore
from time import sleep
from gcp.themes.texts import *
from gcp.setup.Config import *
from gcp.buckets.gclouds_buckets import *

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()



def bucket_menu():
	shell("clear")

	# Displays the MENU
	displays(BUCKET_MENU)

	CC = input(main_menu_text[0])

	# Picking the options
	if CC == "1":
		bucket_submenu()

	elif CC == "x" or CC == "X":
		quit_app()

	else:
		print(text_error)
		bucket_menu()

	return CC


def bucket_submenu():
	displays(SUB_BUCKET_MENU)
	CC = input(main_menu_text[0])

	# Picking the options
	if CC == "1":
		list_buckets()
		sleep(3)
		bucket_submenu()

	elif CC == "2":
		create_buckets(choices(bucket_text_words[0]))
		sleep(3)
		bucket_submenu()

	elif CC == "3":
		upload_object(choices(bucket_text_words[0]),
					  choices(bucket_text_words[2]),
					  choices(bucket_text_words[4]))
		sleep(3)
		bucket_submenu()

	elif CC == "4":
		download_object(choices(bucket_text_words[0]),
						choices(bucket_text_words[3]),
						choices(bucket_text_words[4]))
		sleep(3)
		bucket_submenu()

	elif CC == "5":
		delete_buckets(choices(bucket_text_words[0]))
		sleep(5)
		bucket_submenu()

	elif CC == "6":
		delete_blob(choices(bucket_text_words[0]),
					choices(bucket_text_words[5]))
		sleep(5)

	elif CC == "7":
		update_object_class(choices(bucket_text_words[0]),
							choices(bucket_text_words[4]),
							choices(bucket_text_words[5]))
		sleep(5)
		bucket_submenu()


	elif CC == "8":
		list_blobs(choices(bucket_text_words[0]))

		sleep(5)
		bucket_submenu()

	elif CC == "9":
		delete_blob(choices(bucket_text_words[0]),
					choices(bucket_text_words[4]))

		sleep(5)
		bucket_submenu()

	elif CC == "10":
		get_bucket_info(choices(bucket_text_words[0]))

	elif CC == "B" or CC == "b":
		bucket_menu()

	else:
		print(text_error)
		bucket_menu()

	return CC


def agreement_check_file():

	try:
		if not os.path.exists("agreement.txt"):
			with open("agreement.txt", "wt") as agree_file:
				agree_file.write("; YES TO AGREEMENT")
				agree_file.close()

		else:
			#print("[+] Agreement File created Already....")
			pass

	except IOError as e:
		logger.error(e)
		return False
	return True



def agreements():

	print(Fore.RED + menu_agreement)

	agreementPolicies = input("Enter (Y|y|N|n): ")
	if agreementPolicies == "Y" or agreementPolicies == "y":
		agreement_check_file()
		sleep(3)


	elif agreementPolicies == "N" or agreementPolicies == "n":
		quit_app()

	else:
		print("Enter the write OPTIONS PLEASE .....")
		agreements()

	return True


def quit_app():
	print(Fore.YELLOW + "THANK YOU FOR USING LEFTSIDE.VISION")
	exit(0)




def main():

	shell("clear")

	if os.path.exists("agreement.txt"):
		bucket_menu()

	elif not os.path.exists("agreement.txt"):
		agreements()
		bucket_menu()

	else:
		exit(0)




if __name__ == "__main__":
	# Running the Main
	main()