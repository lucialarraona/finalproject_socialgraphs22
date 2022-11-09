
import bz2
import pickle
import _pickle as cPickle
import ast





# Convert list stored as string to actual string object 
def convert_type(string):
    a_list = ast.literal_eval(string) 
    return a_list


# Pickle a file and then compress it into a file with extension 
def compressed_pickle(title, data):
 with bz2.BZ2File(title + '.pbz2', 'w') as f: 
    cPickle.dump(data, f)


# Load any compressed pickle file
def decompress_pickle(file):
 data = bz2.BZ2File(file, 'rb')
 data = cPickle.load(data)
 return data