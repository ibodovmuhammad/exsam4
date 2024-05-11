def fun(tex):
    cum=0
    for i in tex:
        if i=="a":
            cum+=4
        if i=="e":
            cum+=3
        if i=="i":
            cum+=1
        if i=="o":
            cum+=0
        if i=="u":
            cum+=0

    print(cum)

text= input()
fun(text)
