import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2π
y = np.sin(x)                        # Compute the sine of each x point

# Create the plot
plt.figure(figsize=(10, 5))          # Set the figure size
plt.plot(x, y, label='Sine Wave', color='blue')  # Plot the sine wave

# Add titles and labels
plt.title('Sine Wave Example')
plt.xlabel('X values (radians)')
plt.ylabel('Y values (sine)')

# Add a grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
