import numpy as np
import matplotlib.pyplot as plt
import os

# Define translations directly
translations = {
    'en': {
        'transient_response_title': 'Transient Response of VCO with 100mA L78L09 LDO Regulated Supply for Step Inputs of 0.1V, 1V, 4.5V, and 9V',
        'transient_response_xlabel': 'Time (s)',
        'transient_response_ylabel': 'Voltage (V)',
        'supply_label': '100mA L78L09 LDO Regulated Supply',
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

# Plot and save graphs
def plot_and_save(lang, script_name):
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    # Transient Response Plot
    for size in step_sizes:
        ax.plot(time, transient_data[size], label=f'Step Size {size}V')
    ax.set_title(translations[lang]['transient_response_title'])
    ax.set_xlabel(translations[lang]['transient_response_xlabel'])
    ax.set_ylabel(translations[lang]['transient_response_ylabel'])
    ax.legend()
    ax.grid(True)

    # Save the plots for all languages
    filename = f"{script_name}-en.png"
    plt.savefig(filename)
    plt.close()


# Generate and save plots
script_name = os.path.splitext(os.path.basename(__file__))[0]
plot_and_save('en', script_name)  # English version
