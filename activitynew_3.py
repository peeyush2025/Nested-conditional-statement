print("select your ride")
print("1. bike")
print("2. car")
choice=int(input("enter your choice"))
if choice==1:
    print("what type of bike ")
    print("1. scooty\n")
    print("2. scooter\n")
    choice2=int(input("enter your choice2"))
    if choice2==1:
        print("scooty")
    else:
        print("scooter")
elif (choice==2):
    print("what type of car")
    print("1. XUV\n")
    print("2. sedan\n")
    choice3=int(input("enter your choice2"))
    if choice3==1:
        print("XUV")
    else:
        print("sedan")
else:
    print("invalid")
    