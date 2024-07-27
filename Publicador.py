import stomp
import time
import threading
import random
from enum import Enum, auto

class DataType(Enum):
    velocity = auto()
    umidity = auto()
    temperature = auto()

class PublisherData:
    def __init__(self, type: DataType, id: str, sleepTime: int = 0):
        self.type = type
        self.id = id
        self.data = 0
        self.sleepTime = sleepTime
        self.conn = stomp.Connection()
        self.connected = True
        self.connect()
        threading.Thread(target=self.send).start()
        # self.send('{"id": "' + id + '", "type": "' + type.name + '"}')

    def connect(self): 
        self.conn.connect('admin', 'password', wait=True)
        
    def disconnect(self): 
        self.conn.disconnect()
        
    def send(self):
        while self.connected:
            time.sleep(0.25)
            self.dataGen()
            data = '{ "id": "' + self.id + '", "type": "' + self.type.name + '", "data": ' + str(self.data) + ' }' 
            self.conn.send(body=data, destination='/topic/' + self.id)
    def dataGen(self):
        self.data = random.random()
    
# x = PublisherData(DataType.velocity, '1', 1)
        