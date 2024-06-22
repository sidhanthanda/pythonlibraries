def runMatch():
    selection = int(input("Press '1' for rectangular prism and '2' for sphere: "))
    
    match selection:
        
        case 1:
            print("You have selected rectangular prism")
            opsel = int(input("Press '1' for volume and '2' for surface area: "))
            if opsel == 1:
                    print("You have selected volume")
                    l = int(input("Enter your length: "))
                    w  = int(input("Enter your width: "))
                    h = int(input("Enter your height: "))
                    unit = input("Enter your unit: ")
                    volume = (l*w*h)
                    print(volume, unit)
            else:
                    print("You have selected surface area")
                    l = int(input("Enter your length: "))
                    w  = int(input("Enter your width: "))
                    h = int(input("Enter your height: "))
                    unit = input("Enter your unit: ")
                    surface_area = ((l*w) + (l*h) + (w*h))*2
                    print(surface_area, unit)
        
        case 2:
            print("You have selected sphere")
            opsel = int(input("Press '1' for volume and '2' for surface area: "))
            if opsel == 1:
                    print("You have selected volume")
                    pi = 3.14159262
                    r = int(input("Enter the radius: "))
                    unit = input("Enter your unit: ")
                    volume = 1.3333333333333333333333333333333333 * ((r**3) * pi)
                    print(volume, unit)
            else:
                print("You have selected surface area ")
                r = int(input("Enter radius: "))
                pi  = 3.14159262
                unit = input("Enter your unit: ")
                surface_area = (r**2) * 4 * pi
                print(surface_area, unit)
runMatch()