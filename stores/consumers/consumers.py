import json
from channels.generic.websocket import WebsocketConsumer
from .models import Commodity

class LogisticsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        # Process the received data (e.g., stock update) and broadcast updates
        self.update_logistics()
	self.send(text_data=json.dumps({
            'message': 'Logistics data updated in real-time'
        }))

    def update_logistics(self):
        # Logic to fetch updated logistics data
        commodities = Commodity.objects.all()
        commodities_data = [
            {"name": commodity.name, "quantity": commodity.quantity}
            for commodity in commodities
        ]
        # Send the updated data to the WebSocket
        self.send(text_data=json.dumps({
            'commodities': commodities_data
        }))
