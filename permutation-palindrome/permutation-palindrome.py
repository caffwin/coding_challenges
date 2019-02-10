# Write a function that takes in a string and checks whether or not any permutation is a palindrome

def is_perm_palindrome(str):
    # "Any permutation" means order doesn't matter
    # Does the string take in letters, numbers, or characters?
    # Assuming letters only..

    pal_dict = {}

    for char in str:
        # if the character exists in the dict already, increment counter

        # if it doesn't exist, add to dict as key and value as 1
        if char not in pal_dict:
            pal_dict[char] = 1
        else:
            pal_dict[char] += 1

    odd_counter = 0

    # We know that something is a palindrome if all values are even with the exception of one
    for value in pal_dict.itervalues():
        if value % 2 == 1:
            odd_counter += 1
            print(odd_counter)

    if odd_counter > 1:
        return False
    else:
        return True


# Write the same function to check if a string is a palindrome:

def is_palindrome(str):
    # checks if a string is a palindrome
    index_forward = 0
    index_backward = len(str) - 1

    list_string = []

    for char in str:
        list_string.append(char)

    print("Index backward: ", index_backward)

    while index_forward <= index_backward:
        if list_string[index_forward] == list_string[index_backward]:
            index_forward += 1
            index_backward -= 1
        else:
            return False

    return True

print(is_perm_palindrome("tacocat"))
print(is_palindrome("civil"))
print(is_palindrome("civic"))