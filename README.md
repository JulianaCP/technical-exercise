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


### Implementation details

The solution has 2 classes:

####  DataCapture

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. The logic inside the class is as follows:

- The class uses a list of length N to allow the storage of all desired numbers. 
  The `numbers_existence` list will contain all possible existence between 0, and 
  the max number of elements (by default the maximum number of different values
  is 1000. This means that you can add N number of values between
  the range of 0 and 1000).
  - number existence  = `[0] * MAX_NUMBER_OPTIONS` where MAX_NUMBER_OPTIONS = 1000 by default.
    - By default, all spaces are padded with `0`. he space in the index that represents that 
      number will increase by `1` (meaning that if you add multiple repeating numbers, 
      the value in the index that represents the number will contain how much that 
      number was added in the list).
    - For example, if I have a list with `[0] * 5`, this means that we are going to 
      have an existence list of `[0, 0, 0, 0, 0]` and that data capture allows 
      values between 0 and 4 to be added to that list.

- The `add` method: This method will take care of adding the 
  numbers to the list that contains the full representation of the numbers. 
  - Following the example above, if I add 3 numbers for 
    example: add(2), add(4), add(2), the result in the list will be the 
    following `[0, 0, 2, 0, 1]` (a number 4 added and 2 number 2 added).
    
- The stats build method carries a heavier workload as it creates the 
  resources required to process each possible statistics method. 
  The logic of this method is as follows:
  
  - The first step is to cut and create an ordered list with the 
    complete list of numbers (number existence list). Following the 
    example above, this means that a list would be created with the 
    following content `[2, 2, 4]`. This list represents the numbers 
    that were added excluding all other possible options with no values.
    
  - Using the ordered list, the method will create a dictionary, representing a 
    mapping of each of the values. The logic is as follows:
    
    - We extract what is the first and last element of the 
      ordered list, and using those values, just with the 
      ordered list of numbers we create a representation in the 
      dict with all the values between those 2 numbers (even with numbers 
      that weren't added). Following the example above, this means that 
      you would create a dict with the  following content `{2: {'min_index': 0, 'max_index': 1}, 
      3: {'min_index': 2, 'max_index': 0}, 4 : {'minimum_index': 2, 'maximum_index': 2}}}`.
      
      - These mappings represent the numerical index of each number, 
        for example, in the case of number 2, the minimum index equal to 0
        means that at index 0 there is a value of number 2, and the maximum 
        index represents that between the minimum index, and the maximum index 
        all those values are 2. Sounds a bit confusing, but basically the mapping 
        is just an index representation of the numbers position in the list, and
        the representation of this mapping will be enough to determine which 
        value is less, greater or between a range (This is the most complex 
        method in the solution -> O(n), the rest of the code is quite simple).
        
  -  The next step is to create an object of class Stats and send in
     the arguments the extracted mappings and ordered list.
  

####  Stats class

The Stats class contains functionality to compute some basic 
statistics on a list of numbers (including less, between, and greater). 
The logic inside the class is as follows:

- The classes receive the mappings from the data capture class 
  and will use those indices to determine the numbers in an operation:
  
- The less method: This method will return an integer representing how 
  many numbers in the sorted list are lower than the given number:
  
  - It does a check on the value received, the mappings received, 
    and the ordered list:
    
    - First, it checks if the received number is greater than the 
      value of the last element of the sorted list (in this case, 
      it means that the less method will return the length of the 
      list -> all values in the list are less than the send value).
      
    - Checks if the number received is less than the value 
      of the first element of the sorted list (in this case it 
      means that the less method will return 0 -> no value is 
      less than the number sent).
       
    - Otherwise, if the value is between the list number, 
      you only need to return the minimum index of that number using the mappings. 
      (since the index is cumulative, it means that the previous values 
      are all less than the send number).
      

- greater method: This method will return an integer representing 
  how many numbers in the ordered list are greater than the 
  given number:
  
  - It does a check on the value received, the mappings received, 
      and the ordered list:
    
    - First, it checks if the received number is greater than 
      the value of the last item in the sorted list (in this 
      case it means that the less method will return 0 -> there 
      are no numbers greater than the send value).
      
    - Checks if the number received is less than the value of the first 
      element of the ordered list (in this case it means that the greater
      method will return the length of the list -> all numbers in the 
      ordered list are greater than the send value).
      
    - Otherwise, if the value is between the number of the list, the 
      following calculation must be done: 
      length of the list of numbers - the maximum index 
      of that number - the representation of the maximum index 
      of the number - 1 (due to index 0) . 
      This will return how many numbers are greater than the submitted number.
      
- between method: This method will return an integer presenting how many numbers 
  in the ordered list there are between X and Y.
  
  - It does a check on the values received, the mappings received, 
      and the ordered list:
    
    - To get the numbers between a range, you just need to 
      calculate: length of the numbers in the ordered list - numbers greater 
      than the maximum range value - numbers less than the minimum 
      range value, and this will return the numbers between the range.
      

Note: all operations inside these methods are O(1) since 
accessing the list through the index only 
has O(1) complexity. [documentation](https://wiki.python.org/moin/TimeComplexity)
