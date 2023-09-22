"""

Author: Vinay Williams
Date: 2023-09-23
Description: This is a simple program to calculate the mass flow rate of a gas at a given temperature and pressure

"""


import tkinter as tk
from tkinter import ttk
import CoolProp.CoolProp as CP
import pyfluids

gas_names = {"Nitrous": "N2O",
             "Oxygen": "O2",
             "Propane": "C3H8",
             "Butane": "C4H10",
             "Methane": "CH4"}


def calculate():
    selected_gas = gas_var.get()
    temperature = float(temperature_entry.get())
    pressure = float(pressure_entry.get())

    normalised_fr = float(flowrate_entry.get())
    fr = normalised_fr / (pressure * (273.15 / (273.15 + temperature)))
    fr_ls = fr / 60
    fr_m3s = fr_ls * 0.001

    density = CP.PropsSI(
        "D", "T", temperature + 273.15, "P", pressure * 100000, gas_names[selected_gas]
    )

    m_dot = fr_m3s * density * 1000

    result_label.config(text=f"Mass Flow Rate: {m_dot:.4f} g/s")


root = tk.Tk()
root.title("Gas Density Calculator")

gas_label = ttk.Label(root, text="Select Gas:")
gas_label.pack()

gases = list(gas_names.keys())
gas_var = tk.StringVar()
gas_dropdown = ttk.Combobox(root, textvariable=gas_var, values=gases)
gas_dropdown.pack()

temperature_label = ttk.Label(root, text="Temperature (Deg C):")
temperature_label.pack()
temperature_entry = ttk.Entry(root)
temperature_entry.pack()

pressure_label = ttk.Label(root, text="Pressure (Bar(A)):")
pressure_label.pack()
pressure_entry = ttk.Entry(root)
pressure_entry.pack()

flowrate_label = ttk.Label(root, text="Flow Rate(NL/min)")
flowrate_label.pack()
flowrate_entry = ttk.Entry(root)
flowrate_entry.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
