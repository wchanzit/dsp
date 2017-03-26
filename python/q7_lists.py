# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0
    
    for word in words:
        if len(word) >= 2:
            if word[0] == word[-1]:
                count += 1
    return count
    
#print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
#print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
#print(match_ends(['aaa', 'be', 'abc', 'hello']))


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    
    x_words = []
    others = []
    
    for word in words:
        if word[0] == 'x':
            x_words.append(word)
        else:
            others.append(word)
            
    return sorted(x_words) + sorted(others)

#print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
#print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
#print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    
    tup2 = []
    tup3 = []
    
    for tup in tuples:
        tup2.append((tup[-1::-1]))
        
    tup2.sort()
    
    for tup in tup2:
        tup3.append((tup[-1::-1]))
    
    return tup3

#def sort_last2(tuples):
    
#    return sorted(tuples, key = lambda tup: tup[-1])

#print(sort_last([(1, 3), (3, 2), (2, 1)]))
#print(sort_last2([(1, 3), (3, 2), (2, 1)]))
#print(sort_last([(2, 3), (1, 2), (3, 1)]))
#print(sort_last2([(2, 3), (1, 2), (3, 1)]))
#print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))
#print(sort_last2([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    
    prev = None
    new_list = []
    
    for num in nums:
        #print(prev, num, num != prev)
        if num != prev:
            new_list.append(num)
        
        prev = num
    
    return new_list

#print(remove_adjacent([1, 2, 2, 3]))
#print(remove_adjacent([2, 2, 3, 3, 3]))
#print(remove_adjacent([3, 2, 3, 3, 3]))
#print(remove_adjacent([]))


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    
    union = list1 + list2
    union.sort()
    
    return union
    

#print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
#print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
#print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))
