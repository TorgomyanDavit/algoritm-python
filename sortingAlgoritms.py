

arrayNum = [2, 1, 3, 5, 4]

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

        
print(f"currentElem {bubleSort(arrayNum)}")






