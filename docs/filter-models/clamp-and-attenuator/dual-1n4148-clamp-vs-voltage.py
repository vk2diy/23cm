import matplotlib.pyplot as plt
import numpy as np
import os

# Constants
diode_vf = 0.7  # Forward voltage of 1N4148 in volts

# Voltage range (-2V to 2V to cover both positive and negative clamping)
voltages = np.linspace(-2, 2, 500)

# Attenuation calculation for clamping
# Positive clamping
positive_attenuation = np.where(voltages > diode_vf, 20 * np.log10(diode_vf / voltages), 0)

# Negative clamping
negative_attenuation = np.where(voltages < -diode_vf, 20 * np.log10(-diode_vf / voltages), 0)

# Plotting
plt.figure(figsize=(12, 6))

# Plot positive voltage attenuation
plt.plot(voltages, positive_attenuation, label='Positive Voltage Clamping (1N4148)', color='blue')

# Plot negative voltage attenuation
plt.plot(voltages, negative_attenuation, label='Negative Voltage Clamping (1N4148)', color='green')

# Add horizontal line at 0 dB for reference
plt.axhline(y=0, color='gray', linestyle='--')

# Add vertical lines at diode forward voltage and negative forward voltage
plt.axvline(x=diode_vf, color='red', linestyle='--', label=f'Positive 1N4148 Forward Voltage ({diode_vf} V)')
plt.axvline(x=-diode_vf, color='orange', linestyle='--', label=f'Negative 1N4148 Forward Voltage ({-diode_vf} V)')

# Labels and Title
plt.xlabel('Input Voltage (V)')
plt.ylabel('Attenuation (dB)')
plt.title('Voltage vs. Attenuation for Positive and Negative Clamping with Dual 1N4148')
plt.legend()
plt.grid(True)

# Save the plot as a PNG file with the same name as the script
script_name = os.path.basename(__file__).replace('.py', '.png')
plt.savefig(script_name)

# Show the plot
plt.show()
