"""Extract all names from SSA data"""

import os

ssa_data_dir = "ssa_data"

def get_year_data(year):
    """Get name data belonging to specific year"""
    print "getting year", year
    data_file = os.path.join(ssa_data_dir, "yob%d.txt" % year)
    lines = open(data_file, 'rU').readlines()
    # get name and sex from each line
    names = map(lambda line: tuple(line.strip().split(',')[:2]), lines)
    return names

def get_all_data():
    all_names = []
    for year in xrange(1880, 2012):
        all_names += get_year_data(year)
    # remove duplicates from the list
    all_names = list(set(all_names))
    return all_names


all_names = get_all_data()
male_names = [name for name,sex in all_names if sex == 'M']
female_names = [name for name,sex in all_names if sex == 'F']
