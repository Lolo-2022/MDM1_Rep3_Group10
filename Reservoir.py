
"""
Created on Mon Mar 21 11:52:37 2022

@author: Lujain Altaiyan
"""
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp  
import scipy.constants as const
from mpl_toolkits.mplot3d import Axes3D

''' Assigning the starting conditions and the time range'''



h0 = [50] # m
ai = 0.015 #m2 5 insh pipe
vi = 8.5*1.52 * 60 * 60 # m/s*3600 = m/day

ao = 0.015/2.5 #m2
g = 9.8 #m2/s 
time_limit = 10 # days
times = (0, time_limit)                               # Time range 365 days
ttt = np.linspace(0, time_limit, time_limit * 200)                # Time evaluation points
A = 100 # m2







def Resevoir_hight(t,h): 
    # A*dh/dt = ai*vi - ao*vo
    # A*dh/dt = ai*vi - ao * sqrt(2*g*h)
    dh = (ai*vi - ao*3600 * np.sqrt(2*g*h))/A
    return dh



    


sol = solve_ivp(Resevoir_hight,times,h0,t_eval=ttt)
Water_level = sol.y[0]
Simulation_time_points = sol.t

plt.plot(Simulation_time_points,Water_level, 'c')
plt.title("Water level in a reservoir")
plt.xlabel("Time in days")
plt.ylabel("Level of reservoir")
plt.show()

plt.show()
        


