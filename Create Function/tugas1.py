"""
1. Create a function that converts temperature from Celsius to Fahrenheit and vice versa. The function accepts two parameters, namely the temperature value and the temperature unit ('C' for Celsius, 'F' for Fahrenheit).
"""

def conferts_temperature(value,unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        return "unit harus 'C' atau 'F'."

input_value = float(input("Masukkan nilai suhu: "))
input_unit = input("Masukkan satuan suhu C/F (Gunakan Huruf Kapital): ")
print(conferts_temperature(input_value, input_unit))