doggies ="golden_foof, rottweiller, corso, boerboel, malinois"

# for character  in doggies:
#     print(character)

dog_array = doggies.split(",")
count = 0

for word in dog_array:
    print(word.strip(" "))    
    count += 1
    print(count)