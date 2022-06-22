# puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():

    statement_generator("instructions / information", "=")
    print()
    print("please choose a data type (image/text/ integer)")
    print()
    print("this program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). for text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""
    
# main routine 
instructions()