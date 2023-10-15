from tkinter import *
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt

win = Tk()
win.geometry("700x350")

signal_samples = None
time = None


def open_file():
    global signal_samples, time

    file = filedialog.askopenfile(mode='r', filetypes=[('Signal', '*.txt')])
    if file:
        lines = file.readlines()
        file.close()

        signal_type = int(lines[0])
        is_periodic = int(lines[1])
        n_samples = int(lines[2])
        samples = []

        for line in lines[3:]:
            values = line.split()
            if signal_type == 0:  # Time domain
                sample_index = int(values[0])
                sample_amplitude = float(values[1])
                samples.append((sample_index, sample_amplitude))
            elif signal_type == 1:  # Frequency domain
                frequency = float(values[0])
                amplitude = float(values[1])
                phase_shift = float(values[2])
                samples.append((frequency, amplitude, phase_shift))

        if signal_type == 0:  # Time domain
            indices = [sample[0] for sample in samples]
            amplitudes = [sample[1] for sample in samples]
            if is_periodic:
                indices.append(indices[0] + n_samples)
                amplitudes.append(amplitudes[0])
            interpolated_indices = np.linspace(min(indices), max(indices), num=1000)
            interpolated_amplitudes = np.interp(interpolated_indices, indices, amplitudes)

            plt.figure(figsize=(12, 6))
            # Continuous representation
            plt.subplot(2, 1, 1)
            plt.plot(interpolated_indices, interpolated_amplitudes)
            plt.xlabel('Time')
            plt.ylabel('Amplitude')
            plt.title('Continuous Signal Representation')

            # Discrete representation
            plt.subplot(2, 1, 2)
            plt.stem(indices, amplitudes)
            plt.xlabel('Time')
            plt.ylabel('Amplitude')
            plt.title('Discrete Signal Representation')

            plt.tight_layout()
            plt.show()

        elif signal_type == 1:  # Frequency domain
            frequencies = [sample[0] for sample in samples]
            amplitudes = [sample[1] for sample in samples]
            phase_shifts = [sample[2] for sample in samples]
            interpolated_frequencies = np.linspace(min(frequencies), max(frequencies), num=1000)
            interpolated_amplitudes = np.interp(interpolated_frequencies, frequencies, amplitudes)
            interpolated_phase_shifts = np.interp(interpolated_frequencies, frequencies, phase_shifts)

            plt.figure(figsize=(12, 6))
            # Continuous representation
            plt.subplot(2, 1, 1)
            plt.plot(interpolated_frequencies, interpolated_amplitudes * np.cos(interpolated_phase_shifts))
            plt.xlabel('Frequency')
            plt.ylabel('Amplitude')
            plt.title('Continuous Signal Representation')

            # Discrete representation
            plt.subplot(2, 1, 2)
            plt.stem(frequencies, amplitudes)
            plt.xlabel('Frequency')
            plt.ylabel('Amplitude')
            plt.title('Discrete Signal Representation')

            plt.tight_layout()
            plt.show()


label = Label(win, text="Click the Button to browse the Files")
label.pack(pady=10)

ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

win.mainloop()