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


Possible Additions:

- The addition of multiple columns to a table(not just two).
