import numpy as np
import matplotlib.pyplot as plt

N=[]
t=[]
a=10
b=0.01
det_t=0.001
N.append(1000)
t.append(0)
end_time=0.3

for i in range(int(end_time/det_t)):
    tmp=N[i]+(a*N[i]-b*N[i]*N[i])*det_t
    N.append(tmp)
    t.append(det_t*(i+1))
    print (t[-1],N[-1])
    
    
   
plt.figure(figsize=(8,6)) 
plt.plot(t,N,label="N(t)",color="black",linewidth=1)
plt.plot([0,1.0],[a/b,a/b],label='a/b : '+str(a/b),color='blue',linewidth=1,linestyle="--")
plt.xlabel("t")   
plt.ylabel("N")  
plt.title("a=10,b=0.01,N(0)=1000") 
plt.axis([0,0.3,500,1500])
plt.legend()  
plt.show()  