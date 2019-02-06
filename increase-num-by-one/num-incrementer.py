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

# add_to_array(lst)
# add_to_array([5, 2, 7, 1]) 


def add_one(lst):
    
    # empty list check, return empty array
    
    
    # Check through each number in passed array, from last int to first int
    
    # if current integer is between 0 and 8:
    # increment integer by one, and return new list

    # if number is 9, change number to zero, and check next number
    # second last number increments
    # if we've reached the end of the list in reverse, append "1" to lst[0]
    
    if lst == []:
        return []
    
    print("Original number is: " + str(lst))

    for num in lst[::-1]:
        print("Num is: " + str(num))
        if num > 0 and num < 9:
            # num += 1
            inc_num = num + 1
            print("New incremented num: " + str(num))
            lst[-1] = inc_num
            return lst
        else: 
            print("Else statement entered: " + str(num))
            num = 0
            return lst
            
        
    

print(add_one([5, 2, 7, 8]))

# Constraints (Space Constraints, Time Constraints)
# O(1) - not allowed to use other data structures
# O(N) - other data structures

# In place, no space constraints

# O(1) - runtime
# O(N)
# O(N^2)

# Input: [5, 2, 7, 1]
# Output: [5, 2, 7, 2]