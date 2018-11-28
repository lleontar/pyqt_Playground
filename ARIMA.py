# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:43:23 2018

@author: lab
"""
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot as plt
import numpy as np
data=[2.0, 2.0, 2.0, 1.8, 1.8, 2.0, 2.0 ,2.0, 2.0, 2.0, 1.8,1.8, 1.8, 2.0, 2.0 ,2.0,1.8, 1.7, 1.8, 1.9 ,0.1,1.2,1.2,1.3]
X=data+(np.random.normal(0,.001,len(data)))
#X=data[:10]
o=3
start_params=[]
start_params.append(np.mean(X))
model = ARIMA(X, order=(o,1,0))
for i in range(0,o):
    start_params.append(.1)
model_fit = model.fit(disp=0, start_params=start_params)
# multi-step out-of-sample forecast
forecast = model_fit.forecast(steps=3)[0]
# invert the differenced forecast to something usable
history = [x for x in X]


def create_non_stationary_series(samples):
    data=[]
    for i in range(0,samples):
        if(i<round(samples/3)):
            gen=np.abs(np.random.normal(0,.1,1)*100)[0]
        else:
            gen=np.abs(np.random.normal(0.5,.15,1)*100)[0]
        data.append(gen)
    return data

data=create_non_stationary_series(50)
#data=pandas.DataFrame(data)
result = seasonal_decompose(data, model='additive',freq=2)

data = pandas.Series.from_csv('C:\\passengers.csv',sep=';',header=0)
#result = seasonal_decompose(data, model='multiplicative',freq=2)
#print(result.trend)
#print(result.seasonal)
#print(result.resid)
#print(result.observed)
result.plot()
plt.show()