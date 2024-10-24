choice = int(input("1. Convert from Fahrenheit to Celsius \n2. Convert from Celsius to Fahrenheit \nEnter your choice (1/2): "))

if choice == 1:
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Temperature in Celsius:", round(c))

elif choice == 2:
    c = float(input("Enter the temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print("Temperature in Fahrenheit:", round(f))

else:
    print("Please choose the correct option.")
