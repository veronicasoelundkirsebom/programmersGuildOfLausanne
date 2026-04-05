
import argparse


# Function takes a sorted list of integers and one integer to be searched for 

# Things to improve:
# -> What should one do to make it work for floats?..
# -> check list is sorted and sort if it is not

# Run example 

# python binary_search.py -l 1 2 6 7 9 -i 2


def binary_search(a, item):

	print(f"\nStarting binary search for {item} in list {a}...")

	# Initial indices defining the search boundaries
	low = 0
	high = len(a)-1

	while high>=low:

		# Guess index (round down if mid_idx is not even)
		mid_idx = ( low + high ) // 2

		# Guess value 
		guess = a[mid_idx]
		print(f"\nguess is : {guess} (mid_idx={mid_idx})")

		# Check guess and update low and high
		if guess == item:
			print(f"\nReturning index = {mid_idx} as a[{mid_idx}] = {guess} == {item}\n")
			return mid_idx
		elif guess < item: # we move up
			low = mid_idx+1
		elif guess > item: # we move down
			high = mid_idx-1

		print(f"updated: low={low}, high={high}")
	else:
		print(f"\nReturning NULL as {item} is not found\n")
		return None

	

	


	











if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="binary searh")
	parser.add_argument("-l","--list_of_items", type=int, nargs="+", required=True)
	parser.add_argument("-i","--item", type=int, required=True)

	args = vars(parser.parse_args())

	binary_search(args["list_of_items"], args["item"])



