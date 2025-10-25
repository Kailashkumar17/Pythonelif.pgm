print("\nHumidity:low, Temperature:high")

humidity=input("\nEnter the Humidity :")
temperature=input("\nEnter the Temperature :")

if humidity=="low" and temperature=="low":
    print("Welcome to the Hot desert")
elif humidity=="high" and temperature=="low":
    print("Welcome to the Artic area")
elif humidity=="low" and temperature=="high":
    print("Welcome to the Heavy rainfall area")
else:
    print("Data is not available")
