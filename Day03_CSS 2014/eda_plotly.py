# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:23:01 2024

@author: NosiphoM
"""
import plotly.express as px

react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]

fig = px.line(x = temp, y = react_conv)

fig.write_html("plot.html")

import plotly.express as px

x_line = [1, 2, 3, 4, 5]
y_line = [2, 4, 6, 8, 10]

fig = px.line(x=x_line, y=y_line, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Line Plot')

fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")