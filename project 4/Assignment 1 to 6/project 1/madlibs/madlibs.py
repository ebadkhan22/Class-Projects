import random

def story1():
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb_past = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter one more noun: ")
    verb = input("Enter a verb: ")
    adjective3 = input("Enter one last adjective: ")

    return f"""
    Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
    It {verb_past} {adverb} through the large tunnel that led to its {adjective2} {noun2}.
    I got some peanuts and passed them through the cage to a gigantic {noun3} towering above my head.
    Feeding that animal made me hungry. I went to get a {verb} scoop of ice cream.
    It filled my stomach. Afterwards I had to run to catch our {adjective3} bus home.
    It was such a fun day at the zoo!
    """

def story2():
    person = input("Enter a person's name: ")
    place = input("Enter a place: ")
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    food = input("Enter a type of food: ")
    verb = input("Enter a verb: ")
    adjective2 = input("Enter another adjective: ")

    return f"""
    Once upon a time, {person} went on a trip to {place}. They packed a {noun1} in their bag
    and wore a {adjective1} hat. Along the way, they found a restaurant that served only {food}.
    They decided to {verb} all day and ended the trip feeling very {adjective2}.
    The end.
    """

def story3():
    animal = input("Enter an animal: ")
    verb1 = input("Enter a verb ending in -ing: ")
    color = input("Enter a color: ")
    noun1 = input("Enter a noun: ")
    silly_word = input("Enter a silly word: ")
    verb2 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")

    return f"""
    One day, a {animal} was {verb1} through the {color} forest.
    It stumbled upon a {noun1} that said "{silly_word}!".
    Shocked, the animal decided to {verb2} and hide behind a {noun2}.
    What a weird day!
    """

def madlibs():
    print("🎉 Welcome to Mad Libs! Let's create a silly story.\n")

    stories = [story1, story2, story3]
    selected_story = random.choice(stories)

    result = selected_story()
    print("\nHere is your Mad Libs story:\n")
    print(result)

# Run the Mad Libs game
madlibs()
