import logging 
   
logging.basicConfig(filename="Siddhant.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a')
 
logger=logging.getLogger()
   
logger.setLevel(logging.DEBUG) 
   
logger.info("Just an information.") 
logger.warning("Its a Warning.") 
logger.error("This is any logical error.") 