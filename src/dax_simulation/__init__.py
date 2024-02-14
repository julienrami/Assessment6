import pandas as pd

def remove_whitespace_from_columns(df, columns):
    """
    Remove leading and trailing whitespaces from specified columns in a DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - columns (list): List of column names to remove whitespaces from.

    Returns:
    - pd.DataFrame: Modified DataFrame.
    """
    for column in columns:
        df[column] = df[column].str.strip()

    return df

def whitespace(filepath, columns_to_strip=['role', 'name']):
    """
    Read CSV file, remove whitespace from specified columns, and save the modified DataFrame back to the CSV file.

    Parameters:
    - filepath (str): Path to the CSV file.
    - columns_to_strip (list): List of column names to remove whitespaces from.

    Returns:
    - None
    """
    # Read CSV file into DataFrame
    df = pd.read_csv(filepath)

    # Remove whitespace from specified columns
    df = remove_whitespace_from_columns(df, columns_to_strip)

    # Save the modified DataFrame back to the CSV file
    df.to_csv(filepath, index=False)



