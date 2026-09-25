import tkinter as tk

window = tk.Tk()
window.title("Smart Energy Monitor")
window.geometry("400x450")


def calculate():
    try:
        voltage = float(voltage_entry.get())
        current = float(current_entry.get())
        hours = float(hours_entry.get())
        rate = float(rate_entry.get())

        if voltage <= 0 or current < 0 or hours < 0 or rate < 0:
            result.config(text="Please enter valid positive values")
            return

        power = voltage * current
        energy = (power * hours) / 1000
        cost = energy * rate

        result.config(
            text=f"Power: {power:.2f} W\n"
                 f"Energy: {energy:.2f} kWh\n"
                 f"Cost: ₹{cost:.2f}"
        )

    except ValueError:
        result.config(text="Please enter numbers only")


title = tk.Label(
    window,
    text="SMART ENERGY MONITOR",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

tk.Label(window, text="Voltage (V):").pack()
voltage_entry = tk.Entry(window)
voltage_entry.pack()

tk.Label(window, text="Current (A):").pack()
current_entry = tk.Entry(window)
current_entry.pack()

tk.Label(window, text="Usage Time (hours):").pack()
hours_entry = tk.Entry(window)
hours_entry.pack()

tk.Label(window, text="Rate (₹/kWh):").pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

tk.Button(
    window,
    text="CALCULATE",
    command=calculate
).pack(pady=20)
def reset():
    voltage_entry.delete(0, tk.END)
    current_entry.delete(0, tk.END)
    hours_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    result.config(text="Enter values and click Calculate")

tk.Button(window, text="RESET", command=reset).pack(pady=5)
result = tk.Label(
    window,
    text="Enter values and click Calculate",
    font=("Arial", 12)
)
result.pack()

window.mainloop()
