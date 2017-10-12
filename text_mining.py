# -*- coding: utf-8 -*-
"""
YOUR HEADER COMMENT HERE

@author: ISA BLANCETT

"""

# Assumptions:
# Wikipedia articles of states are up to date
# Distance between states = google maps distance between states
# If states are next to each other, their distance is 0
# Hawaii is considered 5000 miles from Alabama for the sake of this script

import wikipedia
from collections import Counter
from itertools import chain
import matplotlib.pyplot as plt

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
          'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia (U.S. state)',
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
          'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
          'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
          'New Mexico', 'New York (state)', 'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
          'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
          'Virginia', 'Washington (state)', 'West Virginia', 'Wisconsin', 'Wyoming']

# In miles
dist_al = [0, 4303, 1564, 446, 2161, 1444, 1157, 932, 0, 0,
           5000, 2131, 700, 614, 948, 1009, 500, 388, 1507, 869,
           1262, 935, 1324, 0, 609, 1964, 1166, 2084, 1325, 1028,
           1228, 1211, 585, 1620, 728, 728, 2422, 981, 1225, 395,
           1315, 0, 828, 1773, 1360, 669, 2547, 705, 934, 1650]

freq_words = []

def get_content(title):
    """ grabs the content of a wikipedia page

        title: name of the wikipedia page
        returns: content of wiki page in plain text

    >>> get_content('Olin College')
    'Olin College of Engineering (also known as Olin College or simply Olin) is a private....'
    """
    article = wikipedia.page(title)
    return article.content

def find_freq_words(title):
    """ inserts word_freq list ordered by frequency & deletes punctuation

        title: name of the wikipedia page
        calls: get_content(title)
        returns: nothing
    """

    words = get_content(title).split()

    # Checks for words carrying punctuation marks
    for i in range(len(words)):
        if words[i].endswith('.') or words[i].endswith(',') or words[i].endswith(')') or words[i].endswith(':'):
            words[i] = words[i][:-1]
        if words[i].startswith("("):
            words[i] = words[i][1:]
        if words[i].endswith("'s"):
            words[i] = words[i][:-2]

    ordered = sorted(words, key = words.count, reverse=True)

    # Orders by frequency without repeat terms
    seen = {}
    ordered_set = [seen.setdefault(x, x) for x in ordered if x not in seen]
    freq_words.append(ordered_set)
    return

def remove_matches():
    """ removes words that are present in 10 state lists (e.g. 'the')

        returns: nothing
    """

# Make a histogram of all the words
    all_words = []
    for entry in freq_words:
        all_words.extend(entry)
    hist = Counter(all_words)

# Delete words that appear in 10 or more articles
    for word in hist.keys():
        if hist[word] >= 10:
            for i in range(50):
                if word in freq_words[i]:
                    freq_words[i].remove(word)


def find_common_words(state1, state2):
    """ Main Loop: compares two states

        returns: the common_words of two states
    """
    for name in states:
        find_freq_words(name)
        print(name)

    remove_matches()

    common_words = []
    index1 = states.index(state1)
    index2 = states.index(state2)

# Find the common words
    for item in freq_words[index1]:
        if item in freq_words[index2]:
            common_words.append(item)

def comp_al():
    """ compares Alabama to every state

        plots: # of common words vs. distance
    """

    for name in states:
        find_freq_words(name)
        print(name)

    remove_matches()

    num_sim_al = []
    for i in range(1,50):
        common_words = []
        index1 = 0
        index2 = i

        for item in freq_words[index1]:
            if item in freq_words[index2]:
                common_words.append(item)

# Add number of common words to num_sim_al
        num_sim_al.append(len(common_words))

#plot
    plt.plot(dist_al[1:], num_sim_al, 'ro')
    plt.show()
    return



if __name__ == "__main__":
    comp_al()
