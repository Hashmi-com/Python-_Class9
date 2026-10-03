UI = float(input("Please enter a number"))

if UI == 0:
    print("This is neutral")
elif UI > 0:
    print("This is positive")
    if UI % 2 == 0:
        print("This is even")
    else:
        print("This is odd")
else:
    print("This is negitive")
    if UI % 5 == 0:
        CUI = UI / 5
        print(f"This is divisable by 5 the answer is {CUI}")
    else:
        print("This is not divisible by 5 ")
       