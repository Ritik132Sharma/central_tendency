import pandas as pd
from scipy.stats import kurtosis


data = pd.read_csv("C:\\Users\\Admin\\Downloads\\Mall_Customers.csv")
print(data)


'''central tendency'''

'''mean of age'''

m_age = data['Age'].mean()
print(m_age)

'''median'''

me_age = data['Age'].median()
print(me_age)

'''mode'''

mo_age = data['Age'].mode()
print(mo_age)

'''Skewness'''

skewness= (m_age - me_age)/200
print(skewness)

'''kurtosis'''

kl=data['Age'].tolist()
Kurt = kurtosis(kl , axis = 0 ,bias = True)
print(Kurt)















