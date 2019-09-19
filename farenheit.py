'''
Created on 16 sept. 2019

@author: david
'''

def fahrenheit_to_celsius(temperature_fahrenheit):
    return (temperature_fahrenheit - 32) / 1.8


temperature_saisie = input("Température Fahrenheit ? ")
temperature_fahrenheit = float(temperature_saisie)
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
print(f"Une température de {temperature_fahrenheit:.1f}°F \
correspond à {temperature_celsius:.1f}°C")
