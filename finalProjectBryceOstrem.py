import pymongo # imports functions to maniplate  mongo databases
import numpy # adds functions to convert 
try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/") # creates mongo client object object and creates a connnection to it
    print("connection established")
except:
    print("coulden't establish connection") # prints if connection couldn't be connected
mydb = myclient["store"] # creates array for managing data
mycol = mydb['transactions'] # creates array to hold
collist = mydb.list_collection_names()
print(mycol) # debugging code
if "transactions" in  collist:
    try:
        #results = numpy.asarray(collist["transactions"])
        for I in mycol.find():
            print(I)
    except Exception as e: 
        print(e)
else: 
    print("the collection does not exist")
    
