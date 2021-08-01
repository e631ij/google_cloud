import logging
from colorama import Fore
from time import sleep
from gcp.themes.texts import *
from gcp.setup.Config import *


logging.basicConfig(level=logging.WARN)
logger = logging.getLogger()


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



def session_file_probe():

	aws_id = input("Enter ID: ")
	aws_secret = input("Enter Secret: ")
	regional = input("Enter Zone: ")

	try:
		if os.path.exists("aws_configure_file.ini"):
			print("[+] Config File created Already....")
			pass
		else:
			with open("aws_configure_file.ini", "wt") as session_file:
				session_file.write("; config.ini\n ; AWS Configuration file\n\n [default] \n aws_access_key_id = %s \n aws_secret_access_key = %s \n regional_zone = %s" % (aws_id, aws_secret, regional))
				session_file.close()
	except IOError as e:
		logger.error(e)
		return False
	return True



def main_menu():

	CC = "0"
	while CC == "0":

		# Improved version
		displays(MAIN_MENU)

		print("\n")
		CC = input(main_menu_text[0])

		if CC == "1":
			pass

		elif CC == "2":
			pass

		elif CC == "3":
			pass

		elif CC == "4":
			pass

		elif CC == "5":
			pass

		elif CC == "X" or CC == "x":
			quit_app()

		else:
			print(text_error[0])
			main_menu()

		return CC


def quit_app():
	print(Fore.YELLOW + "THANK YOU FOR USING LEFTSIDE.VISION")
	exit(0)




def main():

	shell("clear")

	if os.path.exists("agreement.txt"):
		main_menu()

	elif not os.path.exists("agreement.txt"):
		agreements()
		session_file_probe()
		main_menu()

	else:
		exit(0)




if __name__ == "__main__":
	# Running the Main
	main()