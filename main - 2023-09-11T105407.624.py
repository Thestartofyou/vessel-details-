# Initialize an empty dictionary to store mooring information
moorings = {}

# Function to add a new mooring
def add_mooring():
    mooring_number = input("Enter mooring number: ")
    boat_name = input("Enter boat name: ")
    owner_name = input("Enter owner name: ")
    contact_number = input("Enter contact number: ")

    # Collect vessel details
    vessel_details = {}
    vessel_details['Vessel Type'] = input("Enter vessel type: ")
    vessel_details['Vessel Size'] = input("Enter vessel size: ")
    vessel_details['Registration Number'] = input("Enter registration number: ")

    # Create a mooring entry in the dictionary with vessel details
    moorings[mooring_number] = {
        'Boat Name': boat_name,
        'Owner Name': owner_name,
        'Contact Number': contact_number,
        'Vessel Details': vessel_details  # Include vessel details
    }
    print(f"Mooring {mooring_number} added successfully!")

# Function to view mooring information
def view_mooring():
    mooring_number = input("Enter mooring number to view details: ")
    mooring = moorings.get(mooring_number)

    if mooring:
        print(f"Mooring Number: {mooring_number}")
        print(f"Boat Name: {mooring['Boat Name']}")
        print(f"Owner Name: {mooring['Owner Name']}")
        print(f"Contact Number: {mooring['Contact Number']}")
        
        # Display vessel details
        vessel_details = mooring.get('Vessel Details', {})
        print("Vessel Details:")
        print(f"Vessel Type: {vessel_details.get('Vessel Type', 'N/A')}")
        print(f"Vessel Size: {vessel_details.get('Vessel Size', 'N/A')}")
        print(f"Registration Number: {vessel_details.get('Registration Number', 'N/A')}")
    else:
        print(f"Mooring {mooring_number} not found.")

# Function to list all moorings
def list_moorings():
    if moorings:
        print("List of Moorings:")
        for mooring_number, mooring_info in moorings.items():
            print(f"Mooring Number: {mooring_number}")
            print(f"Boat Name: {mooring_info['Boat Name']}")
            print(f"Owner Name: {mooring_info['Owner Name']}")
            print(f"Contact Number: {mooring_info['Contact Number']}")
            
            # Display vessel details
            vessel_details = mooring_info.get('Vessel Details', {})
            print("Vessel Details:")
            print(f"Vessel Type: {vessel_details.get('Vessel Type', 'N/A')}")
            print(f"Vessel Size: {vessel_details.get('Vessel Size', 'N/A')}")
            print(f"Registration Number: {vessel_details.get('Registration Number', 'N/A')}")
            print()
    else:
        print("No moorings found in the harbor.")

# ... (rest of the code remains the same)

