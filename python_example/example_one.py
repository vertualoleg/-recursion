N = [x for x in range(int(input("enter number:")))]
def summa(N,b=0,i=0):
    if i > len(N)-1:
        return print(b)
    b+=N[i]
    summa(N,b,i+1)
summa(N)

