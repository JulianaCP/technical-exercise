# A step-by-step solution journey analysis.

Internal thoughts generated during the resolution of this problem.

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

### Notes:

#### First step

I started working on this by reading the requirements in the pdf. I have many questions about the requirements 
after reading them. Normally I would schedule a meeting to discuss the requirements or send a list of questions 
to the person requiring the solution but this is something I can't do in this case so for now I'll have to make
some assumptions about the requirements, and the solution ( I really don't like this idea, and I worry that it will 
lead to bad decisions and a bad solution).

  
#### Initial thoughts on the requirements

- `The challenge is to create a program that computes some basic statistics on a collection 
  of small positive integers. You can assume all values will be less than 1,000.` Wonder
  if the 1000 it's relevant? probably yes, if not why mentioned this requirement? I wonder if the 
  1000 is relevant? probably yes, if not why was this requirement mentioned? After a quick search, 
  I discovered that Python has a 1000 constraint with recursions (whenever 
  you exceed the recursion depth of 1000, you get an error in Python). So should I assume that 
  I need to use recursion to solve this problem? could this be the case? I'm not sure yet, 
  but if that's the case, where should be the best place to do it? build_methods() maybe? 
  however, build_methods() won't have the numeric arguments to validate the result build, 
  that would be tricky. For example, how can I generate a list between A and B in build_methods() 
  using recursion, if I don't have A and B? that means that between() must be somehow related to 
  the search, but that will trigger the constraints (need to think more about this).
  
- `The DataCapture object accepts numbers and returns an object for querying 
  statistics about the inputs.` Here it is very clear that I need to create a DataCapture class. 
  I'm not entirely sure about `returns an object to query for statistics`. Does this mean that 
  I can create an additional class or that I have to use something simpler like `type` to 
  create a representation of an object with methods without explicitly creating a class? 
  I'm not sure how I'm going to proceed in this section. However, it is very clear that 
  I need to return an object that has within these methods less(), greater() and between().
  
- `You cannot import a library that solves it instantly`. Does this mean I can't use queues, 
  for example? hmm probably not, it probably means I can't use built-in methods for less(), great() 
  or between() (First guess here).
  
- `The methods add(), less(), greater(), and between() should have constant time O(1)` Ok, this 
  is going to be tricky, normally I would create O(n) methods for this kind of problem. There 
  are no problems with add() since a simple addition will have O(1) complexity, but it's a 
  different story with less(), great() and between(). To find values in a list, it 
  must be an iteration of a list or similar, and that will mean O(n) complexity, so this 
  will definitely require some extra thought. This tells me that build_stats() will be an 
  important generator of the results, as it is the only method that allows O(n) complexity, 
  however build_stats() will not have the arguments passed to these methods, so it 
  will be interesting.

  
- `The method build_stats() can be at most linear O(n)` As I mentioned before, 
  this method will be of great help in solving this problem. However, I still 
  can't figure out how this method can solve the number search process without 
  knowing the limits (greater than and/or less than).

  
- `Tests must be included in the submission.` There are no questions here, it means I 
  need to generate some unit tests after solving the problem.

  
- `Do not split error input validation between the command line code and the 
  class methods, this is not something considered as a best practice.` hmm I have a number 
  of questions here, i would normally ask these questions before anything else, but I'm not sure 
  if this should be considered appropriate and who should be the right person to ask. For now, 
  I'll make some assumptions, but I should probably ask something about this, if not, it will
  probably lead to a wrong implementation.

    1) `command line` Are we talking about an OS command line or python cli to run python code?
    2) Does this mean I need to create a python cli application? 
    3) Does this mean I need to keep the python program execution alive, so I can 
       send multiple add(), build_stats(), less(), great(), between() commands and check 
       sent inputs (error input validation)?

    4) `error input validation` What kind of validation are we talking about? not sure, but I 
       probably need to know what `command line` means first. I'm not sure if this is related
       to the system command line, or the cli app in a .py file. With either option, 
       I still have questions about what is considered an input and how to get it 
       into the .py file.
       
