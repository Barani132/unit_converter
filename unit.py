# Simple Unit Converter

print("----- Unit Converter -----")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = input("Choose an option (1-4): ")

if choice == "1":
    km = float(input("Enter kilometers: "))
    print("Miles:", round(km * 0.621371, 2))

elif choice == "2":
    miles = float(input("Enter miles: "))
    print("Kilometers:", round(miles / 0.621371, 2))

elif choice == "3":
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", round((c * 9/5) + 32, 2))

elif choice == "4":
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", round((f - 32) * 5/9, 2))

else:
    print("Invalid choice.")
