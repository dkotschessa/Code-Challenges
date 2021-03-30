"""
avatar Bite 5. Parse a list of names ☆
In this bite you will work with a list of names.

First you will write a function to take out duplicates
 and title case them.

Then you will sort the list in alphabetical descending 
order by surname and lastly determine what the shortest
 first name is. For this exercise you can assume there is 
 always one name and one surname.

With some handy Python builtins you can write this in a pretty
 concise way. Get it sorted :)
"""




NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    result = []
    for name in names:
        if name not in result:
            result.append(name)
    result = [name.title() for name in result]
    return result


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    splitnames = [name.split() for name in names]
    for name in splitnames:
        name[0], name[1] = name[1], name[0]
    sorted_splitnames = sorted(splitnames, reverse = True)
    for name in sorted_splitnames:
        name[0], name[1] = name[1], name[0]
    names = [' '.join(name) for name in sorted_splitnames]
    return names
    

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    splitnames = [name.split() for name in names]
    firstnames = [name[0] for name in splitnames]
    lengths = [len(name) for name in firstnames]
    shortest_length = min(lengths)
    for name in firstnames:
        if len(name) == shortest_length:
            return name

