import csv

def find_value_with_csv(csv_file_path: str, search_key: str):
    """
    Opens a CSV file and searches for a key match in the first column.
    
    Args:
        csv_file_path: Path to the CSV file.
        search_key: The string to match in the key column (column 0).
        
    Returns:
        The corresponding value from the value column (column 1), or None if not found.
    """
    try:
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            # Use csv.reader to iterate over rows
            reader = csv.reader(file)
            
            # Iterate through each row in the CSV
            for row in reader:
                # Skip empty rows that might appear in the CSV
                if not row:
                    continue
                
                # Check if the first column (index 0) matches the search_key
                # We also check that the row has at least two elements
                if len(row) >= 2 and row[0].strip().lower() == search_key.lower():
                    # Return the second column (index 1) value and stop searching
                    return row[1].strip()
                    
            # If the loop finishes without returning, the key was not found
            print(f"Key '{search_key}' not found in the CSV.")
            return None
            
    except FileNotFoundError:
        print(f"Error: File not found at {csv_file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# # --- Example Usage (Using the same 'key_data.csv' created above) ---
# key_to_find = "apple"
# value = find_value_with_csv(csv_data, key_to_find)

# print(f"\nSearching for key '{key_to_find}':")
# print(f"Result: {value}")
# # Output: Result: red