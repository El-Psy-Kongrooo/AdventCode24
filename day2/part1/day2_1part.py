def getLists():
    reportsList = []
    with open ("day2_1part.txt", "r") as file:
        for line in file:
            reportsList.append(list(map(int,line.split())))
    return reportsList

def getIncDecList(reportList):
    incOrdecList = []
    for lst in reportList:
        isIncreasing = None  
        flag = True  
        for d in range(len(lst) - 1):
            if lst[d] < lst[d + 1]:
                if isIncreasing is None:
                    isIncreasing = True
                elif not isIncreasing:
                    flag = False
                    break
            elif lst[d] > lst[d + 1]:  
                if isIncreasing is None:
                    isIncreasing = False
                elif isIncreasing:
                    flag = False
                    break
        if flag:  
            incOrdecList.append(lst)
    return incOrdecList

def calculateValidLists(incOrderList):
    validReports = 0
    for lst in incOrderList:
        isValid = True  
        for d in range(len(lst) - 1):
            complement = abs(lst[d] - lst[d + 1])
            if complement not in [1, 2, 3]:
                isValid = False  
                break  
        if isValid:  
            validReports += 1
    return validReports

def main():
    reportList = getLists()
    incOrdecList= getIncDecList(reportList)
    validReports=calculateValidLists(incOrdecList)
    print("Number of valid reports", validReports)

main()
