import pickle
import os
class db:
    def __init__(self):
        #lists all things in the directory
        arr = os.listdir()
        self.db = {}
        if 'data.dict' in arr:
            self.file = open('data.dict', "rb+")
            if os.path.getsize("data.dict")==0:
                self.db = {}
            else:
                self.db = pickle.load(self.file)
        else:
            self.file = open("data.dict", "wb") 
    def __setname__(self, name):
        self.name = name    
    #To add an object
    def add(self, obj):
        self.obj = obj
        try:
            if self.name:
                self.db[self.obj] = {}
                #goes to the beginning of the file, deletes everything, and rewrites the file
                self.file.seek(0)
                self.file.truncate()
                pickle.dump(self.db, self.file)
        #gets rid of attributeerror saying name doesn't exist
        except AttributeError:
            print("Name not set, set with __setname__")
    def set_var(self, path, var):
        #In progress
        self.path = path
        self.var = var
    def all(self):
        print(self.db)

db = db()
db.__setname__("Bob")
db.add("test")
db.all()

