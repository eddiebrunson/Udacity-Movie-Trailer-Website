import webbrowser
#Movie class
class Movie():
    #def__init is a constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating):
        #These are the instances variables 
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating

    
