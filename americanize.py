"""prototype to see if name converter works well!"""

from ssa_data import *

def hamming_distance(sa, sb):
    # hamming distance between two same-length words
    assert len(sa) == len(sb)
    return sum(cha != chb for cha,chb in zip(sa,sb))
    
def name_distance(namea, nameb):
    # dummy name similarity measure function for now
    min_len = min(len(namea), len(nameb))
    return hamming_distance(namea[:min_len], nameb[:min_len])

def americanize(name, sex):
    """Find a similar american name"""
    assert sex in ["male", "female"]
    name_list = male_names if sex == 'male' else female_names
    sorted_names = sorted(name_list, key=lambda x: name_distance(name, x))
    return sorted_names[:5]
