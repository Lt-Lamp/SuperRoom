###########################################################################################
# Name: Dominick, Travis, Will, and Juan
# Date: 5-16-17
# Description: Room Adventure Zodiac
###########################################################################################

from Tkinter import *
import RPi.GPIO as GPIO
from time import sleep

class Room(object):
    # the constructor
    def __init__(self, name, image):
	    # rooms have a name, an image (the name of a file), exits (e.g., south), exit locations (e.g., to the south is room n),
	    # items (e.g., table), item descriptions (for each item), and grabbables (things that can
	    # be taken into inventory)
	    self.name = name
	    self.image = image
	    self.exits ={}
	    self.items = {}
	    self.grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
	    return self._name

    @name.setter
    def name(self, value):
	    self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
	    return self._exits

    @exits.setter
    def exits(self, value):
	    self._exits = value

    @property
    def items(self):
	    return self._items

    @items.setter
    def items(self, value):
	    self._items = value

    @property
    def grabbables(self):
	    return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
	    self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
	    # append the exit and room to the appropriate dictionary
	    self._exits[exit] = room

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
	    # append the item and description to the appropriate dictionary
	    self._items[item] = desc

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
	    # append the item to the list
	    self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
	    # remove the item from the list
	    self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
	    # first, the room name
	    s = "You are in {}.\n".format(self.name)

	    # next, the items in the room
	    s += "You see: "
	    for item in self.items.keys():
		    s += item + " "
	    s += "\n"

	    # next, the exits from the room
	    s += "Exits: "
	    for exit in self.exits.keys():
		    s += exit + " "

	    return s

# The Game Class
# inherits from Frame class of Tkinter
class Game(Frame):
    # The Constructor
    def __init__(self, parent):
        # call the constuctor in the superclass
        Frame.__init__(self, parent)

