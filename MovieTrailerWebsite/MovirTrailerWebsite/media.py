"""
-------------------------------------------------------
entertainment_center.py
[program description]
-------------------------------------------------------
Author:  lingchi chen
Email:   jackchen4work@gmail.com
__updated__ = "2017-09-04"
-------------------------------------------------------
"""
import webbrowser


class Movie():
    """ A model of movies"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ initialize movie title,storyline,poster trailer for movie"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    """calling webbrowser to open trailer"""

    def show_trail(self):
        webbrowser.open(self.trailer)
    """print movie information"""

    def show_info(self):
        print("Movie title:    " + self.title)
        print("Story line:     " + self.storyline)
        print("Poster image:   " + self.poster_image_url)
        print("Trailer:        " + self.trailer_youtube_url)
