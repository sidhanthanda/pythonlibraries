st = input("What 3D shape do you want to use? Press '1' for rectangular prism and '2' for sphere: ")

def decide_operation():
    q = "What operation do you want to do? Press '1' for volume and '2' for surface area"
    return q
    
def enter_sizes(l, w, h):
    vf = l*w*h
    return vf 
    

q = decide_operation()

ip= input(q)

l = int(input("Enter length: "))
w = int(input("Enter width: "))
h = int(input("Enter height: "))


vf = enter_sizes(l, w, h)
va = vf