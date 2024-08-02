import numpy as np
import matplotlib.pyplot as plt
import os

# Define translations directly
translations = {
    'en': {
        'transient_response_title': 'Transient Response of VCO with 100mA L78L09 LDO Regulated Supply for Step Inputs of 0.1V, 1V, 4.5V, and 9V',
        'transient_response_xlabel': 'Time (s)',
        'transient_response_ylabel': 'Voltage (V)',
        'noise_floor_title': 'Noise Floor of VCO with 100mA L78L09 LDO Regulated Supply',
        'noise_floor_xlabel': 'Frequency (Hz)',
        'noise_floor_ylabel': 'Noise (µV)',
        'frequency_response_title': 'Frequency Response of VCO with 100mA L78L09 LDO Regulated Supply',
        'frequency_response_xlabel': 'Frequency (Hz)',
        'frequency_response_ylabel': 'Magnitude (dB)',
        'supply_label': '100mA L78L09 LDO Regulated Supply',
        'audio_band': 'Audio Frequency Range (20 Hz - 20 kHz)',
        'if_band': 'Intermediate Frequency Range (30 kHz - 1.5 MHz)'
    }
}

# Define the time and frequency ranges
time = np.linspace(0, 0.01, 1000)  # 10 ms duration
frequency = np.logspace(1, 6, 1000)  # 10 Hz to 1 MHz

# Define step responses
def transient_response(time, step_size):
    return 9 - step_size * np.exp(-time/0.0005)

# Generate data for different step sizes
step_sizes = [0.1, 1, 4.5, 9]
transient_data = {size: transient_response(time, size) for size in step_sizes}

# Noise Floor and Frequency Response
def noise_floor(frequency):
    return 100 + 10 * np.log10(frequency)

def frequency_response(frequency):
    return -20 * np.log10(1 + frequency/1000)

noise_data = noise_floor(frequency)
frequency_data = frequency_response(frequency)

# Frequency bands
audio_band = (20, 20000)  # Audio frequency range from 20 Hz to 20 kHz
if_band = (30000, 1500000)  # Intermediate frequency range in NBFM receivers

# Format frequency axis labels
def format_frequency_ticks(ticks):
    formatted_ticks = []
    for tick in ticks:
        if tick >= 1e6:
            formatted_ticks.append(f'{tick / 1e6:.0f} MHz')
        elif tick >= 1e3:
            formatted_ticks.append(f'{tick / 1e3:.0f} kHz')
        else:
            formatted_ticks.append(f'{tick:.0f} Hz')
    return formatted_ticks

# Plot and save graphs
def plot_and_save(lang, script_name):
    fig, ax = plt.subplots(3, 1, figsize=(12, 18))
    
    # Transient Response Plot
    for size in step_sizes:
        ax[0].plot(time, transient_data[size], label=f'Step Size {size}V')
    ax[0].set_title(translations[lang]['transient_response_title'])
    ax[0].set_xlabel(translations[lang]['transient_response_xlabel'])
    ax[0].set_ylabel(translations[lang]['transient_response_ylabel'])
    ax[0].legend()
    ax[0].grid(True)
    
    # Noise Floor Plot
    ax[1].semilogx(frequency, noise_data, 'k-', label=translations[lang]['supply_label'])
    ax[1].set_title(translations[lang]['noise_floor_title'])
    ax[1].set_xlabel(translations[lang]['noise_floor_xlabel'])
    ax[1].set_ylabel(translations[lang]['noise_floor_ylabel'])
    # Add shaded regions with frequency range summaries
    ax[1].axvspan(audio_band[0], audio_band[1], color='blue', alpha=0.1, label=translations[lang]['audio_band'])
    ax[1].axvspan(if_band[0], if_band[1], color='red', alpha=0.1, label=translations[lang]['if_band'])
    ax[1].set_xticks(np.logspace(1, 6, 6))
    ax[1].set_xticklabels(format_frequency_ticks(np.logspace(1, 6, 6)))
    ax[1].legend(loc='center', bbox_to_anchor=(0.8, 0.5))  # Inset position
    ax[1].grid(True)
    
    # Frequency Response Plot
    ax[2].semilogx(frequency, frequency_data, 'k-', label=translations[lang]['supply_label'])
    ax[2].set_title(translations[lang]['frequency_response_title'])
    ax[2].set_xlabel(translations[lang]['frequency_response_xlabel'])
    ax[2].set_ylabel(translations[lang]['frequency_response_ylabel'])
    # Add shaded regions with frequency range summaries
    ax[2].axvspan(audio_band[0], audio_band[1], color='blue', alpha=0.1, label=translations[lang]['audio_band'])
    ax[2].axvspan(if_band[0], if_band[1], color='red', alpha=0.1, label=translations[lang]['if_band'])
    ax[2].set_xticks(np.logspace(1, 6, 6))
    ax[2].set_xticklabels(format_frequency_ticks(np.logspace(1, 6, 6)))
    ax[2].legend(loc='lower left')
    ax[2].grid(True)
    
    plt.tight_layout()
    
    # Save the plots for all languages
    filename = f"{script_name}-en.png"
    plt.savefig(filename)
    plt.close()

# Generate and save plots
script_name = os.path.splitext(os.path.basename(__file__))[0]
plot_and_save('en', script_name)  # English version
