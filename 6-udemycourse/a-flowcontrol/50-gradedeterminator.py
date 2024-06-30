score = (input("Enter score here: "))
 

if int(score) >= 90 and int(score) <= 100:
    print("The score is", score, ",or an A.")
else:
    if int(score) >= 80 and int(score) <= 90 :
        print("The score is", score, ",or a B.")
    else:
        if int(score) >= 70 and int(score) <= 80 :
            print("The score is", score, ",or an C.")
        else:
            if int(score) >= 60 and int(score) <= 70 :
                print("The score is", score, ",or an D.")
            else:
                if int(score) >= 50 and int(score) <= 60:
                    print("The score is", score, "or an F")
                else:
                    if int(score) > 100:
                        print("Invalid score.")
                    else:
                        if int(score)<=50:
                            print("Your score was so low we don't have a letter grade for it. Git gud!")