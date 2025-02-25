
# Case Study: Optimizing a File Processing Pipeline

# Scenario: We have a large CSV file containing customer data.  We need to process it efficiently, 
# extract relevant information, and store it in a more manageable format (e.g., a database or JSON).

# Best Practices Demonstrated:
# 1. Efficient File Handling (using iterators to avoid loading the entire file into memory)
# 2. Data Validation (checking data integrity before processing)
# 3. Error Handling (handling potential exceptions during file processing)
# 4. Modular Design (breaking down the task into smaller, reusable functions)
# 5. Logging (recording processing steps and errors for debugging and monitoring)
import csv
import logging
import json

# Configure logging
logging.basicConfig(filename='processing_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


def process_customer_data(filepath, output_filepath):
    """Processes customer data from a CSV file, validates data, and writes it to a JSON file."""

    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile) # Efficiently reads CSV as dictionaries
            customer_data = []
            for row in reader:
                # Data Validation
                try:
                    row['age'] = int(row['age']) #Check if age is an integer
                    if row['age'] < 0:
                        raise ValueError("Age cannot be negative")
                    customer_data.append(row)
                except ValueError as e:
                    logging.error(f"Error processing row: {row}. Error: {e}")
                    continue # Skip invalid rows

        # Write to JSON file
        with open(output_filepath, 'w') as jsonfile:
            json.dump(customer_data, jsonfile, indent=4)
        logging.info(f"Customer data processed and written to {output_filepath}")

    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")


# Example usage
input_file = 'customer_data.csv'
output_file = 'customer_data.json'

# Sample CSV data (replace with your actual data)
with open(input_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['customer_id', 'name', 'age', 'city'])
    writer.writerow(['1', 'Alice', '30', 'New York'])
    writer.writerow(['2', 'Bob', '25', 'London'])
    writer.writerow(['3', 'Charlie', '-5', 'Paris']) # Invalid age


process_customer_data(input_file, output_file)

