# Linear Regression
These codes use Linear Regression to find the correlation between the selling price of a car and different factors like transmission no, fuel type,age,etc and uses these factors to make a prediction about a car's price.

## SciKit
SciKit is a python library used commonly to create and use various Machine Learning Models(statistical) in Python.

### Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sklearn.
```bash
pip install sklearn
```
### Usage

```python
from sklearn import linear_model

linear = linear_model.LinearRegression(fit_intercept = True)  # Creating a Linear Regression Model to create a line of best fit
linear.fit(x, y)  #Training the model with x as inputs and y as outputs
y_pred = linear.predict(x)  #Making a prediction using the model based on value of x
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
