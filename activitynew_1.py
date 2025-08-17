medical_cause=input("did you have medical cause Y or N:   ")
attendance=int(input("enter the attendance of student"))
if (medical_cause=="Y"):
    print("allowed")
else:
    if (attendance  >=75):
        print ("allowed")
    else:
        print("not allowed")
