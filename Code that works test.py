import easygui

# Defining what games are in what genres
fighter = ["street_fighter", "mortal_kombat", "super_smash_bros"]
fscores = [0, 0, 0]
platform_fighter = ["super_smash_bros"]
pfscores = [0]
puzzle = ["bejeweled", "portal"]
pscores = [0, 0]

#defining varibles
portal_score = 0
street_fighter_score = 0
bejeweled_score = 0
super_smash_bros_score = 0
mortal_kombat_score = 0


#asking if player likes a specific game
def question(game_score):
    if game == "Yes":
        game_score += 1
    return game_score

# Ask user if they want to play a certain genre
game = easygui.buttonbox("Do you want to play a fighter?", choices=["Yes", "No"])

if game == "Yes":
    for i in range(len(fscores)):
        fscores[i] += 1
    print(fscores)

game = easygui.buttonbox("Do you want to play a puzzle?", choices=["Yes", "No"])

if game == "Yes":
    for i in range(len(pscores)):
        pscores[i] += 1
    print(pscores)

game = easygui.buttonbox("Do you want to play a platform fighter?", choices=["Yes", "No"])

if game == "Yes":
    for i in range(len(pfscores)):
        pfscores[i] += 1
    print(pfscores)

# Ask user if they want to play Street Fighter
game = easygui.buttonbox("Do you want to play Street Fighter?", choices=["Yes", "No"])
street_fighter_score = question(street_fighter_score)
print(street_fighter_score)

# Ask user if they want to play Mortal Kombat
game = easygui.buttonbox("Do you want to play Mortal Kombat?", choices=["Yes", "No"])
mortal_kombat_score = question(mortal_kombat_score)
print(mortal_kombat_score)

# Ask user if they want to play Super Smash Bros
game = easygui.buttonbox("Do you want to play Super Smash Bros?", choices=["Yes", "No"])
super_smash_bros_score = question(super_smash_bros_score)
print(super_smash_bros_score)

# Ask user if they want to play Portal
game = easygui.buttonbox("Do you want to play Portal?", choices=["Yes", "No"])
portal_score = question(portal_score)
print(portal_score)

# Ask user if they want to play Bejeweled
game = easygui.buttonbox("Do you want to play Bejeweled?", choices=["Yes", "No"])
bejeweled_score = question(bejeweled_score)
print(bejeweled_score)

# Calculate scores (remember to devide the score by how many items are in its genrre)
portal_score += sum(pscores) / 2
bejeweled_score += sum(pscores) / 2
street_fighter_score += sum(fscores) / 3
super_smash_bros_score += sum(fscores) / 3 + sum(pfscores)
mortal_kombat_score += sum(fscores) / 3

print("'Street Fighter' score =" + str(street_fighter_score))
print("'Portal' score =" + str(portal_score))
print("'Bejewleed' score =" + str(bejeweled_score))
print("'Smash Bros' score =" + str(super_smash_bros_score))
print("'Mortal Kombat Score =" + str(mortal_kombat_score))

highest_score = max(street_fighter_score, portal_score, bejeweled_score, super_smash_bros_score, mortal_kombat_score)
if highest_score == street_fighter_score:
    easygui.msgbox("After calculating we believe  that Street Fighter would be the perfect game for you.")
if highest_score == portal_score:
    easygui.msgbox("After calculating we believe  that Portal would be the perfect game for you.")
if highest_score == bejeweled_score:
    easygui.msgbox("After calculating we believe  that Bejeweled would be the perfect game for you.")
if highest_score == super_smash_bros_score:
    easygui.msgbox("After calculating we believe  that Smash Bros would be the perfect game for you.")
if highest_score == mortal_kombat_score:
    easygui.msgbox("After calculating we believe  that Mortal Kombat would be the perfect game for you.")
