
"""
Created on Mon Mar 21 11:52:37 2022

@author: Lujain Altaiyan
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp  


''' Assigning the starting conditions and the time range'''




g_sq = 270612.74 # (7.3*10^10 )^0.5 #m/day^2 
time_limit = 365 # days
times = (0, time_limit)                               # Time range 365 days
ttt = list(range(0, time_limit)  )              # Time evaluation points



'''----------------------------------------------------------------------------------------'''
A = 4* 10**6 #  m^2 
v0 = [4* 10**6 * 15] # m^3 ; a = 4 x 10^6 m^2 & h = 15 m start water hight
r =0.11896551724137931 # m for pipe try change the pipe's radius to see curvatue of graph.


'''------------------------------------------------------------------------------------------'''





'''
V = Volume of the reservoir (m^3)
P = Outflow from the reservoir through the pipe (m^3)
I = Inflow of the river into the reservoir (m^3)
R = Volume of the rainfall into the reservoir (m^3)
E = Volume of water evaporated from the reservoir (m^3)
t = Time (days)
A = Surface area of the reservoir (m^2)
r = Radius of the outflow pipe

'''

def Reservoir_volume_average(t,v):
    
    #dV/dt = dP/dt + dI/dt + dR/dt + dE/dt
    #dP/dt = πr^2 √(2gV/A), g = 9.81
    #dI/dt = 51840 m^3/day,
    #dR/dt = 0.0022451A = 8980.396 m^3/day 
    #dE/dt = -0.0019165A = -7665.98 m^3/day,
    #A = 4 x 10^6 m^2
    h = v/A
    
    if h > 50:
        input(" Model one - level higher than 50!!")
        h = 50

    
    dv =   562202 - np.pi* r **2 *g_sq * np.sqrt((2*v)/A)
    return dv



sol = solve_ivp(Reservoir_volume_average,times,v0,t_eval=ttt)
Water_volume_ave = sol.y[0]
Simulation_time_points = sol.t



plt.plot(Simulation_time_points,Water_volume_ave, 'b')
plt.title("Water volume in the reservoir - first model")
plt.xlabel("Time in days, 0 is the first day in January")
plt.ylabel("Water volumer ($m^3$)")
plt.show()



