# Airline Ticket Booking System

base_price = 5000

print("Choose ticket class:")
print("1. Economy")
print("2. Premium Economy")
print("3. Business")

Setting_class = int(input("Enter your choice (1/2/3): "))

if Setting_class == 1:
    class_name = "Economy"
    class_multiplier = 1.0
elif Setting_class == 2:
    class_name = "Premium Economy"
    class_multiplier = 1.2
elif Setting_class == 3:
    class_name = "Business"
    class_multiplier = 1.4
else:
    print("Invalid class choice")
    exit()

days_remaining = int(input("Enter days remaining for boarding: "))
festival_input = input("Is it festival season? (yes/no): ").strip().lower()
festival_season = festival_input in ("yes", "y")

age = int(input("Enter your age: "))

price = base_price * class_multiplier

if days_remaining >= 30:
    price += price * 0.10
elif days_remaining < 7:
    price += price * 0.25

if festival_season:
    price += price * 0.20

if age > 60:
    price -= price * 0.15

print("\nTicket Details")
print("Class:", class_name)
print("Base Price:", base_price)
print("Final Price:", round(price, 2))
