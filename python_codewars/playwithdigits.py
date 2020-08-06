N = int(input("enter number:"))
#main program
def dig_pow(N,p:int):
    summ=0
    for elem in str(N):
        summ += int(elem)**p
        p+=1
    k = summ / N
    return return k if k >=1 else return -1
dig_pow(N,3)

