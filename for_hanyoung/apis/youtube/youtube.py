import os
import json
from googleapiclient.discovery import build
from for_hanyoung import settings

config_file = open(os.path.join(settings.CONF_DIR, 'apis_debug.json'))
config = json.loads(config_file.read())
config_file.close()


__all__ = [
    'search',
]


DEVELOPER_KEY = config['youtube']['DEVELOPER_KEY']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def search(keyword, max_length=50):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_length,
        type="video",
    ).execute()

    return search_response
