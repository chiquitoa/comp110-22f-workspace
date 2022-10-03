"""A froggy cyoa game."""

__author__ = "730295419"

import random

points: int = 0
player: str = ""
frog: str = ""
brook_visit: bool = False
pool_visit: bool = False
mantis_visit: bool = False
trail_visit: bool = False
FROG_EMOJI: str = "\U0001F438"

def greet() -> None:
    """A procedure to start the game and gather the users player name."""
    global player
    froggy_names: list = ["Busta Slimes", "Snoop-frog", "Jim Hopper", "Hypnotoad", "Dwight Eisenhopper", "Gorf", "Croakley", "Optimus Slime", "Gwen Stefroggy", "Pickle", "Legs", "Lord Kroak", "Hoppy", "Gweneth Paltoad", "MC Hopper", "Rosie the Ribbitor", "Anthony Hopkins", "Lillypad Von Ribbit IV"]
    froggy_frogs: list = ["a Yellow-banded Poison Frog", "a Wood Frog", "a Green Frog", "a Madagascar Tomato Frog", "an American Bullfrog", "a Blessed Poison Frog", "a Red-Eyed Tree Frog", "a Desert Rain Frog", "a Cope's Gray Tree Frog", "a Cranwell's Horned Frog"]
    input("Oh no! It seems you've been transformed into a frog while you slept! (or is it really 'Hell yeah?') (Press Enter)")
    input("When you awake, you'll be well rested and cozy under a rock in a forest glade. (Press Enter)")
    input("Anyway, I'll give you a minute or two to come to terms with your new life. (Press Enter)")
    player = input("Okay, cool, let's get to business. First, you'll pick your new, froggy name. If you're not feeling creative, just press Enter, and you'll be given a new name! Otherwise, type your new name here, then press Enter: ")
    while player == " ":
        player = input("Dawg, I thought we were past this. You're a frog now, you gotta pick a froggy name! : ")
    if player == "":
        player = random.choice(froggy_names)
    frog = random.choice(froggy_frogs)
    input(f"Congratulations! Your new name is {player}, and you're {frog} {FROG_EMOJI}! You make a very good frog. (Press Enter)")
    input("After your transformation, you'll be repeating the same froggy day over and over. You get one point every day, and can earn more points by doing froggy things. Once you reach 50 points, you'll become human again. Do your best! (Press Enter)")

def brook() -> None:
    """The event for going to the brook."""
    global points
    reaction: int = 0
    jokes: list = ["What do you call a small pole that can swim? A TADPOLE!!", "Did you guys know that every frog used to have at least some polish genes? In fact, they were a TAD-POLE!", "What does a baby frog and a half-polish person have in common? They're both a TAD-POLE!", "What's a frogs favorite fastener? A RIVET!", "What happens when a frogs car dies? They need a jump! If that doesn't work, they'll need to have it toad.", "Why did the frog complain to the manager of the restaurant? Because there wasn't a fly in his soup!", "Why are frogs always so happy? The eat whatever bugs them!"]
    input("You hip hop over to the brook nearby, slide in to a shallow part, and take a sip from the cool water. (Press Enter)")
    if brook_visit is False:
        input("To your surprise, a little group of tadpoles wiggles up! They're marveling at your legs; and they're clearly jealous. (Press Enter)")
    else:
        input("The familiar group of tadpoles wiggles up and begins marveling at your legs; they seem quite jealous. (Press Enter)")
    input("To diffuse the situation, you decide to tell them a joke . . . . (Press Enter)")
    input(f"You say '{random.choice(jokes)}'")
    reaction = random.randint(4, 15)
    points += reaction
    if reaction < 8:
        input(f"The tadpoles seem unimpressed. They swim away to munch on some algae on the other side of the brook. You got {reaction} points, though! (Press Enter)")
    elif reaction < 12:
        input(f"The tadpoles are entertained and seem to forget their envy of your legs! After a hearty chuckle, they jaunt across the brook to a patch of algae and start munching away. You got {reaction} points! (Press Enter)")
    else:
        input(f"The tadpoles are absolutely dying of laughter. After wriggling about in joy for a bit, they seem to recover and have totally forgotten their envy of your legs! They happily wiggle to a patch of algae and start munching away. You got {reaction} points! (Press Enter)")
    input("You watch the tadpoles snacking, and you feel strangely protective of the little things. Maybe it's your froggy parental instinct. After a bit though, you move off to explore the glade for the rest of the day . . . . . . (Press Enter)")
    input("It's starting to get dark! You better beat it to your rock before some hungry creature comes along! (Press Enter)")
    input("Nice, you're safe and sound. The centipede seems to have gone to sleep already. You join him in slumber . . . . . . (Press Enter)")

