"""We have an existing dictionary that maps US states to their capitals.

1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?

Implement the function def get_state(capital): below so it returns the state.

GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

Created on 3 Mar 2015

@author: paulross
"""
import sys

import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}


def capital_of_Idaho():
    return STATES_CAPITALS['Idaho']

def all_states():
    for i in STATES_CAPITALS.keys():
        print(i)

def all_capitals():
    for i in STATES_CAPITALS.values():
        print(i)

def states_capitals_string():
    import pandas
    xx = pandas.concat([pandas.Series(STATES_CAPITALS.keys()), 
                        pandas.Series(STATES_CAPITALS.values())], axis=1)
    xx.columns = ['Fritz','Box']
    # xx.iterrows()
    # xx.index
    # xxx = xx.iloc[3,] # xxx.shape
    
    xxx = xx['Fritz'] + " -> " + xx["Box"] # Series
    # " ".join(xxx)

    # for keys, values in STATES_CAPITALS:
    #    print(keys)
    # Your code here
    return list(xxx)


def get_state(capital):
    # for i, v in STATES_CAPITALS.items():
    #    print(i + " -> " + v)
    pass



def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())
