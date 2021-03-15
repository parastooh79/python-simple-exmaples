# In this code we do some simple exercises with Pandas functions

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('example.csv' ,sep=',',error_bad_lines=False)

# Analyze file columns

for col in df.columns:
    print(df[col].describe(),'\n\n')

# Pandas function makes sense 
# because it considers specific indicators for each data type

print('---------------------------------------------------------------')
# print unique data
exp1 = pd.unique(df['exp1'])
exp2 = pd.unique(df['exp2'])
print('The distinct number of bedrooms and bathrooms is : ','\n\n',u_bath,'\n\n',u_bed)
print('-----------------------------------------------------------------')

#drop the column

df.drop(columns="examp3",inplace=True)
print('examp3 column was droped')
#inplace = False -->  that make a copy of data frame.
# if inplace = True do operation inplace and return None.
print('------------------------------------------------------------------')

# Rename the columns

print("Columns will be renamed ...",'\n')
df.rename(columns={"old_name":"new_name"} , inplace=True)
print("After rename : " , df.columns)
print('---------------------------------------------------------------------')

# editing the example column 

df["example"] = df["simple"].str.replace('old char','new char',regex=True)
#
df["example"] = pd.to_numeric(df["example"])
print('the example column was edited.')

#Plot this column

n , bins , patches = plt.hist(df["Price/SQ.Ft"] , 10 , facecolor='green')
plt.show()
print('----------------------------------------------------------------------')

#Applying Only on variables with NaN values

for col in df.columns[df.isnull().any(axis=0)]:     
    df[col].fillna(df[col].mean(),inplace=True)
        
print('The NaN characters in each column were filled with averages.')
print('-------------------------------------------------------------------------')

new_values = {"exaple col name":{'exp' : 'exp', 'exp' : 'exp'}}
df.replace(new_values,inplace=True)
print('New values!')
print('----------------------------------------------------------------------------')

print("The End Of This Program")
