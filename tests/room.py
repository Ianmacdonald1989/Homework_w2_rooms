import unittest

from classes.room import Room


class Room(unittest.TestCase):

    def Test_Room(self, room):
        room = Room("Peters room", 2)
        self.assertEqual(room.name, "Peters room")
    
    def tests_room_capacity(self, room):
        self.assertEqual(room.capacity, 2)
    
    def tests_room_left(self, room):
        self.assertEqual(len(room.guest), 0)

        self.assertEqual(len(room.song), 0)