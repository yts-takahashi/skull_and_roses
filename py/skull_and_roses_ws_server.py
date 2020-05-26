#!/usr/bin/env python
import asyncio
import json
import logging
import websockets

from room import Room

logging.basicConfig()

ROOMS = {}


async def notify(room: Room, message):
    players = room.players
    await asyncio.wait([ws.send(message) for ws in players.values()])


def enter(room: Room, player_name, websocket):
    # player enter the room.
    room.admit(player_name, websocket)
    # notify all users in the room that new player comes.
    message = json.dumps({"action": "enter", "player_name": player_name, "players": room.get_players_list()})
    return message


def exit(room: Room, player_name, websocket):
    if room:
        room.exclude(player_name)
        message = json.dumps({"action": "exit", "player_name": player_name, "players": room.get_players_list()})
        return message


def start_game(room: Room, player_name):
    if room.game.is_finished:
        room.game_start()
        message = json.dumps({"action": "start", "players": room.game.get_status_of_players()})
        return message


def down(room: Room, player_name, card):
    game = room.game
    if game.down(player_name, card):
        message = json.dumps({"action": "down", "player_name": player_name, "players": room.game.get_status_of_players()})
        return message


def getRoom(room_name) -> Room:
    # Get the room or create it if it doesn't exist.
    room: Room = ROOMS.get(room_name)
    if not room:
        room = Room()
        ROOMS[room_name] = room

    return room


async def process(websocket):
    async for message in websocket:
        data = json.loads(message)
        room_name = data["room"]
        player_name = data["player"]
        action = data.get("action")
        if action:
            room: Room = getRoom(room_name)
            message = ""
            if action["type"] == "enter":
                message = enter(room, player_name, websocket)
            elif action["type"] == "exit":
                message = exit(room, player_name, websocket)
            elif action["type"] == "start":
                message = start_game(room, player_name)
            elif action["type"] == "down":
                message = down(room, player_name, action["card"])
            # elif action["type"] == "bid":
            #     await bid(room, player_name, action["num"])
            # elif action["type"] == "pass":
            #     await pass_turn(room, player_name)
            # elif action["type"] == "reveal":
            #     await reveal(room, player_name, action["player"])

            if message:
                await notify(room, message)

        else:
            logging.error("unsupported event: {}", data)


async def skull_and_roses(websocket, path):
    logging.info(websocket)
    await process(websocket)

start_server = websockets.serve(skull_and_roses, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
