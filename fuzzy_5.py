import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe of discourse
x = np.arange(0, 10.01, 0.01)

# Define the fuzzy set for numbers close to 5
center = 5
std_deviation = 2
membership = fuzz.gaussmf(x, center, std_deviation)

# Plot the fuzzy set
plt.plot(x, membership, label='Fuzzy Set')
plt.title('Fuzzy Set for Numbers Close to 5')
plt.xlabel('X-axis')
plt.ylabel('Membership')
plt.legend()
plt.show()
