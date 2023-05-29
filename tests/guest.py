import unittest
from classes.guest import Guest

class Guest(unittest.TestCase):


    def test_new_guest(self):
        guest = Guest("Peter Jones")
        self.assertEqual(guest.name, "Peter Jones")

    def test_check_in(self):
        room = Room("Peters room", 2)
        guest = Guest("Peter Jones")
        room.check_in(guest)
        self.assertEqual(len(room.guest), 1)
        self.assertEqual(room.guest[0].name, "Peter Jones")
    


    def test_check_out(self):
        room = Room("Peters room", 2)
        guest = Guest("Peter Jones")
        room.check_in(guest)
        room.check_out(guest)
        self.assertEqual(len(room.guest), 0)

