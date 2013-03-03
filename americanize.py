"""prototype to see if name converter works well!"""

from ssa_data import *
import math

def hamming_distance(sa, sb):
    # hamming distance between two same-length words
    assert len(sa) == len(sb)
    return sum(cha != chb for cha,chb in zip(sa,sb))

def levenshtein_distance_recursive(sa, sb):
    # edit distance of two words
    # neat but slow
    if not sa: return len(sb)
    if not sb: return len(sa)
    return min(levenshtein_distance(sa[1:], sb[1:]) + (sa[0] != sb[0]),
               levenshtein_distance(sa[1:], sb) + 1,
               levenshtein_distance(sa, sb[1:]) + 1)

def levenshtein_distance(sa, sb, gap_penalty=1):
    if len(sa) < len(sb):
        return levenshtein_distance(sb, sa)
    
    if len(sb) == 0:
        return len(sa)

    previous_row = xrange(len(sb) + 1)
    for i, chara in enumerate(sa):
        current_row = [i+1]
        for j, charb in enumerate(sb):
            insertions = previous_row[j+1] + gap_penalty
            deletions = current_row[j] + gap_penalty
            substitutions = previous_row[j] + (chara != charb)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

    
    
def name_similarity(namea, nameb):
    # dummy name similarity measure function for now
    # hamming distance
    #min_len = min(len(namea), len(nameb))
    #return hamming_distance(namea[:min_len], nameb[:min_len])
    name_sim = 1.0 / levenshtein_distance(namea, nameb)
    # use nameb_popularity for scoring
    #name_sim *= math.sqrt(nameb_pop)

    if namea[0] == nameb[0]:
        name_sim *= 2
    return name_sim


def americanize(name, sex):
    """Find a similar american name"""
    assert sex in ["male", "female"]
    name_list = male_names if sex == 'male' else female_names
    # make a list of tuples of name and score.
    name_scores = [(n, name_similarity(name, n)) for n in name_list]
    name_scores.sort(key=lambda x: x[1], reverse=True)
    return name_scores[:50]
