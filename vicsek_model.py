#solves the Vicsek model for active agents in 2D

def find_theta(agents,agents_wrapped):#evaluates the average angle
 for i in range(N):
  agents_dist=(agents[i,0]-agents_wrapped[:,0])**2+(agents[i,1]-agents_wrapped[:,1])**2
  agents_coord=np.where(agents_dist<=r*r)
  theta[i]=np.arctan2(np.mean(np.sin(agents_wrapped[agents_coord,2])),np.mean(np.cos(agents_wrapped[agents_coord,2])))+np.random.sample()*eta-eta/2
 return theta
 
def plot(agents): #function to plot results
 plt.quiver(agents[:,0],agents[:,1],np.cos(agents[:,2]),np.sin(agents[:,2]),agents[:,2])
 plt.clim(-np.pi,np.pi)
 plt.gca().set_aspect('equal', adjustable='box') 
 plt.xlim(0,L)
 plt.ylim(0,L)
 title="N="+str(N)+" $\eta$="+str(eta)+" v="+str(v)+" r="+str(r)
 plt.title(title)
 plt.pause(0.001)
 ax.clear()

def default():
 global L
 global N
 global eta
 global v
 global r
 
 L=1
 N=500
 eta=0.5
 v=0.01
 r=0.2

def fig1a():
 global L
 global N
 global eta
 global v
 global r
 
 L=7
 N=300
 eta=2.0
 v=0.03
 r=1

def fig1b():
 global L
 global N
 global eta
 global v
 global r

 L=25
 N=300
 eta=0.1
 v=0.03
 r=1

def fig1c():
 global L
 global N
 global eta
 global v
 global r

 L=7
 N=300
 eta=2.0
 v=0.03
 r=1

def fig1d():
 global L
 global N
 global eta
 global v
 global r

 L=5
 N=300
 eta=5
 v=0.03
 r=1
 
####function main()####
import numpy as np
import matplotlib.pyplot as plt

global L #dimesions of the system 
global N #number of agents
global eta #random noise	
global v #velocity of agents
global r #radius of interaction

fig,ax=plt.subplots()
plt.ion()
plt.rcParams['image.cmap'] = 'Dark2'

#initialize parameters
fig1d()

agents=np.random.rand(N,3) #initializes agents' position and orientation

agents[:,0]*=L
agents[:,1]*=L
agents[:,2]*=np.pi*2

theta=np.zeros(N)

while 1:
 plot(agents)
 agents_wrapped=np.concatenate([np.concatenate([agents+[0,0,0],agents+[-L,0,0],agents+[-L,L,0]]),np.concatenate([agents+[-L,-L,0],agents+[0,-L,0],agents+[0,L,0]]),np.concatenate([agents+[L,-L,0],agents+[L,0,0],agents+[L,L,0]])]) #takes care of periodic boundary
 agents[:,2]=find_theta(agents,agents_wrapped) #calculates orientation
 agents[:,0]+=v*np.cos(agents[:,2]) #timemarch
 agents[:,0]%=L
 agents[:,1]+=v*np.sin(agents[:,2])
 agents[:,1]%=L

####end of program####
