def  fiseq(a):
    if(a<2):
        return a
    else:
         return fiseq(a-1)+fiseq(a-2)
    

print(fiseq(15))
