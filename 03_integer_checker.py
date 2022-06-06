def num_check (question, low):
    valid = False
    while not valid:

        error = "please enter an integer that is more than "
        "(or equal to) {}".format(low)

        try:
            
            #ask user to enter a number
            response = int(input(question))
            
            # check number is more than zero
            if response > low:
                return response
            
            #outputs error if input is invalid
            else:
                print(error)
                print() 

        except ValueError:
            print(error)