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

def jaro_distance(sa, sb):
    """Jaro distance between two strings"""
    def get_commons(wa, wb, dist):
        return [char for index, char in enumerate(wa)
                if char in wb[int(max(0, index-dist)):int(min(index+dist, len(wb)))]]
        
    max_range = int(max(len(sa), len(sb)) / 2.0) - 1
    # two chars from sa and sb are considered matching if they are same and
    # not farther than max_range
    commons_a = get_commons(sa, sb, max_range)
    commons_b = get_commons(sb, sa, max_range)
    len_a = float(len(commons_a))
    len_b = float(len(commons_b))

    if len_a == 0 or len_b == 0:
        return 0

    num_transpositions = sum(ca != cb for ca,cb in zip(commons_a, commons_b)) / 2.0
    return (len_a/ len(sa) +
            len_b / len(sb) +
            (len_a - num_transpositions) / len_a) / 3.0

    
def jaro_winkler_distance(sa, sb, prefix_scale=0.1):
    """Jaro-winkler distance for short strings such as person names.
    http://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
    """
    def get_prefix(max_prefix=4):
        # length of common prefix up to maximum of 4 characters
        length = min(len(sa), len(sb), max_prefix)
        for i in range(0, length):
            if sa[i] != sb[i]:
                return i
        return length

    jd = jaro_distance(sa, sb)
    prefix = get_prefix()
    return jd + (prefix * prefix_scale * (1 - jd))


def name_similarity(namea, nameb):
    # dummy name similarity measure function for now
    # hamming distance
    #min_len = min(len(namea), len(nameb))
    #return hamming_distance(namea[:min_len], nameb[:min_len])
    #name_sim = 1.0 / levenshtein_distance(namea, nameb)
    name_sim = jaro_winkler_distance(namea, nameb)
    #name_sim = jaro_distance(namea,nameb)
    return name_sim 


def americanize(name, sex):
    """Find a similar american name"""
    assert sex in ["male", "female"]
    name_list = male_names if sex == 'male' else female_names
    # make a list of tuples of name and score.
    name_scores = [(n, name_similarity(name, n)) for n in name_list]
    name_scores.sort(key=lambda x: x[1], reverse=True)
    return [name for name,score in name_scores[:10]]
