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
car_data['Fuel_No'] = car_data['Fuel_Type'].replace({'Petrol':2, 'Diesel':1, 'CNG':0})
car_data['Seller_No'] = car_data['Seller_Type'].replace({'Dealer':1, 'Individual':0})

x = car_data[['Age', 'TransmissionNumber', 'Kms_Driven','Fuel_No','Seller_No',]].values
y = car_data['Selling_Price'].values
multiple = linear_model.LinearRegression(fit_intercept = True, normalize = True)
multiple.fit(x, y)

x1=double(input('Enter the Age of the car'))
x2=double(input('Enter the Kms Driven'))
x3=double(input('Enter the Transmission of the car')).replace({'Manual':1, 'Automatic':0})
x4=double(input('Enter the Fuel Type of the car')).replace({'Petrol':2, 'Diesel':1, 'CNG':0})
x5=double(input('Enter the Seller Type')).replace({'Dealer':1, 'Individual':0})

X=List()
X.append(x1)
X.append(x3)
X.append(x2)
X.append(x4)
X.append(x5)

print('Selling_Price (lakhs): %0.2f'%multiple.predict(X))
print('This model has a score(R^2) of: %0.3f'%multiple.score(x,y))
