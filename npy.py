import random


def randomChooseShortestIndex(queueMatrix):
    # Find the minimum length among the sub-lists
    minLength = min(len(subList) for subList in queueMatrix)

    # Find all indices where the sub-list length matches the minimum length
    shortestIndices = [
        i for i, subList in enumerate(queueMatrix) if len(subList) == minLength
    ]

    # Randomly choose one of the indices
    return random.choice(shortestIndices)


def generateNewCustomer(newCustomerProb) -> bool:
    return random.random() < newCustomerProb


def generateServiceTime(serviceTimeMean):
    return random.randint(1, serviceTimeMean * 2 + 1)


def simulation(totalRunTime, cashierNumber, serviceTimeMean, newCustomerProb):
    queueMatrix = []
    servedCustomerNumber = 0
    leftCustomerNumber = 0
    totalWaitTime = 0
    for i in range(cashierNumber):
        queueMatrix.append([])

    while totalRunTime:
        if generateNewCustomer(newCustomerProb):
            shortestIndex = randomChooseShortestIndex(queueMatrix)
            serviceTime = generateServiceTime(serviceTimeMean)
            queueMatrix[shortestIndex].append([serviceTime, totalRunTime - serviceTime])

        totalRunTime -= 1

        for i in range(cashierNumber):
            if len(queueMatrix[i]):
                queueMatrix[i][0][0] -= 1
                if queueMatrix[i][0][0] == 0:
                    totalWaitTime += queueMatrix[i][0][1] - totalRunTime
                    servedCustomerNumber += 1
                    queueMatrix[i].pop(0)

    print("========================================================")
    print("所服务的顾客总数: ", servedCustomerNumber)
    for i in range(cashierNumber):
        if len(queueMatrix[i]):
            leftCustomerNumber += len(queueMatrix[i])
            servedCustomerNumber += 1
            totalWaitTime += queueMatrix[i][0][1] + queueMatrix[i][0][0]

    print("剩余的顾客总数: ", leftCustomerNumber)
    print("平均等待时间: ", totalWaitTime / servedCustomerNumber)


if __name__ == "__main__":
    totalRunTime = 3333
    cashierNumber = 5
    serviceTimeMean = 5
    newCustomerProb = 0.8
    simulation(totalRunTime, cashierNumber, serviceTimeMean, newCustomerProb)
