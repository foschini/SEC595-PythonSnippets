#Partendo dal percorso mainDir, conto i fil-es e le directory. L'algoritmo sfrutta la ricorsione.
#funzioni della libreria os importanti sono:
#os.listdir(path)->restituisce lista di directories e files
#os.path.join(path1,path2)->restituisce path unione di due path inserendo i giusti separatori
#os.path.isdir(path)-> restituisce true se path è una directory. esiste anche os.path.isfile(path)

import os


def findDirectoriesAndFiles(subDir):
    nDirs=0
    nFiles=0
    listOfItems=os.listdir(subDir) #ottengo lista files e directories
    for item in listOfItems:
        pathToCheck=os.path.join(subDir,item)               #costruisco il path dell'item aggiungendo il path iniziale altrimenti isdir() non funziona
        if os.path.isdir(pathToCheck):                      #se è una directory
            nDirs+=1                                        #incremento il contatore directory
            items = findDirectoriesAndFiles(pathToCheck)    #e cerco i files e le directory contenute
            nDirs+=items[0]                                 #aggiungo le directory trovate nel contatore dell'attuale directory
            nFiles+=items[1]                                #aggiungo i files trovati nel contatore dell'attuale directory
            
        else:
            nFiles+=1
    return nDirs,nFiles
mainDir="C:\\Users\\afosc\\OneDrive\\ebooks"
nDirs=0
nFiles=0
items=findDirectoriesAndFiles(mainDir)
nDirs+=items[0]
nFiles+=items[1]

print(f"Ci sono {nDirs} directories e {nFiles} files")
        