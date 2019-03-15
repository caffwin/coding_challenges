# Sliding Window

nums = [3, -1, 5, 7, 2, 0, 1]
k = 3 # window size

# sliding_window_max(nums, k) ->
#   [ (3, -1, 5) , 7, 2, 0, 1 ]
#      => 5
#   [ 3, (-1, 5, 7), 2, 0, 1]
#          => 7
#   ...

#   [5, 7, 7, 7, 2]


# Input: list of ints
# Output: list of ints

# k is window size
# output is a list of max num per window

# nums = [] > return empty list
# num = [1, -1], k = 3 > return empty list

# [3, -1, 5, 7, 2, 0, 1] => 7 digits
#  0   1  2  3  4  5  6

# 0, 1, 2
# 1, 2, 3
# 2, 3, 4
# 3, 4, 5
# 4, 5, 6

# in a 7 digit list, we want five instances of the sliding window

# number of instances of sliding window is: len(nums) - (k -1) 

# [3, -1, 5, 7, 2 ] => 5 digits
# k = 2 

# 3, -1
# -1, 5
# 5, 7
# 7, 2

# Create a new list 
# Iterate through nums list with restrictions


def sliding_window_nums(nums, k):
    
    
    sliding_window = []# len will be k
    final_list = []
    
    # [3, -1, 5, 7, 2, 0, 1]
    #  |      |
    #  i     i + k
    # for i in range(len(numS))
    #    j = i + k
    
    # 0, 1, 2
    # 1, 2, 3
    # 2, 3, 4
    # 3, 4, 5
    # 4, 5, 6
    # nums[i:i+k]
    # if k if 3, then nums[i], nums[i+1], nums[i+2]
    
    for i in range(0, len(nums) - (k-1)):
        # sliding_window.append(nums[i])
        
        # Compute the max(window)
        max_num = nums[i]
        
        for num in nums[i:i+3]:
            print("num in nums[i:i+3]", num)
            # print("Num", num)
            # if num > max_num:
            #     max_num = num
            #     print("Max num", max_num)
            
        # append the max_num to final_list
        final_list.append(num)

    return final_list
    # check in sliding_window for max

    
    
print(sliding_window_nums(nums, k))
