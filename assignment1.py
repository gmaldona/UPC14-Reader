import csv
#import heapsort as hp
import quicksort
import radixsort

# This Method Parses the CSV file and stores it in a dictionary for easy access
def getDB():
    ITEM_DATABASE = {}
    upc14_collection = []
    
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
            

    return ITEM_DATABASE, upc14_collection



ITEM_DATABASE, upc14_collection = getDB() 
print(ITEM_DATABASE[0])
quicksort.sort(upc14_collection, 0, len(upc14_collection) - 1)
#upc14_collection = radixsort.sort(upc14_collection)
with open('Sorted Database.txt', 'w') as file:
    for i in range(0, len(upc14_collection)):
        file.write('{}, {}, {} \n'.format(
            ITEM_DATABASE.get(upc14_collection[i])[0], 
            ITEM_DATABASE.get(upc14_collection[i])[1], 
            ITEM_DATABASE.get(upc14_collection[i])[2])
                   )
        
    file.close()        
    