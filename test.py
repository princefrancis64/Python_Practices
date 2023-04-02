import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG,format="%(levelname)s %(name)s %(asctime)s %(message)s")
logging.info("this is my log with timestamp")