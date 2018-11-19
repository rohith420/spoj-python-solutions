t=int(input())
while t>0:
    t-=1
    q=input()
    if q=='':
        q=input()
    
    sq=str(q)
    for i in range(0,len(sq)):
        if sq[i]=='=':
            j=i
    w=sq[0:j]
    e=sq[j+1:len(sq)]
    
    for p in range(0,len(w)):
        if w[p]=='+':
            k=p
    r=w[0:k]
    u=w[k+1:len(w)]
    
    if 'machula' in r: 
        print (int(int(e)-int(u)),'+',int(u),'=',int(e),sep=' ' )
    if 'machula' in u: 
        print (int(r),'+',int(int(e)-int(r)),'=',int(e),sep=' ' )
    if 'machula' in e: 
        print (int(r),'+',int(u),'=',int(int(r)+int(u)),sep=' ' )   
