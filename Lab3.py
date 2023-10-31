import math
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

def format_interval(interval, num_bits):
    binary_representation = bin(interval)[2:]  # Convert to binary and remove '0b' prefix
    # Ensure the binary representation has the desired number of bits by padding with leading zeros
    return binary_representation.zfill(num_bits)
def quantize_signal_bits():
    try:
        num_bits = int(bits_entry.get())
        num_levels = 2 ** num_bits
        file_path = r"F:\FCIS\Level 3\First term\DSP\Labs\Tasks\Task 1\tasksol\Quan1_input.txt"
        x, amplitudes = load_file(file_path)
        if amplitudes is not None:
            min_value = min(amplitudes)
            max_value = max(amplitudes)
            range_step = (max_value - min_value) / num_levels
            newIntervals = [min_value + i * range_step for i in range(num_levels)]
            midPoints = [interval + range_step / 2 for interval in newIntervals]
            encoded_signal = []
            quantized_signal = []
            interval_numbers = []  # Store the interval numbers
            intervals = []  # Store the intervals
            #print(midPoints)
            #print(amplitudes)
            for sample in amplitudes:
                interval = min(range(len(newIntervals)), key=lambda i: abs(midPoints[i] - sample))
                interval_numbers.append(interval)
                intervals.append((newIntervals[interval - 1], newIntervals[interval]))

                quantized_value = midPoints[interval]
                quantized_signal.append(quantized_value)
                encoded_signal.append(interval)

            encoded_s = [format_interval(interval, num_bits) for interval in interval_numbers]
            quantized_signal = [round(sample, 2) for sample in quantized_signal]
            print(encoded_s)
            print(quantized_signal)
            quantization_error = sum(
                (original - quantized) ** 2 for original, quantized in zip(amplitudes, quantized_signal))

            output_label.config(
                text=f"Encoded Signal: {encoded_signal}\nQuantized Signal: {quantized_signal}\nQuantization Error: {quantization_error}")

            # Perform the test
            QuantizationTest1(file_path, encoded_s, quantized_signal)

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


def quantize_signal_levels():
    try:
        num_levels = int(bits_entry.get())
        file_path = r"F:\FCIS\Level 3\First term\DSP\Labs\Tasks\Task 1\tasksol\Quan2_input.txt"
        x, amplitudes = load_file(file_path)
        if amplitudes is not None:
            min_value = min(amplitudes)
            max_value = max(amplitudes)
            range_step = (max_value - min_value) / num_levels
            newIntervals = [min_value + i * range_step for i in range(num_levels)]
            midPoints = [interval + range_step / 2 for interval in newIntervals]
            encoded_signal = []
            quantized_signal = []
            interval_numbers = []  # Store the interval numbers
            intervals = []  # Store the intervals
            #print(midPoints)
            #print(amplitudes)
            for sample in amplitudes:
                interval = min(range(len(newIntervals)), key=lambda i: abs(midPoints[i] - sample))
                interval_numbers.append(interval+1)
                intervals.append((newIntervals[interval - 1], newIntervals[interval]))

                quantized_value = midPoints[interval]
                quantized_signal.append(quantized_value)
                encoded_signal.append(interval)

            encoded_s = [format_interval(interval-1, (int)(math.log2(num_levels))) for interval in interval_numbers]
            quantized_signal = [round(sample, 3) for sample in quantized_signal]
            print(interval_numbers)
            print(encoded_s)
            print(quantized_signal)
            quantization_error = [(quantized - original)  for original, quantized in zip(amplitudes, quantized_signal)]
            quantization_error = [round(sample, 3) for sample in quantization_error]
            print(quantization_error)

            output_label.config(
                text=f"Encoded Signal: {encoded_signal}\nQuantized Signal: {quantized_signal}\nQuantization Error: {quantization_error}")

            # Perform the test
            QuantizationTest2(file_path,interval_numbers, encoded_s, quantized_signal,quantization_error)

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
    with open(r"F:\FCIS\Level 3\First term\DSP\Labs\Tasks\Task 1\tasksol\Quan1_Out.txt", 'r') as f:
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


def QuantizationTest2(file_name, Your_IntervalIndices, Your_EncodedValues, Your_QuantizedValues, Your_SampledError):
    expectedIntervalIndices = []
    expectedEncodedValues = []
    expectedQuantizedValues = []
    expectedSampledError = []
    with open(r"F:\FCIS\Level 3\First term\DSP\Labs\Tasks\Task 1\tasksol\Quan2_Out.txt", 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 4:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = str(L[1])
                V3 = float(L[2])
                V4 = float(L[3])
                expectedIntervalIndices.append(V1)
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                expectedSampledError.append(V4)
                line = f.readline()
            else:
                break
    if (len(Your_IntervalIndices) != len(expectedIntervalIndices)
            or len(Your_EncodedValues) != len(expectedEncodedValues)
            or len(Your_QuantizedValues) != len(expectedQuantizedValues)
            or len(Your_SampledError) != len(expectedSampledError)):
        print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_IntervalIndices)):
        if (Your_IntervalIndices[i] != expectedIntervalIndices[i]):
            print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return

    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one")
            return
    for i in range(len(expectedSampledError)):
        if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
            continue
        else:
            print("QuantizationTest2 Test case failed, your SampledError have different values from the expected one")
            return
    print("QuantizationTest2 Test case passed successfully")


# Create main window
root = tk.Tk()
root.title("Signal Quantization")

# # Number of Bits Entry
# bits_label = tk.Label(root, text="Number of Bits:")
# bits_label.pack()
# bits_entry = tk.Entry(root)
# bits_entry.pack()
#
# # Quantize Button
# quantize_button = tk.Button(root, text="Quantize Signal", command=quantize_signal_bits)
# quantize_button.pack()
#
# # Output Label
# output_label = tk.Label(root, text="")
# output_label.pack()


#level Quantization

# Number of Levels Entry
bits_label = tk.Label(root, text="Number of Levels:")
bits_label.pack()
bits_entry = tk.Entry(root)
bits_entry.pack()

# Quantize Button
quantize_button = tk.Button(root, text="Quantize Signal", command=quantize_signal_levels)
quantize_button.pack()

# Output Label
output_label = tk.Label(root, text="")
output_label.pack()

# Start the main loop
root.mainloop()