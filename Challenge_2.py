Y = True
N = False

student = input("Are you a student? Please answer with either a 'Y' for Yes or an 'N' for No: ")
age = int(input("How old are you?: "))
reside = input("Do you reside in the local area? Please answer with either a 'Y' for Yes or an 'N' for No: ")

if student is True:
    if age > 18:
        print("Eligable for free student membership.")
    elif reside is True:
        print("Eligable for discounted student membership.")
    if age < 65: 
        print("Eligable for senior or resident membership.")
else:
    print("Standard membership rates apply.")
    
# By: Andrew Picasso, Antonio Olvera, Logan Lara                                                    
