import logging

FORMAT = '\033[1;38m%(asctime)s %(process)5s Line%(lineno)3d\033[0m %(message)s'
logging.basicConfig(format=FORMAT)
scolor = '\033[32m{}\033[0m'
wcolor = '\033[38m{}\033[0m'
ecolor = '\033[31m{}\033[0m'
dcolor = '\033[34m{}\033[0m'

debugger = logging.getLogger('debugger')
logger = logging.getLogger('logger')
errorer = logging.getLogger('errorer')