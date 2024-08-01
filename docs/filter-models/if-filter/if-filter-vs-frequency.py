import numpy as np
import matplotlib.pyplot as plt

# Component values
C8 = 10e-12  # 10 pF
C9 = 56e-12  # 56 pF
C10 = 1e-12  # 1 pF
C11 = C12 = 15e-12  # 15 pF each
L2 = L3 = 300e-9  # 300 nH each

# Frequency ranges with more divisions near the area of interest
frequencies = np.concatenate((
    np.linspace(1e6, 80e6, 500),  # 1 MHz to 80 MHz
    np.linspace(80e6, 100e6, 201)  # 80 MHz to 100 MHz with finer resolution
))
omega = 2 * np.pi * frequencies

# Impedance of capacitors and inductors
Z_C8 = 1 / (1j * omega * C8)
Z_C9 = 1 / (1j * omega * C9)
Z_C10 = 1 / (1j * omega * C10)
Z_C11 = 1 / (1j * omega * C11)
Z_C12 = 1 / (1j * omega * C12)
Z_L2 = 1j * omega * L2
Z_L3 = 1j * omega * L3

# Total impedances
Z_series1 = Z_C8 + Z_C9
Z_parallel1 = 1 / (1/Z_series1 + 1/Z_L2)
Z_series2 = Z_C11 + Z_C12
Z_parallel2 = 1 / (1/Z_series2 + 1/Z_L3)
Z_total = Z_parallel1 + Z_C10 + Z_parallel2

# Transfer function (assuming voltage divider)
H_f = Z_parallel2 / Z_total

# Magnitude response in dB
H_f_mag = 20 * np.log10(np.abs(H_f))

# Plotting the frequency response
plt.figure(figsize=(12, 6))
plt.plot(frequencies / 1e6, H_f_mag)
plt.title('Frequency Response of the IF Filter Circuit')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

# Adding extra labels
#plt.axvline(88, color='red', linestyle='--', label='88 MHz (Start of FM band)')
#plt.axvline(108, color='blue', linestyle='--', label='108 MHz (End of FM band)')
#plt.axvline(100, color='green', linestyle='--', label='100 MHz')

# Adding extra frequency delineations (marks) between 80 and 100 MHz every 5 MHz

for freq in range(85, 96, 5):

    plt.axvline(freq, color='gray', linestyle='--', linewidth=0.5)

    plt.text(freq, -100, f'{freq}', color='gray', fontsize=8, va='top')

#plt.legend()

plt.show()
