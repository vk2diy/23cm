import numpy as np
import matplotlib.pyplot as plt
import os

# Define snubber circuit components
R = 12  # Resistor value in ohms
C = 47e-9  # Capacitor value in farads (47nF)

# Frequency range for plotting
frequencies = np.logspace(1, 5, 1000)  # From 10 Hz to 100 kHz

# Calculate impedance of the snubber circuit
omega = 2 * np.pi * frequencies
Z = R + 1 / (1j * omega * C)

# Compute magnitude of impedance
Z_magnitude = np.abs(Z)

# Compute attenuation in dB
attenuation_dB = 20 * np.log10(Z_magnitude)

# Plot the frequency response
plt.figure(figsize=(12, 8))
plt.plot(frequencies, attenuation_dB, label='Snubber Attenuation (dB)')

# Mark audio frequency range (e.g., 20 Hz to 20 kHz)
audio_freq_range = [20, 20000]
plt.fill_betweenx(
    [min(attenuation_dB), max(attenuation_dB)],
    audio_freq_range[0],
    audio_freq_range[1],
    color='red',
    alpha=0.1,
    label='Audio Frequency Range'
)

# Customize plot
plt.xscale('log')
plt.yscale('linear')  # Linear scale for dB
plt.xlabel('Frequency (Hz)')
plt.ylabel('Attenuation (dB)')
plt.title('Frequency Response of Snubber Circuit')
plt.legend()
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Set x-axis limits to slightly more than the audio frequency range
plt.xlim(10, 50e3)

# Format x-axis to show discrete kHz values
plt.xticks([10, 100, 1000, 10000, 50000], ['10 Hz', '100 Hz', '1 kHz', '10 kHz', '50 kHz'])

# Get the script name without extension
script_name = os.path.splitext(os.path.basename(__file__))[0]

# Save the plot to a PNG file with the script's name
plt.savefig(f"{script_name}.png")

# Optionally, show the plot
plt.show()
