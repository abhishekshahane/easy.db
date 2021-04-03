from main import db
#tests go here
#here, we are creating two new objects, baseball scores and names 
db = db()
db.__setname__("Things")
db.add("baseball_scores")
db.set_var("db.baseball_scores.Bob", 75)
db.add("names")
db.set_var("db.names.Arthur", 1)
db.remove_key("db.names.Arthur")
db.set_var("db.names.Arthur", 1)
#We haven't created an object with add, so this will give us an error
db.set_var("db.e.e", "e")
#prints one time - storing the result in a var, and then printing it
a = db.query("db.baseball_scores.Bob")
print(a)
#All items from the db

print(db.all())
