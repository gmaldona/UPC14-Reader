import math

# Chapter 6 Page 151

# WORST CASE RUN TIME - O ( n * LOG n )
# AVERAGE CASE RUN TIME - O ( n * LOG n )

# Overview:
    # [] When the initial sorting method is called, the inputted array is turned into a max
    # heap data structure where the root node has the greatest value and the each parent node has a greater
    # value than its child node
    
    # [] The heapify method makes sure that the max heap property is maintained before the sorting
    # algorithm and after each time a node is removed from the heap
    # [] Since the max heap stores the max element in the array at the root, the sorting algorithm sorts
    # from greatest to least starting at the length of the array to 0 {back to front} until the array is sorted
    # and then shortens the array by one for the next iterative call since the last element is already sorted
    # The terminating condition is when the largest value index is equal to the current index 
    
    
# Important Notes:
    # This sorting algorithm uses the data structure 'MAX HEAP' - The parent node is greater than
    # its children nodes

# This method maintains the max heap property by making sure each parent node is greater than both of their children nodes
# and the max value in the array is at the root of the heap
# This method works on a given height in the heap at once
def __heapify(array, n, i):
    
    # Indices of children node if i is the parent node
    childNode_left = ( i * 2 ) + 1 
    childNode_right = ( i * 2 ) + 2 
    
    # This if statement checks to see if the left child node index exist
    # also if the left child value is greater than the parent value
    if childNode_left < n and array[childNode_left] > array[i]:
        # Make the left child the greater value
        largest = childNode_left
    else:
        # Make the current index the largest
        largest = i 
    # This if statement checks to see if the right child node index exist
    # also if the right child value is greater than the parent value
    if childNode_right < n and array[childNode_right] > array[largest]:
        # Makes the right child the greater value
        largest = childNode_right
    
    # If the largest index is not the current index then that means one of the child nodes is greater than the parent node
    if largest != i:
        # Swap the parent node and the child node
        array[i], array[largest] = array[largest], array[i]
        # Recursively call heapify to maintain max heap property
        __heapify(array, n, largest)
    
# Recursive sorting method
def sort(array):
    
    n = len(array)
    
    # Sets up the max heap for the first time
    # starts from the bottom of the max heap and works up to the root of the heap {array[0]}
    for i in range(math.floor(n / 2) - 1, -1, -1):
        __heapify(array, n, i)
    
    # Where the sorting begins
    # Starts from the last node in the heap and works to the root of the heap    
    for i in range(n - 1 , 0, -1): 
        # the heap should already be in a MAX HEAP
        # swap the last element and the root.
        # The root node has the greatest element in the array
        array[0], array[i] = array[i], array[0]
        # Decrease the size of the heap by one because the last element is in the correct sorted index
        n = n - 1
        # maintain the heap property but not including the last removed element
        __heapify(array, i, 0)
        
    
        
        
    
    
    
    