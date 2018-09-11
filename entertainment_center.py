import media
import fresh_tomatoes


def main():

    # create movie object instance
    kung_fu_hustle = media.Movie(
        "Kung Fu Hustle",
        "2004",
        "A wannabe gangster aspires to join the notorious ""Axe Gang"".",
        "https://image.tmdb.org/t/p/original/dZsfDrNLGWgsIUQL1vGhl8tbnqY.jpg",
        "https://image.tmdb.org/t/p/original/qpJWj6MI6VLRt9bGbJVZtmFvqWw.jpg",
        "https://youtu.be/-m3IB7N_PRk")

    # create movie object instance
    shaolin_soccer = media.Movie(
        "Shaolin Soccer",
        "2001",
        "A young Shaolin follower forms a soccer team using thier martial art"
        " skills to their advantage.",
        "https://image.tmdb.org/t/p/original/uoF0fIGAq52kguYFC0Iu5aBv1Ov.jpg",
        "https://image.tmdb.org/t/p/original/3i8exn44yAuYLf5nmlc9mVH35g3.jpg",
        "https://youtu.be/bREfcVPssiE")

    # create movie object instance
    done_mess_with_the_zohan = media.Movie(
        "You Don't Mess with the Zohan",
        "2008",
        "An Israeli Special Forces Soldier fakes his death so he can re-emerge"
        " in New York City as a hair stylist.",
        "https://image.tmdb.org/t/p/original/3n9FYKLJVqwrZ7Wf96eoF2cAowU.jpg",
        "https://image.tmdb.org/t/p/original/zFYo77esGaoWu1wTYucbpz40Vcx.jpg",
        "https://youtu.be/ucmnTmYpGhI")

    # create movie object instance
    starship_troopers = media.Movie(
        "Starship Troopers",
        "1997",
        "Humans in a fascist, militaristic future wage war with giant alien"
        " bugs in a satire of modern world politics",
        "https://image.tmdb.org/t/p/original/t3K2a8jJK5KrIIs8gKyIEhremAA.jpg",
        "https://image.tmdb.org/t/p/original/bt53fKUwY6boUldm8XiFlQ4FQ9.jpg",
        "https://youtu.be/8INy93p2xGU")

    # create movie object instance
    army_of_darkness = media.Movie(
        "Army of Darkness",
        "1992",
        "A man is accidentally transported to 1300 A.D., where he must battle"
        " an army of the dead and retrieve the Necronomicon so he can return"
        " home.",
        "https://image.tmdb.org/t/p/original/2eZKDIwLNnySbwqQtAaUz0kYDIL.jpg",
        "https://image.tmdb.org/t/p/original/xErw1pfmyWYQcXIlXipPY3O9uRH.jpg",
        "https://youtu.be/gasZjgyMxeg")

    # create movie object instance
    Jumanji = media.Movie(
        "Jumanji: Welcome to the Jungle",
        "2017",
        "Four teenagers are sucked into a magical video game, and the only"
        " way they can escape is to work together to finish the game.",
        "https://image.tmdb.org/t/p/w440_and_h660_bestv2/bXrZ5iHBEjH7WMidbUDQ0U2xbmr.jpg",  # NOQA
        "https://image.tmdb.org/t/p/w700_and_h392_bestv2/cpz070zEKbPGXzCWuQsNt42PqXY.jpg",  # NOQA
        "https://youtu.be/2QKg5SZ_35I"
    )

    # movie list array
    my_movies = [
        kung_fu_hustle,
        shaolin_soccer,
        done_mess_with_the_zohan,
        starship_troopers,
        army_of_darkness,
        Jumanji
    ]

    # open a browser and render the movie list
    fresh_tomatoes.open_movies_page(my_movies)

if __name__ == '__main__':
    main()
