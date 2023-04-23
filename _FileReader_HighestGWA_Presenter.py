# Vergel, Chean Bernard Villanueva
# Assignment No. 4
# Question No. 2

# Create Header
import pyfiglet

print("")
print("=" * 80)
print("")
welcome = pyfiglet.figlet_format("Welcome to my space".center(57, " "), font="digital")
print(welcome)
print("")
print("=" * 80)
print("\033[33mHi, I am Chean Bernard V. Vergel a first year college student at Polytechnic University of the Philippines.\033[0m")
print("")

# Ask for the name of the user
name_user = input("\033[40mHow about you what is your name? \033[0m")
print("")
print(f"\033[40m\033[33mHi, {name_user}! I welcome you on this program. \033[0m")
print("")

# Stating the purpose of this program
print("\033[40m\033[35mThis program will output the highest GWA together with the name.\033[0m")
print("")

# Open the file
with open("name_gwa_data.txt", "r") as file_handle:
  
  # Read the file line by line
  lines = file_handle.readlines()

# Initialize the highest GWA
highest_gwa = 5

# Iterate over the lines
for line in lines:
  
  # Split the line into name and GWA
  name, gwa = line.split(",")

  # Convert the GWA to float
  gwa = float(gwa)

  # Compare the GWA with the highest GWA
  if gwa < highest_gwa :

    # Update the highest GWA
    highest_gwa = gwa

    # Update the name
    highest_name = name

# Print the result
print(f"\033[40m\033[34mThe student with the highest GWA is", highest_name, "with a GWA of", highest_gwa, ".\033[0m")
print("")
print("")

# Creating column for the names and GWA
print("\033[40mHere is the list:\033[0m")
print("")
with open("name_gwa_data.txt") as column_file:
  print("\033[0;32m{:<30}{:<30}".format("Student Name", "GWA"))
  for line in column_file:
    name, gwa = line.split(",")
    column_name = name
    column_gwa = gwa
    print("\033[0;38m{:<30}{:<30}".format(column_name, column_gwa))

# Create Footer
print("")
print(f"\033[40m\033[33mThank you for your time, {name_user}! \033[0m")
print("")
goodbye = pyfiglet.figlet_format("Visit me again", font = "digital" )
print (goodbye)
print("")

