import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Title
st.title("Rental Trend Predictor")

# Load dataset
df = pd.read_csv('rental_data.csv')
st.write("### Sample Dataset", df)

# Prediction logic
cities = df['City'].unique()
predictions = {}

plt.figure(figsize=(10, 5))

for city in cities:
    city_df = df[df['City'] == city]
    X = city_df[['Month']]
    y = city_df['Rent']

    model = LinearRegression()
    model.fit(X, y)
    next_month = [[6]]
    pred = model.predict(next_month)[0]
    predictions[city] = pred

    # Plot
    plt.plot(X, y, marker='o', label=city)

# Show plot
plt.title("Rental Trends by City")
plt.xlabel("Month")
plt.ylabel("Rent")
plt.legend()
st.pyplot(plt)

# Show predictions
st.write("### Predicted Rent for Month 6")
for city, rent in predictions.items():
    st.write(f"**{city}**: ₹{rent:.2f}")
