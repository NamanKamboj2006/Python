# Write a python program using function to convert Celsius to Fahrenheit.

def CTF(x):
    # (0°C × 9/5) + 32
    F = (x*(9/5)) + 32;
    return F

x = int(input("Enter Temp In Celsius: "))
print(f"Fahrenheit: {CTF(x)}")