- `Do not create a driver script via the command line, it is not necessary, we 
  are only seeking working classes and tests, as we can run the program via the 
  Python repl.` I assume this means that I only have to create the .py file 
  and that it can be run simply with `python filename.py`. (no need to do 
  anything fancy, not sure if I'm assuming correctly, probably one 
  more of my assumptions).

  
- `Please apply any best practice you think will add value, but do not add extra 
  feature than the requested.` Does this mean that I can add classes, 
  decorators, etc? hmm probably yes, but I'm not sure if that's the 
  intention or if it means that I can only create the mentioned classes 
  in the best possible way (without adding new supporting classes)?. 
  I'm not sure, it will probably also define an assumption on this.

  
- `If you have questions or inconveniences to complete the test, 
  don’t hesitate to ask your recruiter.` I usually like to ask a lot 
  of questions about the requirements to make sure I understand the
  required solution correctly. Like now, as you can see, is no 
  exception. Actually, I probably have more questions than usual since 
  the required solution has some specific implementation requirements, 
  but for now, due to the origin of the process, I'll try to write some
  implementations first and when I have something more robust I'll 
  ask some questions. to check the results.

  
    
#### Initial thoughts on the solution:

1) I started to create the skeleton of the DataCapture class 
   (including the necessary methods).
   
