import numpy as np
from pylab import *

x=[0]
y=[2]
vx,vy=3,3
time,i,dt=0,0,0.001
sdt=0.00001
velocity=[4]

while time<=50:
    X=x[i]+vx*dt
    Y=y[i]+vy*dt
    if Y>0 and Y<4:
        if X>=0:
            if Y<-X*4.0/3.0+4:
                x.append(X)
                y.append(Y)
                velocity.append(vx)
            else:
                x1=x[i]+vx*sdt
                y1=y[i]+vy*sdt
                if y1<-x1*4.0/3.0+4:
                    x.append(x1)
                    y.append(y1)
                    velocity.append(vx)
                else:
                    char1=-vx*0.28-vy*0.96                
                    char2=-vx*0.96+vy*0.28
                    vx=char1
                    vy=char2                
                    x.append(x[i]+vx*sdt)
                    y.append(y[i]+vy*sdt)
                    velocity.append(vx)
        if X<0:
            if Y<X*4.0/3.0+4:
                x.append(X)
                y.append(Y)
                velocity.append(vx)
            else:
                x2=x[i]+vx*sdt
                y2=y[i]+vy*sdt
                if y2<x2*4.0/3.0+4:
                    x.append(x2)
                    y.append(y2)
                    velocity.append(vx)
                else:
                    char3=-vx*0.28+vy*0.96
                    char4=vx*0.96+vy*0.28
                    vx=char3
                    vy=char4
                    x.append(x[i]+vx*sdt)
                    y.append(y[i]+vy*sdt)
                    velocity.append(vx)
    if Y>=4:
        x4=x[i]+vx*sdt
        y4=y[i]+vy*sdt
        if y4<4:
            x.append(x4)
            y.append(y4)
            velocity.append(vx)
        else:   
            vy=-vy
            x.append(x[i]+vx*sdt)
            y.append(y[i]+vy*sdt)
            velocity.append(vx)
    if Y<=0:
        x3=x[i]+vx*sdt
        y3=y[i]+vy*sdt
        if y3>0:
            x.append(x3)
            y.append(y3)
            velocity.append(vx)
        else:   
            vy=-vy
            x.append(x[i]+vx*sdt)
            y.append(y[i]+vy*sdt)
            velocity.append(vx)
    time=time+dt
    i=i+1

plt.figure(figsize=(16,5.5))
subplot(1,2,1)
plt.title("vx0=3,vy0=3")
plt.xlabel("x")
plt.ylabel("y")
plt.xticks([-3,-2,-1,0,1,2,3])
plt.yticks([0,1,2,3,4])
plt.xlim(-3,3)
plt.ylim(0,4)
plt.plot([0,3],[4,0],color="blue",label="isosceles triangle",linewidth=2)
plt.plot([-3,0],[0,4],color="blue",linewidth=2)
plt.plot([-3,3],[0,0],color="blue",linewidth=2)
plt.plot(x,y,label="trajectory",color="red")
plt.scatter(0,2,color="black",alpha=1,linewidth=4,label="initial")
plt.legend()
subplot(1,2,2)
plt.xlabel("x")
plt.ylabel("vx")
for i in range(1000):
    if 1000*i<=len(x):
        plt.scatter(x[1000*i],velocity[1000*i])

plt.show()