def pool() -> int:
    snacky_choice: str = ""
    mayflies: int = 0
    if pool_visit is False:
        input("You hippity hop over to the pool at the edge of your glade. There's a flock of mayflies flitting about near the surface of the water, and a couple frogs watching them from the bank of the pool. (Press Enter)")
    else:
        input("You hippity hop over to the pool at the edge of your glade. You see the flock of mayflies flitting about and the small group of frogs watching them.")
    snacky_choice = input("You're feeling pretty snacky, waking up as a frog is hard work. Try to catch some mayflies? (y/n) : ")
    while snacky_choice != "y" and snacky_choice != "n":
        snacky_choice = input(f"Come on, {player}, you have to pick one! Try again (y/n) : ")
    if snacky_choice == "y":
        mayflies = random.randint(7, 15)
        input(f"You leap into the water, catching an unfortunate mayfly along your arc into the water. You proceed to repeatedly leap out of the water to catch the mayflies buzzing about overhead! You caught a whopping {mayflies} mayflies! (Press Enter)")
        input("Now that you've had your fill, you turn back and head into the glade again. You explore for a while . . . . . (Press Enter)")
    if snacky_choice == "n":
        input("You're hungry, but not mayfly hungry. You turn back and head into the glade again, passively hoping to happen upon a cheese (or veggie) burger, but you don't actually expect to find one. . . . . . (Press Enter)")
    input("It's starting to get dark! You better beat it to your rock before some hungry creature comes along! (Press Enter)")
    input("Nice, you're safe and sound. The centipede seems to have gone to sleep already. You join him in slumber . . . . . . (Press Enter)")
    return (mayflies)

