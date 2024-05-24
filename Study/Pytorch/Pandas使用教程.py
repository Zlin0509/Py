import os
import pandas as pd

os.makedirs(os.path.join('..','data'),exist_ok=True)
data_file=os.path.join('..','data','house_tiny.csv')
with open(data_file,'w') as f:
    f.write('NumRooms,Alley,Price\n')
    f.write('NA,Pave,127000\n')
    f.write('2,NA,34671342\n')


data=pd.read_csv(data_file)
print(data)

inputs=data.iloc[:,0:2]
# inputs=inputs.fillna(inputs.mean())
print(inputs)

inputs=pd.get_dummies(inputs,dummy_na=True)
print(inputs)