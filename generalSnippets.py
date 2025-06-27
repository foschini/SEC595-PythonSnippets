#DATA TYPES PRINCIPALI

#   TUPLE

myTuple=(4,"ciccio",6.72) #le tuple sono liste di oggetti ordinate e immutabili.

for element in myTuple: #le tuple sono iterabili
    print(type(element),element) #la funzione type restituisce il tipo di un oggetto

# se oltre a iterare una tupla voglio tenere traccia dell'indice di iterazione, uso enumerate 
# che restituisce una tupla contenente l'indice dell'oggetto corrente e una copia dell'oggetto.
for idx,item in enumerate(myTuple): 
    print(f"Item index: {idx}, item: {item}")

#la gestione delle eccezioni si fa con la sintassi "try: _________except:"

numerator = 6
denominators = (3,2,0)

for denominator in denominators:
    try:
        print(f"{numerator} fratto {denominator} uguale: ",numerator/denominator)
    except Exception as e:
        print(f"Non puoi dividere {numerator} per {denominator}: catturata eccezione:",e)
# LISTE
myList=[1, 2, 3]
print(f"myList={myList}")

myListTimesTwo=myList*2 #moltiplicare una lista per n significa fare .append per n volte della lista su se stessa
print(f"myListTimesTwo={myListTimesTwo}")

#NUMPY array

import numpy as np
#gli array di numpy sono liste di oggetti dello stesso tipo. se in fase di definizione inserisco oggetti di tipo diverso allora il costuttore riassegna il tipo
myNumpyArray=np.array([1,2,"ciccio"]) 
print(myNumpyArray,"gli interi 1 e 2 sono stati trasformati in stringhe")

myNumpyIntArray =np.array([1,2,4,5])
myNumpyIntArrayTimesTwo=myNumpyIntArray*2
print(f"myNumpyIntArray {myNumpyIntArray}")

#la moltiplicazione di un array Numpy per uno scalare è un array in cui ciascun elemento è il prodotto. 
#Si chiama broadcasting (esecuzione della trasformazione in broadcast su tutti gli elementi dell'array)
print(f"myNumpyIntArrayTimesTwo {myNumpyIntArray*2}") 

#np.shape è una proprietà degli np array che restituisce le dimensioni di un array (arr.shape). 
# np.reshape((n,m)) riarrangia gli elementi di un array arr, secondo le dimensioni indicate nella tupla (n, m).
#np.dim è una proprietà degli np array che restituisce il numero delle dimensioni di un array

print(f"myNumpyIntArray {myNumpyIntArray}")
print(f"La shape è: {myNumpyIntArray.shape}, e ndim è: {myNumpyIntArray.ndim}")
print(myNumpyIntArray.reshape(2,2))
print(f"La shape è: {myNumpyIntArray.shape}, e ndim è: {myNumpyIntArray.ndim}")

#per caricare dati da un file di testo uso np.genfromtxt(file.txt)
data_file = """nomi,cose,città
mario,casa,roma
luca,armadio,milano
marco,sedia,palermo
giovanni,racchetta,firenze
giuseppe,libro,orvieto"""

# Per testare senza un file fisico, uso StringIO
from io import StringIO
file_object = StringIO(data_file)

data=np.genfromtxt(file_object,delimiter=",",dtype=str) #np.genfromtxt assegna come default float e se non riesce a convertire allora inserisce stringa nan (Not A Number) se devo
#acquisire stringhe è meglio esplicitare dtype=str
print(data)
print(data.shape, data.ndim)

dataShuffled=data
np.random.shuffle(dataShuffled)#attenzione a np.random.shuffle(): non restituisce nulla, ma applica lo shuffle direttamente sull'array che gli si passa in argomento.

print(dataShuffled)

#DIZIONARI {}

myDict={"Nome":"Andrea","Età":50,"Capelli":"pochi"}

print(myDict)           #stampa il dizionario
print(myDict.keys())    #stampa una lista contenente le chiavi
print(myDict.values())  #stampa una lista contenente i valori
print(myDict.items())   #stampa una lista contenente le tuple (chiave,valore)

for key,value in myDict.items():    #ricordati che se iteri su un container di array, con il costrutto della virgola puoi ottenere puntatori a ciascun elemento dell'array.
    print(f"Chiave: {key}, Valore: {value}")