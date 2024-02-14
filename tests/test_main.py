#check whether there is whitespace on my column 

import csv
import os
import pytest
import pandas as pd

from dax_simulation import whitespace

@pytest.fixture(scope="module")
def stock_file():
    with open('stock_data.csv', 'w', newline='') as stock_file:
        fieldnames = ['role', 'name']
        stock_writer = csv.DictWriter(stock_file, fieldnames=fieldnames)
        stock_writer.writeheader()
        stock_writer.writerow({'role' : 'visualiser ', 'name' : ' Harry'})
    yield
    os.remove('stock_data.csv')


def test_whitespace (stock_file):
    # Arrange - set up input and expected output
    filepath = 'stock_data.csv'
    expected_role_length = 10
    expected_name_length = 5

    #Act
    report_data = read_csv(filepath)

    #Assert
    assert len(report_data['role']) == expected_role_length
    assert len(report_data['name']) == expected_name_length

print(stock_file)
