import pandas as pd
import numpy as np
import time as tm

data1 = pd.read_csv('CA1_1c_greenhouse_cleanedData_part1.csv')
data2 = pd.read_csv('CA1_1c_greenhouse_cleanedData_part2.csv')
data = pd.concat([data1,data2],ignore_index=True)

# This is a cleaned data using MATLAB for easiness.
# Data is split into 4 parts due to github data restrictions

# Input variables (Change if required)
inputAttributes = np.arange(0,5231)
# Output variables (Change if required)
outputAttributes = np.arange(5231,5232)

inputdata=data.iloc[:,inputAttributes]
outputdata=data.iloc[:,outputAttributes]
X=np.transpose(inputdata)
Y=np.transpose(outputdata)
print(f"Size of input data = {X.shape}")
print(f"Size of output data = {Y.shape}")

alpha = np.float32(2.0) # Lambda: Take a value
p = len(X) # Dimension of data

start = tm.time()
# Find the regressor matrix (or vector) using the closed-form solution
w_opt = np.linalg.inv((X@X.T) + alpha * np.eye(p)) @ (X@Y.T)
stop = tm.time()

print(f"Regressor w=\n {w_opt}")
totTime = stop-start
print(f"\nTotal time time taken to compute the closed form solution = {totTime} seconds")
