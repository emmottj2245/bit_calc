# check user choice is 'integer', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:
        
        #ask user for choice and change response to lowercase
        response = input("file type (integer / text / image): ").lower()

        #if they choose "t" or "text", return "text"
        if response == "text" or response == "t":
            return "text"

        else:
            # if response is not valid, output an error
            print("please choose a valid file type!")
            print()


# main routine goes here 
data_type = user_choice()
print("you choose", data_type)

print()