

import time
import websocket

server = "localhost"

ws = websocket.WebSocket()
ws.settimeout(1)
ws.connect('ws://%s:8000/feed' % server)

while True:
    data = ws.recv()
    print("Received: " + data)
    
    time.sleep(0.5)
    
    data = "test ack"
    print("Sending: " + data)
    ws.send(data)