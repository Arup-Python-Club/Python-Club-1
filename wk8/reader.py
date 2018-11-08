import os
import json
import pickle
import numpy
import pandas

PATH = os.getcwd()


# This function should read the contents of a .txt file
def read_txt(file):
    # Start here:
    # https://www.tutorialspoint.com/python/file_readlines.htm
    with open(file, 'r') as f:
        contents = f.readlines()
        return contents


# This should write a list of data to txt as one line per list element
def write_txt(arr):
    # https://www.tutorialspoint.com/python/file_writelines.htm
    with open('new_data.txt', 'w') as out:
        out.writelines(arr)


# This function should read the contents of a .json file
def read_json(file):
    # https://docs.python.org/2/library/json.html
    return


# This should write some standard data to JSON
def write_json(data):
    return


# This function should read the contents of a .pkl file
def read_pickle(file):
    # https://wiki.python.org/moin/UsingPickle
    return


# This should write some arbitrary data to a pkl file
def write_pickle(data):
    return


# One of the things that we often need to do in scripts is read and write data of various formats.
# I've given you some real data from a project I'm working on at this moment. Your goal is to read those various data
# types and print their contents. Once you've done that, make the edits specified below and then write the new data
# in the same format.

# The pickle file will be the trickiest. I've given you the functions necessary to read the contents of a pandas
# DataFrame. Pandas is a tool to manipulate tabular data that we use a lot. You don't need to worry about this one as
# much, just be aware that this is a powerful tool for more complex data.

# For the txt file, add the following block of text to the bottom of the file. You can hard code this, read the data as
# a list, or whatever makes sense to you.

""""
WaterUse:Equipment,
  Water Fixture 2,                        !- Name
  General,                                !- End-Use Subcategory
  2.04778159473489e-006,                  !- Peak Flow Rate {m3/s}
  DHW Usage,                              !- Flow Rate Fraction Schedule Name
  Floor Hot Water;                        !- Target Temperature Schedule Name
"""
# Todo:
# For the json file, edit the email key to be your email.
# Todo:
# For the pickle file, things are a bit more complicated. The contents are a pandas DataFrame. If you get to this point,
# Add any arbitrary data to the end of the pandas dataframe and pickle it.

# This is for the txt file. You don't need to do anything to this code, but it's here
# to help you figure out how the data flows. The JSON and pickle workflows should look very similar.

txt_data = read_txt(PATH + '\\data.txt')

print(txt_data)

append_data = [
    'WaterUse:Equipment,',
    '  Water Fixture 2,                        !- Name',
    '  General,                                !- End-Use Subcategory',
    '  2.04778159473489e-006,                  !- Peak Flow Rate {m3/s}',
    '  DHW Usage,                              !- Flow Rate Fraction Schedule Name',
    '  Floor Hot Water;                        !- Target Temperature Schedule Name',
]

txt_data += append_data
write_txt(txt_data)

# Todo:
# This is where you'll work for the JSON and pickle data:
