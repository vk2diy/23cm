import numpy as np
import matplotlib.pyplot as plt
import os
import locale

# Define translations
translations = {
    'en': {
        'transient_response_title': 'Transient Response to 0.5A Load Change for Different Capacitor Sizes',
        'time_label': 'Time (s)',
        'voltage_label': 'Voltage (V)',
        'noise_floor_title': 'Noise Floor for Different Capacitor Sizes',
        'frequency_label': 'Frequency (Hz)',
        'noise_label': 'Noise (µV)',
        'frequency_response_title': 'Frequency Response for Different Capacitor Sizes',
        'magnitude_label': 'Magnitude (dB)',
        'audio_label': 'Audio (20 Hz - 20 kHz)',
        'if_label': 'IF (450 kHz - 1.5 MHz)',
        'baseline_label': 'Baseline (9V Regulator Only)'
    },
    'nl': {
        'transient_response_title': 'Transiënte Respons op 0.5A Belastingsverandering voor Verschillende Condensatorwaarden',
        'time_label': 'Tijd (s)',
        'voltage_label': 'Spanning (V)',
        'noise_floor_title': 'Ruisvloer voor Verschillende Condensatorwaarden',
        'frequency_label': 'Frequentie (Hz)',
        'noise_label': 'Ruis (µV)',
        'frequency_response_title': 'Frequentierespons voor Verschillende Condensatorwaarden',
        'magnitude_label': 'Grootte (dB)',
        'audio_label': 'Audio (20 Hz - 20 kHz)',
        'if_label': 'IF (450 kHz - 1.5 MHz)',
        'baseline_label': 'Basislijn (9V Regulator Alleen)'
    },
    'de': {
        'transient_response_title': 'Transiente Reaktion auf 0.5A Laständerung für Verschiedene Kondensatorgrößen',
        'time_label': 'Zeit (s)',
        'voltage_label': 'Spannung (V)',
        'noise_floor_title': 'Rauschpegel für Verschiedene Kondensatorgrößen',
        'frequency_label': 'Frequenz (Hz)',
        'noise_label': 'Rauschen (µV)',
        'frequency_response_title': 'Frequenzgang für Verschiedene Kondensatorgrößen',
        'magnitude_label': 'Magnituden (dB)',
        'audio_label': 'Audio (20 Hz - 20 kHz)',
        'if_label': 'IF (450 kHz - 1.5 MHz)',
        'baseline_label': 'Basislinie (9V Regulator Nur)'
    }
}

# Define capacitor values for emitter follower configurations
capacitor_values = [10e-6, 22e-6, 47e-6, 100e-6, 220e-6]  # 10µF, 22µF, 47µF, 100µF, 220µF

# Time array for transient response (0 to 10 ms)
time = np.linspace(0, 0.01, 1000)

# Frequency array for noise floor and frequency response (10 Hz to 1 MHz)
frequency = np.logspace(1, 6, 1000)

# Baseline response (9V regulator output only, no emitter follower)
def baseline_transient_response(time):
    return 9 - 0.1 * np.exp(-time/0.0005)

# Simulate transient response with varying capacitor sizes
def transient_response(time, capacitor_value):
    if capacitor_value == 47e-6:
        return baseline_transient_response(time)  # Ensure 47µF is treated as baseline
    time_constant = 0.0005 * (47e-6 / capacitor_value)
    return 9 - 0.1 * np.exp(-time/time_constant)

# Simulate noise floor with varying capacitor sizes
def noise_floor(frequency, capacitor_value):
    return 100 + 10 * np.log10(frequency) - 10 * np.log10(capacitor_value/47e-6)

# Simulate frequency response with varying capacitor sizes
def frequency_response(frequency, capacitor_value):
    return -20 * np.log10(1 + frequency/(1000 * (47e-6 / capacitor_value)))

# Generate data for all capacitor values and baseline
transient_responses = {cv: transient_response(time, cv) for cv in capacitor_values}
transient_responses['baseline'] = baseline_transient_response(time)
noise_floors = {cv: noise_floor(frequency, cv) for cv in capacitor_values}
noise_floors['baseline'] = noise_floor(frequency, 47e-6)
frequency_responses = {cv: frequency_response(frequency, cv) for cv in capacitor_values}
frequency_responses['baseline'] = frequency_response(frequency, 47e-6)

