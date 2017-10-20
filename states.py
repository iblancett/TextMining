# -*- coding: utf-8 -*-
"""
YOUR HEADER COMMENT HERE

@author: ISA BLANCETT

"""

import wikipedia
from collections import Counter


def get_content(title):
    """ grabs the content of a wikipedia page

        title: name of the wikipedia page
        returns: content of wiki page in plain text

    >>> get_content('Olin College')
    'Olin College of Engineering (also known as Olin College or simply Olin) is a private....'
    """
    article = wikipedia.page(title)
    return article.content

def find_freq_words(title, freq_words):
    """ inserts word_freq list ordered by frequency & deletes punctuation

        title: name of the wikipedia page
        calls: get_content(title)
        returns: list of words ordered by frequency to be appended to freq_words
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
    return ordered_set

def remove_matches(numStates, freq_words):
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
            for i in range(numStates):
                if word in freq_words[i]:
                    freq_words[i].remove(word)

    return freq_words


def find_common_words(states):
    """ Finds a list of uncommon words for each state

        returns: updated freq_words list
    """

    freq_words = []

    numStates = len(states)

# make list of all words (no repeats per list)
    for name in states:
        ordered_set = find_freq_words(name, freq_words)
        freq_words.append(ordered_set)
        print(name)

# get rid of matching words across state articles
    freq_words = remove_matches(numStates, freq_words)
    return freq_words

def compare_states(state1,state2):
    """ Compares uncommon words between two states

        returns: the common_words of two states
    """

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

# Get all info for comparison
    freq_words = find_common_words(states)
    common_words = []
    index1 = states.index(state1)
    index2 = states.index(state2)

# Compare the states
    for item in freq_words[index1]:
        if item in freq_words[index2]:
            common_words.append(item)

    print(len(common_words))
    return common_words

if __name__ == "__main__":
    # example run
    print(compare_states('Alabama', 'Vermont'))
