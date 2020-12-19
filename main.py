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


def main():
    argList = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]
    desiredSum = 10
    findAllPairs(argList, desiredSum)


main()