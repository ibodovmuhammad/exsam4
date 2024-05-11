l1 = "She sells sea shells by the seashore.".split()
l2 = "s"
kalima=''
listi = []
for i in range(len(l1)):
    kalima=l1[i]
    kalima=kalima.lower()
    suma=0
    for j in kalima:
        if j==l2:
            suma+=1
    listi.append(suma)
    kalima=''
print(listi)
