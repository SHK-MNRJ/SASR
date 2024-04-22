import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.pipeline import make_pipeline 

from sklearn.ensemble import RandomForestRegressor

#from sklearn.metrics import accuracy_score # Accuracy metrics 

import pickle 

dataFrame= pd.read_csv('coords.csv')

X = dataFrame.drop('class', axis=1) # features
y = dataFrame['class'] # target value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
print(X_train)
#print(X_test)
print(y_train)
#print(y_test)


# Create the random forest Regressor
rf_model = RandomForestRegressor(n_estimators=500, random_state=1234)  
# You can adjust the number of estimators as needed

# Train the model
rf_model.fit(X_train, y_train)
print("Trainin completed")

yhat = rf_model.predict(X_test)
#print(accuracy_score(y_test, yhat))

print(y_test)
print('=======================')
print(yhat)
print('=======================')

with open('body_language.pkl', 'wb') as f:
    pickle.dump(rf_model, f)
