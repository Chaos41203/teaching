while(True):

    temp_type = input("Please input temperature type [C (celsius) or F (fahrenheit)] :\n")

    if temp_type in ['C', 'celsius']:

        celsius_temp = input("Please input temperature :\n")
        fahrenheit_temp = int(celsius_temp) * 1.8 + 32
        print("Your input (Celsius):", celsius_temp)
        print("Transformed value :", fahrenheit_temp)

    elif temp_type in ['F', 'fahrenheit']:

        fahrenheit_temp = input("Please input temperature :\n")
        celsius_temp = (int(fahrenheit_temp) - 32) / 1.8
        print("Your input (Fahrenheit):", fahrenheit_temp)
        print("Transformed value :", celsius_temp)

    else:

        print("Please input C, F, celsius or fahrenheit.")

