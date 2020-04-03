""" BINARY SEARCH implementation
	both iterative and recursive
"""


def bin_search_iter(arr, value):
	""" iterative binary search
		arr: ordered / sorted list
		value: value to find 
	"""

	i_left = 0 
	i_right = len(arr)-1

	is_found = False

	while i_left <= i_right and not is_found:
		i_mid = (i_left + i_right) // 2

		if arr[i_mid] == value:
			is_found = True

		else:
			if arr[i_mid] > value:
				i_right = i_mid-1

			else:
				i_left = i_mid+1

	return is_found



def bin_search_recu(arr, value):
	""" recursive binary search 
		arr: ordered / sorted list
		value: value to find 
	"""

	if len(arr) == 1:
		return arr[0] == value

	i_mid = len(arr) // 2

	if arr[i_mid] == value:
		return True

	else:
		if arr[i_mid] > value: 
			return bin_search_recu(arr[0: i_mid], value)
		else:
			return bin_search_recu(arr[i_mid+1:], value)



