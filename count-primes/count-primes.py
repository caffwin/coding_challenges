# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Best to use a generator for this problem - only needs to memorize inital arguments provided
# and generates every number on-the-fly
# Range() has been converted to a generator by default in python3 


# for 7... i is 1, 2, 3, 4, 5, 6, 7
#                  *  *     *     * 

# 7 % 1 = 0 and 7 % 7 = 0
# 7 % 2, 7 % 3, 7 % 4, 7 % 5, 7 % 6 all have remainders (do not evenly divide)
# num % i = 0 means i divides evenly into num

# Write helper function to check if a single number is prime
def one_number_prime(number):

    # A prime number is a number that is:
    # Greater than one (wiki) and
    # Only divisible by itself and 1

    is_prime = True

    for i in range(1, number + 1):
        print(i)
        if i == 1:
            print("1 Divides into ", number)
        elif i > 1 and i < number:
            print("Elif statement entered - i is greater than 1, less than num")
            if number % i == 0:
                print("Another number divides into ", number)
                is_prime = False
            else:
                print("Keep looping")
    
        elif i == number:
            print("i is equal to number")
            
        i += 1

    if is_prime == False:
        return "Byenlo"

    return True


def count_primes(n):

    num_primes = []
    
    # First, check if n is a negative number
    if n < 0:
        return "n must be a positive integer"

    # Then check if it's 1
    if n == 1:
        return 0

    # This covers everything where n is greater than 1:
    for i in range(2, n + 1):
        if one_number_prime(i) is True: # if number is prime
            num_primes.append(i)
        i += 1

    # print("Num_primes list: ", num_primes)

    return len(num_primes)
    
# print(one_number_prime(4))

# print(one_number_prime(5))

# print(one_number_prime(6))

print(count_primes(7))


# print(one_number_prime(5))

# Prime means... 
# n % i == 0 for 1 and itself ONLY