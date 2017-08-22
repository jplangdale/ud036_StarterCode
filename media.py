import webbrowser


# Joseph Langdale FSND 8-20-2017
# Movie class structure file for favorite movie web page
# Version 2


class Movie():
    def __init__(self, movie_title, movie_storyline, director_name,
                 release_year, poster_image, trailer_youtube):
        """Builds movie object including Title, Story line, Director's Name ,
        Year of Release , Poster Image URL, Trailer from YouTube. """
        self.title = movie_title
        self.storyline = movie_storyline
        self.director = director_name
        self.year = release_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens the YouTube trailer for the Movie selected """
        webbrowser.open(self.trailer_youtube_url)
