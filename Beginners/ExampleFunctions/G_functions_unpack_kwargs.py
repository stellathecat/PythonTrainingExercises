#!/usr/bin/env python
"""Illustrates Python function keyword arguments packing and unpacking.

Created on Aug 25, 2011

@author: paulross
"""

# F:
# How to use a single asterisk (*) to unpack iterables
# How to use two asterisks (**) to unpack dictionaries

def unpackKwargs(**kwargs):
    keys = kwargs.keys()
    # keys.sort() # 'dict_keys' object has no attribute 'sort'
    keys = sorted(keys)
    for kw in keys:
        print(kw, ":", kwargs[kw])

def main():
    print('callUnpackKwargs():')
    print('Specific arguments:')
    # unpackKwargs('python', 2.6) # this does not work
    unpackKwargs(name='python', version=2.6)
    d = {
        'name' : 'python',
        'version' : 2.6,
    }
    print
    print('Unpacked arguments:')
    unpackKwargs(**d)

if __name__ == '__main__':
    main()
