import math

# Chapter 6 Page 151

# To get parent node: floor(i/2)
# To get the left child node: 2i
# To get the right child node + 2i + 1

# WORST CASE RUN TIME - O ( n * LOG n )
# AVERAGE CASE RUN TIME - O ( n * LOG n )

def __heapify(array, n, i):
    
    # Initial assumption is that the parent node is already greater than both of their children nodes
    childNode_left = ( i * 2 ) + 1 
    childNode_right = ( i * 2 ) + 2 
    
    if childNode_left < n and array[childNode_left] > array[i]:
        largest = childNode_left
    else:
        largest = i 
    if childNode_right < n and array[childNode_right] > array[largest]:
        largest = childNode_right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        __heapify(array, n, largest)
    
def sort(array):
    
    n = len(array)
    
    for i in range(math.floor(n / 2) - 1, -1, -1):
        __heapify(array, n, i)
        
    for i in range(n - 1 , 0, -1): 
        array[0], array[i] = array[i], array[0]
        n = n - 1
        __heapify(array, i, 0)
        
    
        
        
    
    
    
    