# Author - Dushyant Singh
# Github - https://github.com/dushyant60

# Python3 program to check whether an array can be 
# partitioned into K subsets of equal sum 

# Recursive Utility method to check K equal sum 
# subsetition of array 

"""* 
array	 - given input array 
subsetSum array - sum to store each subset of the array 
taken	 -boolean array to check whether element 
is taken into sum partition or not 
K		 - number of partitions needed 
N		 - total number of element in array 
curIdx	 - current subsetSum index 
limitIdx	 - lastIdx from where array element should 
be taken """

def isKPartitionPossibleRec(arr, subsetSum, taken, 
							subset, K, N, curIdx, limitIdx):
	if subsetSum[curIdx] == subset:
		
		""" current index (K - 2) represents (K - 1) 
		subsets of equal sum last partition will 
		already remain with sum 'subset'"""
		if (curIdx == K - 2):
			return True
		
		# recursive call for next subsetition 
		return isKPartitionPossibleRec(arr, subsetSum, taken, 
									subset, K, N, curIdx + 1 , N - 1)
	
	# start from limitIdx and include 
	# elements into current partition 
	for i in range(limitIdx, -1, -1):
		
		# if already taken, continue 
		if (taken[i]):
			continue
		tmp = subsetSum[curIdx] + arr[i] 
		
		# if temp is less than subset, then only 
		# include the element and call recursively 
		if (tmp <= subset):
			
			# mark the element and include into 
			# current partition sum 
			taken[i] = True
			subsetSum[curIdx] += arr[i] 
			nxt = isKPartitionPossibleRec(arr, subsetSum, taken, 
										subset, K, N, curIdx, i - 1)
										
			# after recursive call unmark the element and 
			# remove from subsetition sum 
			taken[i] = False
			subsetSum[curIdx] -= arr[i] 
			if (nxt):
				return True
	return False

# Method returns True if arr can be 
# partitioned into K subsets with equal sum 
def isKPartitionPossible(arr, N, K):
	
	# If K is 1,
	# then complete array will be our answer 
	if (K == 1):
		return True
	
	# If total number of partitions are more than N, 
	# then division is not possible 
	if (N < K):
		return False
		
	# if array sum is not divisible by K then 
	# we can't divide array into K partitions 
	sum = 0
	for i in range(N):
		sum += arr[i] 
	if (sum % K != 0):
		return False
	
	# the sum of each subset should be subset (= sum / K) 
	subset = sum // K 
	subsetSum = [0] * K 
	taken = [0] * N
	
	# Initialize sum of each subset from 0 
	for i in range(K):
		subsetSum[i] = 0
		
	# mark all elements as not taken 
	for i in range(N):
		taken[i] = False
		
	# initialize first subset sum as 
	# last element of array and mark that as taken 
	subsetSum[0] = arr[N - 1] 
	taken[N - 1] = True
	
	# call recursive method to check 
	# K-substitution condition 
	return isKPartitionPossibleRec(arr, subsetSum, taken, 
								subset, K, N, 0, N - 1)
	
# Driver Code
arr = [2, 1, 4, 5, 3, 3 ]
N = len(arr) 
K = 3
if (isKPartitionPossible(arr, N, K)):
	print("Partitions into equal sum is possible.\n")
else:
	print("Partitions into equal sum is not possible.\n")
