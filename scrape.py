import requests
import logging
import json
import random
import fake_useragent as ua
import time
from config import *
from helpers import build_query, extract_data_from_comments, store_data_to_csv, get_intervals


if __name__ == "__main__":
    
    intervals = get_intervals()

    for endpoint in ENDPOINTS:
        for keyword in KEYWORDS:
            for subreddit in SUBREDDITS:
                for before, after in intervals:
                    try:
                        entries = 0

                        # Make sure that there are MIN_ENTRIES_PER_QUERY comments 
                        while entries <= MIN_ENTRIES_PER_QUERY:
                            q = build_query(
                                endpoint = ENDPOINTS[endpoint],
                                params = {
                                    "q":keyword,
                                    "subreddit":subreddit,
                                    "size": str(QUERY_SIZE),
                                    "before":f"{before}d",
                                    "after":f"{after}d"
                                }
                            )

                            response = requests.get(q)
                            content = response.json()

                            query_data = extract_data_from_comments(content['data'])

                            queries_received = list(query_data.values())[0]
                            entries += len(queries_received)

                            store_data_to_csv(query_data)

                            # Sleep for a few seconds to prevent timeout
                            time.sleep(random.randint(3, 5))

                    except Exception as e:
                        logging.error(f"Error: {e}, at {subreddit} with keyword = {keyword}")
                        print(response)


