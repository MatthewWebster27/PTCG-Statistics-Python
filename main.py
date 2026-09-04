# FUNCTION DEFINITIONS

"""
The function 'getDecklists' reads 'decklists.txt' and produces a list of decklists (2D list),
where each list contains four elements:

- Name
- Pokémon
- Trainers
- Energy

"""

def getDecklists():

    decklists = []
    currentDecklist = [] # Temporary store while appending sections to a decklist

    with open("decklists.txt", "r") as decklistsFile:

        """ 
        My terminal fails to render the 'é' character in 'Pokémon' correctly, so I used the 
        replace method to display it as intended.
        """

        for section in decklistsFile.read().replace("Ã©","é").split("\n\n"):
            currentDecklist.append(section)

            if len(currentDecklist) == 4: # All sections for this decklist have been added
                decklists.append(currentDecklist)
                currentDecklist = []

    return decklists

"""
The function 'addDecklist' takes a new decklist as a paramter (String) and its name (String),
appending it to the 'decklists.txt' text file.
"""

def addDecklist(newDecklist,name):

    # We can only add the decklist if its name is unique, because it acts as the 'primary key'

    if isNameUnique(name):
        with open("decklists.txt", "a") as decklistsFile:
            # By appending, the new decklist is written at the end of the text file
            decklistsFile.write("\n\nName: " + name + "\n\n" + newDecklist)

"""
The helper function 'isNameUnique' goes through every decklist and determines if the given 
name (String) exists already in the text file.
"""

def isNameUnique(name):

    decklists = getDecklists()

    for decklist in decklists:
        # We use string slicing to remove the "Name: " part of the data
        if decklist[0][6:] == name:
            return False

    return True

# MAIN CODE

# Commented the display of decklists so it can be re-used later

"""
decklists = getDecklists()
count = 1 # Indicates the ordering of the decklists, incremented after each pass

for decklist in decklists:
    print("Decklist " + str(count) + ":\n")

    for section in decklist:
        print(section + "\n")

    count += 1
"""

addDecklist("shouldBeIgnored","Piper Lepine")