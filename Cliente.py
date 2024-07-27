
import stomp 
import time
import json 

class Client() :
    def __init__(self): 
        self.conn = stomp.Connection()
        self.listener()
        self.connect()
        self.subscribe('/topic/test4')
        self.list = []

    def connect(self): 
        self.conn.connect('admin', 'password', wait=True)
    def disconnect(self): 
        self.conn.disconnect()
    def subscribe(self, destination: str):
        self.conn.subscribe(destination = destination, id = 1, ack='auto')
    def listener(self):
        self.conn.set_listener('', self.ClientInner(self))
        
    class ClientInner(stomp.ConnectionListener):
        def __init__(self, client):
            self.client = client
        def on_error(self, frame):
            print('received an error "%s"' % frame.body)
            self.client.list.append(frame.body)
        def on_message(self, frame):
            print(json.loads(frame.body))
            self.client.list.append(frame.body)
            
x = Client()

time.sleep(20)