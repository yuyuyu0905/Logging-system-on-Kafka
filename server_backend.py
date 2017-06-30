# Please use app.py apidoc to run this script!
import json
import socket
from kafka import KafkaProducer,KafkaConsumer
#from pymongo import MongoClient

producer=KafkaProducer(bootstrap_servers='localhost:9092')
def run_server():
    address = ('0.0.0.0', 6005)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(address)
    while (1):
        error=0
        print "Listening"
        recv_data, addr = server_socket.recvfrom(2048)
        recv_data = json.loads(recv_data)
        if error==1:continue

        #just to show the sending process
        print 'data:', recv_data, 'address:', addr,'action',recv_data['action']
        future=producer.send('my_topic',json.dumps(recv_data))

        if recv_data == 'quit':
            break

run_server()
