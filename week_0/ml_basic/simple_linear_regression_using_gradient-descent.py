# obtains linear regression parameters using gradient descent
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import plotly.express as px

training_data = pd.read_csv("C:\\Users\\user\\Documents\\local_repo_1\\week_0\\ml_basic\\Student_Performance.csv") #student performance dataset downloaded from https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression
x_training = training_data["Hours_Studied"].values
y_training = training_data["Previous_Scores"].values
z_training = training_data["Performance_Index"].values
m=len(x_training)
#fig = plt.figure(figsize=(m, 8))
#ax = plt.axes(projection='3d')
#ax.scatter3D(x_training, z_training, y_training, color='green')
fig = plt.figure()
ax = plt.axes(projection='3d')
x=x_training 
y=y_training 
z=z_training
c=x + y + z
ax.scatter(x, y, z, c=c)
ax.set_xlabel('Hours Studied')
ax.set_ylabel('Previous Scores')
ax.set_zlabel('Performance Index')
plt.show()