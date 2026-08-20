gpa = float(input("Enter your GPA: "))
institute_approval = input("Approved or Not Approved ")

if gpa >= 3.7:
    if institute_approval == "Approved":
        print("Your addmission is Approved")
    else:
        print("Your addmission is not Approved")
else:
    print("Your GPA is not Approved")