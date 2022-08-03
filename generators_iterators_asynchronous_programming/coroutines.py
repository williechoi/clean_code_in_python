import random
import logging
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class CustomException(Exception):
    pass


class DBHandler:
    def __init__(self, data: list, name: str = 'testdb'):
        self.data = data
        self.name = name

    def read_n_records(self, n: int):
        return random.choices(self.data, k=n)

    def close(self):
        print(f"Closing connection to database {self.name}")


def stream_db_records(db_handler: DBHandler):
    while True:
        try:
            yield db_handler.read_n_records(8)
        except CustomException as e:
            logger.info("controlled error %r, continuing", e)
        except Exception as e:
            logger.info("unhandled error %r, stopping", e)
            db_handler.close()
            break


records = [
    "amazon",
    "lotteon",
    "smartstore",
    "11st",
    "gmarket",
    "iconmarket",
    "tmon",
    "auction",
    "coupang",
    "taobao",
    "rakuten",
    "ohou",
    "everymarket",
    "hellostore",
    "ribbonshop"
]

streamer = stream_db_records(DBHandler(records))
for i, platforms in enumerate(streamer):
    if i == 4:
        streamer.throw(CustomException)
    elif i > 5:
        streamer.throw(RuntimeError)

    logger.info(f"Selected platforms: {platforms}")
    logger.info(f"processing platforms...")
    time.sleep(2)
    logger.info(f"...finished!")
