import os
import random
import numpy as np

path = os.getcwd()
#datasetPath = path + "/Datasets/SalaryDataset.txt" Path pra Linux
datasetPath = path + "\Datasets\SalaryDataset.txt" #Path pra Windows

dataset = np.zeros([52,6])

def createDatasetMatrix():
    file = open(datasetPath, 'r')
    i = 0
    for line in file:
        line2 = line.strip()
        lineList = line2.split(',')
        for j in range(len(lineList)):
            dataset[i][j] = float(lineList[j])         
        i+=1
    file.close()

def chooseInstance(numInstances):
    index = []

    for i in range(numInstances):
        x = random.randint(0,np.shape(dataset)[0]-1)
        while(x in index):
            x = random.randint(0,np.shape(dataset)[0]-1)
        index.append(x)
        
    return index

def chooseTrainingData():
    nLinesEntry = int(np.shape(dataset)[0] * 0.8)
    nColEntry = int(np.shape(dataset)[1])
    indexChosen = chooseInstance(nLinesEntry)
    
    entry = np.zeros((nLinesEntry, nColEntry))
    test = np.zeros((np.shape(dataset)[0] - nLinesEntry, nColEntry))

    for i in range(nLinesEntry):
        entry[i] = dataset[indexChosen[i]]

    j = 0
    for i in range(np.shape(dataset)[0]):
        if not(i in indexChosen):
            test[j] = dataset[i]
            j+=1

    return entry,test

def generateXAndY(trData, teData):  
    xTrData = np.copy(trData[:,[0,1,2,3,4]])
    yTrData = np.copy(trData[:,5])
    
    xTeData = np.copy(teData[:,[0,1,2,3,4]])
    yTeData = np.copy(teData[:,5])
    
    return xTrData,yTrData, xTeData, yTeData

def linearRegression(X,y):
    a =  np.dot(X.transpose(), X)
    pseudoInvX = np.dot(np.linalg.inv(a),X.transpose())

    return np.dot(pseudoInvX,y)

def test(w, xTeData, yTeData):
    N = np.shape(xTeData)[0]
    print("--------------------- Results -------------------------")
    for x,y in zip(xTeData,yTeData):
        y_line = np.dot(x,w.transpose())
        error = abs(y_line - y)
        print("Salary expected: " + str(y) + " | Salary provided: " + str(y_line) +
              " | Error: "+ str(error))

    a = np.subtract(np.dot(xTeData,w), y)
    mod2 = np.linalg.norm(a)**2.0
    totalError = mod2 / N

    print("------------------------------------------------------")
    print("Total error with w = "+ str(w)+" calculated is: " + str(totalError))



createDatasetMatrix()

trainingData, testData = chooseTrainingData()

xTrData, yTrData, xTeData, yTeData = generateXAndY(trainingData,testData)

w = linearRegression(xTrData,yTrData)

test(w,xTeData, yTeData)


