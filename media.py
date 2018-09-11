class Movie():
    """
    A class for storing movie information

    title (str): Movie title
    year (str): Year movie was released
    story_line (str): Brief description of movie
    poster_image_url (str): Movie poster URL
    backdrop_image_url (str): Movie backdrop URL
    trailer_url (str): Movie trailer URL

    """

    def __init__(
        self,
        title,
        year,
        story_line,
        poster_image_url,
        backdrop_image_url,
        trailer_url
    ):

        self.title = title
        self.year = year
        self.storyline = story_line
        self.poster_image_url = poster_image_url
        self.backdrop_image_url = backdrop_image_url
        self.trailer_youtube_url = trailer_url
