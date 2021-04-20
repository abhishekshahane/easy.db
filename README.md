# easy.db
A simple db aimed for beginners familiar with programming, but not with databases. 
Features of this database:
 - Persistent storage - your data is not wiped when you restart, unless you wipe data.dict.
 - Easy to learn, easy to use.
 - Open source.
 - Can query the database with ease. 
<br>
Built using the power of hashmaps(or dictionaries).
<br>
<br>
DB structure:
<br>
DB → Object → Key : Value pair(s)
<br>
<br>
Documentation:
<br>

 - `__setname__(name)` sets the name for the database. This is a required function, and must be set each time you run your code.
 - `add(obj)` adds a object to the database. You must add an object using this function, before you call `set_var`(see below). 
 -  `remove_key(remove_path)` removes a key from a particular object in the database, when provided with a remove_path. Format: db.obj.key
 -  `remove_obj(remove_path_2)` removes a object from the database. Format: db.obj
 -  `set_var(path, var)` adds a key to the database in a object initialised with `add`(see above). Format: *path: db.obj.key*, *var = value*
 -  `query(path)` queries the database to find a object/key with a certain name. For advanced queries, pass in a extra parameter `query_args = ["STARTS" | "ENDS"] | "VALUE"` to query for keys/values. 
 -  `all()` returns everything in the database. 
<br>
An example of code using the module would be this:

```python

from main import db
# tests go here
# here, we are creating two new objects, baseball scores and names 

db = db()
# Setting the name for the database, VERY IMPORTANT!
db.__setname__("Things")

db.add("baseball_scores")
db.set_var("db.baseball_scores.Bob", 75)

db.add("names")
db.set_var("db.names.Arthur", 1)
db.remove_key("db.names.Arthur")

db.set_var("db.names.Arthur", 1)
# We haven't created an object with add, so this will give us an error

db.set_var("db.e.e", "e")
# prints one time - storing the result in a var, and then printing it

a = db.query("db.baseball_scores.Bob")

print(a)
# All items from the db

print(db.all())
```
