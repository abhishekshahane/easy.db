from main import db
#tests go here
#here, we are creating two new objects, baseball scores and names 
db = db()
db.__setname__("MyDB")
#This line isn't compulsory, since in set_var we are anyway creating the object, but i'll make it compulsory later
db.add("baseball_scores")
db.set_var("db.baseball_scores.Bob", 75)
db.add("names")
db.set_var("db.names.Arthur", 1)
print(db.all())
