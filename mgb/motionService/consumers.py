import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer,WebsocketConsumer
import json
from django.core.cache import cache

class MotionConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # Perform any necessary setup when a client connects
        print("Connected")
        await self.accept()

    async def disconnect(self, close_code):
        # Perform any necessary cleanup when a client disconnects
        pass

    async def receive_json(self, content, **kwargs):
        # Handle incoming motion information from the client
        player_name = content.get('player_name')
        motion_data = content.get('motion_data')

        # Store the motion data in Redis cache
        cache_key = player_name
        # Append the new motion data to the existing list
        cache.set(player_name,motion_data)
       

        # Process the motion data (e.g., save it to the database, perform actions, etc.)
        # Implement your logic here

        # Retrieve all stored player motion data from Redis cache
        all_player_motion_data = []
        cache_keys = cache._cache.keys()
        for _cache_key in cache_keys:
            motion_data = cache.get(_cache_key.split(':')[-1])
            print(motion_data)
            all_player_motion_data.append(motion_data)
        



        # Send the array of all player motion data back to the client
        await self.send_json(all_player_motion_data)

# class  MotionConsumer(WebsocketConsumer):
#     async  def  connect(self):
#         self.accept()
#         print("connected")
#         self.send(text_data=json.dumps({'text':'Henlo'}))
#         return await super().connect()

        