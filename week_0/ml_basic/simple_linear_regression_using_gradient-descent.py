# obtains linear regression parameters using gradient descent
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

training_data = pd.read_csv("C:\\Users\\user\\Documents\\local_repo_1\\week_0\\ml_basic\\Student_Performance.csv") #student performance dataset downloaded from https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression
x_training = training_data["Hours_Studied"].values
y_training = training_data["Performance_Index"].values
z_training = training_data["Previous_Scores"].values
m=len(x_training)
#fig = plt.figure(figsize=(m, 8))
#ax = plt.axes(projection='3d')
#ax.scatter3D(x_training, z_training, y_training, color='green')
fig = px.scatter_3d(
    training_data, 
    x='Hours_Studied', 
    y='Previous_Scores', 
    z='Performance_Index'
    )
fig.show()