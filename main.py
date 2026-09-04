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

    with open("decklists.txt", "a") as decklistsFile:
        # By appending, the new decklist is written at the end of the text  file

        decklistsFile.write("\n\nName: " + name + "\n\n" + newDecklist)

# MAIN CODE

decklists = getDecklists()
count = 1 # Indicates the ordering of the decklists, incremented after each pass

for decklist in decklists:
    print("Decklist " + str(count) + ":\n")

    for section in decklist:
        print(section + "\n")

    count += 1

piperList = """Pokémon: 19
4 N's Zorua JTG 97
4 N's Zoroark ex JTG 98
2 N's Darumaka JTG 26
2 N's Darmanitan JTG 27
1 N's Zekrom ASC 155
1 N's Reshiram JTG 116
1 Budew ASC 16
1 Munkidori TWM 95
1 Yveltal MEG 88
1 Fezandipiti ex ASC 142
1 Pecharunt ex SFA 39

Trainer: 33
4 Lillie's Determination MEG 119
3 Boss's Orders MEG 114
3 Cyrano SSP 170
1 Black Belt's Training JTG 143
1 Janine's Secret Art PRE 112
4 Buddy-Buddy Poffin TEF 144
3 Poké Pad POR 81
3 N's PP Up JTG 153
2 Night Stretcher ASC 196
1 Ultra Ball MEG 131
1 Special Red Card CRI 82
1 Pokégear 3.0 SVI 186
1 Secret Box TWM 163
1 Binding Mochi PRE 95
1 Powerglass SFA 63
2 N's Castle JTG 152
1 Lumiose City POR 77

Energy: 8
8 Darkness Energy MEE 7"""

addDecklist(piperList, "Piper Lepine")