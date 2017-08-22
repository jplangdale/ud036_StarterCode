import media
import fresh_tomatoes

# Joseph Langdale FSND 8-20-2017
# this code is used in conjuction with media.py and fresh_tomatoes.py
# to build a HTML page
# media.py contains class movie
# fresh_tomatoes.py builds the html page
# highlighting my favorite movies of 2017
# Version 2


# Build Movie Objects

dunkirk = media.Movie("Dunkirk",
                      "The strugle of the British Army to return home from"
                      " France early in World War 2.",
                      "Christopher Nolan",
                      "2017",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

baby_driver = media.Movie("Baby Driver",
                          "A young get-away driver gets in over his head.",
                          "Edgar Wright",
                          "2017",
                          "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=z2z857RSfhk")

spider_man_homecoming = media.Movie("Spider-Man:Homecoming",
                                    "Peter Parker returns to New York after"
                                    "his Avenger outing.",
                                    "Jon Watts",
                                    "2017",
                                    "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",  # NOQA
                                    # NOQA
                                    "https://www.youtube.com/watch?v=8wNgphPi5VM")  # NOQA

guardians = media.Movie("Guardians of the Galaxy Vol. 2",
                        "The Galaxy needs savigng again.",
                        "James Gunn",
                        "2017",
                        "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=duGqrYw4usE")

wonder_woman = media.Movie("Wonder Woman                ",
                           "In a time of war a hero leaves her home to save"
                           "the world.",
                           "Patty Jenkins",
                           "2017",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

colossal = media.Movie("Colossal",
                       "An unemployed writer returns to her hometown to sort"
                       "things out",
                       "Nacho Vigalondo",
                       "2017",
                       "https://upload.wikimedia.org/wikipedia/en/3/33/Colossal_%28film%29.png",  # NOQA
                       "https://www.youtube.com/watch?v=Q8hpm_BcHKE"
                       )

kong = media.Movie("Kong:Skull Island",
                   "Researchers are escorted to a seculded island in the"
                   "Pacific",
                   "Jordan Vogt-Roberts",
                   "2017",
                   "https://upload.wikimedia.org/wikipedia/en/3/34/Kong_Skull_Island_poster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=44LdLqgOpjo")

wick = media.Movie("John Wick: Chapter 2",
                   "An assassin becomes the hunted",
                   "Chad Stahelski",
                   "2017",
                   "https://upload.wikimedia.org/wikipedia/en/3/31/John_Wick_Chapter_Two.png",  # NOQA
                   "https://www.youtube.com/watch?v=ChpLV9AMqm4")

logan = media.Movie("Logan",
                    "The Wolverines journey continues.",
                    "James Mangold",
                    "2017",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

# Assemble list of movie objects
movies = [
    baby_driver, wonder_woman,
    logan, wick,
    dunkirk, colossal,
    kong, spider_man_homecoming,
    guardians]

# call function from fresh_tomatoes to build web page
fresh_tomatoes.open_movies_page(movies)
