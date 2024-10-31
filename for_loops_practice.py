# Create a list of famous horror movie characters
horror_characters = {"Freddy Krueger", "Jason Voorhees", "Michael Myers", "Pennywise", "Chucky"}
# Iterate though the list and print each character 

for x in horror_characters:
    if x == "Michael Myers":
        x = "Dracula"
    if x == "Pennywise":
        x = "Human Centipede"
    print(x)

    
horror_movies = {"Child's Play 2", "The Shining", "The Fly", "A Nightmare on Elm Street", "Halloween", "Scream"}

for x in horror_movies:
    if x == "Child's Play 2":
        continue
    if x == "The Fly":
        x = "Saw"
    print(x)