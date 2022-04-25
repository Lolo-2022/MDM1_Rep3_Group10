# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:15:18 2022

@author: Lujain Altaiyan
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp 

class Model_2:
    
    def __init__(self,drain_pipe_radius):
        self.g_sq = 270612.74 # (7.3*10^10 )^0.5 #m/day^2 
        time_limit = 365 # days
        self.times = (0, time_limit)                               # Time range 365 days
        # ttt = list(range(0, time_limit)  ) 

        self.ttt =  np.linspace(0,time_limit,time_limit * 100)             # Time evaluation points


        # self.v0 = [3.3*10**7] # m^3 ; a = 4 x 10^6 m^2 & h = 15 m start water hight
        self.v0 = [15*10**7] # m^3 ; a = 4 x 10^6 m^2 & h = 15 m start water hight
        self.r = drain_pipe_radius # m for pipe try change the pipe's radius to see curvatue of graph.

 
        self.Riverflow_2 = [3464640,3240000,3041280,2808000,2540160,2324160,2168640,2030400,1909440,1779840,1753920,2160000,2160000,2557440,2384640,3481920,2877120,2488320,3473280,7145280,10195200,8009280,4950720,4026240,3611520,3542400,4069440,7931520,11491200,10540800,8579520,6143040,6652800,6324480,5581440,6099840,5140800,4199040,3585600,3170880,2833920,2522880,2332800,2151360,2298240,3127680,4121280,5633280,6194880,4760640,4587840,4008960,3818880,3395520,2946240,2617920,2367360,2194560,2056320,1952640,1848960,2125440,2445120,1909440,1719360,1607040,1512000,1451520,1892160,1900800,2592000,3879360,2626560,2090880,1840320,1658880,1563840,1477440,1399680,1356480,1287360,1218240,1175040,1252800,1831680,1926720,1520640,1347840,1226880,1157760,1080000,1010880,976320,950400,933120,898560,881280,861408,856224,831168,811296,793152,759456,747360,719712,717120,695520,686880,700704,663552,641088,622944,609984,609984,597024,585792,677376,1054080,872640,720576,658368,627264,692928,796608,700704,643680,662688,1097280,950400,791424,695520,698112,1157760,1114560,1036800,1278720,1270080,1088640,1244160,1149120,1641600,2367360,2280960,3473280,2946240,2125440,1710720,1486080,1330560,1192320,1114560,1028160,984960,915840,839808,807840,791424,761184,722304,698112,682560,679104,647136,618624,600480,559872,582336,580608,653184,698112,714528,654912,654048,584928,531360,508896,486432,705888,1183680,783648,624672,533088,506304,505440,521856,572832,609120,663552,618624,513216,503712,595296,844128,702432,558144,465696,444960,438912,430272,419040,406080,388800,386208,378432,645408,812160,501984,482976,623808,540864,562464,508032,575424,631584,584928,480384,437184,495936,650592,719712,1270080,1175040,734400,602208,540000,498528,475200,451872,419040,421632,452736,463104,559872,648864,565920,461376,402624,367200,380160,367200,370656,356832,353376,336096,324000,314496,314496,314496,316224,316224,292896,331776,342144,317952,311040,307584,399168,390528,335232,324864,293760,304992,300672,286848,287712,301536,299808,290304,316224,410400,803520,950400,665280,547776,1105920,1330560,1157760,2116800,1399680,959040,825120,724896,672192,611712,578016,570240,534816,518400,501984,491616,504576,705888,3395520,5201280,2522880,1598400,1330560,1175040,1028160,967680,924480,1425600,2263680,4968000,5624640,3844800,2548800,2064960,1728000,1555200,1434240,1287360,1226880,1149120,1080000,1097280,1054080,976320,907200,881280,852768,808704,795744,787968,754272,715392,688608,682560,674784,693792,707616,668736,626400,596160,656640,624672,793152,838944,741312,702432,1460160,2125440,1650240,1693440,1356480,1270080,1261440,1278720,1200960,1088640,1028160,967680,933120,907200,864000,828576,827712,872640,1779840,3136320,2479680,3222720,4086720,3456000,3430080,3153600]
        
        
    def get_v0(self):
        return self.v0
    
    def get_r(self):
        return self.r
    
    
    def Rainfall_2(self,t):
        
       
        dr = 6*10**6*(195.03 * np.sin(0.005891 * t + 1.29) + 193.06* np.sin(0.005974 * t + 4.42))/1000
        return dr
    
    
    
    def Evaporation_2(self,t,A_2):
        
       
        de = A_2* (1.55* np.sin(0.005131 * t + 0.5569) + 0.76 * np.sin(0.02239 *t + 3.532))/1000
        return de






    def Reservoir_2_volume(self,t,v):
        
        
        #dV/dt = dP/dt + dI/dt + dR/dt + dE/dt
        #dP/dt = πr^2 √(2gV/A), g = 9.81 m/s^2 = g_sq^2 = 270.1*10**3 m/day^2
        #dR/dt = 2628.41 cos(2π(t+31) / 365.24) + 9199.43 in m^3 per day
        #dI/dt = 43200 cos(2π*t / 365.24) + 51840   m^3/day    
        #dE/dt = -0.0019165A = -7665.98 m^3/day   
        #A = 4 x 10^6 m^2
        
        # v = (h/(1.462*10**(-4)))**(3/2)        
        h = (1.462*10**(-4))*v**(2/3)
        if h > 50:
            # print(v)
            # input("level higher than 50!!")
            h = 50
            v = (h/(1.462*10**(-4)))**(3/2)
            # print(v)
        # if v > 2*10**8:
        #     v =  2*10**8
        A_2 = np.pi*np.sqrt(h *7.3*10**10 )
        dv =  self.Rainfall_2(t) + self.Riverflow_2[int(t)] - np.pi* self.r **2 *self.g_sq * np.sqrt((2*v)/A_2) - self.Evaporation_2(t,A_2)
        h = 50
        vmax = (h/(1.462*10**(-4)))**(3/2) 
        if v + dv > vmax:
            dv = vmax - v
       
            
            
        
    
        
       
            
        return dv
    
    
    def get_water_area(self,v):
        
        h = (1.462*10**(-4))*v**(2/3)
        if h > 50:
            h = 50
        A_2 = np.pi*np.sqrt(h *7.3*10**10 )
    
    
    
        return A_2
    
    
    def simulation(self):
        solv = solve_ivp(self.Reservoir_2_volume,self.times,self.v0,t_eval=self.ttt,dense_output = True )
        Water_2_volume = solv.y[0]
        Simulation_time_points = solv.t
        return Water_2_volume,Simulation_time_points
    
    def Plot_graph(self,Water_2_volume,Simulation_time_points):
            
        plt.plot(Simulation_time_points,Water_2_volume, 'b')
        plt.title("Water volume in the reservoir - second model")
        plt.xlabel("Time in days, 0 is the first day in January")
        plt.ylabel("Water volume ($m^3$)")
        plt.savefig("../../../../../../../Pictures/MDM1_plots/Model2volume.png")
        plt.show()
        
        
        
        
        plt.plot(Simulation_time_points,list(map(self.Rainfall_2,Simulation_time_points)), 'b')
        plt.title("Volume of accumlated rainfall water in the reservoir - second model ")
        plt.xlabel("Time in days, 0 is the first day in January")
        plt.ylabel("Volume of accumlated rainfall water ($m^3$)")
        plt.savefig("../../../../../../../Pictures/MDM1_plots/Model2Rainfall.png")
        plt.show()
        
        
        Areas = list(map(self.get_water_area,Water_2_volume))
        
        plt.plot(Simulation_time_points,list(map(self.Evaporation_2 ,Simulation_time_points, Areas)), 'b')
        plt.title("Volume of evaporated water from the reservoir - second model ")
        plt.xlabel("Time in days, 0 is the first day in January")
        plt.ylabel("Volume of evaporated water rainfall water ($m^3$)")
        plt.savefig("../../../../../../../Pictures/MDM1_plots/Model2Evaporation.png")
        plt.show()
        
        
        
        plt.plot(Simulation_time_points,Areas, 'b')
        plt.title("Area of the water surface - second model ")
        plt.xlabel("Time in days, 0 is the first day in January")
        plt.ylabel("Water surface area ($m^2$)")
        plt.savefig("../../../../../../../Pictures/MDM1_plots/Model2AreaChange.png")
        plt.show()
        
        
        plt.scatter(list(range(0,366)),self.Riverflow_2)
        plt.title("River flow - second model ")
        plt.xlabel("Time in days, 0 is the first day in January")
        plt.ylabel("Water volume flows in the reservoir ($m^3/day$)")
        plt.savefig("../../../../../../../Pictures/MDM1_plots/Model2RiverFlow.png")
        plt.show()
            