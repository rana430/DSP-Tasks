import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt


def generate_waveform():
    global t, signal
    amplitude = float(amp_entry.get())
    phase_shift = float(phase_entry.get())
    analog_frequency = float(analog_freq_entry.get())
    sampling_frequency = float(sampling_freq_entry.get())

    if signal_type.get() == "Sine":  # Sine wave
        t = np.linspace(0, 1, int(sampling_frequency))  # Generate time array from 0 to 1 second
        signal = amplitude * np.sin(2 * np.pi * analog_frequency * t + phase_shift)
        waveform_label.config(text="Sine Waveform")
    elif signal_type.get() == "Cosine":  # Cosine wave
        t = np.linspace(0, 1, int(sampling_frequency))  # Generate time array from 0 to 1 second
        signal = amplitude * np.cos(2 * np.pi * analog_frequency * t + phase_shift)
        waveform_label.config(text="Cosine Waveform")

    plt.figure()
    plt.plot(t, signal)
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.show()


window = tk.Tk()
window.title("Signal Generation")
window.geometry("1000x700")

signal_type_label = tk.Label(window, text="Select Signal Type:")
signal_type_label.pack()
signal_type = tk.StringVar()
signal_type.set("Sine")  # Default value
signal_type_menu = tk.OptionMenu(window, signal_type, "Sine", "Cosine")
signal_type_menu.pack()

amp_label = tk.Label(window, text="Amplitude:")
amp_label.pack()
amp_entry = tk.Entry(window)
amp_entry.pack()

analog_freq_label = tk.Label(window, text="Analog Frequency:")
analog_freq_label.pack()
analog_freq_entry = tk.Entry(window)
analog_freq_entry.pack()

sampling_freq_label = tk.Label(window, text="Sampling Frequency:")
sampling_freq_label.pack()
sampling_freq_entry = tk.Entry(window)
sampling_freq_entry.pack()

phase_label = tk.Label(window, text="Phase Shift:")
phase_label.pack()
phase_entry = tk.Entry(window)
phase_entry.pack()

generate_button = tk.Button(window, text="Generate", command=generate_waveform)
generate_button.pack()

waveform_label = tk.Label(window, text="")
waveform_label.pack()

window.mainloop()
