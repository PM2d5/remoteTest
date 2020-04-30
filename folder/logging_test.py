import logging
import datetime

now = datetime.datetime.now()
filename = now.strftime('%Y-%m-%d %H.%M.%S') + ".log"
logging.basicConfig(handlers=[logging.FileHandler(filename, encoding="utf-8")], format="%(asctime)s %(levelname)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

logging.info("Start print log")
logging.debug("再")
logging.warning("Something maybe fail.")
logging.info("Finish")
