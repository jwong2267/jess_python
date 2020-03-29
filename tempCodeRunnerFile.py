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