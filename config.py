import os
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
# ARQ_API_KEY = os.getenv("ARQ_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MSG = os.getenv("START_MSG")
BOT_ADI = os.getenv("BOT_ADI")
PLAY_LIST = os.getenv("PLAY_LIST")
PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID"))
CHANNEL =  os.getenv("CHANNEL", "-1001369182739")
DATABASE_URL = os.getenv("DATABASE_URL")
DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "60"))
ARQ_API_KEY = os.getenv("ARQ_API_KEY")
# CLON_BOT = os.getenv("CLON_BOT")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "1924693109").split()})
