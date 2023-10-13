import numpy as np
import matplotlib.pyplot as plt

# Open the file and read its contents
with open("test.txt", "r") as file_object:
    data = file_object.readlines()

#Discrete plot function
def discretePlot():
    # Initialize empty lists to store indices and amplitudes
    indices = []
    amplitudes = []

    # Loop through each line in the data
    for line in data[3:]:
        parts = line.strip().split()
        index = int(parts[0])
        amplitude = float(parts[1])
        indices.append(index)
        amplitudes.append(amplitude)

    # Plot the signal
    plt.figure(figsize=(10, 4))
    plt.stem(indices, amplitudes)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('Signal x(n)')
    plt.grid(True)
    plt.show()


if data[0].strip() == "0":
    discretePlot()
elif data[0].strip() == "1":
    print("Write continous function here")


