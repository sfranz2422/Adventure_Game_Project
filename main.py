from adventurelib import *


# > go north
# I don't understand 'go north'.

# > help
# Here is a list of the commands you can give:
# ?
# help
# quit



# The @when decorator is written on the line above a function. The function will then be called when a player types a matching command.

# This code will be called when the player types “scream”:

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
  print(f"You take the {thing}.")


@when("give ITEM to RECIPIENT")
def give(item, recipient):
  print(f"You give the {item} to the {recipient}.")


# try cast fireball
@when('cast SPELL', context='wonderland')
def cast(spell):
  say(f"You cast the {spell} spell.")

@when('enter mirror')
def enter_mirror():
    if get_context() == 'wonderland':
        say('There is no mirror here.')
    else:
        set_context('wonderland')
        say('You step into the silvery surface, which feels wet and cool.')
        say('You realise that clicking your heels will let you return.')

  
# all code must go above
start()