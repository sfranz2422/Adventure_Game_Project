from adventurelib import *

########################################
# DEFINE YOUR ROOMS
house = Room("""
This is your house.  You know what it looks like. 


""")

outside = Room("""

It is a pleasant November day. A little cool but sunny. 

""")

#####################################

# DECLARE YOUR CURRENT ROOM AND CONSTANTS
current_room = house
inventory = []

########################################
########################################
# OPENING TEXT
def opening_text():
  global current_room
  current_room = house
  print("""
  
  You get out of bed at 6:00am.  You need to get ready for school.
  
  Enter rooms of the house to visit such as "kitchen", "family room" etc or type "leave house" to go to school.
  
  You can view your inventory by typing 'bag'.
  
  You can view your current surroundings by typing 'look around'
  
  
  """)

opening_text()


@when('kitchen')
def kitchen_room():
  global current_room
  if current_room == house:
      
    say("""
    You are in the kitchen.  It looks like most kitchens.  There is a stove, a microwave, and a table with a toolset.

    You can 'leave house' or
    You can view your inventory by typing 'bag'.
  
  You can view your current surroundings by typing 'look around'
    """)
  else:
    say("There is no kitchen here. ")

@when('open toolset')
def open_tools():
  if 'toolset' in inventory:
    say("""
  
    You open the tool set, there is a screwdriver, pliers, a hammer and some nails.

    
    """)
  else:
    say("You don't have a toolset")

@when('look around')
def where():
  print(current_room)


def print_house():
  print(""" 
         `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
     `""`
  
  """)

@when("leave house")
def outside_of_house():
  print_house()
  global current_room
  current_room = outside
  print("You walk out the front door of your house.  The road is deserted. \n What do you want to do?  You can 'walk toward school' or 'go back into house'. ")

@when('house')
@when("go back into house")
def back_into_house():
  print("You walk back into the house and find it is exactly how you left it....or is something different? \n You can 'go back outside' or stay in the house")
  

@when("go back outside")
def back_outside():
  print("You walk out the front door again and notice someone sitting in front of you house.  You can 'approach the person' or 'call the police'")
  
@when("call the police")
def call_police():
  print("You call the police, they are busy and think you are a prank call.")

@when("approach the person")
def approach_person():
  global current_room
  if current_room == outside:
    print("You approach the person sitting in front of you house.  The person is looking at a comic book.")
  else:
    say("There is no person here.")


  
@when("scream")
def scream():
  print("You unleash a piercing shriek that reverberates around you.")
  

@when("eat lunch")
def brush_teeth():
    print("You eat a hamburger and five pieces of pizza.")


@when("brush teeth")
def brush_teeth():
    say("""
        You squirt a bit too much toothpaste onto your
        brush and dozily jiggle it round your mouth.

        Your teeth feel clean and shiny now, as you
        run your tongue over them.
    """)

@when("shout loudly")
@when("shout")
@when("yell")
def yell():
  print("You bellow at the top of your lungs.")

# take hat
@when("take THING")
def take(thing):
  global inventory
  inventory.append(thing)
  print(f"You take the {thing}.")

@when("bag")
def print_inventory():
  global inventory
  if len(inventory)==0:
    print("Your bag is empty")
  else:
    for i in inventory:
      print(i)
    

@when("give ITEM to RECIPIENT")
def give(item, recipient):
  if 'chair' in inventory:
    print(f"You give the {item} to the {recipient}.")
    inventory.remove(item)
  
start()