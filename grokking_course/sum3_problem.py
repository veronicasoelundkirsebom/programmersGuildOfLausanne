# Problem : Sum of Three Values (see: https://www.educative.io/courses/grokking-coding-interview/3sum)
#
# Explore how to solve the 3Sum problem by finding unique triplets that sum to zero in an integer array. 
# This lesson teaches you to apply the two pointers pattern to efficiently traverse linear data structures and avoid duplicate results.
# 
# Statement :
# Given an integer array nums, find all unique triplets [nums[i], nums[j], nums[k]] 
# where i, j, and k are distinct indices, such that the three elements sum to zero.
# The result must not contain any duplicate triplets. The order of the output and 
# the order of elements within each triplet does not matter.

# Below is my messy first approach (seems to work, but too slow, probably driven by the check for duplicates)
# A better and clearner solution is explained here: https://www.youtube.com/watch?v=TBePcj8DgxM
# Some improvements: 
# 	stop iteration when nums[i]>0 (at this point all numbers in the sum will be positive and therefor not sum to zero)
#	avoid duplicates by skipping i when nums[i]==nums[i-1], something similar when changing j and k
#	if sum is zero change both k (=high) and j (=low) (if you stay on one, only duplicates will yield zero, so you have to move both pointers)

def three_sum(nums):
    
	nums.sort()

	print(f"nums={nums=} : ")

	N = len(nums)

	i, j, k = 0, 1, N-1

	sum0 = []

	for i in range(0,N-2):
	
		print(f"----------------------")
		print(f"{i=}")
		print(f"{j=}")
		print(f"{k=}\n")

		j = i + 1
		k = N - 1

		while j<k:
			
			sum3 = nums[i]+nums[j]+nums[k]
			print(f"\n{sum3=}")
			print(f"{sum0=}")

			if sum3 > 0:
				k = k - 1
			elif sum3 < 0:
				j = j + 1
			elif sum3 == 0:
				triplet_new = [nums[i],nums[j],nums[k]]
				triplet_new.sort()
				
				# Avoiding duplicates
				if len(sum0)>0:
					print(f"\n{triplet_new=}")
					print(f"previous ones : {sum0=}")
					unique = []
					
					for triplet_old in sum0:
						triplet_unique = [True,True,True]
						print(f"{triplet_old=}")
						for n in range(len(triplet_old)):
							if triplet_old[n]==triplet_new[n]:
								triplet_unique[n]=False
						print(f"{triplet_unique=}")
						unique.append(triplet_unique)
					
					flag_isUnique = True
					for triplet_unique in unique:
						if (triplet_unique[0]==False and triplet_unique[1]==False and triplet_unique[2]==False):
							print("not unique! : ")
							flag_isUnique = False
					
					if flag_isUnique:	
						sum0.append(triplet_new)

				
				if len(sum0)==0:
					print(f"len(sum0)==0 ==> {triplet_new=}")
					sum0.append(triplet_new)
				
				j = j + 1
				
	print(f"\nFinal result : {sum0=}")
	return sum0


nums = [-3,-1,0,1,2,3,-2,4]
nums = [0,0,0,-1,1,2,-2]

three_sum(nums)


# Input : nums = [0,0,0,-1,1,2,-2]
# Expected : [[-2,0,2],[-1,0,1],[0,0,0]]
# Final result : sum0=[[-2, 0, 2], [-1, 0, 1], [0, 0, 0]]

# Input : nums = [-3,-1,0,1,2,3,-2,4]
# Expected : [[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,0,1]]
# Final result : sum0=[[-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]