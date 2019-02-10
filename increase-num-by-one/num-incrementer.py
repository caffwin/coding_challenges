# Given a positive integer represented by an array of digits, add one to that number and return it in the form of a list.
# Modify list in place - don't make a new list!

# Input: Array of integers
# Output: Array of integers

# Test Cases
# Invalid inputs
# Empty Array

# Diagramming

# Empty list returns empty list
# [] > []

# Input: [5, 2, 7, 1]
# Output: [5, 2, 7, 2]

# Input: [5, 2, 7, 9]
# Output: [5, 2, 8, 0]

# Input: [9, 9, 9]
# Output: [1, 0, 0, 0]

# Input: [0, 0, 0, 0]
# Output: [1]
    
# Input: [5, 2, 7, 9]
# Output: [5, 2, 8, 0]

# Input: ["a"]
# Output: "That is not a valid number"


# Pseudocode:

# Empty list check, return empty array
# If list contains only zeros, it's the same thing as just one zero
# the output is just 1
# Check to see if list has any invalid characters, if yes then throw an error

# If the list is valid, then..
# Check through each number in passed array, from last int to first int

# if current integer is between 0 and 8:
# increment integer by one, and return new list

# if number is 9, change number to zero, and check next number
# second last number increments
# if we've reached the end of the list in reverse, append "1" to lst[0]


def add_one(lst):

    list_length = len(lst)

    if lst == []:
        return []

    for i in range(0, len(lst)):
        if not str(lst[i]).isdigit():
            return "This list contains a non integer"
        i += 1

        # try:
        #     char = int(lst[i])
        # except ValueError:
        #     print("Sorry, this list contains a non-integer")

    # Tests for sum zero before any changes are made to the original list
    if sum(lst) == 0:
        return [1]

    # Check through list to make sure each letter is a single digit (less than 10):
    for i in range(0, len(lst)):
        if not lst[i] < 10:
            return "One or more integers is greater than ten, please re-enter characters as a single digit"
        i += 1

    for num in lst[::-1]:
        if num >= 0 and num < 9:
            inc_num = num + 1
            lst[-1] = inc_num
            return str(lst)

        else: 
            for i in range(1, len(lst) + 1):
                lst[-i] = 0

                # If next number is NOT a 9, increment next num
                # and print out the rest of the list

                while i < list_length:
                    # Covers case where next number does not affect rest of list
                    if lst[-(i+1)] >= 0 and lst[-(i+1)] < 9:
                        lst[-(i+1)] += 1      
                        return str(lst)
                    
                    i += 1

            # How to tell if the end of the list is reached and all 9s changed to 0?
            # If sum is zero even after going through each character
            # This works because entering this loop means the sum of the list was not
            # zero to begin with, but became zero after changes were made
            if sum(lst) == 0:
                lst.insert(0, 1)

            return str(lst)
            
print("999 > ", add_one([9, 9, 9]))
print("5279 > ", add_one([5, 2, 7, 9]))
print("abc > ", add_one(["a", "b", "c"]))
print("a4 > ", add_one(["a", 4]))
print("12 > ", add_one([12]))
# print(add_one([3, "b", 9])) # This case breaks one of the if statements, fix later

# Constraints (Space Constraints, Time Constraints)
# O(1) - not allowed to use other data structures
# O(N) - other data structures

# In place, no space constraints

# O(1) - runtime
# O(N)
# O(N^2)

# Input: [5, 2, 7, 1]
# Output: [5, 2, 7, 2]


# Simpler method using casting, returning new list rather than modifying original list

def inc_num_with_casting(lst_nums):

    str_lst = ""

    for num in lst_nums:
        str_lst += str(num)

    int_lst = int(str_lst)
    int_lst += 1
    str_lst_two = str(int_lst)

    new_lst = []

    for num in str_lst_two:
        new_lst.append(num)

    return new_lst

print(inc_num_with_casting([9, 9, 9]))