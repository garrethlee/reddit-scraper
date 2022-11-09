from config import *
from datetime import datetime
import pandas as pd
import os


def build_query(base_url = BASE_URL, endpoint = ENDPOINTS['comment'], params = {}):
    """Build API query based on endpoints and parameters"""
    return base_url + \
           endpoint + \
           "?" + \
           "&".join([f"{k}={'+'.join(v.split())}" for k,v in params.items()])

def extract_data_from_comments(content):
    """Extract data from pushshift query"""
    results = dict(
        comment_id = [],
        author_id = [],
        author = [],
        is_poster = [],
        score = [],
        url = [],
        subreddit = [],
        body = [],
        date = []
    )
    # Data is a list of dictionaries (entries)
    for entry in content:
        results["comment_id"].append(entry["id"])
        results["author_id"].append(entry.get("author_fullname", "None"))
        results["author"].append(entry["author"])
        results["is_poster"].append(entry["is_submitter"])
        results["score"].append(entry["score"])
        results["url"].append("https://reddit.com" + entry["permalink"])
        results["subreddit"].append(entry["subreddit"])
        results["body"].append(entry["body"])
        results["date"].append(datetime.fromtimestamp(entry["created_utc"]).strftime("%Y-%m-%d"))

    return results

def store_data_to_csv(query_data, dir = DATA_DIR, filename = "data.csv"):
    """Stores query results to csv file"""
    if not os.path.isdir(dir):
        os.mkdir(dir)
    df = pd.DataFrame(query_data)
    filepath = os.path.join(dir, filename)
    if not os.path.exists(filepath):
        df.to_csv(filepath, index = False)
    else:
        df.to_csv(filepath, header = False, mode = 'a', index = False)


def get_intervals(days = DAYS_PER_INTERVAL, start_date = COVID_START_DATE):
    """Set intervals for queries based on `days` argument"""

    intervals = []
    d = 0

    START_DATE = datetime.strptime(start_date, "%Y-%m-%d")
    END_DATE = datetime.today()

    DAYS = (END_DATE - START_DATE).days

    while True:
        if DAYS - d < days:
            intervals.append((d, DAYS))
            break
        intervals.append((d, d+days))
        d += days

    return intervals  
    

