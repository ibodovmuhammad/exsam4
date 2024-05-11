a=input()
cum=0

for i in range(len (a)):
    cum = cum + int(a[i])

if int(a)%cum ==0 :
    print("YES")

else:
    print("NO")
