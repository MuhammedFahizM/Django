from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            "message" : "WebSocket connected"
        }))
        print("Websocket connection established")

    def disconnect(self, close_code):
        print("WebSocket disconnected")
    
    def receive(self, text_data ):
        print(f"Raw data recieved: {text_data}")
        try:
            data = json.loads(text_data)
            message = data.get("message", "")
            print(f"User sent message : {message}")
            self.send(text_data=json.dumps({
                "message" : f"You said : {message}"
            }))
        except json.JSONDecodeError:
            print("Invalid JSON received")
        