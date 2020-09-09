import time
import csv
import heapsort
import quicksort
import radixsort
import os
import sys

# This Method Parses the CSV file and stores it in a dictionary for easy access
def getDB(isSorted):
    ITEM_DATABASE = {}
    upc14_collection = []
    
    # If the user wants the file is not be already sorted
    if isSorted == False:
        # {Order Number, UPC14, UPC12, brand, name}
        with open('Grocery UPC Database.csv', newline='') as csvfile:
            # Separates Strings on the delimiter ','
            file = csv.reader(csvfile, delimiter= ',')
            # For each Row in the CSV file, contains a different item
            for row in file:
                # If the type is a string then the for loop will skip over the row
                if row[1] == 'upc14':
                    continue
                # key - UPC 14 Code
                # Value - UPC 14 Code, brand, name
                else: 
                    ITEM_DATABASE[int(row[1])] = [row[1], row[3], row[4]] 
                    upc14_collection.append(int(row[1]))
    
    # If the user wants the file is already sorted                
    else:
        with open('Sorted Database.csv', newline='') as csvfile:
            sys.setrecursionlimit(10**(6)) 
            file = csv.reader(csvfile, delimiter=',')
            for row in file:
                ITEM_DATABASE[int(row[0])] = [row[0], row[1], row[2]]
                upc14_collection.append(int(row[0]))
            

    return ITEM_DATABASE, upc14_collection

# Functionality
    
    # Dictionary (ITEM_DATABASE) that has the keys as the UPC14 codes that are stored as integers 
    # The values for the dictionary are arrays that contains the product information
    
    # index = 0 : String form of the UPC14 code (contains leading zeros)
    # index = 1 : Brand of the product
    # index = 2: Name of the product
    
    # Array (UPC14_COLLECTION) that just stores the UPC14 codes in the primative type int
    # The elements are stored as ints for sorting purposes
    
    # After the array is sorted (lowest -> greatest), the dictionary ITEM_DATABASE
    # has a .get(key) method that returns the value for that key. The keys in the 
    # dictionary are also stored as integers so the array can match up with the dictionary
    
    # To get an file output of all of the sorted items, a for loop go through all the
    # sorted elements in the array and matches the index of the upc code to the dictionary
    
# Method that is called to start the sorting of the data set
def sort(method, isSorted, i):
    
    # Tuple that is returned from the getDB() method
    # ITEM_DATABASE is a dictionary where the keys are integers and the values are an array
    # upc14_collection is an array of integers
    ITEM_DATABASE, upc14_collection = getDB(isSorted)
    
    while i < len(upc14_collection):
        if i == 0:
            break
        else:
            del upc14_collection[i]
    # Tracks the amount of time it takes for the algorithm to run
    start_time = time.clock()
    
    # Checks to see which method the user wants to use
    if method == 'QUICKSORT':
        quicksort.sort(upc14_collection) 
    elif method == 'RADIXSORT':
        radixsort.sort(upc14_collection)
    elif method == 'HEAPSORT':
        heapsort.sort(upc14_collection)
    
    # Ends the time when the algorithm is finished
    end_time = time.clock()
    # Prints the algorithm used and how long it took to compute
    clock = end_time - start_time
    print('{} DONE: {} seconds'.format(method, clock))
    
    #Opens the output sorted file and writes to the file to enter the newly sorted data
    with open('Sorted Database.csv', 'w') as file:
        
        #For each upc code, a new line in the file will be written
        for i in range(0, len(upc14_collection)):
            #Written in the format: UPC14 CODE, BRAND, PRODUCT NAME
            file.write('{}, {}, {} \n'.format(
                ITEM_DATABASE.get(upc14_collection[i])[0], 
                ITEM_DATABASE.get(upc14_collection[i])[1], 
                ITEM_DATABASE.get(upc14_collection[i])[2]
                                            )
                    )
            
        file.close()
        # OS opens the sorted text file
        os.system('open Sorted\ Database.csv')  

# If the user runs the program in interactive mode      
if __name__ == '__main__':
    print("---sort( 'The Sorting Method', isSorted? (T/F), number of elements to sort(int) )")