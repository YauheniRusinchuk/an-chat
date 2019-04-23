from channels.consumer import AsyncConsumer


class CommentCunsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })
        print("SOCKET MSG ...")

    async def websocket_receive(self, event):
        print('receive ...')

    async def websocket_disconnect(self, event):
        print("disconnect")
