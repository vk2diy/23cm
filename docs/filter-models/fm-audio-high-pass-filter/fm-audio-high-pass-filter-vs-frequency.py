import numpy as np
import matplotlib.pyplot as plt

# Constants for the high-pass filter
R = 10e3  # 10k ohms
C = 33e-9  # 33nF

# Calculate the cutoff frequency
f_c = 1 / (2 * np.pi * R * C)

# Frequency range for the plot (0 to 10 kHz)
frequencies = np.linspace(1, 10e4, num=500)  # 1 Hz to 10 kHz
omega = 2 * np.pi * frequencies  # Angular frequency

# High-pass filter transfer function
H = omega / np.sqrt(omega**2 + (1 / (R * C))**2)

# Plot the frequency response
plt.figure(figsize=(12, 6))
plt.plot(frequencies, 20 * np.log10(H), label='High-Pass Filter Response')

# Highlighting audio frequency range (20 Hz to 20 kHz)
plt.axvspan(20, 20e3, color='lightblue', alpha=0.3, label='Audio Frequency Range')

# Highlighting audible frequency range (typically 20 Hz to 20 kHz)
plt.axvspan(20, 20e3, color='lightgreen', alpha=0.3, label='Audible Range')

# Adding cutoff frequency line
plt.axvline(f_c, color='r', linestyle='--', label=f'Cutoff Frequency: {f_c:.2f} Hz')

# Labeling the axes
plt.title('Frequency Response of FM Audio High-Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')

# Set x-axis to kHz for better readability
plt.xticks(ticks=[1, 1e3, 10e3], labels=['1 Hz', '1 kHz', '10 kHz'])

# Limit x-axis to 1 Hz to 21kHz
plt.xlim(1, 21e3)

# Adding grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Show plot
plt.show()
