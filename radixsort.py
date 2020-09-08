# Chapter 8 Page 197

# Overall Time Complexity is O( d * (n + k) )
    # d : The number of digits in the largest number in the set
    # n : The number of elements in the set
    # k : The number of possible digits when in the counting array
    
# Overall Space Complexity is O( n + 2^d )
    # n : The number of elements in the set
    # d : The number of digits in the largest number in the set
    
# Overview:
    # [] When the initial sort method is called, the method finds the
    # max number within the set. The max number is then divided each time by
    # 10 * n times where n is the number of digits in the max number. Each time dividing,
    # The method counting sort, will be called on that particular column of numbers (i.e. ones column, tens column, hundreds column, ......) 
       
    # [] When __countingSort() is called:  
        # [] Makes a new 'counting' array to hold the recurrence of an element in the original array
        # [] The value at a index in the counting array, is how many times the index shows up in the original array
        # [] Each value at a index in the counting array is then added with the value of the index right before that index
            # [] If the index is i then counting[i] = counting[i] + counting[i - 1]  
        # [] A new Array is made to hold the sorted output
        # [] To get the index at which each element in the original array belongs at
            # (1) Get the value at the original array at [i]
            # (2) Use the value given at (1) in the counting array shifted to the right by 1 to get the index for each element to be stored in the sorted array
            # (3) Use the value given at (2) as the index in the new sorted array
            # (4) The index that is given for the sorted array at (3) is where the value of the original array at index [i] should be set  

# Important Notes:
    # This method of sorting is iterative. When the sort method is called, it calculates
    # the max number divided by 10 * n digits. When the max number divided by 10 * n is
    # approximately equal to zero, then the while loop will terminate.  
    
    # Radix sorts relies on a stable sorting algorithm
    # Stable Sorting Algorithm : "Maintain the relative order of records with equal keys"

# The starting point for the sorting algorithm    
def sort(array):
    
    # Finds the max number in the given array
    max_number = max(array)
    
    # exponential that is multiplied by 10 every time the while loop iterates through
    exp = 1
    # Checks to see if the max numbers maximum number column has been sorted
    while int(max_number/exp) > 0:
        # Calls the counting sort algorithm to sort the number column that is given
        __countingSort(array, exp)
        # After the array is sorted by the column, it moves on to the next number column
        exp *= 10

# Stable sorting algorithm that moves elements based on their recurrence, in the data set    
def __countingSort(array, exp): 

    # The final sorted array is to be sorted in here
    sorted = [0] * len(array)
  
    # The counting array holds the possible digits in a number column (0-9)
    # There are 10 possible digits a number can be when it goes through the counting sort algorithm
    counting = [0] * 10 
  
    # This for loop is in charge of looping through the oringal array and finding the recurrences in the array
    for i in range(0, len(array)): 
        # Each index in the counting array is the number in the original array
        index = (array[i]/exp)
        # The value for each index in the counting array in the number of ocurrences in the original array 
        counting[int((index)%10)] += 1
    
    # This for loop is in charge of adding each value at an index in the counting array with the value at the index right before
    # Note: The index i = 0, is not affected
    for i in range(1,10): 
        counting[i] += counting[i-1] 
   
    # This for loop is in charge of looping through the original array and placing each element in the correct sorted position
    for i in range(len(array) - 1, -1, -1):
        # Index is the number column being worked on in the original array
        index = array[i] / exp 
        # The index of sorted is the value of counting at the index of the number column in the original array shifted 1 to the right
        sorted[counting[int(index % 10)] - 1] = array[i] 
        # The number of occurances are brought down by 1
        counting[int(index%10)] -= 1
        
    # This foor loop is in charge of setting the inputted array equal to the sorted array, to reuse the given array
    for i in range(0, len(array)): 
        array[i] = sorted[i] 
    
        
            