import sys
import pandas as pd
import re

def clean_filename(name):
    if isinstance(name, str) and name != "nan":
        # Remove all non-alphanumeric characters (except underscores) and replace with underscores
        return re.sub(r'[^a-zA-Z0-9_]', '_', name)
    else:
        return "unknown_filename"

def extract_csv_by_batch(original_csv_file):
    # Load the original CSV file into a pandas DataFrame
    df = pd.read_csv(original_csv_file)

    # Iterate over unique values of "Batch Name" and create separate CSVs
    for batch_name in df['Batch Name'].unique():
        clean_batch_name = clean_filename(batch_name)
        batch_df = df[df['Batch Name'] == batch_name]
        output_file = f'{clean_batch_name}_output.csv'
        batch_df.to_csv(output_file, index=False)
        print(f'Saved {output_file}')

    print('Extraction completed!')

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        csv_files = sys.argv[1:]
    else:
        # Read from standard input (pipe)
        csv_files = sys.stdin.read().splitlines()

    if csv_files:
        for csv_file in csv_files:
            extract_csv_by_batch(csv_file)
    else:
        print("Usage: python script_name.py <path_to_csv1> [<path_to_csv2> ...] OR input from pipe")

