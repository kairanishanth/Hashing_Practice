# def solve(arr):
#     hashmap={} 
#     for i in arr:
#         if i in hashmap:
#             hashmap[i]+=1 
#         else:
#             hashmap[i]=1 
#     for i in hashmap:
#         print(i," ",hashmap[i])
# arr=[10,20,20,10,10,20,5,20]
# print(solve(arr))


# Python 3 program to count frequencies
# of array items
# def countFreq(arr, n):
	
# 	# Mark all array elements as not visited
# 	visited = [False for i in range(n)]

# 	# Traverse through array elements
# 	# and count frequencies
# 	for i in range(n):
		
# 		# Skip this element if already
# 		# processed
# 		if (visited[i] == True):
# 			continue

# 		# Count frequency
# 		count = 1
# 		for j in range(i + 1, n, 1):
# 			if (arr[i] == arr[j]):
# 				visited[j] = True
# 				count += 1
		
# 		print(arr[i], count)

# # Driver Code
# if __name__ == '__main__':
# 	arr = [10, 20, 20, 10, 10, 20, 5, 20]
# 	n = len(arr)
# 	countFreq(arr, n)
	
# # This code is contributed by
# # Shashank_Sharma

# # This code is contributed by shubhamsingh10
# def solve(arr):
#     freq={}
#     for i in range(len(arr)):
#         if arr[i] in freq:
#             freq[arr[i]]+=1
#         else:
#             freq[arr[i]]=1 
            
#     for key,val in freq.items():
#         print(f"{key} {value}")
# arr = [10, 20, 20, 10, 10, 20, 5, 20]
# print(solve(arr))
# Python program to count frequencies of
# integers in array using Hashmap

def frequencyNumber(arr,size):
	# Creating a HashMap containing integer
		# as a key and occurrences as a value
		freqMap = {}

		for i in range(size):
			if (arr[i] in freqMap):

				# If number is present in freqMap,
				# incrementing it's count by 1
				freqMap[arr[i]] = freqMap[arr[i]] + 1
			else:

				# If integer is not present in freqMap,
				# putting this integer to freqMap with 1 as it's value
				freqMap[arr[i]] = 1

		# Printing the freqMap
		for key, value in freqMap.items():
			print(f"{key} {value}")

		
		Welcome to the Hashing_Practice wiki!




	#Counting frequencies of array elements
	# Input :  arr[] = {10, 20, 20, 10, 10, 20, 5, 20}
	# Output : 10 3
	#          20 4
	#          5  1
	# Input : arr[] = {10, 20, 20}
	# Output : 10 1
	#          20 2 
	# def solve(arr):
	# 	mp={} 
	# 	for i in arr:
	# 		if i in mp:
	# 			mp[i]+=1 
	# 		else:
	# 			mp[i]=1 
	# 	# for key,value in mp.items():
	# 	#     print(f"{key} {value}")
	# 	for x in mp:
	# 		print(x, " ", mp[x])
	# arr=[30,10, 20, 20, 10, 10, 20, 5, 20]
	# print(solve(arr))


# Driver Code
arr = [10, 20, 20, 10, 10, 20, 5, 20]
size = len(arr)
frequencyNumber(arr,size)

# This code is contributed by shinjanpatra
