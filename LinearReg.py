import pandas as pd
import gdown
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
from sklearn.model_selection import train_test_split

gdown.download('https://drive.google.com/uc?id=1nDjHLBMBZ3THSck1Ah3XyhgtRHIBT2Ec', 'dekho.csv', True)
data_path  = 'dekho.csv'
car_data = pd.read_csv(data_path)

x = car_data['Age'].values
x = x[:,np.newaxis]
y = car_data['Selling_Price'].values
linear = linear_model.LinearRegression(fit_intercept = True)
linear.fit(x, y)

x1=double(input('Enter the Age of the car'))
print('Selling_Price (lakhs): %0.2f'%linear.predict(x1))

y_pred = linear.predict(x)
plt.plot(x, y_pred)
plt.scatter(x, y)
plt.xlabel('Age')
plt.ylabel('Selling_Price (lakhs)')
plt.show()

print('Our slope is %0.2f lakhs/year'%linear.coef_)
print('Our y intercept is %0.2f lakhs'%linear.intercept_)
