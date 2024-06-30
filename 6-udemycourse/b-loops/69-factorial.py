def factorial(n):  
    result = 1 
    for item in range(n, 1, -1):
        result *= item
    return result
 
print(factorial(3))  
print(factorial(4)) 
print(factorial(5))  
