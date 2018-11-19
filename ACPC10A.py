while 1:
    
    t=list(map(int,input().rstrip().split()))
    if int(t[0])==0 and int(t[1])==0 and int(t[2])==0 :
        i=0
        break
    if int(t[1])-int(t[0])==int(t[2])-int(t[1]) :
        print("AP",int(t[2])+(int(t[1])-int(t[0])),sep=' ')
    if (t[1])*(t[1])==(t[2])*(t[0]) :
        print("GP",int(t[2]*(t[1]/t[0])),sep=' ')
