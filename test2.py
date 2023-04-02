import logging
logging.basicConfig(filename="test2.log",level=logging.DEBUG,format="%(levelname)s %(name)s %(asctime)s %(message)s")

try:
    logging.info("i am trying to read a file")
    with open("prince.txt","r"):
        logging.info("successfully it has read the file")
except Exception as e:
    logging.critical("this is a situation for us")
    logging.error(e)
    logging.exception(e)