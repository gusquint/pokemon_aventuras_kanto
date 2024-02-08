from docx import Document
import csv

def read_docx(file_path):
    try:
        # Load the .docx file
        doc = Document(file_path)
        
        # Extract text from paragraphs and store in a list
        paragraphs = [paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()]
        
        return paragraphs
    except Exception as e:
        print(f"Error reading the .docx file: {e}")
        return None
    
    
def create_dictionary_list(input_list):
    try:
        # Check if the length of the input list is a multiple of 7
        if len(input_list) % 7 != 0:
            raise ValueError("Input list length is not a multiple of 7")

        # Initialize variables
        dictionaries_list = []
        
        # Iterate over the input list with a step of 7
        for i in range(0, len(input_list), 7):
            # Extract key-value pairs from every 7 entries
            key_value_pairs = input_list[i:i + 7]
            
            # Create a dictionary from key-value pairs
            dictionary = dict(pair.split(': ', 1) for pair in key_value_pairs)
            
            # Append the dictionary to the list
            dictionaries_list.append(dictionary)
        
        return dictionaries_list
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    
    
def organize_dictionaries(input_list):
    # Define the desired order of keys
    order_of_keys = ['Nombre', 'Movimiento', 'Tipo', 'PP', 'Precision', 'Damage', 'Efecto']

    # Create a new list of dictionaries with the desired order of keys
    organized_list = [{key: dictionary[key] for key in order_of_keys} for dictionary in input_list]

    return organized_list


def create_csv_from_dictionaries(input_list, output_file):
    # Extract keys from the first dictionary in the list
    fieldnames = input_list[0].keys()

    # Write dictionaries to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        
        # Write the header row
        writer.writeheader()

        # Write each dictionary as a row in the CSV file
        writer.writerows(input_list)





if __name__ == "__main__":
    # Replace 'your_file.docx' with the actual path to your .docx file
    file_path = 'movimientos pokemon.docx'
    
    # Read the content of the .docx file
    document_content = read_docx(file_path)
    
    # Create a list of dictionaries
    result = create_dictionary_list(document_content)
    
    # Organize the list of dictionaries
    organized_list = organize_dictionaries(result)

    # Replace 'output_file.csv' with the desired name for the CSV file
    output_file = 'movimientos pokemon.csv'

    # Create CSV file from list of dictionaries
    create_csv_from_dictionaries(organized_list, output_file)

    print(f"CSV file '{output_file}' created successfully.")
    
    
            