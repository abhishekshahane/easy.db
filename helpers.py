import pickle
def file_delete(file):
    file.seek(0)
    file.truncate()
def file_write(db, file):
    pickle.dump(db, file)