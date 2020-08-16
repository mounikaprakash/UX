import matplotlib.pyplot as plt


x1 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# corresponding y axis values
y1 = [29,29,28,30,28,32,26,25,30,27,26,22,17,15]
# plotting the line 1 points
plt.plot(x1, y1, label="Monday_Old_data")

# line 2 points
x2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
y2 = [14,16,17,16,14,12,9,8,7,5,4,3,2,2]
# plotting the line 2 points
plt.plot(x2, y2, label="Monday_New_data")
##############################################################################
x1 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# corresponding y axis values
y1 = [35,37,35,38,38,40,36,34,35,35,37,26,24,18]
# plotting the line 1 points
plt.plot(x1, y1, label="Wednesday_Old_data")

# line 2 points
x2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
y2 = [15,17,17,16,15,13,10,7,6,4,4,3,2,2]
# plotting the line 2 points
plt.plot(x2, y2, label="Wednesday_New_data")

##############################################################################
x1 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# corresponding y axis values
y1 = [33,34,33,35,35,36,36,31,34,33,30,24,21,20]
# plotting the line 1 points
plt.plot(x1, y1, label="Thursday_Old_data")

# line 2 points
x2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
y2 = [15,15,14,12,12,13,9,8,8,6,6,2,2,2]
# plotting the line 2 points
plt.plot(x2, y2, label="Thursday_New_data")

##############################################################################

x1 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# corresponding y axis values
y1 = [32,31,28,30,28,30,30,28,37,31,25,22,20,15]
# plotting the line 1 points
plt.plot(x1, y1, label="Friday_Old_data")

# line 2 points
x2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
y2 = [13,13,12,12,12,12,10,9,8,6,4,3,3,3]
# plotting the line 2 points
plt.plot(x2, y2, label="Friday_New_data")

##############################################################################
x1 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# corresponding y axis values
y1 = [23,22,23,26,27,30,31,26,31,27,22,20,16,13]
# plotting the line 1 points
plt.plot(x1, y1, label="Saturday_Old_data")

# line 2 points
x2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
y2 = [14,16,18,15,15,14,10,7,7,5,6,2,2,2]

# plotting the line 2 points
plt.plot(x2, y2, label="Saturday_New_data")

##############################################################################
# line 1 points
# x axis values
x1 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# corresponding y axis values
y1 = [22,21,20,22,24,27,24,23,25,23,19,18,13,11]
# plotting the line 1 points
plt.plot(x1, y1, label="Sunday_Old_data")

# line 2 points
x2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24]

y2 = [15,18,20,14,15,13,9,8,8,4,5,2,2,2]
# plotting the line 2 points
plt.plot(x2, y2, label="Sunday_New_data")

# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('Percentage')
# giving a title to my graph
plt.title('Graph')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()