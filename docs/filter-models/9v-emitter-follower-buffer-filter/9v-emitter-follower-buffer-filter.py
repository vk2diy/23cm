import numpy as np
import matplotlib.pyplot as plt
import os

# Time array for transient response (0 to 10 ms)
time = np.linspace(0, 0.01, 1000)

# Simulate transient response
def transient_response(time, step_time, regulator_type):
    if regulator_type == 'L78L09':
        response = np.where(time >= step_time, 9 - 0.5 * np.exp(-(time-step_time)/0.001), 9)
    elif regulator_type == 'Emitter Follower':
        response = np.where(time >= step_time, 9 - 0.1 * np.exp(-(time-step_time)/0.0005), 9)
    return response

# Generate transient responses
step_time = 0.005
response_L78L09 = transient_response(time, step_time, 'L78L09')
response_emitter_follower = transient_response(time, step_time, 'Emitter Follower')

# Frequency array for noise floor and frequency response (10 Hz to 1 MHz)
frequency = np.logspace(1, 6, 1000)

# Simulate noise floor (in µV)
noise_floor_L78L09 = 100 + 10 * np.log10(frequency)
noise_floor_emitter_follower = 10 + 5 * np.log10(frequency)

# Simulate frequency response (magnitude in dB)
def frequency_response(frequency, regulator_type):
    if regulator_type == 'L78L09':
        response = -20 * np.log10(1 + frequency/1000)
    elif regulator_type == 'Emitter Follower':
        response = -3 * np.log10(1 + frequency/10000)
    return response

# Generate frequency responses
freq_response_L78L09 = frequency_response(frequency, 'L78L09')
freq_response_emitter_follower = frequency_response(frequency, 'Emitter Follower')

# Plotting
fig, ax = plt.subplots(3, 1, figsize=(10, 15))

# Transient Response Plot
ax[0].plot(time, response_L78L09, label='L78L09')
ax[0].plot(time, response_emitter_follower, label='Emitter Follower')
ax[0].set_title('Transient Response')
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Voltage (V)')
ax[0].legend()
ax[0].grid(True)

# Noise Floor Plot
ax[1].semilogx(frequency, noise_floor_L78L09, label='L78L09')
ax[1].semilogx(frequency, noise_floor_emitter_follower, label='Emitter Follower')
ax[1].set_title('Noise Floor')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('Noise (µV)')
ax[1].legend()
ax[1].grid(True)

# Frequency Response Plot
ax[2].semilogx(frequency, freq_response_L78L09, label='L78L09')
ax[2].semilogx(frequency, freq_response_emitter_follower, label='Emitter Follower')
ax[2].set_title('Frequency Response')
ax[2].set_xlabel('Frequency (Hz)')
ax[2].set_ylabel('Magnitude (dB)')
ax[2].legend()
ax[2].grid(True)

plt.tight_layout()

# Save the plot
script_name = os.path.splitext(os.path.basename(__file__))[0]
filename = f"{script_name}-en.png"
plt.savefig(filename)
plt.close()
