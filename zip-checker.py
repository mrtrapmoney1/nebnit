import csv

def load_zipcodes(filename="Zipcodes Metro TV.xlsx - Sheet1.csv"):
    """
    Loads zip code data from a CSV file into a dictionary.

    Args:
        filename (str): The name of the CSV file to read.

    Returns:
        dict: A dictionary where keys are zip codes and values are location data.
              Returns an empty dictionary if the file is not found or an error occurs.
    """
    zip_data = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip header row
            for row in reader:
                if row:
                    # Assumes the zip code is in the first column
                    # and the rest of the data is in the subsequent columns.
                    zip_code = row[0].strip()
                    # The second column contains 'zipcode+city'
                    location_info = row[1].strip() if len(row) > 1 else ""
                    zip_data[zip_code] = location_info
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return zip_data

def check_service_area(zip_data):
    """
    Allows a user to repeatedly check if a zip code is in the service area.
    """
    while True:
        print("\n--- Service Area Checker ---")
        zip_code_input = input("Enter your 5-digit zip code (or 'quit' to exit): ").strip()

        if zip_code_input.lower() == 'quit':
            print("Thank you for using the Service Area Checker!")
            break

        if not zip_code_input.isdigit() or len(zip_code_input) != 5:
            print("Invalid input. Please enter a valid 5-digit zip code.")
            continue

        if zip_code_input in zip_data:
            location_info = zip_data[zip_code_input]
            print(f"✅ Great news! We service the {zip_code_input} area ({location_info}).")
        else:
            print(f"❌ Sorry, we do not currently service the {zip_code_input} area.")

if __name__ == "__main__":
    # Load the zip code data from the CSV file.
    # Make sure the CSV file is in the same directory as this script,
    # or provide the full path to the file.
    service_zipcodes = load_zipcodes()

    if service_zipcodes:
        # If the zip codes were loaded successfully, start the checker.
        check_service_area(service_zipcodes)
    else:
        print("Could not load service area data. Exiting.")
