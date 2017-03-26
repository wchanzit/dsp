# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both are Python data structures that contain sequences of values. In addition, they can both contain elements of different data types, including other lists and tuples. Lists are mutable, whereas tuples are immutable. Tuples can be keys in dictionaries because they are immutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are like lists in that they contain multiple elements and are mutable, but there are differences as well. These include that each element in a set must be immutable and unique, and a set is unordered.

An example list is ['Bob', 'Rachel', 'Bob', 'John'].

An example set (corresponding to the list above) is {'Bob', 'Rachel', 'John'}.

Finding an element in a set is faster than doing so in a list because sets use hash functions to map elements to respective specific "buckets" that can be immediately searched for values. Searching for lists, on the other hand, necesitates testing through every element in the list for equality.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` in Python is a keyword for creating small 'anonymous' functions. (The functions are 'anonymous' in that are are not assigned a name in any namespace.) One common use of `lambda` functions in Python is in `map` as the `func` argument. This allows the Python user to apply an anonymous function to every element of a sequence. Another use of the lambda function is in the `key` argument to `sorted` for custom sorting criteria. One could execute `sorted(my_tuple, key = lambda element: element[1])` to sort a list of tuples by their one-eth entries. 

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a tool in Python for creating new lists (or dicts or sets) from other ones with a concise syntax.

For example, the list comprehension `new_nums = [num + 1 for num in nums]` is equivalent to `map(lambda num: num =1, nums)`.

In addition, the list comprehension `[num for num in nums if num > 6]` is equivalent to `filter(lambda num: num > 6, nums)`. 

The capabilities of list comprehensions are similar to those of `map` and `filter` but with more concise syntax. List comprehensions that are equivalent to a combination of `map` and `filter` can even be written in one line of code.

Here is an example of a dictionary comprehension: `{num: -num for num in range(10)}`.

Here is an example of a set comprehension: `{num for num in range(15)}`.

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days 

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days 

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





