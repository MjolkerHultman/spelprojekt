class Actor():
    def __init__(self, name, purse):
        self.name = name
        self.purse = purse
        self.inventory = []

        
    #method for simultaneously moving items and funds between actors
    #def buy(self, itemID, price):
        

class Shopkeeper(Actor):
    def __init__(self, name, purse, stingy, favouriteID, introduction):
        Actor.__init__(self, name, purse)
        self.stingy = stingy #multiplier for determining the values the script is willing to accept based off of the true value of a given item
        self.favourite = favouriteID #Item ID for their favourite thing
        self.introduction = introduction

    #def unacceptable(self, exchangedItemID):
       # exchangedItemID = 
       # return exchangedItemID

trinketGuy = Shopkeeper("Joachim", 50, 12, 1, "placeholder")
locketGuy = Shopkeeper("Balthazar", 120, 12, 2, "placeholder")

#The main list of all items
items = [
    {
        "id": 1,
        "name":"Placeholder",
        "description": "Placeholder"
    },
    {
        "id": 2,
        "name":"Placeholder",
        "description": "Placeholder"
    },
    {
        "id": 3,
        "name":"Placeholder",
        "description": "Placeholder"
    }
]

#Transaction loop draft

playerBid = 0
oppBid = 0

opponent = trinketGuy #placeholder

#while playerBid < 

for i in items: #Thing to find items of a given item ID
    if i['id'] == 1:
