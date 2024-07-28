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
    def __init__(self, type: DataType, id: str, start: int, end: int):
        self.type = type
        self.id = id
        self.data = 0
        self.start = start
        self.end = end
        self.conn = stomp.Connection()
        self.connected = True
        self.connect()
        threading.Thread(target=self.send).start()

    def connect(self): 
        self.conn.connect('admin', 'password', wait=True)
        
    def disconnect(self): 
        self.conn.disconnect()
        
    def send(self):
        while self.connected:
            time.sleep(0.25)
            self.dataGen()
            self.conn.send(body=str(self.data), destination=('/topic/sensor' + str(self.id)))
            
    def dataGen(self):
        self.data = random.uniform(float(self.start), float(self.end))
