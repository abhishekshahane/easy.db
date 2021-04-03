import pickle
def file_delete(file):
    file.seek(0)
    file.truncate()
def file_write(db, file):
    pickle.dump(db, file)
def obj_query(db, path):
    ar = path.split(".")
    try:
        return db[ar[1]]
    except KeyError:
        raise KeyError("Object not in db")
def key_query(db, path):
    ar = path.split(".")
    try:
        return db[ar[1]][ar[2]]
    except KeyError:
        raise KeyError("Object/key not in db.")