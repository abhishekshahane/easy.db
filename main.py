import pickle
import os
# Helper function imports. 
from helpers import file_delete, file_write, obj_query, key_query

# Specific function imports.
from advanced_query import advanced_query
# Creating a class for all of the database.
class db:


    def __init__(self):
        # Lists all things in the directory.
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


    # To add an object.
    def add(self, obj):
        self.obj = obj
        try:
            if self.name:
                self.db[self.obj] = {}
                # Goes to the beginning of the file, deletes everything, and rewrites the file.
                file_delete(self.file)
                file_write(self.db, self.file)
        # Raises AttributeError, saying name doesn't exist.
        except AttributeError:
            raise AttributeError("Name not set, set with __setname__.")


    def remove_key(self, remove_path):
        # Function to remove a key.
        self.remove_path = remove_path
        ar = self.remove_path.split('.')
        try:
            if self.name:
                o = ar[1]
                ke = ar[2]
                try:
                    del self.db[o][ke]
                    file_delete(self.file)
                    file_write(self.db, self.file)
                except KeyError:
                    raise KeyError(f"Key (or object) doesn't exist in {self.name}.")
        except AttributeError:
            raise AttributeError("Name not set, set with __setname__")


    def remove_obj(self, remove_path_2):
        """
        Removing an object is simple in easy.db.
        Breakdown of remove_path_2:
        - db.obj, where obj is the object.
        That's it!
        """
        self.remove_path_2 = remove_path_2
        ar = self.remove_path_2.split(".")
        ob = ar[1]
        try:
            del self.db[ob]
            file_delete(self.file)
            file_write(self.db, self.file)

        except KeyError:
            raise KeyError(f"Object doesn't exist in {self.name}.")



    def set_var(self, path, var):
        # Sets a new object in the db.
        try:
            self.name
            self.path = path
            self.var = var
            ar = self.path.split(".")
            # ar[1] is obj, ar[2] is var       
            get_obj = ar[1]         
            var_insert = ar[2]
            if get_obj not in self.db:
                raise NameError(f"Object not found in {self.name}, set it.")
                return
            file_delete(self.file)
            self.db[get_obj][var_insert] = self.var
            file_write(self.db, self.file)
            pickle.dump(self.db, self.file)
        
        except AttributeError:
            raise AttributeError("Name not set, set with __setname__.")


    def query(self, *args):
    # obj = db.obj or db.obj.key
        ar = [arg for arg in args]
        if len(ar) >= 2:
            results = advanced_query(args, self.db)
            return results
        if len(ar) < 1:
            raise AttributeError("Pass in correct number of arguments!")
            return
        else:
            if len(ar[0].split(".")) == 2:
                return obj_query(self.db, ar[0]) 
            elif len(ar[0].split(".")) == 3:
                return key_query(self.db, ar[0])
    def all(self):
        return self.db