import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe of discourse
x = np.arange(0, 1.01, 0.01)

# Define the fuzzy set
center = 0.5
std_deviation = 0.5
membership = fuzz.gaussmf(x, center, std_deviation)

# Plot the fuzzy set
plt.plot(x, membership, label='Fuzzy Set')
plt.title('Fuzzy Set with Membership 1 for Patterns Away from (0.5, 0.5)')
plt.xlabel('X-axis')
plt.ylabel('Membership')
plt.legend()
plt.show()
