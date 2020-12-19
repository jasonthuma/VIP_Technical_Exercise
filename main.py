def findAllPairs(paramList, targetSum):
    allOutputPairs = []
    for i in range(len(paramList)):
        for j in range(len(paramList)):
            if i != j and paramList[i] + paramList[j] == targetSum:
                matchingIndices = (paramList[i], paramList[j])
                allOutputPairs.append(matchingIndices)
    for i in range(len(allOutputPairs)):
        print(allOutputPairs[i], end="")
        if i < len(allOutputPairs) - 1:
            print(", ", end="")
        else:
            print()


def findUniquelyOrderedPairs(paramList, targetSum):
    uniquelyOrderedOutputPairs = []
    for i in range(len(paramList)):
        for j in range(len(paramList)):
            if i != j and paramList[i] + paramList[j] == targetSum:
                matchingIndices = (paramList[i], paramList[j])
                if matchingIndices not in uniquelyOrderedOutputPairs:
                    uniquelyOrderedOutputPairs.append(matchingIndices)
    for i in range(len(uniquelyOrderedOutputPairs)):
        print(uniquelyOrderedOutputPairs[i], end="")
        if i < len(uniquelyOrderedOutputPairs) - 1:
            print(", ", end="")
        else:
            print()


def findUniquePairs(paramList, targetSum):
    uniqueOutputPairs = []
    for i in range(len(paramList)):
        for j in range(len(paramList)):
            if i != j and paramList[i] + paramList[j] == targetSum:
                matchingIndices = (paramList[i], paramList[j])
                reversedMatchingIndices = (paramList[j], paramList[i])
                if matchingIndices not in uniqueOutputPairs and reversedMatchingIndices not in uniqueOutputPairs:
                    uniqueOutputPairs.append(matchingIndices)
    for i in range(len(uniqueOutputPairs)):
        print(uniqueOutputPairs[i], end="")
        if i < len(uniqueOutputPairs) - 1:
            print(", ", end="")
        else:
            print()


def main():
    argList = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]
    desiredSum = 10
    findAllPairs(argList, desiredSum)
    findUniquelyOrderedPairs(argList, desiredSum)
    findUniquePairs(argList, desiredSum)


main()
