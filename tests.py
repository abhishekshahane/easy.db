from main import db
import unittest

# Initializes DB
db = db()
db.__setname__("Things")

# Creates a baseball_scores table
db.add("baseball_scores")
db.set_var("db.baseball_scores.Bob", 75)

# Creates a names table
db.add("names")
db.set_var("db.names.Arthur", 1)

# Removes a key from the names table
db.remove_key("db.names.Arthur")
db.set_var("db.names.Arthur", 1)

# Tests
class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(db.query("db.baseball_scores.Bob"), 75)
    def test_2(self):
        self.assertEqual(db.all(), {'baseball_scores': {'Bob': 75}, 'names': {'Arthur': 1}})
if __name__ == "__main__":
    unittest.main()

