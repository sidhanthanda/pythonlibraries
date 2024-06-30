all_low = "there are no capital letters here"
print(all_low.upper())  
print(all_low)  

all_cap = "ALL CAPS HERE"
print(all_cap.lower())
print(all_cap) 

print(all_cap.islower())  
print(all_low.islower())  

print("CAPITAL WORDS".lower().isupper())

print("1454152415".isalpha())
print("hello".isalpha())

print("h3ll0".isalnum())
print("2405612".isalnum())

print("2405612".isdecimal())
print("hello my name is ".isdecimal())

print("          ".isspace())
print("nospaces".isspace())

print("The Last Stand".istitle())
print("idshjahdskjsd".istitle())

riddle_answer = input("How much wood would a woodchuck chuck if a woodchuck could chuck wood?: ")

if riddle_answer.startswith("A woodchuck would chuck as much wood as a woodchuck could chuck if a ") and riddle_answer.endswith("woodchuck could chuck wood"):
    print("Correct!")
else:
    print("WRONG!")

print("".join(["this ", "word is ", "random"]))

print("Some, Random, Words, I, Thought, Off".split())