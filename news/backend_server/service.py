"""backend_service"""
import logging

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

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

#Threading RPC server
RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
#'add' is the name exposed to outside
RPC_SERVER.register_function(add, 'add')

logger.info("Starting RPC Server on %s:%d", SERVER_HOST, SERVER_PORT)
RPC_SERVER.serve_forever()
