M = input("enter number")
N =list(M)
k = 0
b=0
while k < len(N)-1:
    if int(N[k]) < int(N[k+1]):
        N[k+1],N[k]=N[k],N[k+1]
    k+=1
k=len(N)
while k >=0:
   pass
 

