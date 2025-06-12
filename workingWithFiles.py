import os
#Lettura files e path da sistema operativo
def getFilesList(startingDirectory):
    finalList=list()
    listOfFiles=os.listdir(startingDirectory)
    for file in listOfFiles:
        file=os.path.normpath(file)
        if os.path.isdir(file):
            #print(file," is a directory")
            c=True
        file_name=os.path.join(startingDirectory,file)
        finalList.append(file_name)
    return finalList
initialPath="C:\\Users\\afosc\\Andrea"

def listFilesInPath(initialPath):
    testPaths=os.listdir(initialPath)
    nDirectory=0
    nFiles=0

    for testPath in testPaths:
        testPath=os.path.join(initialPath,testPath)
        isDirectory=os.path.isdir(testPath)
        if isDirectory:
            subNDirectory,subNFiles=listFilesInPath(testPath)
            nDirectory+=1
            nDirectory+=subNDirectory
            nFiles+=subNFiles
            #print(testPath," is a directory")
        else:
            print(testPath)
            nFiles+=1
    return(nDirectory,nFiles)
numeriPath=listFilesInPath(initialPath)
print(f"Ci sono {numeriPath[0]} directory e {numeriPath[1]} files")
#print(getFilesList("z:/"))
#print(help(os.listdir))