def rev(a):
    if len(a) == 0:
        return a
    else:
        return rev(a[1:]) + a[0]


b=input()
print(rev(b)) 







