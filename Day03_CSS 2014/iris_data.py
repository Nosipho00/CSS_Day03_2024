# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:40:59 2024

@author: NosiphoM
"""

import pandas
import matplotlib.pyplot as plt

file = pandas.read_csv("iris.csv")

file["class"] = file["class"].str.replace("iris-", "")

plt.scatter(file["class"].str.replace("Iris-",""))
plt.scatter(file["sepal_lenght"],file['sepal_width'])
plt.xlabel("sepal_lenght")
plt.ylabel("sepal_width")
plt.show()

