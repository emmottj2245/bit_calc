# check user choice is 'integer', 'text' or 'image'
from typing_extensions import dataclass_transform


def user_choice():

    valid = False
    while not valid:

        response = "file type (integer / text / image): ".lower()

        if response == "text" or response == "t":
            return response

        else:
            print("please choose a valid file type!")
            print()


# main routine goes here 
data_type = user_choice()