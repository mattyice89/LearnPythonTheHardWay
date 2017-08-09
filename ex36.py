from sys import exit

def start():
    print("You wake up in a cold, wet dungeon with both hands shackled to the wall.")
    print("What do you do?")

    choice_start = input("> ")
    if "key" in choice_start:
        print("Oh shit, you totally have a key.  You use it to pick the lock.")
        start_unshackled()
    elif "examine lock" in choice_start:
        print("You examine the lock, it's pretty badly rusted and looks like it could be broken.")
        start()
    else:
        print("That didn't work...")
        start()

def start_unshackled():
    print("You free yourself from your shackles and look around the room.")
    print("There are two exits, one to the East and one to the West.")
    print("Which way do you go?")

    choice_start_unshackled = input("> ")
    if choice_start_unshackled == "west":
        print("You head West.")
        Goblin_Room()
    else:
        print("You head East.")
        Monkey_Room()

def Goblin_Room():
    print("You enter a room with a creepy green goblin crouched in the corner.")
    print("\"Well hello there!\" I've been waiting alone down here for quite a while... it gets so lonely.")
    print("Will you play a game with me? (yes/no)")

    choice_Goblin_Room = input("> ")
    if choice_Goblin_Room == "yes" or "Yes":
        print("Really? Great!")
        print("Solve this riddle - What is so delicate that even saying its name will break it?")

        answer_Goblin_Game = input("> ")
        if answer_Goblin_Game == "silence" or "Silence":
            print("The goblin shouts: \"That's right! Well done!\"")
            print("\"You may continue on with your journey.\" He continues.")
            print("The room has two exits, one to the north, and one to the west.")
            print("Which way do you go?")

            choice2_Goblin_Room = input("> ")
            if choice2_Goblin_Room == "west":
                print("You move to the west.")
                Dragon_Room()
            else:
                print("You head north.")
                Finger_Game()
        else:
            print("The goblin looks disappointed. \"Sorry, that's not quite right.\n I guess you're not smart enough to escape this place.\"")
            print("The goblin takes out a small rusty knife and stabs you in the spleen.  You are dead.")
            exit()

def Dragon_Room():
    print("You enter a huge room.")
    print("After a few steps you look down to see a sea of gold.")
    print("\"I'm rich!\" You say to yourself.")
    print("However, after a few seconds, you hear a rumbling, and you realize a massive dragon was sleeping on top of the pile of gold.")
    print("The dragon wakes up. \"Uh oh, he looks pissed...\" You say to yourself.")
    print("\"What do you think you're doing, coming in here and waking me up?\"")
    print("You better think of a good response if you want to get out of here alive.")

    # it doesn't matter what they put on this line, you're going to have to solve his riddle
    meaningless_choice = input("> ")
    print("\"Alright, I guess if I'm awake, we may as well play a game.\" He bellows.")
    print("\"Solve this riddle:")
    print("Johnny's mother has three children.  The first was named Peter, the second Annabelle.")
    print("\"What was the name of the third child?\"")

    Answer_Dragon_Game = input("> ")
    if Answer_Dragon_Game == "Johnny" or "johnny":
        print("\"That's right. I guess humans CAN listen.\"")
        print("\"Feel free to move along\"")
        Win()
    else:
        print("\"You clearly don't pay attention. I'm getting hungry, I could use a snack.\"")
        print("The dragon eats you. You are dead. You should probably just give up now.")
        exit()

def Win():
    print("You continue along into the next room.  As you turn the corner, you catch a glimpse of light.")
    print("It's daylight! Congratulations, you've made your way out of the dungeon!")
    exit()

def Finger_Game():
    print("You make your way into the next room and find a bored-looking guard eating a candy bar and muttering to himself.")
    print("\"Abba Zabba, you my only friend...\"")
    print("\"... Oh hey man, I didn't see you there.")
    print("It's so boring down here, I've been pulling an all nighter by myself with nothing to do. They don't even let me watch Netflix!")
    print("I know, let's play a game. If you can guess how many fingers I'm holding up behind my back, I'll let you pass.")
    print("Get it wrong though, and I'll throw you back in your cell.")
    print("What's your guess?\"")

    guess_finger_game = int(input("> "))
    if guess_finger_game >= 5:
        print(f"That's right! {guess_finger_game} is right!")
        print("Off you go!")
        Win()
    else:
        print("Nope! Back you go!")
        start()

def Monkey_Room():
    print("You enter a very small room with a monkey in the middle (ha!)")
    print("What do you do?")

    choice_Monkey_Room = input("> ")
    if "kill" in choice_Monkey_Room:
        print("You reach out and strangle the poor monkey with your bare hands.")
        print("What the hell is wrong with you? That monkey probably had a monkey family.")
        print("Want to try that one again, you sick son of a bitch?")
        Monkey_Room()
    else:
        print("Yeah, you should probably just talk to the monkey.")
        print("This is, after all, a video game, so I'm sure he can talk.")
        print("You approach the monkey...")
        print("\"Oh hello! My name is Guybrush Threepwood.\n I used to be a might pirate, \nbut I was cursed by an evil pirate named LeChuck and turned into a monkey.")
        print("Will you help me?\"")

        # Why isn't this working?
        choice2_Monkey_Room = input("> ")
        if "No" or "no" in choice2_Monkey_Room:
            print("\"Cool, thanks man.\"")
            print("You now have an ex-pirate, talking monkey in your party... I'm sure that will somehow come in handy.")
            Monkey_Choice()
        else:
            print("\"Fuck you man! Monkeys, attack!\"")
            print("A troop (yes, a troop is the right word for a group of monkeys) descends on you, reigning down purple nurples and crotch shots.")
            print("They don't stop until your junk has been turned to dust.")
            print("You lose the will to live.  You kill yourself.")
            exit()

def Monkey_Choice():
            print("There are two exits to this room.  One to the east, and the other to the north.")
            print("Which way do you want to go?")

            #Why Doesn't this work if i type east?
            choice3_Monkey_Room = input("> ")
            if choice3_Monkey_Room == "north" or "North":
                print("You continue north")
                Shaky_Bridge_Room()
            elif "ask" in choice3_Monkey_Room:
                print("You ask Guybrush which way to go")
                print("\"Definitely don't go East, there's nothing but darkness and pain that way.\"")
            else:
                print("You continue east...")
                Hole_Room()

def Hole_Room():
    print("You enter the next room and fall into a deep hole.")
    print("You fall several hundred feet before going splat on the floor.")
    print("You are dead.")
    exit()

def Shaky_Bridge_Room():
    print("You enter a huge room with a long, rickety looking rope bridge.")
    print("What do you do?")

    choice_Shaky_Bridge_Room = input("> ")
    if choice_Shaky_Bridge_Room == "cross the bridge" or "Cross the bridge":
        print("You cross the bridge and enter the next room")
        Win()
    else:
        print("Yeah... you should probably just cross the bridge.")
        Shaky_Bridge_Room()

start()
