# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:27:02 2022

@author: Lujain Altaiyan 
"""

import SecondModelClass
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    while True:
        choise = input("Enter S for simulation of a specific drainpipe radius, F to find the drainpipe radius that make the water level in the reservoir equal to a seocific value after one year, Q to exit")
        if choise == 'q':
            break
        elif choise == 's':
            r = float(input("Enter the required drainpipe radius in meters"))
        
            # model = SecondModelClass.Model_2(0.607)
            # model = SecondModelClass.Model_2(0.469)
            model = SecondModelClass.Model_2(r)
            # 0.496
            water_volume, time_points = model.simulation()
            model.Plot_graph(water_volume, time_points)
        elif choise == 'f':
           required_volume = float( input("Enter required volume in meter cube"))
           r_max = 0.8
           r_list = np.linspace(0.001,r_max,40)
           v_end_list = []
           for r in r_list:
               model = SecondModelClass.Model_2(r)
               water_volume, time_points = model.simulation()
               v_end_list.append(water_volume[-1])
                    
                                            
            
           # v_g = min(v_end_list, key=lambda x:abs(x-5))
           initial_volume = required_volume
            
                                            
           v_g = min(v_end_list, key=lambda x:abs(x-initial_volume))
           r_g = r_list[v_end_list.index(v_g)]
           print("The required drainpipe radius is: ",r_g) 
            
           plt.plot(r_list,v_end_list, 'b') 
           plt.plot(r_list,[initial_volume for _ in range(len(r_list))], linestyle = 'dashed', color = 'r')
           plt.plot([r_g for _ in range(len(v_end_list))],v_end_list,linestyle = 'dashed',color = 'r')
           plt.text(0.1,initial_volume, 'v = $15 x 10^7$', fontsize = 18)
           # plt.text(-5, 60, 'Parabola $Y = x^2$', fontsize = 22)
            
           plt.title("Change of water volume after one year per drain pipe radius ", y=1.08)
           plt.xlabel("Drain pipe radius $m$")
           plt.ylabel("Volume of water after one year $m^3$")
           plt.savefig("../../../../../../../Pictures/MDM1_plots/Model2radiuschange.png")
           plt.show()
            
        else:
            print("invalid choise")
    
    





if __name__ == "__main__":
    
    main()