def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


# Convert the boiling point of water
water_bp = celsius_to_fahrenheit(100)
print(water_bp)  # 212.0
_bp = celsius_to_fahrenheit(int(input("Enter any specific temperature: ")))
print(_bp)

def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f -32)* 5 / 9
    return round(temps_c, 3)

_bp = fahrenheit_to_celsius(int(input()))
print(_bp)