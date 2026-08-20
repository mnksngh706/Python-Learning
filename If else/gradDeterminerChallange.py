gradingScale = float(input("Enter your grading scale: "))
if gradingScale >= 90:
    print("Your grading scale is A " +str(gradingScale))
else:
    if gradingScale >= 80:
        print("Your grading scale is B")
    else:
        if gradingScale >= 70:
            print("Your grading scale is C")
        else:
            if gradingScale >= 60:
                print("Your grading scale is D")
            else:
                print("Your grading scale is F")