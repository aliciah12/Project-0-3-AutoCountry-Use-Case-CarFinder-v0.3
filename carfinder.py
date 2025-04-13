# Define the dataset
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Define a function to display the menu and handle user input

def display_menu():
    while True:
        print("\n=== CarFinder MENU ===\n")
        print("1. PRINT all Allowed Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. Exit")

# Get the user's choice
choice = input("Enter your choice (1-4): ")
if choice == '1':
    print("\nAllowed Vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
elif choice == '2':
    search_vehicle = input("Enter the vehicle name to search: ")
    if search_vehicle in AllowedVehiclesList:
        print(f"{search_vehicle} is an authorized vehicle.")
    else:
        print(f"{search_vehicle} is not an authorized vehicle.")
elif choice == '4':
    print("Exiting the program. Goodbye!")
    
# Main program execution
if __name__ == "__main__":
    display_menu()