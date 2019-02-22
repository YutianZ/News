from cloudAMQP_client import CloudAMQPClient

TEST_CLOUDAMQP_URL = 'amqp://iqkabpol:QiCRaTihVSztSzCyP78w9O2r3nuT2_s0@shark.rmq.cloudamqp.com/iqkabpol'#TODO: use your own config.
TEST_QUEUE_NAME = 'test'#TODO: use your own config.

def test_basic():
    client = CloudAMQPClient(TEST_CLOUDAMQP_URL, TEST_QUEUE_NAME)
    
    sentMsg = {'test':'123'}
    client.sendMessage(sentMsg)
    client.sleep(3)
    receivedMsg = client.getMessage()
    
    assert sentMsg == receivedMsg
    print('test_basic passed!')
    

if __name__ == '__main__':
    test_basic()