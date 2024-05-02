

array = [12, 43, 64, 38, 39, 29, 39]


"""# Linear search algorithm
def linearSearch(array, toFind):
    found = []
    for item in array:
        if item == toFind:
            found.append(item)
    print(f"Found the item {len(found)} times.")"""
    
# Quick sort
def partition(array, low, high): # Low & High pointer passed in params
    pivot = array[high] # Get init pivot
    
    pointerLow = low - 1 
    
    for item in range(low, high):
        if array[item] <= pivot: # Check to move right/left
            pointerLow += 1 # Incriment
            (array[pointerLow], array[item]) = (array[item], array[pointerLow]) # Swaps items
            
    (array[pointerLow + 1], array[high]) = (array[high], array[pointerLow + 1])
    
    return pointerLow + 1

def quickSort(array, low, high): # Main quicksort function
    
    if low < high:
        part = partition(array, low, high)
        quickSort(array, low, part - 1) # do left of pivot
        quickSort(array, part + 1, high) # do right of pivot
    

# Binary search algorithm
def binarySearch(array, toFind):
    low = 0
    high = len(array)-1
    
    quickSort(array, low, high) # binary search needs sorted list

    while low <= high:
        midpoint = (low + high)//2 # // to floor divide
        
        if array[midpoint] == toFind: 
            print(f"Found {toFind}")
            return toFind
        elif array[midpoint] < toFind:
            low = midpoint + 1
        else:
            high = midpoint - 1
    print("Item not found.")

binarySearch(array, 39) # Call binary search function
