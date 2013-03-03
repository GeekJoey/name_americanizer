"""Extract all names from SSA data.
You can download the name dataset at http://www.ssa.gov/oact/babynames/limits.html
"""

import os

ssa_data_dir = "ssa_data"

def get_year_data(year):
    """Get name data belonging to specific year"""
    print "getting year", year
    data_file = os.path.join(ssa_data_dir, "yob%d.txt" % year)
    with open(data_file, 'rU') as f:
        name_data = [line.strip().split(',') for line in f]
    return [(name,sex,int(cnt)) for name,sex,cnt in name_data]
    
def get_all_data():
    """return male and female names as two dictionaries,
    key holds the name and the value is count, the popularity of the name"""
    male_names = []
    female_names = []
    for year in xrange(1985, 2012):
        name_data = get_year_data(year)
        male_data = [name for name,sex,cnt in name_data if sex == 'M']
        female_data = [name for name,sex,cnt in name_data if sex == 'F']
        male_names += male_data[:200]
        female_names += female_data[:200]
        
    return list(set(male_names)), list(set(female_names))

male_names, female_names = get_all_data()
