import matplotlib.pyplot as plt
import numpy as np
import os

# Constants
resistor_value = 100e3  # 100kΩ resistor
potentiometer_settings = [0, 5e3, 25e3, 50e3, 100e3]  # Potentiometer settings in ohms

# Function to calculate attenuation
def calculate_attenuation(pot_value, resistor_value=resistor_value):
    total_resistance = pot_value + resistor_value
    return 20 * np.log10(total_resistance / resistor_value)

# Create an array of potentiometer settings from 0 to 100kΩ
potentiometer_range = np.linspace(0, 100e3, 500)
attenuation_values = [calculate_attenuation(pot_value) for pot_value in potentiometer_range]

# Plotting
plt.figure(figsize=(12, 6))

# Plot attenuation vs. potentiometer settings
plt.plot(potentiometer_range, attenuation_values, label='Attenuation vs. Potentiometer Setting', color='blue')

# Define colors for different potentiometer settings
colors = ['red', 'green', 'purple', 'orange', 'brown']

# Plot specific potentiometer settings
for setting, color in zip(potentiometer_settings, colors):
    att = calculate_attenuation(setting)
    plt.axvline(x=setting, color=color, linestyle='--', label=f'Potentiometer Setting = {setting / 1e3:.1f} kΩ\nAttenuation = {att:.2f} dB')

# Labels and Title
plt.xlabel('Potentiometer Setting (Ω)')
plt.ylabel('Attenuation (dB)')
plt.title('Attenuation vs. Potentiometer Settings')
plt.legend()
plt.grid(True)

# Save the plot as a PNG file with the same name as the script
script_name = os.path.basename(__file__).replace('.py', '.png')
plt.savefig(script_name)

# Show the plot
plt.show()
