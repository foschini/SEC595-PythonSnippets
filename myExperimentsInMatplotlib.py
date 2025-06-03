import matplotlib.pyplot as plt # Importa la libreria matplotlib per la creazione di grafici
import numpy as np # Importa la libreria numpy, spesso utile per operazioni numeriche

def myDrawSubPlot(ax, data, titolo, labelOrdinate): # Definisce una funzione per disegnare un singolo subplot
     # ax: l'oggetto Axes su cui disegnare
    # data: i dati da plottare
    # titolo: il titolo del subplot
    # labelOrdinate: l'etichetta dell'asse y

    ax.plot(data) # Disegna i dati sull'oggetto Axes specificato
    ax.set_title(titolo) # Imposta il titolo per il subplot
    ax.set_xlabel("Valori") # Imposta l'etichetta per l'asse x del subplot
    ax.set_ylabel(labelOrdinate) # Imposta l'etichetta per l'asse y del subplot

    # Assicura che le posizioni dei tick siano una lista/array corretto
    ax.set_xticks(list(range(len(data)))) # Imposta i tick dell'asse x in base alla lunghezza dei dati

    ax.autoscale(True, "both") # Adatta automaticamente gli assi per visualizzare tutti i dati
    ax.grid(True) # Aggiunge una griglia al subplot

figure, subplots = plt.subplots(2, figsize=(12, 6), dpi=100) # Crea una figura e un set di subplot (2 righe, 1 colonna)

squares = [i**2 for i in range(5)] # Calcola i quadrati dei numeri da 0 a 4
cubes = [i**3 for i in range(5)] # Calcola i cubi dei numeri da 0 a 4

# Passa gli oggetti Axes dei singoli subplot alla funzione
myDrawSubPlot(subplots[0], squares, "Quadrati dei numeri da 0 a 4", "Quadrati") # Disegna il primo subplot con i quadrati
myDrawSubPlot(subplots[1], cubes, "Cubi dei numeri da 0 a 4", "Cubi") # Disegna il secondo subplot con i cubi

# Regola il layout per evitare che titoli/etichette si sovrappongano
figure.tight_layout()

plt.show() # Mostra la figura con tutti i subplot
