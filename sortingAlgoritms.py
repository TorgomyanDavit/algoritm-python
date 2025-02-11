import math

arrayNum = [2, 1, 3, 5, 4]
''' 
    Bubble Sort repeatedly compares adjacent elements in an array and swaps them 
    if they are in the wrong order. This process continues in multiple passes until 
    no swaps are needed, meaning the array is sorted. During each pass, larger elements 
    "bubble up" to their correct positions, starting from the beginning of the array.
'''

def bubleSort(input):
    swipped = True
    length = len(input)

    while(swipped):
        swipped = False

        for index in range(length - 1):
            currentElem = input[index]
            nextElem = input[index + 1]

            if currentElem > nextElem: 
                input[index] = nextElem
                input[index + 1] = currentElem
                swipped = True

    return input

        
# print(f"currentElem {bubleSort(arrayNum)}")


def SelectionSort(input):
    length = len(input)
    for index in range(length - 1):
        minIndex = index  # Assume the current index is the smallest

        # Find the smallest element in the unsorted portion
        for ind in range(index + 1, length):
            if input[ind] < input[minIndex]:
                minIndex = ind

        # Swap the smallest element with the first element of the unsorted portion
        if minIndex != index:
            elem = input[index]
            input[index] = input[minIndex]
            input[minIndex] = elem

    return input

# Test the function
# print(f"Sorted list: {SelectionSort([3, 2, 5, 4, 1])}")

def InsertionSort(input):
    length = len(input)
    for index in range(1,length - 1):
        nextElement = input[index]  
        prevElement = index - 1  

        # Find the smallest element in the unsorted portion
        while(prevElement >= 0 and input[prevElement] > nextElement):
            input[prevElement + 1] = input[prevElement]
            prevElement -= 1

        
        input[prevElement + 1] = nextElement
    return input

# Test the function
# print(f"Sorted list: {InsertionSort([3, 2, 5, 4, 1])}")



def QuickSort(input):
    length = len(input)

    if length == 0:
        return []

    pivot = input[0]
    less = []
    equal = []
    greater  = []

    for index in range(0, length):  # Start from index 1 (skip pivot)
        if input[index] < pivot:
            less.append(input[index])
        elif input[index] > pivot:
            greater.append(input[index])
        else:
            equal.append(input[index])  # Add to 'equal' if equal to pivot
    

    
    lessArr = QuickSort(less)
    greaterArray = QuickSort(greater)

    return lessArr + equal + greaterArray

# Test the function
# print(f"Sorted list: {QuickSort([3, 2, 5, 4, 1])}")

def merge(leftArray, rightArray):
    sortedArray = []
    
    while len(leftArray) > 0 and len(rightArray) > 0:
        if leftArray[0] < rightArray[0]:
            sortedArray.append(leftArray.pop(0))
        else:
            sortedArray.append(rightArray.pop(0))

    # Add remaining elements
    sortedArray.extend(leftArray)
    sortedArray.extend(rightArray)

    return sortedArray

def MergeSort(inputArray):
    length = len(inputArray)
    if length <= 1:
        return inputArray

    middle = length // 2  
    left = inputArray[:middle]
    right = inputArray[middle:]

    return merge(MergeSort(left), MergeSort(right))

# Test the function
print(f"Sorted list: {MergeSort([3, 2, 5, 4, 1])}")
