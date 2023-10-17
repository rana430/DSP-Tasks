import matplotlib.pyplot as plt
import numpy as np

# Open the file and read its contents
with open("test.txt", "r") as file_object:
    data = file_object.readlines()

indices = []
amplitudes = []
def parseDatainTimeDomain():

    # Parse data
    for line in data[3:]:
        parts = line.strip().split()
        index = int(parts[0])
        amplitude = float(parts[1])
        indices.append(index)
        amplitudes.append(amplitude)


n_samples = int(data[2].strip())


# Discrete plot function
def discretePlot():
    # Plot the signal
    plt.figure(figsize=(10, 4))
    plt.stem(indices, amplitudes)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('Signal x(n)')
    plt.grid(True)
    plt.show()


def discreteToContinuous():
    continuous_indices = np.linspace(0, n_samples, n_samples * 10)
    continuous_signal = np.interp(continuous_indices, indices, amplitudes)
    # Plot the original discrete signal and the continuous signal
    plt.figure(figsize=(10, 4))
    plt.stem(indices, amplitudes, markerfmt='ro', linefmt='r-', basefmt='r-', label='Original Discrete Signal')
    plt.plot(continuous_indices, continuous_signal, label='Continuous Signal (Interpolated)')
    plt.xlabel('Sample/ Time')
    plt.ylabel('Amplitude')
    plt.title('Discrete to Continuous Signal')
    plt.grid(True)
    plt.legend()
    plt.show()


if data[0].strip() == "0":
    parseDatainTimeDomain()
    discretePlot()
    discreteToContinuous()
    print("function")
elif data[0].strip() == "1":
    print("Write continous function here")

# import tkinter as tk
# from tkinter import *
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
#
# #Create the main window
# root = ttk.Window(themename="superhero")
# root.title("Signal Generator")
# root.eval("tk::PlaceWindow . center")
# bgColor="#eee"
# # Create a frame to contain the input fields
# frame = tk.Frame(root,width=700,height=600,bg=bgColor)
# frame.grid(row=0,column=0)
# frame.pack_propagate(False)
#
# # Signal type selection
# signal_var = tk.StringVar(value="Sine")
# signal_label = tk.Label(frame, text="Select Signal Type:",bg=bgColor)
# signal_label.grid(row=0, column=0)
# sine_checkbutton = Checkbutton(frame, text="Sine", variable=signal_var, onvalue="Sine",bootstyle="success").grid(row=1,column=1,sticky=W)
# cosine_checkbutton = Checkbutton(frame, text="Cosine", variable=signal_var, onvalue="Cosine",bg=bgColor).grid(row=2,column=1,sticky=W)
#
# # Amplitude Entery
# amp_label = tk.Label(frame, text="Amplitude (A):",bg=bgColor)
# amp_label.grid(row=3, column=0)
# amp_entry = tk.Entry(frame)
# amp_entry.grid(row=3, column=1)
#
# #Angular frequancy entry
# AFreq_label = tk.Label(frame, text="Angular Frequency (F):",bg=bgColor)
# AFreq_label.grid(row=4, column=0)
# AFreq_entry = tk.Entry(frame)
# AFreq_entry.grid(row=4, column=1)
#
#
# root.mainloop()
