number = int(input("enter number:"))
def sqrt(number:int):
    return (True if number >= 0 and (number**(1/2)*10)%10 == 0 else False)
print(sqrt(number))

