
"""
Created on Mon Mar 21 11:52:37 2022

@author: Lujain Altaiyan
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp  


''' Assigning the starting conditions and the time range'''




g_sq = 270612.74 # (7.3*10^10 )^0.5 #m/day^2 
time_limit = 366 # days
times = (0, time_limit)                               # Time range 365 days
ttt = np.linspace(0, time_limit, time_limit * 365)                # Time evaluation points



'''----------------------------------------------------------------------------------------'''
A = 4* 10**6 #  m^2 
v0 = [4* 10**6 * 15] # m^3 ; a = 4 x 10^6 m^2 & h = 15 m start water hight
r = 0.1099 # m for pipe try change the pipe's radius to see curvatue of graph.



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


def Rainfall(t):
    
    #dR/dt = 2628.41 cos(2π(t+31) / 365.24) + 9199.43 in m^3 per day
    dr = 9199.43 + 2628.41 * np.cos(2*np.pi*(t+31)/365.24)
    return dr


def Riverflow(t):
    #dI/dt = 43200 cos(2π*t / 365.24) + 51840 in m^3 per day
    di = 43200 *np.cos(2*np.pi*(t) / 365.24) + 51840
    return di


def Reservoir_volume(t,v):
    
    #dV/dt = dP/dt + dI/dt + dR/dt + dE/dt
    #dP/dt = πr^2 √(2gV/A), g = 9.81 m/s^2 = g_sq^2 = 270.1*10**3 m/day^2
    #dR/dt = 2628.41 cos(2π(t+31) / 365.24) + 9199.43 in m^3 per day
    #dI/dt = 43200 cos(2π*t / 365.24) + 51840   m^3/day    
    #dE/dt = -0.0019165A = -7665.98 m^3/day   
    #A = 4 x 10^6 m^2

    dv =  Rainfall(t) + Riverflow(t) - np.pi* r **2 *g_sq * np.sqrt((2*v)/A) -7665.98
    return dv



def Reservoir_volume_average(t,v):
    
    #dV/dt = dP/dt + dI/dt + dR/dt + dE/dt
    #dP/dt = πr^2 √(2gV/A), g = 9.81
    #dI/dt = 51840 m^3/day,
    #dR/dt = 0.0022451A = 8980.396 m^3/day 
    #dE/dt = -0.0019165A = -7665.98 m^3/day,
    #A = 4 x 10^6 m^2
    
    dv =   53154.41 - np.pi* r **2 *g_sq * np.sqrt((2*v)/A)
    return dv






sol = solve_ivp(Reservoir_volume_average,times,v0,t_eval=ttt)
Water_volume_ave = sol.y[0]
Simulation_time_points = sol.t


'''
if you want separate plot for first model please delet # for all this code 
and don't forget to deactivate the green graph from the next plot code
'''

# plt.plot(Simulation_time_points,Water_level, 'g')
# plt.title("Water volume in a reservoir with average R & I & E")
# plt.xlabel("Time in days")
# plt.ylabel("Level of reservoir")
# plt.show()




sole = solve_ivp(Reservoir_volume,times,v0,t_eval=ttt)
Water_volume = sole.y[0]
Simulation_time_points = sole.t

plt.plot(Simulation_time_points,Water_volume, 'r')
plt.plot(Simulation_time_points,Water_volume_ave, 'g')

plt.title("Water volume in a reservoir")
plt.xlabel("Time in days")
plt.ylabel("volume of reservoir m^3")
plt.show()




        


