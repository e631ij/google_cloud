from gcp.themes.texts import *
import main
from time import sleep
from gcp.setup.Config import *
from gcp.buckets.gclouds_buckets import *


def bucket_menu():
    
    shell("clear")

    # Displays the MENU 
    displays(BUCKET_MENU)
    
    CC = input(main_menu_text[0])

    # Picking the options
    if CC == "1":
        bucket_submenu()

    elif CC == "B" or CC == "b":
        main.main_menu()

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
        main.main_menu()

    else:
        print(text_error)
        bucket_menu()

    return CC


bucket_menu()