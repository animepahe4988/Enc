import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "23902408")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "6a36a4ef2f07d63aeba7b53b99c64d73") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6924920834:AAF3HdgQrNurFEjAlyhYut6Q4OAyIaBOHqI") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002217353256') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://mex:rex@cluster7.jrzowqz.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot44") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "7179837246")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002290310505')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
