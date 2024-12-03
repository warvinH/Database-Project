import csv
from pathlib import Path
import string

def clean_csv(input_file):
    input_path = Path(input_file)
    output_file = input_path.with_name(f"{input_path.stem}_cleaned{input_path.suffix}")  # Also a Path object
    #output_file = f"{input_path.stem}_cleaned{input_path.suffix}"  # Add "_cleaned" to the file name
    allowed_chars = set(string.printable) # Make a set of allowable characters
    lines_cleaned = 0

    # Opens the file with encoding utf-8 because MySQL supports utf-8 and errors='replace' to replace invalid characters
    with input_path.open(mode='r', encoding='utf-8', errors='replace') as infile:
        # Writes the cleaned file with encoding utf-8 and newline='' to make newline universal
        with output_file.open(mode='w', encoding='utf-8', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            for row in reader:
                cleaned_row = [''.join(filter(allowed_chars.__contains__, cell)) for cell in row]
                if row != cleaned_row:  # Check if cleaning was necessary
                    lines_cleaned += 1
                writer.writerow(cleaned_row)
    
    print(f"Cleaned CSV file saved as: {output_file}")
    print(f"Number of lines cleaned: {lines_cleaned}")

# Replace 'your_file.csv' with your actual file name
clean_csv('team_table.csv')

