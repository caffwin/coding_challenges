# Given a positive integer represented by an array of digits, add one to that number and return it in the form of a list.

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

# empty list check, return empty array
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

    for i in range(1, len(lst)):
        if not str(lst[i]).isdigit():
            return "This list contains a non integer"

        # try:
        #     char = int(lst[i])
        # except ValueError:
        #     print("Sorry, this charater is not an integer\n")

    if sum(lst) == 0:
        return [1]

    for num in lst[::-1]:
        # print("Num is: " + str(num))
        if num > 0 and num < 9:
            # num += 1
            inc_num = num + 1
            print("New incremented num: " + str(num))
            lst[-1] = inc_num
            return "Output number is: " + str(lst)

        else: 
            # Enter this loop if the number is 9
            # 9 > 0 and the next number increments by one
            # [5, 2, 8, 0]

            print("Else statement entered: " + str(num))

            # Already know that the last number is a 9
            # Change the 9 to a 0, and check next number

            # ---------
            # If next number is also 9, change to zero and continue searching
            # If not, increment by 1 
            # ---------

            # Do this until hitting len[-(list_length)]
            # If the last number is also a 9, change that to a zero append 1 to the beginning
            # Return list

            for i in range(1, len(lst) + 1):
                print("i is: ", i)
                print(lst[-i])
                # lst[-1], lst[-2], lst[-3]
                lst[-i] = 0

                while i < list_length:
                    print("i in while loop: ", i)

                    if lst[-(i+1)] > 0 and lst[-(i+1)] < 9:
                        lst[-(i+1)] += 1                     

                    i += 1
                    # How to tell if the end of the list is reached?
                    print("While loop printed list: ", lst)

            if sum(lst) == 0:
                lst.insert(0, 1)

            return "Output number is: " + str(lst)
            
print(add_one(["a", "b"]))

# Constraints (Space Constraints, Time Constraints)
# O(1) - not allowed to use other data structures
# O(N) - other data structures

# In place, no space constraints

# O(1) - runtime
# O(N)
# O(N^2)

# Input: [5, 2, 7, 1]
# Output: [5, 2, 7, 2]