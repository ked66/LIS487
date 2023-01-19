"""
Simple demo of a horizontal bar chart.
Based on code from
http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html
and
https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python
Modified by Amber Stubbs
"""

import numpy as np
import matplotlib.pyplot as plt


# Example data, stored in lists
years = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011']
degrees_women= [10522, 12048,  13690,  15668,  15066, 12159,  9939, 7944, 6884, 6894, 7306, 7700]

#set up the figure
fig = plt.figure()
#create axes - one row, one column, one plot
ax = fig.add_subplot(111)

#set up marks for the y axis
y_pos = np.arange(len(years))

#create the graph
ax.barh(y_pos, degrees_women, align='center', color='r', alpha=0.4)
#set labels and spacing for y axis
plt.yticks(y_pos, years)
#label x axis
plt.xlabel('Number of degrees')
#label figure
plt.title("Computer Science Bachelor's degrees earned by women, 2000-2011")

#show the figure
plt.show()
