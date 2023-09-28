import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
data = pd.read_csv("neuron-firing-deltas.csv", header=None)

# Step 2: Extract the column with the firing deltas (assuming it is the first column)
firing_deltas = data[0]

# Step 3: Calculate λ using the MLE formula
lambda_hat = 988 / firing_deltas.sum()
print(f"The MLE for the exponential rate parameter λ is: {lambda_hat}")
print(f"Deltas sum: {firing_deltas.sum()}")

# Step 4: Create a histogram with 30 evenly spaced buckets
plt.hist(firing_deltas, bins=30, edgecolor="black")

# Step 5: Set up the plot labels and title
plt.xlabel("Time (s)")
plt.ylabel("Frequency")
plt.title("Histogram of Firing Deltas")

# Step 6: Display the histogram
plt.show()
