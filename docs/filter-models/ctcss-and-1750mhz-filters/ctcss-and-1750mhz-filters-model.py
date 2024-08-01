import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

# Define the low-pass filter function
def lowpass_filter(cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Sampling frequency
fs = 10e3  # 10 kHz

# Define filter parameters
# CTCSS Path (4 stages, 100nF each)
cutoff_ctcss = 1 / (2 * np.pi * 27e3 * 100e-9)
b_ctcss, a_ctcss = lowpass_filter(cutoff_ctcss, fs, order=4)

# 1750Hz Path (3 stages, 3.3nF each)
cutoff_repeater = 1 / (2 * np.pi * 27e3 * 3.3e-9)
b_repeater, a_repeater = lowpass_filter(cutoff_repeater, fs, order=3)

# Frequency array for plotting (limited to 5 kHz for clarity)
freq = np.linspace(0, 5e3, 8000)

# Calculate the frequency response of each path
def calculate_response(b, a):
    w, h = freqz(b, a, worN=len(freq), fs=fs)
    return w, np.abs(h)

# Responses for each path
w_ctcss, h_ctcss = calculate_response(b_ctcss, a_ctcss)
w_repeater, h_repeater = calculate_response(b_repeater, a_repeater)

# Potentiometer resistance values and percentages
pot_min = 1.25e3  # 5% of 25kΩ
pot_center = 12.5e3  # Midpoint of 25kΩ potentiometer
pot_max = 25e3  # 100% of 25kΩ

# Calculate responses with different potentiometer settings
def calculate_repeater_response(pot_value):
    if pot_value == 0:
        return np.zeros_like(h_repeater)  # No signal when resistance is 0
    return h_repeater * (pot_value / 25e3)  # Scale by resistance

# Calculate the responses
response_repeater_min = calculate_repeater_response(pot_min)
response_repeater_center = calculate_repeater_response(pot_center)
response_repeater_max = calculate_repeater_response(pot_max)

# Plotting
plt.figure(figsize=(12, 8))

# Plot CTCSS path
plt.plot(w_ctcss, 20 * np.log10(h_ctcss), label='CTCSS Path (4 stages, 100nF)', color='blue')

# Plot 1750Hz path with different potentiometer settings
plt.plot(w_repeater, 20 * np.log10(response_repeater_min + 1e-6), label=f'1750Hz Path (Potentiometer 1.25kΩ, 5%)', color='green')
plt.plot(w_repeater, 20 * np.log10(response_repeater_center + 1e-6), label=f'1750Hz Path (Potentiometer 12.5kΩ, 50%)', color='red')
plt.plot(w_repeater, 20 * np.log10(response_repeater_max + 1e-6), label=f'1750Hz Path (Potentiometer 25kΩ, 100%)', color='purple')

# Add vertical bars indicating the tone frequencies
plt.axvline(x=67, color='blue', linestyle='--', label='CTCSS Tone (67Hz)')
plt.axvline(x=1750, color='orange', linestyle='--', label='1750Hz Tone')

plt.title('Frequency Response of Low-Pass Filters with Tone Markers')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.xlim(0, 2000)  # Limit x-axis to cover the tones of interest
plt.ylim(-40, 0)  # Adjust y-axis for better visualization
plt.grid(True)
plt.legend()
plt.show()
