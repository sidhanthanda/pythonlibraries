selection = int(input("Press '1' for rectangular prism and '2' for sphere: "))

def calculate_volume(l, w, h):
        volume_calc = l * w* h
        return  volume_calc




if selection == 1:
    print("You have selected rectangular prism")
    opsel = int(input("Press '1' for volume and '2' for surface area: "))
    if opsel == 1:
        print("You have selected volume")
        l = int(input("Enter your length: "))
        w  = int(input("Enter your width: "))
        h = int(input("Enter your height: "))
        unit = input("Enter your unit: ")
        volume = calculate_volume(l, w, h)
        print(volume, unit)

else selection == 2:
     print("You have selected sphere")
     opsel = int(input("Press '1' for volume and '2' for surface area:"))
     if opsel == 1:
          print("You have selected volume")