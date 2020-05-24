const urlParameters = getUrlParameters();
const room = urlParameters.room;
const player = urlParameters.player;

const websocket = new WebSocket("ws://127.0.0.1:5000");
let app;

const enter = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "enter" }
  }
  websocket.send(JSON.stringify(message));
}

const exit = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "exit" }
  }
  websocket.send(JSON.stringify(message));
  window.location.href = 'index.html';
}

const game_start = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "start" }
  }
  websocket.send(JSON.stringify(message));
}

const down = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "down", "card": 0 }
  }
  websocket.send(JSON.stringify(message));
}

const bid = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "bid", "num": 0 }
  }
  websocket.send(JSON.stringify(message));
}

const reveal = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "reveal", "player": "name" }
  }
  websocket.send(JSON.stringify(message));
}

const pass = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "pass" }
  }
  websocket.send(JSON.stringify(message));
}

const on_message = function(event) {
  // app.users.push({ name: 'New Player' })
  const json = JSON.parse(event.data);
  switch (json.action) {
    case 'enter':
    case 'exit':
    case 'start':
      app.players = json.players
      console.log(event.data);
      break;
  }
}

$(document).ready(function() {
  $("#exit_button").click(exit);
  $("#start_button").click(game_start);

  app = new Vue({
    el: '#player_list',
    data: {
      game: {},
      players: []
    }
  })

  websocket.onopen = function(event) {
    enter(room, player)
  };
  websocket.onmessage = on_message;
});