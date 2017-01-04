import fresh_tomatoes
import media

#These are the instances of the movie class contains the 6 movie objects 
the_wizard_of_oz = media.Movie(
    "The Wizard of OZ",
    "The Wizard of Oz stars legendary Judy Garland as Dorothy,\
    an innocent farm girl whisked out of her mundane earthbound existence\
    into a land of pure imagination.",
    "https://upload.wikimedia.org/wikipedia/commons/c/ca/WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg",  
    "https://www.youtube.com/watch?v=H_3T4DGw10U",
    "G")

et = media.Movie(
    "E.T. The Extra-Terrestrial",
    "AE.T. is a sci-fi adventure that captures that strange moment in youth when the world is a\
    place of mysterious possibilities (some wonderful, some awful), and the universe seems somehow\
    separate from the one inhabited by grown-ups",
    "https://upload.wikimedia.org/wikipedia/en/6/66/E_t_the_extra_terrestrial_ver3.jpg",  
    "https://www.youtube.com/watch?v=qYAETtIIClk",
    "PG")

toy_story = media.Movie(
    "Toy Story",
    "Woody plots to get rid of Buzz, but things backfire and he finds himself lost in the outside\
     world with Buzz as his only companion. Joining forces to find their way home, the two rivals\
     set out on an adventure that lands them in the clutches of Sid, a sadistic neighborhood kid\
     who is notorious for dismembering and reassembling mutant toys in his bedroom.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  
    "https://www.youtube.com/watch?v=4KPTXpQehio",
    "G")

finding = media.Movie(
    "Finding Nemo",
    "Finding Nemo follows the comedic and momentous journey of an overly protective clownfish\
    named Marlin and his son Nemo -- who become separated in the Great Barrier Reef when Nemo\
    is unexpectedly taken far from his ocean home and dumped into a fish tank in a dentist's office.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",  
    "https://www.youtube.com/watch?v=f7yX-4Brzww",
    "G")

jungle = media.Movie(
    "The Jungle Book",
    "In this reimagining of the classic collection of stories by Rudyard Kipling, director Jon Favreau\
    uses visually stunning CGI to create the community of animals surrounding Mowgli (Neel Sethi), a\
    human boy adopted by a pack of wolves. ",
    "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",  
    "https://www.youtube.com/watch?v=5mkm22yO-bs",
    "PG")

moana = media.Movie(
    "Moana",
    "Aa sweeping, CG-animated feature film about an adventurous teenager who sails out on a daring\
    mission to save her people. During her journey, Moana meets the mighty demigod Maui, who\
    guides her in her quest to become a master wayfinder.",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
    "https://www.youtube.com/watch?v=M5dnZKrUpdA",
    "PG")

# This list all the movie instances in a array to be used as an argument in open_movies_page function
movies = [
    the_wizard_of_oz, et, toy_story, finding, jungle, moana]

# This calls the function open movies page and takes in the array of movies
fresh_tomatoes.open_movies_page(movies)
