from numeroscomplejos import *

def position(V,p):
    raiz=0
    
    for i in V:
        raiz+=(i[0]**2)+(i[1]**2)
        
    prob =((V[p][0]**2)+(V[p][1]**2))/raiz
    
    return prob

def transition(V1,V2):
    total=(0,0)
    norm1=0
    norm2=0
    for z,y in zip(V1,V2):
        total=suma(total,producto(z,y))
        norm1+=(z[0]**2)+(z[1]**2)
        norm2+=(y[0]**2)+(y[1]**2)
        
    norm1f=norm1**(1/2)
  
    norm2f=norm2**(1/2)
    
    
    deno=norm1f*norm2f
  

    return((total[0]/deno),(total[1]/deno))
    


        
    
        
