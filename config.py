import os
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MSG = os.getenv("START_MSG")
BOT_ADI = os.getenv("BOT_ADI")
DATABASE_URL = os.getenv("DATABASE_URL")
DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "7"))
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
