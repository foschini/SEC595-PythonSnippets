import pandas as pd

#dataseries


#Pandas è una libreria costruita su numpy e ne espande 
#definisco una struttura dizionario
d = {'col1': [10, 25, 40], 'col2': [30, 45,60],'col3':[50,75,100]}
print(d)
#creo una struttura DataFrame Pandas, impostando indici di riga in modo esplicito. Se non metto nulla gli indici di riga sono 0,1,2...
df2 = pd.DataFrame(data=d, index=["riga1","riga2","riga3"])
print(df2)
#faccio slicing degli ultimi 4 valori
print(df2[1:])
#estraggo la riga 1 con pd.loc che si basa su eticetta
element=df2.loc["riga1"]

print(f"riga1: {element}")

#estraggo la colonna 1. Attenzione, visto che di default loc serve per estrarre le righe, se voglio estrarre una colonna devo dirgli che voglio tutte le righe e poi l'etichetta della colonna
element=df2.loc[:,"col1"]

print(f"col1: {element}")

#estraggo la riga in cui il valore in col2 è 60
riga10=df2.loc[df2["col2"]==60]
print(riga10)

#faccio lo stesso con iloc, che estrae su base indice numerico e no su base etichetta.

element=df2.iloc[0]
print(f"Index0: {element}")
element=df2.iloc[:,0]
print(f"index di colonna 0: {element}")

element=df2.loc[df2["col2"]==45]