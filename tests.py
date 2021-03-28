from main import db
#tests go here
#here, we are creating two new objects, baseball scores and names 
db = db()
db.add("baseball_scores")
db.set_var("db.baseball_scores.Bob", 75)
db.add("names")
db.set_var("db.names.Arthur", 1)
db.remove_key("db.names.Arthur")
db.set_var("db.names.Arthur", 1)
#We haven't created an object with add, so this will give us an error
db.set_var("db.e.e", "e")
#prints two times
a = db.query("db.baseball_scores")
print(a)

print(db.all())
