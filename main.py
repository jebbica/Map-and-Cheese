# Create an intro message for the user :) Come up with a good name
# name -> Map & Cheese
print("\n--------------------Map & Cheese----------------------")
print("Welcome to Map & Cheese! Been around since '21")
print("Visit our website -> 222.mapandcheese.com")
print("Our business hours are at the bottom of our page :)")
print("------------------------------------------------------\n")


# We want to ask the user for their first and last name and age
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print(f"Full Name: {first_name} {last_name}\n")
correct_name = input("Is your name entered correctly? ") 
if(correct_name == "no"):
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print(f"Updated Full Name: {first_name} {last_name}\n")


age = int(input("\nEnter your age: "))
correct_age = input("Is your age entered correctly? ")
if(correct_age != "yes"):
    age = int(input("Enter your age: "))
    print(f"Updated Age: {age}\n")




# We want to ask the user for their phone number
phone_number = input("Enter your phone number: ")
print(f"Phone Number: {phone_number}\n")
correct_number = input("Is your phone number entered correctly? ")
if(correct_number != "yes"):
    phone_number = int(input("Enter your phone number: "))
    print(f"Updated Phone Number: {phone_number}\n")



# We want to ask the user if they want takeout or delivery
takeout_deliv = input("\nWould you like to order for takeout or delivery? ")
print(f"Ordering for {takeout_deliv}\n")




# We want to ask what cuisine they want
cuisine = input("What kind of cuisine would you like? ")
print(f"Checking for {cuisine} food. \n")




# We want to ask the user for their current address
address = input("Enter your address: ")
print(f"Your Address: {address}")
correct_address = input("\nIs your address entered correctly? ")
if(correct_address != "yes"):
    address = input("Enter your address: ")
    print(f"Updated Address: {address}\n")


# Calculating Distances...
print("\nCalculating Distances...")
