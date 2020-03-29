############# Ask the user for an integer
### If it is an even number, print "even"
### If it is an odd number, print "odd"
### If it is not an integer (e.g. character or decimal #), continue asking the user for an input

### THIS PROGRAM SHOULND'T CRASH UNDER THESE CIRCUMSTANCES:
# The user enters an alphabet
# The user enters a decimal number
# The user enters a non numeric character
# The user enters a negative number

# For example, if the user enters "a", the program should ask the user to try again and enter an integer

# Topic: conditionals, user input, loops

# Hint: You can use the try except:

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        user_int = int(input("Please choose an integer: "))
    except :
        # print("Sorry, I didn't understand that.")
        # #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if user_int % 2 == 0:
    print("even")
else:
    print("odd")