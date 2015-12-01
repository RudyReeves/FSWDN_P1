import fresh_tomatoes
import media

# Create a Movie instance for toy_story, from the media module
toy_story = media.Movie("Toy Story", 1995,
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Create another Movie instance for the_matrix
the_matrix = media.Movie("The Matrix", 1999,
            "Neo discovers he is living in a computer simulation",
            "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
            "https://www.youtube.com/watch?v=vKQi3bBA1y8")

# Create a list of all our movies
movies = [toy_story, the_matrix]

# Display them in a browser window (in a page generated from fresh_tomatoes)
fresh_tomatoes.open_movies_page(movies)