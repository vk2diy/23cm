import numpy as np
import matplotlib.pyplot as plt
import os

# Time array
time = np.linspace(0, 0.01, 1000)  # Time from 0 to 10 ms

# Define capacitor values in Farads
capacitor_values = np.array([
    10e-6,  # 10µF
    22e-6,  # 22µF
    33e-6,  # 33µF
    47e-6,  # 47µF
    68e-6,  # 68µF
    100e-6, # 100µF
    220e-6  # 220µF
])

# Define a load resistance (example value)
R = 1000  # 1kΩ for simulation

# Calculate voltage response over time for each capacitor
voltages = {}
for C in capacitor_values:
    time_constant = R * C
    voltages[C] = 5 * (1 - np.exp(-time / time_constant))

# Create the plot
plt.figure(figsize=(12, 8))

# Plot the voltage responses for each capacitor
for C, voltage in voltages.items():
    plt.plot(time, voltage, label=f'{C*1e6:.0f}µF')

# Customize plot
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Transient Response of Capacitors to a 5V Step Input')
plt.legend()
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Remove extra bottom margin
plt.subplots_adjust(bottom=0.1)  # Adjust bottom margin to remove extra space

# Get the script name without extension
script_name = os.path.splitext(os.path.basename(__file__))[0]

# Save the plot to a PNG file with the script's name
plt.savefig(f"{script_name}.png")

# Optionally, show the plot
plt.show()
