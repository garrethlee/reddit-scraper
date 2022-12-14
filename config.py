MIN_ENTRIES_PER_QUERY = 150
QUERY_SIZE = 25
DAYS_PER_INTERVAL = 7
COVID_START_DATE = "2020-03-14"

DATA_DIR = "./data"
BASE_URL = "https://api.pushshift.io"

# MODIFY THIS TO CHANGE THE KEYWORDS TO SCRAPE
KEYWORDS = [
    "quit work", "quit my job", 
    "resign", "resign my job", "resignation"
    "laid off", "layoff", 
    "fired"
]

# MODIFY THIS TO ADD / REMOVE SUBREDDITS TO SCRAPE
SUBREDDITS = [
    "antiwork", "resignationporn", "legaladvice",
    "advice", "lifeadvice", "careerguidance", "workreform",
    "overemployed"
]


ENDPOINTS = dict(
    comment = "/reddit/search/comment",
    post = "/reddit/search/submission",
    # comments_under_post = "/reddit/submission/comment_ids/{base36-submission-id}"
)

