"""
Example execution of the DataCapture and the
Stats class.
"""
from data_capture.data_capture import DataCapture


def main():
    """The DataCapture object accepts numbers and returns
    an object for querying statistics about the inputs.
    The returned object supports querying how many numbers
    in the collection are less than a value, greater
    than a value, or within a range. This are the output
    of the provided example.
    """
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(f"Numbers: {stats.sorted_numbers}")
    print(f"-> Less than 4 = {stats.less(4)} numbers.")
    print(f"-> Greater than 4 = {stats.greater(4)} numbers.")
    print(f"-> Between 3 and 6 = {stats.between(3, 6)}  numbers.")


if __name__ == '__main__':
    main()
