import pickle
def file_delete(file):
    file.seek(0)
    file.truncate()
def file_write(db, file):
    pickle.dump(db, file)
def obj_query(db, path):
    ar = path.split(".")
    try:
        print(db[ar[1]])
        return db[ar[1]]
    except KeyError:
        print("Object not in db")