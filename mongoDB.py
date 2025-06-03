#In MongoDB Atlas (cloud hosting di MongoDB) l'ambiente si compone di un cluster nel quale posso istanziare DBs e in ciascun DB una o più Collections. In questo esempio mi connetto al DB inserito nel cluster
# AndreaCluster. Il DB si chiama testDB e la collection testCollection.
# bisogna mettere l'IP del server su cui gira il codice in whitelist

from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://Andrea:mongodb123!@andreacluster.18aoaja.mongodb.net/?retryWrites=true&w=majority&appName=AndreaCluster")
dbList=cluster.list_database_names()
print("Lista DBs: ",dbList)
db=cluster["testDB"]
collectionList=db.list_collection_names()
print("Lista collections: ",collectionList)
collection=db["testCollection"]

collection.insert_one({"_id":0, "name": "Ciccio", "score":15}) #inserisco un "post" nel database. Il "post" è l'elemento atomico informativo che può essere inserito in un DB Mongo.
#collection.insert_one({"name":"Dario","Segni particolari": "Bellissimo"})
results=collection.find({"name":"tim"})
print("find name=tim: ",results)
results=collection.find_one({"_id":1}) #attenzione ad usare find_one: deve ritornare un unico valore quindi è bene usarlo solo per ricerche su base _id (che è per definzione univoco)
print("find_one _id=1: ",results)
results=collection.find({})
print("find parentesi graffe vuote : ")
for x in results:
    print(x)

collection.delete_one({"_id":0})
results=collection.find({})
print("find parentesi graffe vuote dopo cancellazione _id=0: ")
for x in results:
    print(x)

collection.update_one({"_id": 1},{"$set":{"name":"Fabio"}})