import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Step 1: Load the dataset
df = pd.read_csv('rental_data.csv')

# Step 2: Predict next month rent for each city
cities = df['City'].unique()
predictions = {}

for city in cities:
    city_df = df[df['City'] == city]
    
    # Reshape data
    X = city_df[['Month']]  # Independent
    y = city_df['Rent']     # Dependent
    
    # Train model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict next month (month 6)
    next_month = [[6]]
    predicted_rent = model.predict(next_month)[0]
    predictions[city] = predicted_rent
    
    # Visualize trend
    plt.plot(X, y, marker='o', label=city)

# Step 3: Plot
plt.title("Rental Trends by City")
plt.xlabel("Month")
plt.ylabel("Rent")
plt.legend()
plt.grid(True)
plt.show()

# Step 4: Print predictions
print("Predicted Rent for Month 6:")
for city, rent in predictions.items():
    print(f"{city}: ₹{rent:.2f}")
