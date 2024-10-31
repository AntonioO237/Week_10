# Create a list of famous horror movie characters
horror_characters = {"Freddy Krueger", "Jason Voorhees", "Michael Myers", "Pennywise", "Chucky"}
# Iterate though the list and print each character 

for x in horror_characters:
    if x == "Michael Myers":
        x = "Dracula"
    if x == "Pennywise":
        x = "Human Centipede"
    print(x)