import math
import matplotlib.pyplot as plt
# import modules above
g=9.8
omega=4000*math.pi/60
vd=35
v_wind=3
Delta=5
S0m=0.00041#it means s0/m
# B2m=0.00004
# y_zero=10000
# a=0.0065
# T0=300
# alpha=2.5
class baseball:
    def __init__(self,v0,theta,yFinal=0):
        self.x0=0
        self.y0=1.8
        self.yFinal=yFinal
        self.v0=v0
        self.Theta=theta
        self.theta=theta*math.pi/180
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.dt=0.01
        return None
    
    def B2m(self,v):#it means B2/m
        return 0.0039+0.0058/(1+math.exp(v-vd/Delta))
    def F(self,vx,vy):
        vxy=math.sqrt(vx**2+vy**2)
        Fx=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*(vx-v_wind)-S0m*omega*vy
        Fy=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*vy+S0m*omega*vx
        return Fx,Fy
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        while not (self.Y[-1]<self.yFinal and self.Vy[-1]<0):
            newVx=self.Vx[-1]+self.F(vx=self.Vx[-1],vy=self.Vy[-1])[0]*self.dt
            newVy=self.Vy[-1]-g*self.dt+self.F(self.Vx[-1],self.Vy[-1])[1]*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy=0.5*(self.Vy[-1]+self.Vy[-2])
#            meanV=math.sqrt(meanVx**2+meanVy**2) # not used in Cannon0 because there is no air drag
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            self.X.append(newX)
            self.Y.append(newY)
        # fix the final landing coordinate        
#        r=-self.Y[-2]/self.Y[-1]
        self.X[-1]=((self.Y[-2]-self.yFinal)*self.X[-1]+(self.yFinal-self.Y[-1])*self.X[-2])/(self.Y[-2]-self.Y[-1])
        self.Y[-1]=self.yFinal
        return 0
    # get the final distance shells can reach

        
# select the angle casting the largest distance
import numpy as np

theta=np.linspace(15,75,12)
f=[]
for i in range (len(theta)):
    k=baseball(41.6,theta[i],0)
    k.fly()
    plt.plot(k.X,k.Y,label=r'$\theta=%.2f^\circ$'%theta[i])
    plt.xlabel('x/m')
    plt.ylabel('y/m')
    plt.title('the trajectory at different initial angles')
    plt.legend(loc='best',frameon=False)
    f.append(k.X[-1])
    
plt.show()

phi=np.linspace(13.5,73.5,12)
width=3
plt.bar(phi,f,width,color='gray')
plt.xlabel(r'$\theta^\circ$')
plt.ylabel('the maximum range')
plt.title('the maximum ranges at different initial angles')
plt.show()

