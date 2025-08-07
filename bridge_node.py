bridge_node.py

import asyncio import websockets import json

class BridgeNode: def init(self, node_id, endpoint="ws://localhost:8765"): self.node_id = node_id self.endpoint = endpoint

async def connect(self):
    async with websockets.connect(self.endpoint) as websocket:
        await websocket.send(json.dumps({"node_id": self.node_id, "status": "connected"}))
        print(f"[{self.node_id}] Connected to bridge endpoint.")

        while True:
            try:
                message = await websocket.recv()
                print(f"[{self.node_id}] Received: {message}")
            except websockets.exceptions.ConnectionClosed:
                print(f"[{self.node_id}] Connection closed.")
                break

if name == "main": node = BridgeNode(node_id="albayancor-node-01") asyncio.run(node.connect())

