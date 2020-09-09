# Chapter 7 Page 170 

# WORST CASE RUN TIME - N^2
# AVERAGE CASE RUN TIME - (expected) n LOG n

# Overview:
    # The pivot point is set to the last index in the array
    # The right pointer is compared to the pivot and if the right pointer
    # is less than the pivot then the left pointer index increases
    # and then index at i and j are swapped
    # At the end of the for loop, the index one higher than i and j are swapped
    # and i + 1 is returned as the pivot

# Important Notes:
    # This method of sorting relies on recursion where the end case is if the right
    # pointer index is greater than the left pointer index

# Moves the pivot to the correct spot in the array
def partition(array, first, last):
    
    i = first - 1
    # Sets the pivot to the last element in the array or partitioned array
    pivot = array[last]
    
    #Loops through the starting and ending indices given 
    for j in range(first, last):
        # Checks if the index is less than the pivot
        if array[j] <= pivot:
            i = i + 1
            # Swaps the left pointer index and the right pointer index
            array[i], array[j] = array[j], array[i]
            
    #Swaps the left pointer index + 1 and the last index (pivot)
    array[i + 1], array[last] = array[last], array[i + 1]
    #Returns the index of the pivot
    return i + 1

def sort(array):
    __sort(array, 0, len(array) - 1)

# Recursive Function
def __sort(array, first, last):
    # End case: if the length of the partitioned array is equal to 1
    if len(array) == 1:
        return array
    # If starting index is less than the ending index then recursively call the method
    if first < last:
        # Finds the index of the pivot in the correct spot
        pivot = partition(array, first, last)
        # Recursively calls to partition the array before and after the array
        __sort(array, first, pivot - 1)
        __sort(array, pivot + 1, last) 