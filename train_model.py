import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# load dataset
data = pd.read_csv("large_delivery_data.csv")

# convert text → numbers
data = pd.get_dummies(data)

# split input & output
X = data.drop("time", axis=1)
y = data["time"]

# train model
model = RandomForestRegressor(n_estimators=100, max_depth=20)
model.fit(X, y)

# save model
joblib.dump(model, "rf_model.pkl")

print("Model trained and saved!")