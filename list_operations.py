"""
Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.
"""

def head(input_list):
    """Return the first element of the input list."""
    return input_list[0]    

def tail(input_list):
    """Return all elements of the input list except the first."""
    return input_list[1:]
    # note the absence in the end index, meaning no end until the very end of the list

def last(input_list):
    """Return the last element of the input list."""
    return input_list[-1]
    # goes backward

def init(input_list):
    """Return all elements of the input list except the last."""
    return input_list[:-1]
    # note absence again in the start index, meaning no specific start but the very first index

def first_three(input_list):
    """Return the first three elements of the input list."""
    return input_list[0:3]
    # 0 is the first, 1 is the second, 2 is the third. Put down 3 in the end index
    # because in the end index of the slice notation, it always end before the given index.

def last_five(input_list):
    """Return the last five elements of the input list."""
    return input_list[-5:]
    # go backward thru the last five elements, then starts towards the end

def middle(input_list):
    """Return all elements of the input list except the first two and the last
    two."""
    return input_list[2:-2]
    # starts at the third index, which is index 2 and ends at the index second to last.

def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of the input list."""
    return input_list[2:6]

def inner_four_end(input_list):
    """Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.
    """
    return input_list[-6:-2]
    # goes backward to the 6th element from the last.
    # and ends before the 2nd element from the last for the third element.

def replace_head(input_list):
    """Replace the head of the input list with the value 42."""
    input_list[0] = 42
    return input_list
    # using list indexing assignment to replace the value with 42.

def replace_third_and_last(input_list):
    """Replace the third and last elements of the input list with the value 37."""
    input_list[2] = 37
    input_list[-1] = 37
    return input_list
    # list indexing assignment

def replace_middle(input_list):
    """Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    """
    input_list[2:-2] = [42, 37]
    return input_list
    # using list slicing assignment to replace with the value of 42 and 37.

def delete_third_and_seventh(input_list):
    """Remove the third and seventh elements of the input list."""
    del input_list[6], input_list[2]
    return input_list
    # using delete statement to remove elements from the list

def delete_middle(input_list):
    """Remove all elements from the input list except for the first two and the
    last two.
    """
    del input_list[2:-2]
    return input_list
    # using list slicing deletion to remove elements


"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""

def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    items = 0
    for item in input_list:
        items += 1
    return items

# For the next four functions, get clever using slice operations described in the first half
def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
    input_list += [value]
    return input_list
    # example: returns [1, 2, 3, [4, 5]]
    # the append method simply adds the values

def custom_extend(input_list, values):
    """custom_extend(input_list, values) imitates input_list.extend(values)"""
    for value in values:
        input_list += [value]
    return input_list
    # example returns [1, 2, 3, 4, 5]
    # the extend method simply goes inside the values and add the value to the list

def custom_insert(input_list, index, value):
    """custom_insert(input_list, index, value) imitates
    input_list.insert(index, value)
    """
    input_list[index:index] = [value]
    return input_list
    # using list slicing assignment to insert the value in the list

def custom_remove(input_list, value):
    """custom_remove(input_list, value) imitates input_list.remove(value)"""
    # creating a for loop to loop over specific index when the index is unknown,
    # I use the range(len(input_list)) to give me the index, which I can iterate over
    for x in range(custom_len(input_list)):
        # if stmt to check if the value is the same as the value from the given index from the for loop,
        # which helps us check inside the value of input_list[x]
        if value == input_list[x]:
            # if yes, delete the element
            del input_list[x]
            break
    return input_list

def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    # assigning the last element to a variable 
    # because I want to keep the last number 
    # before I delete it off the face of the earth, haha
    last_number = input_list[-1]
    # delete the last number
    del input_list[-1]
    # returns the last number
    return last_number


def custom_index(input_list, value):
    """custom_index(input_list, value) imitates input_list.index(value)"""
    # using for loop and range(len(list)) to find the index of the list
    for i in range(custom_len(input_list)):
        if input_list[i] == value:
            # returns the index if the value matches
            return i

def custom_count(input_list, value):
    """custom_count(input_list, value) imitates input_list.count(value)"""  
    # creates a counter to count each time a value matches a value in each element
    count = 0
    # using for loop to iterate over each value in the list
    for same_value in input_list:
        if same_value == value:
            # add to the counter if the value matches
            count += 1
    # returns the total count
    return count

def custom_reverse(input_list):
    """custom_reverse(input_list) imitates input_list.reverse()"""
    # assigning indexes to the variables
    start_index = 0 # beginning index
    end_index = -1 # ending index

    # using while loop to avoid going over half
    # custom_len(list)/2 helps us know 
    # to stop in the middle where the stopping index is
    while start_index  < custom_len(input_list)/2:
        # assigning the list to a temporary variable
        temp = input_list[start_index]
        # assigning the end index to the start index
        input_list[start_index] = input_list[end_index]
        # assigning the temp, containing the start index, 
        # to the end index
        input_list[end_index] = temp
        # bump up the start index, moving forward
        start_index += 1
        # bump down the end index, moving backward
        end_index -= 1
    # NOTE: this is a complex memory concept!!! 
    # It's all about reassigning the elements in the same list
    # Avoid making a new list because it is not efficient
    # to have floating garbage in the unknown space within the memory

    return input_list

    # shortcut for custom_reverse
        # input_list[:] = input_list[::-1]

def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""
    # using for loop to iterate over item
    for item in input_list:
        # using if stmt whether the item has a value
        if item == value:
            # if yes, returns true
            return True 
    return False 

    # This below also works, but it is not efficent 
    # because it keeps running after it knows the answer
        # matched = False
        # for item in input_list:
        #     if item == value:
        #         matched = True
        # return matched

def custom_equality(some_list, another_list):
    """custom_equality(some_list, another_list) imitates
    (some_list == another_list)
    """
    # if the list is the same as the other list,
    if some_list == another_list:
        # returns true
        return True
    # otherwise, returns
    return False