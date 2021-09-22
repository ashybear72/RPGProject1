def begin():
	print("Hello there!")
	print("My names bot")
	print("I'm going to be your guide")
	print("For what?")
	print("Well the game of course")
	print("Now you can chose whatever you want to do, but your kind of someone else")
	print("So whatever you chose you want to make sure that person is happy with it")
	print("We've got a lot to do so let's get going")
	character()

def character():
	print("Finn")
	print("Jeni")
	print("Ben")
	lore()

def lore():
	sel = input("Chose your character: ").lower()

	if(sel == "finn"):
		print("This is Finn, he is a pretty happy person.")
		print("He lives with his bestfriend and helps people whenever he can")

begin()