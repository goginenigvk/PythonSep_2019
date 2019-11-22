# Logging Module 
# import logging 
# DEBUG  -10
# INFO -20
# WARNING -30
# ERROR -40
# CRICTICAL=50


#---> 5 bathes - one - transfer the data from db to another db, read all data, - one 

import logging 

logging.debug('This is in debgug log message') # debug mode - developer 
logging.info('thiis is info log') # specify message 

logging.warning('this is a warning log message')
logging.error('this is error log')
logging.critical('this is critical message')

logging.basicConfig(level=logging.WARNING,filename="logfile.log",filemode='w')
logging.warning('This is in debgug log message after seeting the level')

user='Raja'
logging.error('%s is not have permisisons',user)
logging.error(f'{user} is not have permission')

a=5 
b=0
try:
    c=a/b
except Exception as ex:
    logging.exception('Division occured')

 