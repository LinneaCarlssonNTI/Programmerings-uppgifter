def celsius_till_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

celsius = int(input("Hur många grader celsius är det?"))
print(celsius_till_fahrenheit(celsius))