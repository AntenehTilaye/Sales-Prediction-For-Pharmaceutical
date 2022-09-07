import logging

logging.basicConfig(filename='../logs/sales.log',  
                    level=logging.DEBUG, 
                    format="%(asctime)s :  %(filename)s : %(levelname)s : %(lineno)d : %(message)s")

logging.getLogger('matplotlib.font_manager').disabled = True

def d(text):
    logging.debug(text)

def i(text):
    logging.info(text)

def e(text):
    logging.error(text)

def w(text):
    logging.warning(text)
