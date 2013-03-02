"""prototype to see if name converter works well!"""

def get_names():
    # get names from file
    name_file = "american_names.txt" # tabulated data
    male_names = []
    female_names = []
    with open(name_file) as f:
        for line in f:
            cols = line.split()
            male_names.append(cols[1])
            female_names.append(cols[3])
    return male_names, female_names

def hamming_distance(sa, sb):
    # hamming distance between two same-length words
    assert len(sa) == len(sb)
    return sum(cha != chb for cha,chb in zip(sa,sb))
    
def name_distance(namea, nameb):
    # dummy name similarity measure function for now
    min_len = min(len(namea), len(nameb))
    return hamming_distance(namea[:min_len], nameb[:min_len])

def find_most_similar_names(name, name_list):
    """Find the most similar name in the name list"""
    sorted_names = sorted(name_list, key=lambda x: name_distance(name, x))
    return sorted_names[:5]
