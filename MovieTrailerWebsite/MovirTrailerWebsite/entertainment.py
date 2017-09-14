"""
-------------------------------------------------------
media.py
[program description]
-------------------------------------------------------
Author:  lingchi chen
Email:   jackchen4work@gmail.com
__updated__ = "2017-09-03"
-------------------------------------------------------
"""

import fresh_tomatoes
import media


# create movie instance
ryan = media.Movie("Saving Private Ryan",
                   "Saving soldier Ryan during WarII",
                   "https://upload.wikimedia.org/wikipedia/zh/a/ac/Saving_Private_Ryan_poster.jpg",
                   "https://www.youtube.com/watch?v=zwhP5b4tD6g")

schindler = media.Movie("Schindler's list",
                        "Oskar Schindler saved Jewish during War II",
                        "https://upload.wikimedia.org/wikipedia/zh/thumb/3/38/Schindler%27s_List_movie.jpg/220px-Schindler%27s_List_movie.jpg",
                        "https://www.youtube.com/watch?v=gG22XNhtnoY")

andy = media.Movie("The Shawshank Redemption",
                   "Andy Dufresne skip from the Shawshank prison ",
                   "https://upload.wikimedia.org/wikipedia/zh/f/fc/Shawshankost.jpg",
                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

box = media.Movie(" Love me if you dare",
                  "story about girl and boy and box",
                  "https://upload.wikimedia.org/wikipedia/zh/thumb/e/e7/Love_Me_If_You_Dare_movie.jpg/220px-Love_Me_If_You_Dare_movie.jpg",
                  "https://www.youtube.com/watch?v=sFcuv4NenZM")

amelie = media.Movie("Amelie",
                     "legend story about Amelie ",
                     "http://www.linternaute.com/cinema/image_cache/objdbfilm/image/540/71728.jpg",
                     "https://www.youtube.com/watch?v=B-uxeZaM-VM")

tiger = media.Movie("Crouching Tiger, Hidden Dragon",
                    "Chinese classical Kongfu Movie",
                    "http://a1.att.hudong.com/14/08/01300000329092124403084878881.jpg",
                    "https://www.youtube.com/watch?v=T5Be1WvLTYQ")

movie_list = [ryan, schindler, andy, box, amelie, tiger]
# open browser by calling  .open_movies_page
fresh_tomatoes.open_movies_page(movie_list)
# print the information about each movie
for i in movie_list:
    i.show_info()
    print("------------------------")
