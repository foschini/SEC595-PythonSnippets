#Partendo dal percorso mainDir, conto i files e le directory. L'algoritmo sfrutta la ricorsione.
import os


def findDirectoriesAndFiles(subDir):
    nDirs=0
    nFiles=0
    listOfItems=os.listdir(subDir) #ottengo lista files e directories
    for item in listOfItems:
        pathToCheck=subDir+"\\"+item                        #costruisco il path dell'item aggiungendo il path iniziale altrimenti isdir() non funziona
        if os.path.isdir(pathToCheck):                      #se è una directory
            nDirs+=1                                        #incremento il contatore directory
            items = findDirectoriesAndFiles(pathToCheck)    #e cerco i files e le directory contenute
            nDirs+=items[0]                                 #aggiungo le directory trovate nel pathToCheck
            nFiles+=items[1]                                #aggiungo i files trovati nel pathToCheck
            
        else:
            nFiles+=1
    return nDirs,nFiles
mainDir="C:\\Users\\afosc\\Andrea"
nDirs=0
nFiles=0
items=findDirectoriesAndFiles(mainDir)
nDirs+=items[0]
nFiles+=items[1]

print(f"Ci sono {nDirs} directories e {nFiles} files")
        