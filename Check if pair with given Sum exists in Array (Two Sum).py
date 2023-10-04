# Check if pair with given Sum exists in Array (Two Sum)
# Examples: 
# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation:  If we calculate the sum of the output,1 + (-3) = -2
# Input: arr[] = {1, -2, 1, 0, 5}, x = 0
# Output: No

"""#BruteForce
def chkPair(A, size, x):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (A[i] + A[j] == x):
                return 1
    return 0"""

#Using Hashmap
def printPairs(arr, arr_size, sum): 
    # Create an empty hash map
    # using an hashmap allows us to store the indices
    hashmap = {} 
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in hashmap):
            print('Yes')
            return
        hashmap[arr[i]] = i
    print("No")

A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)