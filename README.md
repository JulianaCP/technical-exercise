#  DataCapture

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.

## Requirements:

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.

Here’s the program skeleton in Python to explain the structure:

```
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and 9 are the only two values greater
than 4)
```

### Instructions

- The challenge is to create a program that computes some
basic statistics on a collection of small positive integers. You
can assume all values will be less than 1,000.

- Implement this challenge in whatever programming language
best highlights your skills.
  
- Do not split error input validation between the command line
code and the class methods, this is not something considered as a
best practice.
  
- Do not create a driver script via the command line, it is not
necessary.
  
- Please apply any best practice you think will add value, but do not
add an extra feature than the requested.

### Challenge conditions:

- You cannot import a library that solves it instantly.
- The methods add(), less(), greater(), and between() should have 
  constant time O(1).
- The method build_stats() can be at most linear O(n).
- Apply the best practices you know.


## Implemented Solution

### Installation

- `git clone git@github.com:JulianaCP/data_capture.git`
- `cd technical-exercise`
- `pip install .`
  
### Run application

- `python main.py`

### Tests

- `pytest`

### Details



