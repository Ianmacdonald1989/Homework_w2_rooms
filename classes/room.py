class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest =[]
        self.song = []

    def check_out(self, guest):
        self.guest.remove(guest) 

    
        
    # def room(self, room):
    #     if room <= 6:   
    #         return "You may have a room"
    #     if room >= 7:
    #         return "Sorry, we are full "