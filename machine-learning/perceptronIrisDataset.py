import os
import random
import numpy as np

path = os.getcwd()
#datasetPath = path + "/Datasets/IrisDataset.txt" #Path para o Linux
datasetPath = path + "\Datasets\IrisDataset.txt" #Path para o Windows

dataset = np.zeros([150,5])


def typeOfIrisNumber(x):
    if x == "Iris-setosa":
        return 0
    elif x == "Iris-versicolor":
        return 1
    elif x == "Iris-virginica":
        return 2
    else:
        return -1

def createDatasetMatrix():
    file = open(datasetPath, 'r')
    i = 0
    for line in file:
        line2 = line.strip()
        lineList = line2.split(',')
        for j in range(len(lineList)):
            if(j != len(lineList)-1):
                dataset[i][j] = float(lineList[j])
            else:
                dataset[i][j] = typeOfIrisNumber(lineList[j])
        if(typeOfIrisNumber(lineList[len(lineList)-1])) == -1:
            print("Error: Can't recognize " + lineList[len(lineList)-1])
            break            
    
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

def generateXAndY(trData, teData, classOfFlower):
    xOnes1 = np.ones((np.shape(trData)[0],1))
    xOnes2 = np.ones((np.shape(teData)[0],1))
    
    xTrData = np.append(xOnes1,trData[:,[0,1,2,3]], axis=1)
    yTrData = np.where(trData[:,4] == classOfFlower, 1,-1)
    
    xTeData = np.append(xOnes2,teData[:,[0,1,2,3]], axis=1)
    yTeData = np.where(teData[:,4] == classOfFlower, 1,-1)
    
    return xTrData,yTrData, xTeData, yTeData 

def h(x,w):
    result = np.dot(x,w)
    return np.where(result >= 0.0, 1,-1)
    
def perceptron(X,Y):
    w = np.zeros((1,np.shape(X[0])[0]))
    error = [0]
    stoppedByLimit = 0
    limit = 0
    while(len(error) != 0):
        if(limit < 1000):
            error.pop()
            for x,y in zip(X,Y):
                
                err = y - h(x,w.transpose())
                if (err != 0):
                    w = w + x*y
                    error.append(err)
            limit += 1
        else:
            stoppedByLimit = 1
            break

    return w,stoppedByLimit
    
def test(w,xTeData,yTeData):
    numR = 0
    numW = 0
    for x,y in zip(xTeData,yTeData):
        k = h(x,w)
        if (k == y):
            numR += 1
            print("Acertou! Classificação esperada: "+ str(y) + ", prevista: "+ str(k))
        else:
            numW += 1
            print("Errou! Classificação esperada: "+ str(y) + ", prevista: "+ str(k))
    print("Quantidade de acertos: "+ str(numR))
    print("Quantidade de erros: "+str(numW))

def separateEntry(w1,xTA):
    xA = []
    xNotA = []
    
    for i in range(np.shape(xTA)[0]):
        if(h(xTA[i,:],w1.transpose()) == 1):
            xA.append(xTA[i,:])
        elif (h(xTA[i,:],w1.transpose()) == -1):
            xNotA.append(xTA[i,:])

    if(len(xA) != 0):
        xA = np.array(xA)
    else:
        xA = np.zeros((1,1))
    if(len(xNotA) != 0):
        xNotA = np.array(xNotA)
    else:
        xNotA = np.zeros((1,1))

    return xA,xNotA

def reconstructY(xNS, testData):
    index = []
    j = 0
    for i in range(np.shape(testData)[0]):
        if (np.all(testData[i,:4] == xNS[j,1:5], axis=0)):
            index.append(i)
            j+=1
    return testData[index,4]

def classification(w1,w2,xTeDataS,yTeDataS,testData, choice):
    xSetosa,xNotSetosa = separateEntry(w1,xTeDataS)
    
    if( np.any(xSetosa) and np.any(xNotSetosa)  ):
        if(choice == 1):
            yNS = reconstructY(xNotSetosa,testData)
            yNotSetosa = np.where(yNS == 1, 1,-1)
            xVersi, xNotVersi = separateEntry(w2,xNotSetosa)
        elif(choice == 2):
            yNS = reconstructY(xNotSetosa,testData)
            yNotSetosa = np.where(yNS == 2, 1,-1)
            xNotVersi, xVersi = separateEntry(w2,xNotSetosa)
    else:
        xVersi = np.zeros((2,2))
        xNotVersi = np.zeros((2,2))

    return xSetosa, xVersi, xNotVersi

def finalTest(xSet,xVer,xVir,testData):
    hits = 0
    errors = 0
    j = k = t = 0
    print("Resultados:")
    for i in range(np.shape(testData)[0]):

        if j < np.shape(xSet)[0] and (np.all(testData[i,:4] == xSet[j,1:5], axis=0) and testData[i,4] == 0):
            print("Acertou! É setosa!")
            hits +=1
            j+=1
        elif j < np.shape(xSet)[0] and (np.all(testData[i,:4] == xSet[j,1:5], axis=0) and testData[i,4] != 0):
            print("Errou! Não é setosa!")
            errors += 1
            j+=1
        elif k < np.shape(xVer)[0] and (np.all(testData[i,:4] == xVer[k,1:5], axis=0) and testData[i,4] == 1):
            print("Acertou! É versicolor!")
            hits +=1
            k+=1
        elif k < np.shape(xVer)[0] and (np.all(testData[i,:4] == xVer[k,1:5], axis=0) and testData[i,4] != 1):
            print("Errou! Não é versicolor!")
            errors += 1
            k+=1
        elif t < np.shape(xVir)[0] and (np.all(testData[i,:4] == xVir[t,1:5], axis=0) and testData[i,4] == 2):
            print("Acertou! É virginica!")
            hits += 1
            t+=1
        elif t < np.shape(xVir)[0] and (np.all(testData[i,:4] == xVir[t,1:5], axis=0) and testData[i,4] != 2):
            print("Errou! Não é virginica!")
            errors += 1
            t+=1

    return hits, errors

createDatasetMatrix()
trainingData, testData = chooseTrainingData()


xTrDataS, yTrDataS, xTeDataS, yTeDataS = generateXAndY(trainingData, testData,0) 
wFinalS,stoppedByLimitS = perceptron(xTrDataS,yTrDataS)


xTrDataVe, yTrDataVe, xTeDataVe, yTeDataVe = generateXAndY(trainingData, testData, 2)
wFinalVe,stoppedByLimitVe = perceptron(xTrDataVe,yTrDataVe)

xSetosa,xVersi,xVirgi = classification(wFinalS,wFinalVe,xTeDataS,yTeDataS,testData,2)

hits, errors = finalTest(xSetosa,xVersi,xVirgi,testData)
hitRate = (hits / (np.shape(testData)[0])) * 100
print("O número de acertos foi: "+ str(hits) + " e os erros: "+ str(errors))
print("A taxa de acertos foi: " + str(hitRate) + "%")
#print("Pesos que dividem os iris-setosa dos não iris-setosa:")
#print(wFinalS)
#print("Pesos que dividem os iris-versicolor dos não iris-versicolor:")
#print(wFinalVe)

