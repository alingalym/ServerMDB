import pymongo
my_client = pymongo.MongoClient(
    'mongodb+srv://gaga:Pass321@cluster0.gnqlxjh.mongodb.net/test?retryWrites=true&w=majority'
)
try:
    print("MongoDB version is %s" % 
            my_client.server_info()['version'])
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)
my_database = my_client.test
my_collection = my_database.records
my_collection.insert_one({
    "_id": 2,
    "name": "gaga",
    "position": "developer",
    "level":"senior"
})