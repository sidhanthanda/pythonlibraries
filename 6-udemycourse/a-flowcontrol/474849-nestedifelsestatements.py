GPA = float(input("Enter the GPA here: "))

if GPA >= 3.7:
    print("Your GPA is high enough")
    acceptyesorno = input("Were you accepted by a college?")
    if acceptyesorno == "Yes":
        print("Loan Approved")
    else:
        print("Loan Denied")
else:
    print("GPA is too low")
    print("Loan Denied")
