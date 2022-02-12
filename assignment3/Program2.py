genre = input("This program is intended to help you find some new music\nPlease answer all the following questions\nAre you interested in Rock, Jazz or Soul? ")

if genre.upper() == "ROCK":
    sub_genre = input("Are you interested in Ska, Punk or Metal? ")
    if sub_genre.upper() == "SKA":
        sub_sub_genre = input("Are you interested in Calypso, Reggae or Punk? ")
        if sub_sub_genre.upper() == "CALYPSO":
            pass
        elif sub_sub_genre.upper() == "REGGAE":
            print("You might try listening to The Specials")
        elif sub_sub_genre.upper() == "PUNK":
            pass
    elif sub_genre.upper() == "PUNK":
        sub_sub_genre = input("Are you interested in x, xx or xxx? ")
        if sub_sub_genre.upper() == "x":
            pass
        elif sub_sub_genre.upper() == "xx":
            pass
        elif sub_sub_genre.upper() == "xxx":
            pass
    elif sub_genre.upper() == "METAL":
        pass
        pass
        pass
elif genre.upper() == "JAZZ":
    pass
elif genre.upper() == "SOUL":
    pass