def mantis(points: int) -> int:
    choice: str = ""
    if mantis_visit is False:
        input("As the praying mantis strides into the forest like a carpet carrier, you hop your fastest hops to catch up. He hears you approaching, turns around, and lets loose a loud, angry, mantis hiss: 'What the FUCK do you want!? I'll kick your ass!!' (Press Enter)")
        input("Oh shit. This particular mantis seems to be on a roid rage. Do you . . . (Press Enter)")
    else:
        input("You approach the roid raging mantis. He turns around and, predictably, hisses: 'What the FUCK do you want!? I'll kick your ass!!' (Press Enter)")
        print("Do you . . .")
    print("1) Turn back and RUN")
    print("2) Try to talk him down")
    print("3) Perform a pre-emptive strike")
    choice = input("Your action: ")
    while choice != "1" and choice != "2" and choice != "3":
        choice = input(f"Come on, {player}, you have to do something! He's going to rip your head off! : ")
    if choice == "1":
        input("You do your biggest hops back the way you came. Thankfully the mantis doesn't follow. You spend the rest of the day enjoying the dappled sunlight in the glade and trying to get your heart rate down. 5 points for bravery! . . . . . (Press Enter)")
        points += 5
    if choice == "2":
        if points < 30:
            input("You ribbit at him, but he doesn't seem to get it. He stalks over to you and seems to tower high above your head. You gulp. (Press Enter)")
            input("The mantis let's out a loud hiss and boxes you with his fist, sending you flying into a nearby pile of leaves and twigs. Once you manage to extricate yourself, the mantis is nowhere to be seen. (Press Enter)")
            input("You take a series of dejected hops back to the glade where you sulk for the day in a sunbeam. (You need at least 30 points for this option!) Here are 5 points to make you feel better . . . . . (Press Enter)")
            points += 5
        else:
            input("You ribbit at him, and you instantly see his mean, mantis face soften. He stalks over to you and seems to tower above your head. You gulp. (Press Enter)")
            input("He reaches out a claw, but just pats you gently on the noggin. He lets out a sympathetic hiss: 'I know it's rough out there as a frog. I think I saw some mayflies you could snack on in a pool over that way. Good luck.' (Press Enter)")
            input("In your terrified state, you can only muster a nod. The mantis turns around and heads into the depths of the forest. (Press Enter)")
            input("You head back to your glade, pondering what kind of a life that mantis must have had. 20 points for your impressive diplomacy! You spend the rest of the day philosophising . . . . . (Press Enter)")
            points += 20
    if choice == "3":
        if points < 30:
            input("Without hesitation, you leap straight at the mantis and you try to give him the biggest, strongest chomp you can muster! (Press Enter)")
            input("The mantis hisses and, lightning fast, wallops you with a claw, sending you hurtling into a nearby pile of leaves and twigs. Once you manage to extricate yourself, the mantis is nowhere to be seen. (Press Enter)")
            input("You take a series of dejected hops back to the glade where you sulk for the day in a sunbeam. (You need at least 30 points for this option!) Here are 5 points for your bravery . . . . . (Press Enter)")
            points += 5
        else:
            input("Without hesitation, you leap straight at the mantis and you try to give him the biggest, strongest chomp you can muster! (Press Enter)")
            input("The mantis tries to give you a good whack with a claw, but you're too quick. Your chomp hits home on his abdomen, and he lets out a pained shriek: 'Let go of me you blackbelt motherfucker!' (Press Enter)")
            input("The merciful soul you are, you let go. The mantis grumbles: 'I'll get you one of these days...' and limps into the forest. (Press Enter)")
            input("Proud of yourself, you let out a bellowing croak. Here are 20 points for your froggy martial arts skills! You happily hop back into the glade where you spend the day replaying the events of the encounter . . . . . (Press Enter)")
            points += 20
    input("It's starting to get dark! You better beat it to your rock before some hungry creature comes along! (Press Enter)")
    input("Nice, you're safe and sound. The centipede seems to have gone to sleep already. You join him in slumber . . . . . . (Press Enter)")
    return (points)

def trail(points: int) -> int:
    choice: str = ""
    are_you_sure: str = ""
    if trail_visit is False:
        input("You hop hop hop over to where the dark, mysterious trail enters the forest. You feel a strange sense of forboding about it. (Press Enter)")
        input("Some cosmic force causes you to realize that if you take the path into the forest, there is no going back. You'll never be human again, and the days will no longer repeat themselves; you'll be on your own. (Press Enter)")
    else:
        input("You hop hop hop back to the trailhead and peer into the darkness, pondering what it might be like to be a frog forever. (Press Enter)")
    print("You can:")
    print("1) Hippity hop down the trail")
    print("2) Turn around and go back to the glade")
    choice = input("What do you do? : ")
    while choice != "1" and choice != "2":
        choice = input(f"{player}, you can't just vibe at the trailhead all day, you gotta do something! : ")
    if choice == "1":
        if points < 30:
            input("You try to hop down the trail, but you feel increasing resistance. Eventually, it's impossible for you to continue. You realize you need at least 30 points to take the path. (Press Enter)")
            input("You turn around and hop back into the glade where you hang out for the day. 5 points for your curiosity! You spend the day wondering what life might have been like had you been able to take the trail . . . . . (Press Enter)")
            points += 5
        else:
            are_you_sure = input(f"{player}, are you 100% sure you want to do this? You do know frogs don't live that long, right? (y/n) : ")
            while are_you_sure != "y" and are_you_sure != "n":
                are_you_sure = input(f"{player}, you have to choose something! : ")
            if are_you_sure == "y":
                input("You hip hop down the trail in pursuit of your new, permanent life as a frog. Good luck, eat lots of bugs, and don't get eaten! (Press Enter)")
                points += 100
            else:
                input("You turn around and hop back into the glade where you hang out for the day 5 points for your curiosity! You spend the day wondering what life might have been like had you taken the trail . . . . . (Press Enter)")
                points += 5
    else:
        input("You turn around and hop back into the glade where you hang out for the day. 5 points for your curiosity! You spend the day wondering what life might have been like had you taken the trail . . . . . (Press Enter)")
        points += 5
    return (points)

