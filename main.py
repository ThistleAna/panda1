# Save an excel destination.csv data
# Import Panda
# Data correlation between number of all inclusive hotels and the score

import pandas as pd

dt = pd.read_csv("destination.csv")
print("Correlation between number of all inclusive hotels and the score is")

col_1 = dt["Hotels"]
col_2 = dt["Feedback"]
correlation = col_1.corr(col_2)
print(correlation)




