while True:
    try:
        user_int = int(input("Please choose an integer: "))
    except :
        continue
    else:
        break
if user_int % 2 == 0:
    print("even")
else:
    print("odd")