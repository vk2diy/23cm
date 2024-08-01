import numpy as np
import matplotlib.pyplot as plt

# Define frequencies
frequencies = np.array([1000, 20000])  # 1 kHz and 20 kHz

# Capacitor values in Farads, ensuring 10µF is the last value shown
capacitor_values = np.array([
    10e-9,   # 10nF
    22e-9,   # 22nF
    33e-9,   # 33nF
    47e-9,   # 47nF
    68e-9,   # 68nF
    100e-9,  # 100nF
    220e-9,  # 220nF
    330e-9,  # 330nF
    470e-9,  # 470nF
    680e-9,  # 680nF
    1e-6,    # 1µF
    2.2e-6,  # 2.2µF
    3.3e-6,  # 3.3µF
    4.7e-6,  # 4.7µF
    10e-6,   # 10µF (last value shown)
]) 

# Convert values to nanofarads (nF) and microfarads (µF) for labeling
def format_capacitance(value):
    if value >= 1e-6:
        return f"{value*1e6:.1f}µF"
    elif value >= 1e-9:
        return f"{value*1e9:.0f}nF"
    else:
        return f"{value*1e12:.1f}pF"

# Labels for capacitor values
labels = [format_capacitance(val) for val in capacitor_values]

# Calculate impedance
def calculate_impedance(frequencies, capacitors):
    impedances = np.zeros((len(capacitors), len(frequencies)))
    for i, C in enumerate(capacitors):
        for j, f in enumerate(frequencies):
            impedances[i, j] = 1 / (2 * np.pi * f * C)
    return impedances

# Get impedances
impedances = calculate_impedance(frequencies, capacitor_values)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot impedances at 1 kHz and 20 kHz
plt.plot(capacitor_values, impedances[:, 0], 'bo-', label='1 kHz')
plt.plot(capacitor_values, impedances[:, 1], 'ro-', label='20 kHz')

# Add threshold line for potential degradation (1 kΩ)
plt.axhline(y=1000, color='gray', linestyle='--', label='Degradation Threshold (1kΩ)')

# Fill areas indicating signal degradation and no degradation
plt.fill_between(capacitor_values, impedances[:, 0], 1000, where=(impedances[:, 0] > 1000), color='red', alpha=0.3, label='Signal Degradation')
plt.fill_between(capacitor_values, impedances[:, 0], 1000, where=(impedances[:, 0] <= 1000), color='blue', alpha=0.3, label='No Signal Degradation')
plt.fill_between(capacitor_values, impedances[:, 1], 1000, where=(impedances[:, 1] > 1000), color='red', alpha=0.3)
plt.fill_between(capacitor_values, impedances[:, 1], 1000, where=(impedances[:, 1] <= 1000), color='blue', alpha=0.3)

# Plot capacitor values with correct positioning and human-readable comments
for i, (value, txt) in enumerate(zip(capacitor_values, labels)):
    plt.text(value, impedances[i, 0] + 10, txt, ha='center', va='bottom', rotation=45, fontsize=8)

# Customize tick labels and axis limits
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e-9, 15e-6)  # Limit x-axis to capacitor values up to 10 µF with some space
plt.xlabel('Capacitance')
plt.ylabel('Impedance (Ω)')
plt.title('Capacitor Size as Impedance vs Signal Degradation at Audio Frequencies (1-20kHz)')
plt.legend()
plt.gca().invert_yaxis()  # Reverse the vertical axis
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Add summary text directly in the image file
plt.figtext(0.5, -0.15, 
    'Capacitor values that result in impedance above 1 kΩ can negatively affect signal integrity, especially at high frequencies, due to increased impedance.', 
    ha='center', va='center', fontsize=10)

# Show plot
plt.tight_layout()
plt.savefig('capacitor_impedance_analysis.png', bbox_inches='tight')
plt.show()
