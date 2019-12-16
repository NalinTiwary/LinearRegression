import pandas as pd
import gdown
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
from sklearn.model_selection import train_test_split

gdown.download('https://drive.google.com/uc?id=1nDjHLBMBZ3THSck1Ah3XyhgtRHIBT2Ec', 'dekho.csv', True)
data_path  = 'dekho.csv'
car_data = pd.read_csv(data_path)

car_data['TransmissionNumber'] = car_data['Transmission'].replace({'Manual':1, 'Automatic':0})
x = car_data[['Age', 'TransmissionNumber', 'Kms_Driven']].values
y = car_data['Selling_Price'].values
multiple = linear_model.LinearRegression(fit_intercept = True, normalize = True)
multiple.fit(x, y)

x1=double(input('Enter the Age of the car'))
x2=double(input('Enter the Kms Driven'))
x3=double(input('Enter the Transmission of the car')).replace({'Manual':1, 'Automatic':0})
X=List()
X.append(x1)
X.append(x3)
X.append(x2)

print('Selling_Price (lakhs): %0.2f'%multiple.predict(X))
print('This model has a score(R^2) of: %0.3f'%multiple.score(x,y))
