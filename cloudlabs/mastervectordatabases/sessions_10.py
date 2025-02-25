
# Sample Python program demonstrating some future trends and emerging technologies.  This is a simplified example and doesn't cover the full breadth of each topic.


# 1. Artificial Intelligence (AI) and Machine Learning (ML):  Predictive modeling using scikit-learn
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data:  Predicting house prices based on size
house_size = np.array([[1000], [1500], [2000], [2500]]) # Size in sq ft
house_price = np.array([200000, 300000, 400000, 500000]) # Price in USD

# Create and train a linear regression model
model = LinearRegression()
model.fit(house_size, house_price)

# Make a prediction
new_house_size = np.array([[1750]])
predicted_price = model.predict(new_house_size)

# Print the prediction (This is a very basic example of ML prediction)
print(f"Predicted price for a 1750 sq ft house: ${predicted_price[0]}")



# 2. Internet of Things (IoT): Simulating data from a smart device
import random
import time

# Simulate temperature data from a smart thermostat
def get_temperature():
    # Simulate some random fluctuation
    return random.uniform(20, 25)

# Simulate data logging for 5 seconds
print("Simulating IoT device data...")
for i in range(5):
    temperature = get_temperature()
    print(f"Time: {time.time():.2f}, Temperature: {temperature:.1f}°C")
    time.sleep(1)  # Simulate data collection interval


# 3. Blockchain Technology:  Illustrating a simple blockchain structure (highly simplified)
class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        #In a real blockchain, a more robust hashing algorithm would be used.
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        #Extremely simplified hash function for demonstration purposes only!
        return str(self.data) + str(self.previous_hash)

# Create a simple blockchain
genesis_block = Block("Genesis Block", "0") #First block in the blockchain has no previous hash.
block2 = Block("Transaction 1", genesis_block.hash)
block3 = Block("Transaction 2", block2.hash)

print("\nSimplified Blockchain:")
print(f"Block 1: {genesis_block.__dict__}")
print(f"Block 2: {block2.__dict__}")
print(f"Block 3: {block3.__dict__}")



# 4. Cloud Computing: Using a simple cloud-based service (Illustrative only - Requires actual cloud setup)
# This section is commented out because it requires an actual cloud service setup and credentials which are not included here for security reasons.
# It would typically involve connecting to a cloud provider's API (e.g., AWS, Azure, GCP) and performing operations such as creating a virtual machine or storing data.


# 5. Big Data Analytics:  Illustrative data processing (using a small dataset for simplicity)
data = [10, 15, 20, 25, 30, 12, 18, 22, 28, 35]

# Simple average calculation (In reality, Big Data would require distributed processing frameworks like Spark or Hadoop)
average = sum(data) / len(data)
print(f"\nAverage of data: {average}")

#Note: Real-world big data analytics would involve significantly larger datasets and more sophisticated techniques.


