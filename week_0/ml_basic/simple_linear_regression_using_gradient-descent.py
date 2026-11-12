# obtains linear regression parameters using gradient descent
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

def cost_function(x, y, z, w1, w2, b):
    total_cost = 0
    m = len(x)
    for i in range(m):
        f = w1 * x[i] + w2 * y[i] + b
        total_cost += (f - z[i]) ** 2
    return total_cost / (2 * m)
    # ^^ above function calculates the cost for given weights w1, w2 and bias b for the training data x, y and z
    # cost is the mean squared error (MSE) divided by 2
    
def gradient_function(x, y, z, w1, w2, b):
    m = len(x)
    dw1 = 0
    dw2 = 0
    db = 0
    for i in range(m):
        f = w1 * x[i] + w2 * y[i] + b
        error = (f - z[i])
        dw1 += error * x[i]
        dw2 += error * y[i]
        db += error
    return dw1 / m, dw2 / m, db / m
    # ^^ above function calculates the gradients of the cost function with respect to weights w1, w2 and bias b for the training data x, y and z
    # gradients are the partial derivatives of the cost function with respect to each parameter

def gradient_descent(x, y, z, learning_rate, iterations):
    w1 = 0.0
    w2 = 0.0
    b = 0.0
    for i in range(iterations):
        dw1, dw2, db = gradient_function(x, y, z, w1, w2, b)
        w1 -= learning_rate * dw1
        w2 -= learning_rate * dw2
        b -= learning_rate * db
        print(f"Iteration {i+1}: w1 = {w1}, w2 = {w2}, b = {b}, cost = {cost_function(x, y, z, w1, w2, b)}") 
        # ^^ printing to see the values of w1, w2, b and cost function at each iteration and check for decreasing trend in cost function
    print ("Finished!")
    return w1, w2, b
    # ^^ above function performs gradient descent to find the optimal weights w1, w2 and bias b for the training data x, y and z 

training_data = pd.read_csv("C:\\Users\\user\\Documents\\local_repo_1\\week_0\\ml_basic\\Student_Performance.csv") 
                            # ^^ student performance dataset location.
# ^^ dataset downloaded from https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression
x_training = training_data["Hours_Studied"].values
y_training = training_data["Previous_Scores"].values
z_training = training_data["Performance_Index"].values
w1, w2, b = gradient_descent(x_training, y_training, z_training, 0.00035, 1000)
# ^^ above line calls the gradient_descent function to find the optimal weights w1, w2 and bias b
# for the training data with learning rate 0.00035 and 1000 iterations
fig = plt.figure()
ax = plt.axes(projection='3d')
x = x_training
y = y_training
z = z_training
c = x + y + z
ax.scatter(x, y, z, c=c) # scatter plot of the training data in 3D space
m = math.floor(len(x) / 1000)
    # ^^ above line calculates the number of points to be plotted in the 3D scatter plot
x_grid = np.linspace(min(x), max(x), m)
y_grid = np.linspace(min(y), max(y), m)
x, y = np.meshgrid(x_grid, y_grid) 
z = w1 * x + w2 * y + b  
ax.plot_surface(x, y, z, cmap ='viridis', edgecolor='red') # plotting the regression plane in 3D space using the optimal weights w1, w2 and bias b
ax.set_xlabel('Hours Studied')
ax.set_ylabel('Previous Scores')
ax.set_zlabel('Performance Index')
plt.show()