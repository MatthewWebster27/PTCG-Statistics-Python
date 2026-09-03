# FUNCTION DEFINITIONS

"""
The function 'getDecklists' reads a text file and produces a list of decklists (2D list),
where each list contains four elements:

- Name
- Pokémon
- Trainers
- Energy

"""

def getDecklists(filename):

    decklists = []
    currentDecklist = [] # Temporary store while appending sections to a decklist

    decklistsFile = open(filename, "r")

    """ 
    My terminal fails to render the 'é' character in 'Pokémon' correctly, so I used the 
    replace method to display it as intended.
    """

    for section in decklistsFile.read().replace("Ã©","é").split("\n\n"):
        currentDecklist.append(section)

        if len(currentDecklist) == 4: # All sections for this decklist have been added
            decklists.append(currentDecklist)
            currentDecklist = []

    decklistsFile.close()

    return decklists

# MAIN CODE

decklists = getDecklists("decklists.txt")
count = 1 # Indicates the ordering of the decklists, incremented after each pass

for decklist in decklists:
    print("Decklist " + str(count) + ":\n")

    for section in decklist:
        print(section + "\n")

    count += 1