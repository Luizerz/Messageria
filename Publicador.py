import stomp
import time
import threading
import random
import json
from DataType import DataType

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
            time.sleep(1)
            self.dataGen()
            alarm = False
            if self.data < self.start or self.data > self.end:
                alarm = True
            else:
                alarm = False
            data = {"id": str(self.id), "data": str(self.data), "type": str(self.type), "alarm": str(alarm)}
            self.conn.send(body=json.dumps(data), destination=('/topic/sensor' + str(self.id)))
            
    def dataGen(self):
        self.data = random.uniform(float(self.start * 2), float(self.end * 2))
