print("==============================")
print("     SMART ENERGY MONITOR")
print("==============================")

voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))

power = voltage * current

hours = float(input("Enter usage time (hours): "))

energy = (power * hours) / 1000

rate = float(input("Enter electricity rate (₹ per kWh): "))

cost = energy * rate

print("\n------ ENERGY DETAILS ------")
print("Voltage          :", voltage, "V")
print("Current          :", current, "A")
print("Power            :", power, "W")
print("Energy Consumed  :", energy, "kWh")
print("Estimated Cost   : ₹", cost)
print("----------------------------")

 