while True:
    try:
        user_int = int(input("Please choose an integer: "))
        break
    except :
        continue

if user_int % 2 == 0:
    print("even")
else:
    print("odd")