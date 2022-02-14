import pandas as pd
from typing import List, Dict, TextIO



def get_dic(filename:str) -> Dict:
    """ return a dictionary with keys from the report before ":". 
    >>> get_dic("textf.txt")
    {'asd123': [], 'asd321': []}
    """
    report = open(filename)
    di = {}
    line = report.readline().strip()
    while line !=  "": 
        if ":" in line:
            a = line.split(":")
            di[a[0]]=[]
            line = report.readline().strip()
        else:
            line = report.readline().strip()
    return di

def get_key_list(dict: Dict):
    """return a list of the keys of dict
    >>> x = get_dic("textf.txt")
    >>> get_key_list(x)
    ['asd123', 'asd321']
    """
    list = []
    for key in dict.keys():
        list.append(key)
    return list

#assign values to dictionary keys 
def assign_to_dict(filename: str) -> Dict:
    """ return a dictionary with lists that are assigned to keys from the same
    filename
    >>> assign_to_dict("textf.txt")
    {'asd123': ['asdasd'], 'asd321': ['asdadas']}
    """
    d = get_dic(filename)
    l = get_key_list(d)
    report = open(filename)
    line = report.readline().strip()
    while line !=  "":
        l = get_key_list(d)
        if ":" in line:
            a = line.split(":")
            d[a[0]].append(a[1].strip())
            if a[0] not in line:
                l.pop(a[0])
                for i in l:
                    d[i].append("")           
            line = report.readline().strip()
        else:
            line = report.readline().strip()
    return d

#To create a data frame that can be exported:
df = pd.DataFrame(assign_to_dict("textf.txt"))

import doctest
doctest.testmod()