# Function to plot and save graphs
def plot_and_save(language, script_name):
    fig, ax = plt.subplots(3, 1, figsize=(12, 18))

    # Transient Response Plot
    ax[0].plot(time, transient_responses['baseline'], 'k-', label=translations[language]['baseline_label'])
    for capacitor_value in capacitor_values:
        if capacitor_value != 47e-6:
            ax[0].plot(time, transient_responses[capacitor_value], linestyle='--', label=f'Capacitor {capacitor_value*1e6:.0f} µF')
    # Plot 47µF last to ensure visibility
    ax[0].plot(time, transient_responses[47e-6], linestyle='--', color='red', label=f'Capacitor 47 µF')
    ax[0].set_title(translations[language]['transient_response_title'])
    ax[0].set_xlabel(translations[language]['time_label'])
    ax[0].set_ylabel(translations[language]['voltage_label'])
    ax[0].legend()
    ax[0].grid(True)

    # Noise Floor Plot
    ax[1].semilogx(frequency, noise_floors['baseline'], 'k-', label=translations[language]['baseline_label'])
    for capacitor_value in capacitor_values:
        if capacitor_value != 47e-6:
            ax[1].semilogx(frequency, noise_floors[capacitor_value], linestyle='--', label=f'Capacitor {capacitor_value*1e6:.0f} µF')
    # Plot 47µF last to ensure visibility
    ax[1].semilogx(frequency, noise_floors[47e-6], linestyle='--', color='red', label=f'Capacitor 47 µF')
    ax[1].set_title(translations[language]['noise_floor_title'])
    ax[1].set_xlabel(translations[language]['frequency_label'])
    ax[1].set_ylabel(translations[language]['noise_label'])

    # Shading frequency bands
    audio_band = [20, 20000]
    if_band = [450e3, 1.5e6]
    ylim = ax[1].get_ylim()
    ax[1].fill_between(frequency, ylim[0], ylim[1], where=((frequency >= audio_band[0]) & (frequency <= audio_band[1])), color='green', alpha=0.1, label=translations[language]['audio_label'])
    ax[1].fill_between(frequency, ylim[0], ylim[1], where=((frequency >= if_band[0]) & (frequency <= if_band[1])), color='blue', alpha=0.1, label=translations[language]['if_label'])
    ax[1].legend()
    ax[1].grid(True)

    # Frequency Response Plot
    ax[2].semilogx(frequency, frequency_responses['baseline'], 'k-', label=translations[language]['baseline_label'])
    for capacitor_value in capacitor_values:
        if capacitor_value != 47e-6:
            ax[2].semilogx(frequency, frequency_responses[capacitor_value], linestyle='--', label=f'Capacitor {capacitor_value*1e6:.0f} µF')
    # Plot 47µF last to ensure visibility
    ax[2].semilogx(frequency, frequency_responses[47e-6], linestyle='--', color='red', label=f'Capacitor 47 µF')
    ax[2].set_title(translations[language]['frequency_response_title'])
    ax[2].set_xlabel(translations[language]['frequency_label'])
    ax[2].set_ylabel(translations[language]['magnitude_label'])

    # Shading frequency bands
    audio_band = [20, 20000]
    if_band = [450e3, 1.5e6]
    ylim = ax[2].get_ylim()
    ax[2].fill_between(frequency, ylim[0], ylim[1], where=((frequency >= audio_band[0]) & (frequency <= audio_band[1])), color='green', alpha=0.1, label=translations[language]['audio_label'])
    ax[2].fill_between(frequency, ylim[0], ylim[1], where=((frequency >= if_band[0]) & (frequency <= if_band[1])), color='blue', alpha=0.1, label=translations[language]['if_label'])
    ax[2].legend()
    ax[2].grid(True)

    # Formatting x-axis labels with Hz suffixes
    def format_hz(x, pos):
        if x >= 1e6:
            return f'{x/1e6:.0f}M'
        elif x >= 1e3:
            return f'{x/1e3:.0f}k'
        else:
            return f'{x:.0f}'

    ax[1].xaxis.set_major_formatter(plt.FuncFormatter(format_hz))
    ax[2].xaxis.set_major_formatter(plt.FuncFormatter(format_hz))

    # Save the plots
    plt.tight_layout()
    for lang in ['en', 'de', 'nl']:
        filename = f"{script_name}-{lang}.png"
        plt.savefig(filename)
    plt.close()

# Plot and save graphs
plot_and_save('en', 'capacitor_analysis')
plot_and_save('de', 'capacitor_analysis')
plot_and_save('nl', 'capacitor_analysis')
