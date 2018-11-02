import os
import json
import pickle
import numpy
import pandas

PATH = os.getcwd()


# This function should read the contents of a .txt file
def read_txt(file):
    with open(file, 'r') as f:
        contents = f.readlines()
        return contents


# This should write a list of data to txt as one line per list element
def write_txt(arr):
    with open('new_data.txt', 'w') as out:
        out.writelines(arr)


# This function should read the contents of a .json file
def read_json(file):
    data = json.load(open(file))
    return data


# This should write some standard data to JSON
def write_json(data):
    with open('new_data.json', 'w') as out:
        json.dump(data, out)


# This function should read the contents of a .pkl file
def read_pickle(file):
    with open(file, 'rb') as f:
        contents = pickle.load(f)
        return contents


# This should write some arbitrary data to a pkl file
def write_pickle(data):
    with open('new_data.pkl', 'wb') as out:
        pickle.dump(data, out)


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

# For the json file, edit the email key to be your email.

# For the pickle file, things are a bit more complicated. The contents are a pandas DataFrame. If you get to this point,
# Add any arbitrary data to the end of the pandas dataframe and pickle it.

txt_data = read_txt(PATH + '\\data.txt')
json_data = read_json(PATH + '\\data.json')
pkl_data = read_pickle(PATH + '\\data.pickle')

print(txt_data)
print(json_data)
print(pkl_data)

append_data = [
    'WaterUse:Equipment,',
    '  Water Fixture 2,                        !- Name',
    '  General,                                !- End-Use Subcategory',
    '  2.04778159473489e-006,                  !- Peak Flow Rate {m3/s}',
    '  DHW Usage,                              !- Flow Rate Fraction Schedule Name',
    '  Floor Hot Water;                        !- Target Temperature Schedule Name',
]

txt_data += append_data
for d in json_data:
    d['email'] = 'new.email@arup.com'

pkl_data = pkl_data.append(
    {
        'ID': 'NEW',
        'Description': 'NEW',
        'Object': 'NEW',
        'Zone': 'NEW',
        'Variable': 'NEW',
        'Type': 'NEW',
        'Value': 'NEW',
        'Cost': 'NEW',
        'Exclude': None,
        'Include': None,
        'Global_Include': True,
    }, ignore_index=True
)

print(txt_data)
print(json_data)
print(pkl_data)

write_txt(txt_data)
write_json(json_data)
write_pickle(pkl_data)
