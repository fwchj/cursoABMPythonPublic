
import random as rd

def ir_al_centro(a,b,mindiff=0.0001,iter=1):
    if(abs(a-b)>mindiff):
        c = rd.uniform(min(a,b),max(a,b))
        print("%s) [%12.8f , %12.8f] => %12.8f" % (iter,a,b,c)) 
        newa = rd.choice([a,b])
        iter  +=1
        ir_al_centro(newa,c,mindiff,iter)
        
    
ir_al_centro(1,500,mindiff=0.00000001)

