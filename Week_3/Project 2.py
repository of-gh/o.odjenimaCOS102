print("Welcome to the Izifin Technology Staff Annual Tax Revenue Calculator.\nPlease Login Below:")
name = input("\nStaff Full name: ")
age = int(input("Age: "))
yrsofexp = int(input("Years of Experience: "))

if (yrsofexp > 25) and (age >= 55):
    print("\n------------------------------------------")
    print("\nName: ",name)
    print(f"Age: {age} years old")
    print("Years of Experience: ",yrsofexp)
    print("ATR = 5,600,000")
elif (yrsofexp > 20) and (age >= 45):
    print("\n------------------------------------------")
    print("\nName: ",name)
    print(f"Age: {age} years old")
    print("Years of Experience: ",yrsofexp)
    print("ATR = 4,480,000")
elif (yrsofexp > 10) and (age >= 35):
    print("\n------------------------------------------")
    print("\nName: ",name)
    print(f"Age: {age} years old")
    print("Years of Experience: ",yrsofexp)
    print("ATR = 1,500,000")
elif (yrsofexp < 10) and (age < 35):
    print("\n------------------------------------------")
    print("\nName: ",name)
    print(f"Age: {age} years old")
    print("Years of Experience: ",yrsofexp)
    print("ATR = 550,000")
else :
    print("Sorry we either dont have staff like you or you aren't eligible for ATR. Maybe try again")

    