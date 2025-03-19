#  Type definition in python from python version 3.8 onwards

a : int = 3
b : str = "Avi"
c : float = 4
print(a , type(a))
print(b , type(b))

def addNumber (a:int, b:int) -> int :
    return a+b

print(addNumber(a,c))