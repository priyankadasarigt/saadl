import logging
import logging.config
import importlib
from dotenv import load_dotenv  # ✅ Required import

try:
    import uvloop
    uvloop.install()
except ImportError:
    pass

def main():
    # Get logging configurations
    logging.config.fileConfig('logging.conf')
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger("pyrogram").setLevel(logging.WARNING)

    load_dotenv()  # ✅ This will now work
    bot = importlib.import_module("jiosaavn.bot").Bot
    bot().run()

if __name__ == "__main__":
    main()
