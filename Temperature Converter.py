print("Welcome to Temperature Converter")
def menu():
    print("""Convert
1. Celsius to Fahrenheit
2. Celsius to Kelvin
3. Fahrenheit to Celsius
4. Fahrenheit to Kelvin
5. Kelvin to Celsius
6. Kelvin to Fahreheit""")
def case():
    a=int(input("Enter your choice:"))
    match (a):
        case 1:
            Celsius=int(input("Enter Value of Celsius"))
            Fahrenheit=Celsius *9/5+32
            print("Temperature in Fahrenheit",Fahrenheit)
        case 2:
            Celsius=int(input("Enter Value of Celsius"))
            Kelvin=Celsius + 273.15
            print("Temperature in Kelvin",Kelvin)
        case 3:
            Fahrenheit=int(input("Enter Value of Fahrenheit"))
            Celsius=(Fahrenheit-32)*(5/9)
            print("Temperature in Celsius",Celsius)
        case 4:
            Fahrenheit=int(input("Enter Value of Fahrenheit"))
            Kelvin=(Fahrenheit+459.67)*(5/9)
            print("Temperature in Kelvin",Kelvin)
        case 5:
            Kelvin=int(input("Enter Value of Kelvin"))
            Celsius=Kelvin-273.15
            print("Temperature in Celsius",Celsius)
        case 6:
            Kelvin=int(input("Enter Value of Kelvin"))
            Fahrenheit=(Kelvin*(9/5))-459.67
            print("Temperature in Fahrenheit",Fahrenheit)
            
print(menu())
print(case())
