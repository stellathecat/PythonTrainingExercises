"""Create a function that reads a CSV file and return a list of dictionaries
where the keys are the names in the first row and each dict contains the values
in each subsequent row.

A CSV file 'data.csv' is provided.

Issues: What happens if the row is to long or two short?
What happens with duplicate names in the first row.

Stretch: Convert the DoB strings to actual Python datetime.dates.
 
Created on 18 Feb 2016

@author: paulross
"""
import csv

import pytest

def read_csv(file_name='data.csv'):
    import pandas as pd
    df = pd.read_csv('/Users/fd/Documents/GitHub/PythonTrainingExercises/Beginners/stdlib/csv/data.csv')
    # df.columns
    df['Ordinal'] = df['Ordinal'].astype("string")
    # a = df.iloc[1,]
    # a.to_string()
    # list(a.items())
    # a[::-1]
    # [df.iloc[i,::-1].to_dict() for i in range(df.shape[0])]
    return [df.iloc[i,::-1].to_dict() for i in range(df.shape[0])]

def test_read_csv():
    expected = [
        {'DoB': '08/18/2007', 'Name': 'Annabel', 'Ordinal': '1'},
        {'DoB': '08/19/2007', 'Name': 'Brian', 'Ordinal': '2'},
        {'DoB': '08/20/2007', 'Name': 'Charlie', 'Ordinal': '3'},
        {'DoB': '08/21/2007', 'Name': 'Derek', 'Ordinal': '4'},
        {'DoB': '08/22/2007', 'Name': 'Emily', 'Ordinal': '5'},
        {'DoB': '08/23/2007', 'Name': 'Fortune', 'Ordinal': '6'},
        {'DoB': '08/24/2007', 'Name': 'Gerald', 'Ordinal': '7'},
        {'DoB': '08/25/2007', 'Name': 'Harriet', 'Ordinal': '8'},
        {'DoB': '08/26/2007', 'Name': 'India', 'Ordinal': '9'}
    ]
    assert expected == read_csv()

def main():
    return pytest.main(__file__)

if __name__ == '__main__':
    main()