################################################
# 
################################################
    # create the rooms
    def createRooms(self): 
        # currentRoom is the room the player is currently in (which can be one of r1 through r4)

        # create the rooms and give them meaningful names and an image in the current directory
        r1 = Room("Aquarius Room", "Aquarius.gif")
        r2 = Room("Pisces Room", "Pisces.gif")
        r3 = Room("Aries Room", "Aries.gif")
        r4 = Room("Taurus Room", "Taurus.gif")
        r5 = Room("Gemini Room", "Gemini.gif")
        r6 = Room("Cancer Room", "Cancer.gif")
        r7 = Room("Leo Room", "Leo.gif")
        r8 = Room("Virgo Room", "Virgo.gif")
        r9 = Room("Libra Room", "Libra.gif")
        r10 = Room("Scorpio Room", "Scorpio.gif")
        r11 = Room("Sagittarius Room", "Sagittarius.gif")  
        r12 = Room("Capricorn Room", "Capricorn.gif")
        r13 = Room("Ophiuchus Room", "Ophiuchus.gif")
        r14 = Room("Start Room", "StartRoom.gif")
        
        # add exits to Aquarius
        r1.addExit("south", r3)
        # add grabbables to Aquarius
        r1.addGrabbable("aquarius-gem")
        # add items to Aquarius
        r1.addItem("chair", "It is made of winster and no one is sitting on it but there seems to be scroll laying on the seat.")
        r1.addItem("lamp", "A normal looking lamp.")
                   
        # add exits to Pisces
        r2.addExit("east", r3)
        r2.addExit("south", r6)
        # add grabbables to Pisces
        r2.addGrabbable("pisces-gem")
        # add items to Pisces
        r2.addItem("rug", "It is nice and Indian. Oh there seems to be a gem on the ground next to it.")
        r2.addItem("fireplace", "It is full of ashes.")

        # add exits to Aries
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        r3.addExit("south", r14)
        r3.addExit("west", r2)
        # add grabbables to Aries
        r3.addGrabbable("aries-gem")
        # add items to Aries
        r3.addItem("statue", "There is nothing special about it.")
        r3.addItem("desk", "The statue is resting on it.  So is a gem!")

        # add exits to Taurus
        r4.addExit("west", r3)
        r4.addExit("south", r7)
        # add grabbables to Taurus
        r4.addGrabbable("taurus-gem")
        # add items to Taurus
        r4.addItem("table", "It is made of oak, and a gem rests on it.")
        r4.addItem("book", "A book with the title Paul Bunyun.") 

        # add exits to Gemini
        r5.addExit("east", r6)
        # add grabbables to Gemini
        r5.addGrabbable("gemini-gem")
        # add items to Gemini
        r5.addItem("closet", "You rummage around and you spot a gem!")
        r5.addItem("window", "The sky sure does look beautiful.")

        # add exits to Cancer
        r6.addExit("north", r2)
        r6.addExit("west", r5)
        r6.addExit("east", r14)
        r6.addExit("south", r9)
        # add grabbables to Cancer
        r6.addGrabbable("cancer-gem")
        # add items to Cancer
        r6.addItem("clock", "Tick Toc Tick Toc")
        r6.addItem("box", "You open the box and find a gem!")

        # add exits to Leo
        r7.addExit("north", r4)
        r7.addExit("east", r8)
        r7.addExit("west", r14)
        r7.addExit("south", r11)
        # add grabbables to Leo
        r7.addGrabbable("leo-gem")
        # add items to Leo
        r7.addItem("chest", "Just a bunch of dusty old clothes but under those clothes is hidden a gem!")
        r7.addItem("sofa", "A comfy looking sofa to relax on.")
                   
        # add exits to Virgo)
        r8.addExit("west", r7)
        # add grabbables to Virgo
        r8.addGrabbable("virgo-gem")
        # add items to Virgo
        r8.addItem("bed", "A well made bed ready to sleep in.")
        r8.addItem("pillow", "You lift the pillow up and see a gem!") 
                
        # add exits to Libra
        r9.addExit("north", r6)
        r9.addExit("east", r10)
        # add grabbables to Libra
        r9.addGrabbable("libra-gem")
        # add items to Libra
        r9.addItem("bookshelves", "A assortment of books covering mostly on the stars.")
        r9.addItem("book", "With sheer luck you pick a book out and find it hollowed out with a gem lying inside!.")

        # add exits to Scorpio
        r10.addExit("north", r14)
        r10.addExit("east", r11)
        r10.addExit("west", r9)
        r10.addExit("south", r12)
        # add grabbables to Scorpio
        r10.addGrabbable("scorpio-gem")
        # add items to Scorpio
        r10.addItem("wardrobe", "A very old looking handcrafted wardrobe.")
        r10.addItem("drawer", "You spot a gem mixed with a bunch of random things.")
        
        # add exits to Sagittarius
        r11.addExit("north", r7)
        r11.addExit("west", r10)
        # add grabbables to Sagittarius
        r11.addGrabbable("sagittarius-gem") 
        # add items to Sagittarius
        r11.addItem("workbench", "It has a variety of tools layed out and there is a gem amgonst them.")
        r11.addItem("stool", "A sturdy stool fit for anyone to sit on.")  
        
        # add exits to Capricorn
        r12.addExit("north", r10)
        r12.addExit("south", r13)
        # add grabbables to Capricorn
        r12.addGrabbable("capricorn-gem")
        # add items to Capricorn
        r12.addItem("nightstand", "A vase and gem are placed on the stand!")
        r12.addItem("painting", "The painting is of a night sky with stars shining bright.")
        
        # add exits to Ophiuchus
        r13.addExit("north", r12)
        # add grabbables to Ophiuchus
        r13.addGrabbable("crown")
        # add items to Ophiuchus
        r13.addItem("crown", "A beautiful crown decorated with the gems of the zodiacs granting unlimited power to the wearer.")
        
        # add exits to StartRoom
        r14.addExit("north", r3)
        r14.addExit("east", r7)
        r14.addExit("west", r6)
        r14.addExit("south", r10)
        # add grabbables to StartRoom
        # add items to StartRoom
        r14.addItem("rulebook", "Explore each room to find each zodiacs respective gem. When a gem is found type (take zodiacsname-gem, ex. take apollo-gem). Once all gems are in your inventory unlock the 13th zodiacs room and take the crown for unlimited power!.")
                   
        # set room 14 as the current room at the beginning of the game
        Game.currentRoom = r14

        # initialize the player's inventory
        Game.inventory = []

	
    # set up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)


    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do now is quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) +\
                "\nYou are carrying: " + str(Game.inventory) +\
                "\n\n" + status)
            Game.text.config(state=DISABLED)
 

    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")
        #SWITCHES 23-North 18- east, 24-south, 25-west
        switches = [23, 18, 24, 25]

    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye"\
            or action == "sionara!"):
            exit(0)

        # if the player is dead if goes/went south from room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

         #looks for the sigulkar word go as an input.
        if(words[0] == "go" and len(words) == 1): #looks for the word go and if the lenght is 1
            
            
            def wait_for_push():#waits for an input
                while(True):
                    for pin in range(len(switches)):
                        if GPIO.input(pins[pin]):
                            return pin
                    sleep(0.01)

            def wait_for_pull(pin):
                while(GPIO.input(pins[pin])):
                    sleep(.01)
            pins = {0:23, 1:18, 2:24, 3:25}
            switches = {23: "north" , 18: "east" , 24: "south" , 25: "west" }

            GPIO.setmode(GPIO.BCM)
            GPIO.setup(switches.keys(), GPIO.IN, GPIO.PUD_DOWN)
        #main section of the GPIO code
            try:
                while(True):
                    pressed = False
                    while(not pressed):
                        pin = wait_for_push()
                        wait_for_pull(pin)
                        pressed = True
                    #when pressed is true it looks to see if the pin is mapped to the direction
                    #if the direction is a valid exit it changes the room
                    if pressed == True:
                        if (switches[switches.keys()[pin]] == "south" and Game.currentRoom.name == "Capricorn Room" ):
                            if ("aquarius-gem" and "pisces-gem" and "aries-gem" and "taurus-gem" and "gemini-gem" and "cancer-gem" and "leo-gem" and "virgo-gem" and "libra-gem" and "scorpio-gem" and "sagittarius-gem" and "capricorn-gem" in Game.inventory): # checks to see if key is in inventory
                                Game.currentRoom = Game.currentRoom.exits["south"]
                                response = "You have entered the room of Ophiuchus go take the crown and make all your dreams come true!" #if true
                            else:
                                response = "The door is locked"
                        elif (switches[switches.keys()[pin]] in Game.currentRoom.exits.keys()):
                            Game.currentRoom = Game.currentRoom.exits[switches[pins[pin]]]
                            response = "Room Changed"

                    break
            except KeyboardInterrupt: #will run if there is an ecption in the try block
                GPIO.cleanup()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]
                   
            
            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."

                # check for valid exits in the current room
                if (noun in Game.currentRoom.exits):
                    if (noun == "south" and Game.currentRoom.name == "Capricorn Room" ):
                        if ("aquarius-gem" and "pisces-gem" and "aries-gem" and "taurus-gem" and "gemini-gem" and "cancer-gem" and "leo-gem" and "virgo-gem" and "libra-gem" and "scorpio-gem" and "sagittarius-gem" and "capricorn-gem" in Game.inventory): # checks to see if key is in inventory
                            Game.currentRoom = Game.currentRoom.exits["south"]
                            response = "You have entered the room of Ophiuchus go take the crown and make all your dreams come true!" #if true
                        else:
                            response = "The door is locked"
                    # if one is found, change the current room to
                    # the one that is associated with the specified exit
                    else:
                        Game.currentRoom =\
                             Game.currentRoom.exits[noun]
                        # set the response (success)
                        response = "Room changed."
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."

                # check for valid items in the current room
                if (noun in Game.currentRoom.items):
                    # if one is found, set the response to the item's description
                    response = Game.currentRoom.items[noun]
            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."

                # check for valid grabbable items in the current room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable items
                        break
        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)


################MAIN PART########################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600
# create the window
window = Tk()
window.title("Room Adventure")
# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()

