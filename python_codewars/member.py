N = [(12,33),(76,8),(13,5)]
OutPut = []
for tuplee in N:
    if tuplee[0] >= 55 and tuplee[1] >=7:
        OutPut.append('Senior')
    else:
        OutPut.append('Open')
print(OutPut)
print(N)