2) After that, I started thinking about the implementation of the methods.
    - capture.add(n): 
      - Can have at most O(1) complexity.
      - A simple list_name.append(n) should be fine. -> O(1) complexity. 
      - I've thought about lists a lot, and I'm wondering if actually lists 
        are the best approach.
      
    - stats = capture.build_stats()
        - Can have at most O(n) complexity.
          
        - Keep thinking about the 1000 number. 
          
        - The only way I can think of at the moment to achieve the O(1) 
          in the methods is to do the heavy calculation here, 
          so I'm wondering if I can somehow fill in a set of possible 
          results here, so I can use them later. in the desired methods. 
          However, I'm wondering if I can somehow complete a set of 
          possible results before I get the method arguments?
          
        - I keep thinking about how to sort the list without affecting the O(n) 
          constraints. I've done a lot of research on the internet about sorting 
          algorithms and their complexity, and there aren't many options that 
          meet the O(n) constraint. Most sorting algorithms do not meet 
          this requirement [SORT ALGORITHMS](https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/)
          
        - I spent a **significant** amount of time here, looking at sorting options 
          (including lists, queues, and different data structures), creating various
          exercises/examples in Python, until I think I finally found something 
          interesting -> PriorityQueue. Therefore, I created a number sort method 
          capable of sorting a list of numbers with complexity O(n). At first, 
          I wasn't sure if the priority queue's data type really met the time complexity, 
          but multiple sources assure me that was the case, so I decided to go ahead
          with this solution (with some concerns about the selection, but at 
          least with better options than before.).
          
            - Uses the heapq module in Python to create a priority queue. 
            
            - This implementation has O(log n) time for insertion and extraction. 
              The PriorityQueue uses the same heapq implementation internally 
              and thus has the same time complexity (PriorityQueue is the classic 
              OOP style of implementing and using Priority Queues).
            
            - The priority queue is an advanced type of the queue data structure. 
              Instead of dequeuing the oldest element, a priority queue sorts
              and dequeues elements based on their priorities. Since the 
              queue.PriorityQueue class needs to maintain the order of
              its elements, a sorting mechanism is required every time a new
              element is enqueued. Python solves this by using a binary heap
              to implement the priority queue. The Python priority
              queue is built on the heapq module, which is basically a
              binary heap with O(n) complexity. 
              
            - Example of some sources [HERE](https://www.educative.io/answers/what-is-the-python-priority-queue),
              [HERE](https://www.growingwiththeweb.com/data-structures/binary-heap/build-heap-proof/),
              and [HERE](https://towardsdatascience.com/introduction-to-priority-queues-in-python-83664d3178c3).
            
        - So far, I figured out how to handle the sorting of the list, however, 
          I still don't have a clear path how to handle the rest of the process 
          to be able to extract the desired numbers with O(1) complexity using the 
          methods. What I know about this is that I can't do nested iterations 
          (a for inside a for, for example, since it will exceed the complexity 
          limit) ((This could have been useful if I wanted to create a dict or 
          something similar with the major/minor number mappings for each 
          existing number in the list, so I could access these mappings in 
          the methods, but this is not an option, since it will require a for 
          inside a for, to process each number in the list.).
          
HERE
    
    - stats.less(n), stats.less(n), stats.between(min_n, max_n):
        - Still, not sure how to handle this, I spent a significant amount of time thinking on this,
          and how to solve these methods without increasing the complexity to O(n).
          
        - Keeping a complexity O(1) means iterate, slice or handle in any way a list, since
          it will immediately increase the complexity to O(n). 
          
        - Thinking even harder even since the arguments are sent in these methods, so I'm wondering, 
          Is it possible to extract the numbers of a list between X and Y with O(1) in
          the between() method, when the min and max value are actually sent in the 
          mentioned method? Right now, I don't think is possible, I mean, there are 2 options
          that I'm seeing right now.
            - I can extract the numbers when I received the methods calls (iterating over a list
              or calling a recursive function) but that will cause a O(n) complexity in the methods.
              
            - I can create some kind of mapping using the build_stats() method, iterating over 
              each list item, and creating all the possible combination of the number so the 
              stats.less(n), stats.less(n), stats.between(min_n, max_n) just need to call for the
              results, however that will cause a O(n^2) complexity in the build_stats since it needs
              to generate outcomes for each element in the list. So, not an option either. I can also
              try to extract the indices of each number, representing a min and max value of each of 
              then but that will required a slicing when the numbers are received in the less(), greater()
              between() so not an option either since that will increase the complexity to O(n).
              So, for now, this problem requires more thinking.
          
2) Keep thinking about the methods' implementation.
    - I'm still researching about code complexity, did a lot of research about search algorithms and
      keep thinking about sort algorithms.
      - After my continuous research on sort algorithms, it seems that priorityQueue is still the best
        possible option with my current understanding, probable not the best solution but seems to
        accomplish the O(n) complexity to sort the list (a sorted list will definitely facilitate the
        solution of the problem).
      
    - capture.add(n): Keep thinking that list_name.append(n) should be the right approach.
    
    - stats.less(n), stats.less(n), stats.between(min_n, max_n):
        - Have some ideas about how to solve this process, basically I would be using this methods 
          as validation methods. Basically they will check when a number should be included in a solution
          or not. A recursion function will be checking the elements of the list, and a validation function
          will be checking the number and verifying in the number being checked should be included or not.
          (basically it will mean that the stats.less(n), stats.less(n), stats.between(min_n, max_n) will
          have conditionals lines -> O(1) complexity.  So this should solve the complexity of the methods, 
          however still not sure about the caller of these methods, but will detail more about this below). 
      
    - stats = capture.build_stats()
        - So, did a lot of thinking about how to solve this, still not completely sure about the 
          solution but at least it's a start. Thinking about creating a recursion functions that 
          will iterate over each element of the sorted list. That recursion function will receive
          a validation method (less, greater or between), and will use that validation method
          to determine if the number will be added to the results or not. At the end the recursion
          method will return a list of numbers that fulfil the validation method.
          
        - Create a typer class to return an object with the greater(), less() and between() methods. I would
          normally create an external class (even located in a different .py file) but decided
          to create the class with typer to attach some time complexity to the build_stats() method. Although, I'm
          not sure if that's even been the case. (need more thinking). 
          
        - I'm still not completely sure if this solution simplifies the complexity of greater(), less() 
          and between(). I have the methods greater(), less(), between() with complexity O(1) inside the 
          DataCapture class, and I created a typer Stats class inside the build_stats() that has the 
          tags "greater", "less", and "between" to call the O(1) methods, and the recursion function in charge
          of filtering the results with O(n) complexity. However, should I consider the Stats tags as the 
          greater(), less(), between() methods or should I consider  the DataCapture methods to be the
          official ones. Probably, technically  the Stats one should be considered the official ones, meaning
          I may be breaching the requirements, but for now, let's keep this implementation.

DataCapture class:

```
class DataCapture:
    """The DataCapture object accepts numbers and returns an object for querying
    statistics about the inputs. Specifically, the returned object supports
    querying how many numbers in the collection are less than a value, greater
    than a value, or within a range.
    """
    def __init__(self):
        # O(1) complexity.
        self._numbers = []

    def add(self, number):
        """Adds a number to the numbers list (available numbers to
        manipulate and generate the stats).
        """
        # O(1) complexity.
        self._numbers.append(number)

    @check_arguments
    def less(self, number, number_to_check=None):
        """Checks if the sent number is lower than X (being X
        the number to check that will represent an element
        in the list). In case no number to check was
        sent, the method will return false by default.

        :param int number: Stats number.
        :param int, None number_to_check: Number to check. Method with
        check if the 'number' is lower than this number.
        """
        # O(1) complexity.
        return number < number_to_check if number_to_check else False

    @check_arguments
    def between(self, number, min_number=None, max_number=None):
        """Checks if the sent number is between X and Y (being X
        the minimum number to check and Y the maximum number to
        check. Both values represent an interval and this method
        will check if the sent number is between this interval.
        In case no min or max number were, the method will
        return false by default.

        :param int number: Stats number.
        :param int, None min_number: Minimum number to check. Method with
        check if the 'number' is greater than this number.
        :param int, None max_number: Maximum number to check. Method with
        check if the 'number' is lower than this number.
        """
        # O(1) complexity.
        return min_number <= number <= max_number if min_number and max_number else False

    @check_arguments
    def greater(self, number, number_to_check=None):
        """Checks if the sent number is greater than X (being X
        the number to check that will represent an element
        in the list). In case no number to check was
        sent, the method will return false by default.

        :param int number: Stats number.
        :param int, None number_to_check: Number to check. Method with
        check if the 'number' is greater than this number.
        """
        # O(1) complexity.
        return number > number_to_check if number_to_check else False

    def _searcher(self, numbers, validator, *args, selections=None):
        """This is a recursive function to find all the numbers inside a list that 
        passed a validation (validation could be 'numbers lower than X', 
        'numbers between than X and Y' and 'numbers greater than X'). At the 
        end of the execution it will return the list  of all of the numbers
        that passed the validation.
        
        :param list numbers: Number of the list.
        :param function validator: Validation could be 'numbers lower than X', 
        'numbers between than X and Y' and 'numbers greater than X'.
        :param tuple args: Inputs of the validation function.
        :param list, None selections: Number that passed the restriction.
        """
        # O(n) complexity.
        # We can assume all values will be less than 1,000 so the recursion will not failed.

        if not selections:
            selections = []

        if not numbers:
            return selections

        # add number and keep analyzing
        if validator(numbers[0], *args):
            selections.append(numbers[0])

        return self._searcher(numbers[1:], validator, *args, selections=selections)

    def _sort_numbers(self):
        """Uses the heapq module in Python to create a priority queue.
        This implementation has O(log n) time for insertion and extraction.
        The PriorityQueue uses the same heapq implementation internally and
        thus has the same time complexity (PriorityQueue is the classic OOP style
        of implementing and using Priority Queues).

        The priority queue is an advanced type of the queue data structure.
        Instead of dequeuing the oldest element, a priority queue sorts
        and dequeues elements based on their priorities. Since the
        queue.PriorityQueue class needs to maintain the order of
        its elements, a sorting mechanism is required every time a new
        element is enqueued. Python solves this by using a binary heap
        to implement the priority queue. The Python priority
        queue is built on the heapq module, which is basically a
        binary heap with O(n) complexity.
        """
        # O(1) complexity.
        # we initialise the PriorityQueue class to operate upon a list.
        sorted_queue_numbers = PriorityQueue()
        for number in self._numbers:
            # Insertion	O(log n) complexity.
            # Puts an number into the queue (It will be adding the numbers
            # in ordered).
            sorted_queue_numbers.put(number)

        # O(n) complexity.
        # generates a ordered list with the sorted queue.
        sorted_numbers = []
        while not sorted_queue_numbers.empty():
            # Deletion O(log n) complexity.
            # The get command dequeues the highest priority elements from the queue.
            # here we are going to be adding one by one all the values of
            # the ordered queue to a list, basically we are moving from a
            # ordered priorityQueue to a ordered list (will be easier
            # to use lists to handle the 'less', 'greater' and 'between'
            # methods with lists instead of a a queue).
            sorted_numbers.append(sorted_queue_numbers.get())

        return sorted_numbers

    def build_stats(self):
        """Sorts the list of numbers and returns an object for querying
        statistics about the inputs. The returned object supports
        querying how many numbers in the collection are less than a value, greater
        than a value, or within a range.
        """
        # O(n) complexity
        # create an ordered list using the numbers list.
        # Note: I would normally use list.sort() but I discarded that option
        # since it has a O(n log n) complexity. So, in regards of the
        # requirement I implemented a priorityQueue, more details in the
        # sort numbers method.
        sorted_numbers = self._sort_numbers()

        # O(n) complexity
        # Dynamic Stats class to handle calls on less, greater and between methods.
        return type("Stats", (object,), {
            "_sorted_numbers": sorted_numbers,
            "less": lambda cls, n: self._searcher(cls._sorted_numbers, self.less, n),
            "greater": lambda cls, n: self._searcher(cls._sorted_numbers, self.greater, n),
            "between": lambda cls, min_n, max_n: self._searcher(cls._sorted_numbers, self.between, min_n, max_n)
        })()
```

3) Keep thinking about the methods' implementation. 
    - Previous implementation generated a working solution, able to generate the desired 
      outputs. However, still not sure about the complexity. I tried to reorganize the code
      in a way that the heavier complexity was in the build_stats() method, but not sure
      if I was successful or not. I'm still thinking about the O(1) complexity and deciding 
      who technically has the complexity in my solution.
      
    - I'm still unsure about the solution, so I started with some research again, want to see 
      if I can map somehow the numbers to generate some default responses in the build_stats,
      so I can just extract those responses in the O(1) methods using a O(1) complexity. Using 
      this approach I can create a separate Stats class instead of attaching the class in the
      build_stats method.
      
    - On a side note: I would have loved to talk to some co-workers about this, I probably would if 
      this was work or even a personal goal, but I'm keeping it individual due to the origin of the 
      exercise, but a brainstorming session would be great in these types of cases. 
      In fact, I think I probably would have done it for some time now, as I prefer to work in a 
      very collaborative style. Think that discussing with more people can always help you to have more ideas,
      new perspectives and new insights.

      
4) Keep thinking about the methods' implementation.
    - Had been trying multiple solutions with different approaches but still can't find a solution that
      I love.
        - Tried to map the results in the build_stats method (using recursion), but at the end I ended up 
          with a build_stats() with O(n^2) complexity or a stats.less(n), stats.less(n), 
          stats.between(min_n, max_n) with O(n) complexity. At this point I suspect one of three things is true:
            - I'm misinterpreting the requirements.
            - The problem is unsolvable with the stipulated complexity restrictions.
            - I'm focused on the wrong things.
          
        - I can't find myself completely agreeing with the current solution, but for now, 
          I'm just going to move forward with the previous presented solution, at least it gives 
          a representation of accomplishment.
          
5) I started creating some unit tests with the current implementation.

6) I still have some questions about the command line, not sure what is expected about that and how
should the python code be executed, so I would probably ask for some clarification about that.
   
7) Created the README of the code.

8) End


At this point I think I'm out of ideas, and the worst thing for me to do is to keep trying 
and misrepresent my understanding of the topic by continuing to work on this. 
I would have loved to talk to with someone else about this problem and get some new ideas,
perspectives, insights, about how to improve/fix my current implementation. I ended up
with a working solution but would have love to discuss and share some of my ideas to check
correctness but due to the origin of the exercise I would probably have to keep 
desired final implementation of this problem as an unknown.

If you still read until this point, just want to tell you thank you for the attention, and hope my 
thoughts have made any sense to you. These types of exercises are not something I engage in often in my work, so
I enjoyed digging about this.
