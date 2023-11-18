import logging


def createLoggerObj():
    fileName = '2023-11-18.log'
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(filename=fileName, format=formatStr, level = logging.INFO)
    myLogObj = logging.getLogger('sqa2023-logger')
    return myLogObj
     