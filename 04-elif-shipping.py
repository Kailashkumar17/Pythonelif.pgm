#based on the destination of thr package logic

destination=input("\nEnter the destination address : ")

#Shipping for domestic rate is 100rs
domestic_rate = 100

#Shpping for international rate depends on weight and chargs 30 rs per kg
international_rate_per_kg= 30

if destination == "Bangalore":
    shipping_cost=domestic_rate
elif destination=="Chennai":
    shipping_cost=domestic_rate
else:
    weight=float(input("\nEnter the weight in kg : "))
    shipping_cost=domestic_rate+(weight*international_rate_per_kg)

print("The shipping cost to " , destination , "is : Rs " , shipping_cost)
