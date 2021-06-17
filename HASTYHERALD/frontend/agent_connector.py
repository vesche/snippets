
import json
import time
import threading
import websocket


class Agent:
    def __init__(self, name, ip, port):
        self.ip = ip
        self.port = port
        self.name = name
        self.ws = None
        self.tool_to_run = None
        # TODO: variable for the malware to analyze

    def start(self):
        def run_agent(ws):
            while True:
                # TODO: get the command from redis for the specific agent using the name
                #       pass this as a json payload to the windows websocket server

                if self.tool_to_run:
                    # TODO: comeback to this, fix args
                    dict_payload = {'command': self.tool_to_run} # , 'args': ''}
                    json_payload = json.dumps(dict_payload)
                    ws.send(json_payload)
                    self.tool_to_run = None

                time.sleep(1)
    
        def on_message(ws, message):
            # TODO: redis
            print(message) # out to a file tmp if not

        def on_open(ws):
            agent_thread = threading.Thread(target=run_agent, args=(ws,))
            agent_thread.daemon = True
            agent_thread.start()

        #def on_error(ws):
        #    # TODO: come back to this
        #    pass

        self.ws = websocket.WebSocketApp(
            f'ws://{self.ip}:1337/hhagent_connect',
            on_message=on_message
        )
        self.ws.on_open = on_open
        self.ws.run_forever()
