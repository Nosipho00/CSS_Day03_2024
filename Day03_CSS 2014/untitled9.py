# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:28:35 2024

@author: NosiphoM
"""

# import numpy as np
# import matplotlib.pyplot as plt
# data = np.loadtxt("noisydata.csv", skiprows=1, delimiter=",")
# data_avg =np.mean(data,0)
# print("average of columns")
# print(data_avg)
# pressure = data[:,0]
# flowrate =data[:,1]
# fit=np.polyfit(pressure,flowrate,2)
# flowfit=np.polyval(fit,pressure)
# plt.plot(pressure,flowrate,"go")
# plt.plot(pressure,flowfit,"k-")
# plt.xlabel("pressure (Pa)")
# plt.ylabel("flowrate ($m^3/s$)")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
n=3000
x = np. random. uniform (size=n)
y = np. random. uniform(size=n)
print(sum(x*x+y*y <=1)/n*4)
plt. plot (x[x*x+y*y<=1] ,y [x*x+y*y<=1], "bo" )
plt. plot (x[x*x+y*y>1], y [x*x+y*y>1], "ro")
plt. show()
