import pylab as pl
import math
class chaos:
    def __init__(self,theta=0.2,omega=0,t=0,time_step=0.04,F_D=1.4,q=0.5,l=9.8,g=9.8,OMEGA_D=2/3):
        self.theta=[theta]
        self.o=[omega]
        self.t=[t]
        self.dt=time_step
        self.F_D=F_D
        self.O=OMEGA_D
        self.q=q
        self.l=l
        self.g=g
    def calculate1(self):
        while(self.t[-1]<=100):  
            o_new1=self.o[-1]-((self.g/self.l)*math.sin(self.theta[-1])+self.q*self.o[-1]-self.F_D*math.sin(self.O*self.t[-1]))*self.dt
            self.o.append(o_new1)
            theta_new1=self.theta[-1]+self.o[-1]*self.dt
            while(theta_new1<-math.pi):
                theta_new1+=2*math.pi
            while(theta_new1>math.pi):
                theta_new1-=2*math.pi
            self.theta.append(theta_new1)
            t_new1=self.t[-1]+self.dt
            self.t.append(t_new1)
    def show_results1(self):
        pl.subplot(131)          
        pl.plot(self.t, self.theta)
        pl.title(r'$\theta$ versus time')
        pl.xlabel('time(s)')
        pl.ylabel(r'$\theta$(rad/s)')
        pl.legend(['$F_D$=1.4'])
        pl.show()
        self.theta=[0.2]
        self.o=[0]
        self.t=[0]
        self.F_D=1.44
    def calculate2(self):
        while(self.t[-1]<=100):  
            o_new2=self.o[-1]-((self.g/self.l)*math.sin(self.theta[-1])+self.q*self.o[-1]-self.F_D*math.sin(self.O*self.t[-1]))*self.dt
            self.o.append(o_new2)
            theta_new2=self.theta[-1]+self.o[-1]*self.dt
            while(theta_new2<-math.pi):
                theta_new2+=2*math.pi
            while(theta_new2>math.pi):
                theta_new2-=2*math.pi
            self.theta.append(theta_new2)
            t_new2=self.t[-1]+self.dt
            self.t.append(t_new2)
    def show_results2(self):        
        pl.subplot(132)
        pl.plot(self.t, self.theta)
        pl.title(r'$\theta$ versus time')
        pl.xlabel('time(s)')
        pl.ylabel(r'$\theta$(rad/s)')
        pl.legend(['$F_D$=1.44'])
        pl.show()
        self.theta=[0.2]
        self.o=[0]
        self.t=[0]
        self.F_D=1.465
    def calculate3(self):
        while(self.t[-1]<=100):  
            o_new3=self.o[-1]-((self.g/self.l)*math.sin(self.theta[-1])+self.q*self.o[-1]-self.F_D*math.sin(self.O*self.t[-1]))*self.dt
            self.o.append(o_new3)
            theta_new3=self.theta[-1]+self.o[-1]*self.dt
            while(theta_new3<-math.pi):
                theta_new3+=2*math.pi
            while(theta_new3>math.pi):
                theta_new3-=2*math.pi
            self.theta.append(theta_new3)
            t_new3=self.t[-1]+self.dt
            self.t.append(t_new3)
    def show_results3(self):        
        pl.subplot(133)
        pl.plot(self.t, self.theta)
        pl.title(r'$\theta$ versus time')
        pl.xlabel('time(s)')
        pl.ylabel(r'$\theta$(rad/s)')
        pl.legend(['$F_D$=1.465'])
        pl.show()
a = chaos()
a.calculate1()
a.show_results1()  
a.calculate2()
a.show_results2() 
a.calculate3()
a.show_results3()