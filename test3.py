import logging
logging.basicConfig(filename="test3.log",level=logging.DEBUG,format="%(levelname)s %(name)s %(asctime)s %(message)s ")


def divide(a,b):
    logging.info("trying to divide %s and %s",a,b)

    try:
        logging.info("francis asdfasfa")
        div =a/b
        logging.info("we have completed division operation")
        logging.info("the result of code is %s",div)
        return div
    except Exception as e:
        logging.exception(e)

divide(4,0)