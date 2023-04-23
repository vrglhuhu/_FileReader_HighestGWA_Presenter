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
# Open the file
with open("name_gwa_data.txt", "r") as file_handle:
  # Read the file line by line
  lines = file_handle.readlines()
# Initialize the highest GWA
highest_gwa = 0
# Iterate over the lines
for line in lines:
  # Split the line into name and GWA
  name, gwa = line.split()
  # Convert the GWA to float
  # Compare the GWA with the highest GWA
    # Update the highest GWA
    # Update the name
# Print the result
# Create Footer

