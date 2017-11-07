b,p=list(' '*9),'xo'
while 1:
    print'\033c'+'\n-+-+-\n'.join(['|'.join(b[0:3]),'|'.join(b[3:6]),'|'.join(b[6:9])])
    if (list('x'*3) or list(' '*3)) in [b[0:3],b[3:6],b[6:9],b[0::3],b[1::3],b[2::3],b[0::4],[b[2],b[4],b[6]]]:print'win';break
    if ' ' not in b:print'cats';break
    n=input()
    if b[n]==' ':b[n],p=p[0],p[::-1]
