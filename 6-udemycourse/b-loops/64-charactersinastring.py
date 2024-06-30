user_input = input("Enter the input here: ")
counter= 0 

for letter in str(user_input):
    print(letter)
    counter += 1

print("The word you entered was", user_input)
print("It had",counter, "letters in it.")