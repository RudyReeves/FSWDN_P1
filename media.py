import webbrowser

# Represents a movie with a title, release year, storyline, poster image, and trailer URL
class Movie():
    def __init__(self, movie_title,
                 release_year,
                 storyline,
                 poster_image_url,
                 trailer_youtube_url):
        self.title = movie_title
        self.release_year = release_year
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # Shows the trailer in a browser window
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)