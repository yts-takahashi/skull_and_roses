#!/usr/bin/env python
import asyncio
import json
import logging
import websockets

from player import Player
from room import Room

logging.basicConfig()

ROOMS = {}

async def notify(room_name, message):
    room = ROOMS.get(room_name)
    players = room.players
    await asyncio.wait([player.websocket.send(message) for player in players.values()])

async def enter(room_name, player_name, websocket):
    player = Player(player_name, websocket)
    # Get the room or create it if it doesn't exist.
    room = ROOMS.get(room_name, Room(room_name))
    ROOMS[room_name] = room

    room.admit(player)
    message = json.dumps({"action":"enter", "player_name":player_name, "players":room.get_players_list()})
    await notify(room.name, message)

async def exit(room_name, player_name, websocket):
    room = ROOMS.get(room_name)
    if room:
        room.exclude(player_name)
        message = json.dumps({"action":"exit", "player_name":player_name, "players":room.get_players_list()})
        await notify(room.name, message)

async def start_game(room_name, player_name):
    room:Room = ROOMS.get(room_name)
    if room.game.is_finished:
        room.game_start()
        message = json.dumps({"action":"start", "players":room.game.get_status_of_players()})
        await notify(room_name, message)
        

async def process(websocket):
    async for message in websocket:
        data = json.loads(message)
        room_name = data["room"]
        player_name = data["player"]
        action = data.get("action")
        if action:
            if action["type"] == "enter":
                await enter(room_name, player_name, websocket)                
            elif action["type"] == "exit":
                await exit(room_name, player_name, websocket)
            elif action["type"] == "start":
                await start_game(room_name, player_name)

        else:
            logging.error("unsupported event: {}", data)

async def skull_and_roses(websocket, path):
    logging.info(websocket)
    try:
        await process(websocket)
    except:
        pass

start_server = websockets.serve(skull_and_roses, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()