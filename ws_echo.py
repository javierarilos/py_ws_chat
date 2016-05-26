#!/usr/bin/env python

import asyncio
import websockets
import uvloop

import datetime
import random

async def hello(websocket, path):
    if path == '/time':
        while True:
            try:
                now = datetime.datetime.utcnow().isoformat() + 'Z'
                await websocket.send(now)
                await asyncio.sleep(random.random() * 3)
            except websockets.exceptions.ConnectionClosed as e:
                print('--- /time closed connection.')
                break
    else:
        while True:
            try:
                name = await websocket.recv()
                print("< {} with path {}".format(name, path))

                greeting = "Hello {}!".format(name)
                await websocket.send(greeting)
                print("> {}".format(greeting))
            except websockets.exceptions.ConnectionClosed as e:
                print('--- '+path+' closed connection.')
                break

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
