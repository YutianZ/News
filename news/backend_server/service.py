"""backend_service"""
import logging
import json
import os
import sys
from bson.json_util import dumps
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

#import utils dir
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
import mongodb_client

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

logger_format = '%(asctime)s - %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('backend_server')
logger.setLevel(logging.DEBUG)

def add(num1, num2):
    """ Test method"""
    logger.debug("add is called with %d and %d", num1, num2)
    return num1 + num2

def getOneNews():
    """Test method"""
    logger.debug('getOneNews is called')
    res = mongodb_client.get_db()['news'].find_One()
    return json.loads(dumps(res))

#Threading RPC server
RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
#'add' is the name exposed to outside
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(getOneNews, "getOneNews")

logger.info("Starting RPC Server on %s:%d", SERVER_HOST, SERVER_PORT)
RPC_SERVER.serve_forever()
