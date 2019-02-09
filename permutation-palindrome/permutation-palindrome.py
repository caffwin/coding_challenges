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

    # return pal_dict
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
# Write the same function to check if a string is a palindrome

# def is_palindrome(str):


print(is_perm_palindrome("tacocat"))