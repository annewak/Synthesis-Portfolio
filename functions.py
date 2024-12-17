# Celsius to fahrenheit -> (C * 9/5) + 32
#Fahrenheit to celsius -> (F-32) * 5/9

temp = int(input("Enter the temperature: "))
scale = input("In celsius or fahrenheit? Enter 'C' or 'F'.")


if scale == 'F':
    print((temp - 32) * (5/9)), "C")

if scale == 'C':
    print((temp * 9/5) + 32, "F")
        
