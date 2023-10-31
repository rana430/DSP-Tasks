import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            x = []
            amplitudes = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 2:
                    x.append(float(parts[0]))
                    amplitudes.append(float(parts[1]))
            amplitudes = np.array(amplitudes)
            return x, amplitudes
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file: {e}")
        return None, None


def quantize_signal():
    try:
        num_bits = int(bits_entry.get())
        num_levels = 2 ** num_bits
        file_path = r"F:\FCIS\Level 3\First term\DSP\Labs\Tasks\Task 1\tasksol\Quan1_input.txt"
        x, amplitudes = load_file(file_path)
        if amplitudes is not None:
            min_value = min(amplitudes)
            max_value = max(amplitudes)
            range_step = (max_value - min_value) / (num_levels)
            encoded_signal = [(sample - min_value) // range_step for sample in amplitudes]
            quantized_signal = [int(value * range_step + min_value) for value in encoded_signal]

            quantization_error = sum(
                (original - quantized)**2 for original, quantized in zip(amplitudes, quantized_signal))

            output_label.config(
                text=f"Encoded Signal: {encoded_signal}\nQuantized Signal: {quantized_signal}\nQuantization Error: {quantization_error}")

            # Perform the test
            QuantizationTest1(file_path, encoded_signal, quantized_signal)

            # Plot original and quantized signals
            plt.figure(figsize=(8, 6))
            plt.plot(x, amplitudes, label='Original Signal')
            plt.plot(x, quantized_signal, label='Quantized Signal')
            plt.xlabel('Index')
            plt.ylabel('Amplitude')
            plt.legend()
            plt.title('Original vs Quantized Signal')
            plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


def QuantizationTest1(filename,encoded_signal, quantized_signal):
    expectedEncodedValues = []
    expectedQuantizedValues = []
    with open(r"F:\FCIS\Level 3\First term\DSP\Labs\Tasks\Task 1\tasksol\Quan1_input.txt", 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V2 = str(L[0])
                V3 = float(L[1])
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                line = f.readline()
            else:
                break
    if (len(encoded_signal) != len(expectedEncodedValues)) or (len(quantized_signal) != len(expectedQuantizedValues)):
        print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(encoded_signal)):
        if encoded_signal[i] != expectedEncodedValues[i]:
            print("QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the "
                  "expected one")
            return
    for i in range(len(expectedQuantizedValues)):
        if abs(quantized_signal[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one")
            return
    print("QuantizationTest1 Test case passed successfully")




# Create main window
root = tk.Tk()
root.title("Signal Quantization")

# Number of Bits Entry
bits_label = tk.Label(root, text="Number of Bits:")
bits_label.pack()
bits_entry = tk.Entry(root)
bits_entry.pack()

# Quantize Button
quantize_button = tk.Button(root, text="Quantize Signal", command=quantize_signal)
quantize_button.pack()

# Output Label
output_label = tk.Label(root, text="")
output_label.pack()

# Start the main loop
root.mainloop()