def main() -> None:
    global points
    global brook_visit
    global pool_visit
    global mantis_visit
    global trail_visit
    day: int = 1
    choice: str = ""
    exit: str = ""
    greet()
    while points < 50:
        if day == 1:
            input("You awake in a comfortable hollow area underneath a rock. A centipede on your ceiling waves it's antennae at you cheerily; maybe it's saying good morning? (Press Enter)")
            input(f"The centipede squeaks at you: 'You have {points} points!' . . . You ribbit an acknowledgement. The centipede nods and scuttles off, presumably on centipede business. (Press Enter)")
            input("After you groggily blink a few times, you wriggle out from under the rock into an early morning sunbeam shining through green leaves. You are in a small clearing in a lush forest. You peer around and see . . . (Press Enter)")
            print("1) A gurgling brook merrily making it's way past your rock and through your glade.")
            print("2) A small pool in the brook at the far edge of the glade.")
            print("3) A rather intimidating praying mantis stalking away from the glade and into the forest.")
            print("4) A mysterious, shadowy trail leading into the forest.")
            print("5) A hole with a sign carefully made out of twigs that says 'exite.' You suspect that it's supposed to say 'exit'")
        else:
            input(f"You awake again under your cozy rock on day {day}. The centipede does his now familiar wave and squeaks: 'You have {points} points!' then scuttles off on centipede business. (Press Enter)")
            input(f"You head outside once more, and are presented with a familiar sight: (Press Enter)")
            print("1) The gurgling brook, still merrily making it's way past your rock and through your glade.")
            print("2) The small pool in the brook at the far edge of the glade.")
            print("3) The intimidating praying mantis stalking away from the glade and into the forest.")
            print("4) The mysterious trail leading into the forest.")
            print("5) The hole marked 'exite'")
        choice = input("Where do you want to go? Type 1, 2, 3, 4, or 5 : ")
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            choice = input(f"{player}, you have to choose somewhere to go, come on. : ")
        if choice == "1":
            brook()
            brook_visit = True
        elif choice == "2":
            points += pool()
            pool_visit = True
        elif choice == "3":
            points = mantis(points)
            mantis_visit = True
        elif choice == "4":
            points = trail(points)
            trail_visit = True
            if points >= 100:
                exit()
        elif choice == "5":
            exit = input("You hoppity hop over to the hole. As you gaze into the abyss, you realize that if you hop in there, you'll become human again. But you won't be a good frog, and that might weigh on your conscience. Are you sure you want to quit? (y/n) : ")
            while exit != "y" and exit != "n":
                exit = input(f"{player}, you have to decide one way or the other! No judgement... or maybe just a little, we made a good froggy life for you!")
            if exit == "y":
                print("Okay, fine, we see how it is! This was part of a great cosmic experiment that, frankly, is beyond your understanding. When you next awake, you'll be human and cozy in your bed, and no time will have passed. Also you'll have no memory of your life as a frog, but you didn't want to be a frog anyway so I don't expect you'll miss it. We've put you on the cosmic experience blacklist though, so don't expect any more fun surprises!")
                quit()
            if exit == "n":
                input("An excellent choice! You turn back and hop about the glade until you find the perfect spot for a little sunbathing. You hang out there sunbathing for the rest of the day . . .")
                input("It's starting to get dark! You better beat it to your rock before some hungry creature comes along! (Press Enter)")
                input("Nice, you're safe and sound. The centipede seems to have gone to sleep already. You join him in slumber . . . . . . (Press Enter)")
        day += 1
        points += 1
    input(f"{player}, you did it! You were the best frog, you scored a whopping {points} points, and it only took you {day} days! This was part of a great cosmic experiment that, frankly, is beyond your understanding. When you next awake, you'll be human and cozy in your bed, and no time will have passed! Also you'll have no memory of your life as a frog, sorry to say. We'll know you were a great frog, though. The best frog. (Press Enter)")

if __name__ == "__main__":
    main()