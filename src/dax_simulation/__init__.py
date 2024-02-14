import pandas as pd

def whitespace(filepath):
    # Read CSV file into DataFrame
    df = pd.read_csv(filepath)

    # Remove whitespace from specified columns
    df['role'] = df['role'].str.strip()
    df['name'] = df['name'].str.strip()

    # Save the modified DataFrame back to the CSV file
    df.to_csv(filepath, index=False)
