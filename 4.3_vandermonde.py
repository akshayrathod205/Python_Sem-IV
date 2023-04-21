import numpy as np

def vm(m,asc=True):
    ls=[]
    
    if asc==True:
        for item in m:
            ll=[]
            for i in range(len(m)):
                ll.append(item**i)
            ls.append(ll)
        print(np.array(ls))
    else:
        for item in m:
            ll=[]
            for i in range(len(m)-1,-1,-1):
                ll.append(item**i)
            ls.append(ll)
        print(np.array(ls))
        
a = vm([1,2,3,4,5])
