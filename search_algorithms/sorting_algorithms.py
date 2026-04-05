import argparse



# First version (not optimal)
def bubble_sort_1version(list_of_items):

	print(f"\nlist_of_items = {list_of_items}\n")

	a = list_of_items

	flag_swapped = True
	count_operation = 0

	while flag_swapped:

		flag_swapped = False
		
		
		for i in range(0,len(a)-1):

			a1 = a[i]
			a2 = a[i+1]

			count_operation = count_operation + 1
			print("count_operation",count_operation)
			print("len(a)**2",len(a)**2)
			print(" ")

			if a1>a2:
				
				a[i]=a2
				a[i+1]=a1
				a1=a2
				flag_swapped = True 

			print(f"idx={i}   : {a1} -> {a[i]}")
			print(f"idx={i+1}   : {a2} -> {a[i+1]}\n")

	print(f"\nSorted list : {a}")
			

# First version (not optimal)
def bubble_sort(list_of_items):

	arr = list_of_items

	print(f"\nInput array : {arr}")
	count_op=0

	for i in range(0,len(arr)):
		flag_swapped = False
		for j in range(0, len(arr)-1-i):
			count_op = count_op+1
			if arr[j]>arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				flag_swapped = True
		if flag_swapped == False:
			break
	
	print(f"\nSorted array : {arr} (c={count_op})")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="binary searh")
	parser.add_argument("-l","--list_of_items", type=float, nargs="+", required=True)
	
	args = vars(parser.parse_args())

	bubble_sort(args["list_of_items"])