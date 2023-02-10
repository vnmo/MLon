import pandas as pd
import numpy as np
import time as tm


# data1 = pd.read_csv('CA1_cleanedData1.csv')
# data2 = pd.read_csv('CA1_cleanedData2.csv')
# data3 = pd.read_csv('CA1_cleanedData3.csv')
# data4 = pd.read_csv('CA1_cleanedData4.csv')
# data = pd.concat([data1,data2,data3,data4],ignore_index=True)
data = pd.read_csv('CA1_1b_householdPower_cleanedData.csv')
# This is a cleaned data using MATLAB for easiness.
# Data is split into 4 parts due to github data restrictions
# Date and Time are combined and converted to UNIX format
##      --- one can subtract any date base from this if required to reduce the data range
##      --- For example, lowest date time is 21/12/2006	11:17:00. Subtract 1166289840 to make this zero
##      --- Subtract  1164931200 to make the base to 01-Dec-2006 00:00:00
##      --- Subtract  1136073600 to make the base to 01-Jan-2006 00:00:00
# All NaNs and invalid cells are deleted.
# Hence new size is 2049280 x 8
#-----Attributes-----
#           Date Time in UNIX format
#           Active Power
#           Reactive Power
#           Voltage
#           Global Intensity
#           Submetering 1
#           Submetering 2
#           Submetering 3


# Take  Powers, voltage and intensity as input variable, i.e., x_i for i=1:N
inpudata=data.iloc[:,[1,2,3,4]]

# Take all sub-meterings as output variable, i.e., y_i for i=1:N
# Change if required
outputdata=data.iloc[:,[5,6,7]]

X=np.transpose(inpudata)
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
